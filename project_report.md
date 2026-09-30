# Domain-Specific RAG Chatbot for PDF Question Answering

## 1. Introduction

This project is a Domain-Specific Retrieval-Augmented Generation (RAG) chatbot for answering questions from uploaded PDF documents.

The chatbot extracts information from a PDF, divides the text into smaller chunks, creates embeddings, stores them in a FAISS vector database, retrieves relevant information, and generates an answer using a local Llama 3.2 model through Ollama.

## 2. Objective

The objective of this project is to build a chatbot that can answer questions using information from an uploaded PDF and provide the source document and page number.

The chatbot should not invent information when the answer is not available in the uploaded document.

## 3. Technologies Used

- Python
- Streamlit
- PyPDF
- LangChain
- Sentence Transformers
- FAISS
- Ollama
- Llama 3.2

## 4. Working of the System

The system follows these steps:

1. User uploads a PDF.
2. Text is extracted from the PDF.
3. The text is divided into smaller chunks.
4. Embeddings are generated for the chunks.
5. The embeddings are stored in FAISS.
6. The user asks a question.
7. The system retrieves the most relevant chunks.
8. The retrieved information is provided as context to the LLM.
9. Llama 3.2 generates the answer.
10. The chatbot displays the answer along with the source PDF and page number.

## 5. User Interface

The application is built using Streamlit.

Users can upload a PDF and ask multiple questions through the chatbot interface. Previous questions and answers remain visible during the session.

## 6. Guardrail

The chatbot is instructed to answer only using information available in the retrieved document context.

If the information is not available, the chatbot responds:

"I could not find this information in the uploaded document."

## 7. Testing

The chatbot was tested using 15 questions.

The testing included:

- Questions whose answers were present in the PDF.
- Questions whose answers were not present in the PDF.

The chatbot successfully answered document-related questions and refused questions about information that was not available in the uploaded document.

## 8. Conclusion

This project demonstrates the use of Retrieval-Augmented Generation for PDF question answering.

The system combines PDF processing, text chunking, embeddings, vector search, retrieval, and a local language model to provide answers grounded in uploaded documents.