# NLP Preprocessing Engine

## Overview
This project builds an NLP preprocessing pipeline to clean noisy text data and convert it into meaningful tokens for machine learning.

## Features
- Remove URLs, numbers, and special characters  
- Handle repeated characters  
- Convert text to lowercase  
- Remove short tokens (except "no", "not")  
- Tokenization and frequency analysis  

## Tech Stack
Python, re, Pandas, Counter  

## Example
Input: "I absolutely looooved this product 😍😍"  
Output: ['absolutely', 'loved', 'this', 'product']

 
## Conclusion
The pipeline effectively cleans and prepares text data for NLP tasks.

