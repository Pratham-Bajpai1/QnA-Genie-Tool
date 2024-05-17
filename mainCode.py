import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Helvetica', sans-serif;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #72edf2 10%, #5151e5 100%);
        color: white;
        font-family: 'Arial Black', sans-serif;
        padding: 20px;
    }
    .main {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        margin-top: 50px;
    }
    .stTextInput input {
        background-color: #e9ecef;
        border: none;
        border-radius: 10px;
        padding: 15px;
        font-size: 18px;
        width: 100%;
    }
    .stTextInput input:focus {
        background-color: #fff;
        border: 2px solid #007BFF;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 15px 30px;
        margin-top: 20px;
    }
    .stButton button:hover {
        background-color: #0056b3;
        color: white;
    }
    .stMarkdown h1 {
        color: #333;
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        margin-top: 20px;
    }
    .stMarkdown h2 {
        color: #007BFF;
        font-family: 'Arial', sans-serif;
        margin-top: 30px;
    }
    .stMarkdown p {
        font-family: 'Arial', sans-serif;
        font-size: 16px;
    }
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("# QnA Genie Tool 🌟🧩")
st.sidebar.markdown("Welcome to the QnA Genie Tool! Use this tool to generate answers to your questions.")
btn = st.sidebar.button("Generate Knowledgebase 🌐🚀")
if btn:
    create_vector_db()

# Main content
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.header("Ask Your Question Below")

# Text input for the user's question
question = st.text_input("Put Your Minded Question📈:")

# If there's a question, process it and display the answer
if question:
    chain = get_qa_chain()
    response = chain(question)

    # Display the answer
    st.header("ANSWER🔄")
    st.write(response["result"])

st.markdown("</div>", unsafe_allow_html=True)

# Footer with copyright
st.markdown("""
    <footer>
        &copy; Made By Pratham Bajpai
    </footer>
""", unsafe_allow_html=True)





# original code previous.
#import streamlit as st
#from langchain_helper import get_qa_chain, create_vector_db

#st.title("QnA Genie Tool 🌟🧩")
#btn = st.button("Generate What Do you Think, Knowledgebase 🌐🚀")
#if btn:
#    create_vector_db()

#question = st.text_input("Put Your Minded Question📈: ")

#if question:
#    chain = get_qa_chain()
#    response = chain(question)

#    st.header("ANSWER🔄")
#    st.write(response["result"])

