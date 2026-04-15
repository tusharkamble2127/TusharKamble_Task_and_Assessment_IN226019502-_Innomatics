#  AI Resume Screening System

##  Overview
This project is an AI-based Resume Screening System built using LangChain.  
It evaluates resumes based on a given job description and assigns a score with explanation.

---

##  Objective
- Automate resume evaluation  
- Provide skill-based scoring  
- Generate explainable results  

---

##  Tech Stack
- Python  
- LangChain  
- LangSmith (for tracing)

---

##  Approach
The system follows a modular pipeline:

Resume → Skill Matching → Score Calculation → Explanation

- PromptTemplate used for structured design  
- Matching logic compares resume skills with job requirements  
- Score calculated based on matched skills  

---

##  Results

| Candidate | Score |
|----------|------|
| Strong   | 100/100 |
| Average  | 50/100  |
| Weak     | 0/100   |

---

##  Features
- Skill-based resume evaluation  
- Clear explanation for each result  
- Modular pipeline design  
- LangSmith tracing for monitoring  

---

##  Tracing Proof
LangSmith is used to track execution of the pipeline.

(Add screenshots here)

---

##  Limitations
- Uses rule-based matching (no LLM due to API limits)  
- Limited to predefined skills  

---

##  Future Improvements
- Integrate real LLM  
- Use embeddings for semantic matching  
- Build a web interface  

---

##  Conclusion
This project demonstrates how LangChain can be used to build structured and scalable AI pipelines for real-world applications like resume screening.
