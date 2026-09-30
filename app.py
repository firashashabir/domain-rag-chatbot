import streamlit as st

from document_loader import load_pdf
from rag_pipeline import split_documents
from vector_store import create_vector_store, search_vector_store
from prompt import create_prompt
from llm import generate_answer


st.title("📚 Domain-Specific RAG Chatbot")

st.write("Upload a PDF and ask questions about it.")


# Upload PDF
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    # 1. Extract text
    documents = load_pdf(uploaded_file)

    if not documents:

        st.error("Could not extract text from this PDF.")

    else:

        # 2. Split text into chunks
        chunks = split_documents(documents)

        # 3. Create vector store
        vector_store = create_vector_store(chunks)

        st.success("PDF processed successfully!")

        st.write("Pages:", len(documents))
        st.write("Chunks:", len(chunks))


        # -----------------------------
        # Chat history
        # -----------------------------

        if "messages" not in st.session_state:
            st.session_state.messages = []


        # Display previous messages
        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.write(message["content"])

                if message["role"] == "assistant":

                    if "sources" in message:

                        st.write("**Sources:**")

                        for source in message["sources"]:

                            st.write(
                                f"{source['source']} — Page {source['page']}"
                            )


        # -----------------------------
        # Chat input
        # -----------------------------

        question = st.chat_input(
            "Ask a question about your PDF..."
        )


        if question:

            # Display question
            with st.chat_message("user"):

                st.write(question)


            # Save question
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )


            # -----------------------------
            # Retrieve relevant chunks
            # -----------------------------

            results = search_vector_store(
                vector_store,
                question
            )


            # Combine context
            context = "\n\n".join(
                result.page_content
                for result in results
            )


            # Create prompt
            prompt = create_prompt(
                context,
                question
            )


            # Generate answer
            answer = generate_answer(prompt)


            # -----------------------------
            # Collect sources
            # -----------------------------

            sources = []

            for result in results:

                page = result.metadata.get(
                    "page",
                    "Unknown"
                )

                source = result.metadata.get(
                    "source",
                    uploaded_file.name
                )

                already_added = False

                for item in sources:

                    if (
                        item["source"] == source
                        and item["page"] == page
                    ):

                        already_added = True

                if not already_added:

                    sources.append(
                        {
                            "source": source,
                            "page": page
                        }
                    )


            # -----------------------------
            # Display answer
            # -----------------------------

            with st.chat_message("assistant"):

                st.write(answer)

                if "I could not find this information" not in answer:

                    st.write("**Sources:**")

                    for source in sources:

                        st.write(
                            f"{source['source']} — Page {source['page']}"
                        )


            # -----------------------------
            # Save answer
            # -----------------------------

            message_data = {
                "role": "assistant",
                "content": answer
            }


            if "I could not find this information" not in answer:

                message_data["sources"] = sources


            st.session_state.messages.append(
                message_data
            )