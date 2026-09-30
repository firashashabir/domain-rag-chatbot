from langchain_ollama import OllamaLLM


def generate_answer(prompt):
    llm = OllamaLLM(model="llama3.2:latest")

    answer = llm.invoke(prompt)

    return answer