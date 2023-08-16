import streamlit as st
from langflow import load_flow_from_json

# Load the flow
flow = load_flow_from_json("chat_1.json")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("You: "):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get the bot's response
    response = flow(prompt)

    # Extract bot's response from the dictionary
    # Replace 'text' with the actual key
    bot_response = response.get('text', '')

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for word in bot_response.split():
            full_response += word + " "
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
