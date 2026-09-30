def create_prompt(context, question):

    prompt = f"""
You are a PDF question-answering assistant.

Answer the user's question ONLY using the information provided in the context.

If the answer is not present in the context, say:
"I could not find this information in the uploaded document."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt