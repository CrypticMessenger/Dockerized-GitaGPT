import streamlit as st
import requests

st.set_page_config(page_title="Gita GPT",page_icon=":peacock:")
assistant_avatar = "✨"
user_avatar = "🙏"

# Inference URL
inference_url = "http://127.0.0.1:40000/enlighten"
test_url = "http://127.0.0.1:40000/test"
test_args_url = "http://127.0.0.1:40000/test_args"



st.title("Gita's Streamlit App 🦚🕉️")

with st.sidebar:
    st.title('🦙💬 Gita Chatbot')
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=512, step=8)
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')


# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hare Krishna! I am Gita, a chatbot trained on the Bhagavad Gita. How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    if(message["role"] == "user"):
        with st.chat_message(message["role"],avatar=user_avatar):
            st.write(message["content"])
    else:
        with st.chat_message(message["role"],avatar=assistant_avatar):
            st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hare Krishna! I am Gita, a chatbot trained on the Bhagavad Gita. How may I assist you today?"}]

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating GitaGPT response
def generate_gita_response(prompt):

    # Starting prompt
    string_dialogue = "you're here to selflessly help and answer any question or dilemma of anyone who comes to you. Analyze the person's question below and identify the base emotion and the root for this emotion, and then frame your answer by summarizing how the verses below apply to their situation and be emphatetic in your answer.  You are a helpful assistant. [context]:\n\n"
    
    for dict_message in st.session_state.messages[-6:]:
        if(dict_message["role"] == "user"):
            string_dialogue+= dict_message["content"] + "\n"

    string_dialogue += "You give random bhagwat gita quotes to uplift user, now answer:\n"

    final_prompt = f"{string_dialogue} {prompt}"
    params ={"top_p":top_p, "max_length":max_length, "repetition_penalty":1, "prompt": final_prompt }
    sz = len(final_prompt)

    # print(requests.get(test_args_url, params=params).text)

    # response = requests.get(test_args_url, params=params).text[sz:]
    response = requests.get(inference_url, params=params).text[sz:]

    return response

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user",avatar=user_avatar):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant",avatar=assistant_avatar):
        with st.spinner("Thinking..."):
            response = generate_gita_response(prompt)
            placeholder = st.empty()
           
            
            placeholder.markdown(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)