import streamlit as st
import openai
import os

# Set OpenAI API key
openai.api_key = "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"

# Initialize session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "document_text" not in st.session_state:
    st.session_state.document_text = ""
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# Upload a file
uploaded_file = st.file_uploader("Upload a document")
if uploaded_file is not None:
    # Assuming it's a text file for simplicity, adjust this if you're using a different file type
    st.session_state.document_text = uploaded_file.read().decode()

# Display previous messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input for user message
user_message = st.chat_input("Your message", key=st.session_state.input_key)

# Check if a non-empty message was sent
if user_message:
    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_message})

    # Generate assistant message
    conversation = st.session_state.chat_history + [{"role": "system", "content": "test"}]
    message = openai.ChatCompletion.create(
        model="gpt-4",  # replace with the model you're using
        messages=conversation,
    )

    # Append assistant message to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": message["choices"][0]["message"]["content"]})

    # Increment the input key to clear the chat input
    st.session_state.input_key += 1

    # Rerun the script to update the chat display
    st.experimental_rerun()
