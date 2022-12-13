import streamlit as st
from textblob import TextBlob

statement = st.text_input("Enter a word, and the AI will detect which word you are typing and evaluate its spelling:") #User Input
button = st.button("Evaluate Spelling")

with st.spinner("Discovering Answers.."):
    if button and statement:
      if(statement == TextBlob(statement).correct()):
        st.write("Correct spelling")
      else:
        st.write("Incorrect spelling. The correct spelling is: ", TextBlob(statement).correct())
