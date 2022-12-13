import streamlit as st
import transformers
import pandas as pd
from transformers import pipeline


senti_pipeline = pipeline("sentiment-analysis")

statement = st.text_input("Enter a statement, and the AI will guess its sentiment:")
button = st.button("Evaluate Sentiment")

with st.spinner("Discovering Answers.."):
    if button and statement:
      st.write(senti_pipeline(statement))
