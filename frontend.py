import streamlit as st
import backend as bk  
import time

st.set_page_config(
    page_title="Wellcome to CloseAI",
    page_icon="🤖",
    layout="centered"
)

st.sidebar.title("CloseAI Assistant")
st.sidebar.write("Powered by CloseAI to answer your questions.")
st.sidebar.image("./CloseAI.png", use_column_width=True)  

st.title("CloseAI" )
st.write("Type your question below and let AI answer it for you.")


input_query = st.text_input("Enter your question here:")

enterButton = st.button("Submit")

# with st.form("LLM-FORM"):
#     input_query = st.text_area("Enter Prompt")
#     enterButton = st.form_submit_button("Submit")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if enterButton:
    if not input_query.strip():
        st.error("Please enter a valid question.") 
    else:
        with st.spinner("Generating..."):  
            try:
                backend_res = bk.get_response(input_query)
                
                time.sleep(1)

                if isinstance(backend_res, str,):
                    st.success("Here's your answer:")
                    st.write(backend_res)
                else:
                    st.success("Here's your answer:")
                    st.write(backend_res.get('message', 'No message found'))
                st.session_state['chat_history'].append({"user":input_query,"Response":backend_res})

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.write("Please try again later.")
                
st.write("Chat History")
for chat in st.session_state["chat_history"]:
        st.write("------------------------------------------------")
        st.write(F"User: {chat['user']}")
        st.write(F"Response: {chat['Response']}")
                
st.markdown("""
---
**Ask Me App** - Powered by ClsoeAI  
For support, contact [support@CloseAI.com](mailto:support@example.com)  
[Privacy Policy](https://example.com/privacy)
""")
