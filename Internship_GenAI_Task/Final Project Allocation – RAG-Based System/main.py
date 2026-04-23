import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langgraph.graph import StateGraph
from langchain_groq import ChatGroq

# STEP 1: Load & Process PDF
def process_pdf(file):
    loader = PyPDFLoader(file)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings()
    db = Chroma.from_documents(chunks, embeddings)

    return db

# STEP 2: Retrieve + Answer

def generate_answer(state):
    query = state["query"]
    db = state["db"]

    retriever = db.as_retriever()
    docs = retriever.invoke(query)

    context = " ".join([doc.page_content for doc in docs])

    # Groq setup
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0
    )

    response = llm.invoke(
        f"Answer based only on this context:\n{context}\n\nQuestion: {query}"
    )

    answer = response.content if response else "No response generated."

    # Confidence logic
    confidence = 0.9 if len(docs) > 0 else 0.3

    return {"answer": answer, "confidence": confidence}


# STEP 3: HITL

def hitl(state):
    st.warning("Low confidence. Human intervention required.")
    human_input = st.text_input("Enter manual answer:")
    return {"answer": human_input}

# STEP 4: Routing Logic

def router(state):
    if state["confidence"] < 0.5:
        return "hitl"
    return "output"

# STEP 5: Output Node

def output(state):
    return state


# STEP 6: LangGraph Setup
def build_graph():
    graph = StateGraph(dict)

    graph.add_node("process", generate_answer)
    graph.add_node("hitl", hitl)
    graph.add_node("output", output)

    graph.set_entry_point("process")

    graph.add_conditional_edges(
        "process",
        router,
        {
            "hitl": "hitl",
            "output": "output"
        }
    )

    graph.add_edge("hitl", "output")

    return graph.compile()

# STREAMLIT UI
st.title(" RAG Customer Support Assistant")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    db = process_pdf("temp.pdf")
    st.success("PDF Processed!")

    query = st.text_input("Ask your question:")

    if st.button("Get Answer"):
        app = build_graph()

        result = app.invoke({
            "query": query,
            "db": db
        })

        st.write("### Answer:")
        st.write(result["answer"])