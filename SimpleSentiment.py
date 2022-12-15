import streamlit as st
import transformers
import pandas as pd
from transformers import pipeline 

#NLP's Transformer is a new architecture that aims to solve tasks sequence-to-sequence while easily handling long-distance dependencies
#A Transformer pipeline describes the flow of data from origin systems to destination systems and defines how to transform the data along the way.

senti_pipeline = pipeline("sentiment-analysis")
#senti_pipeline will decipher sentiment

statement = st.text_input("Enter a statement, and the AI will guess its sentiment:") #User Input
button = st.button("Evaluate Sentiment")

with st.spinner("Discovering Answers.."):
    if button and statement:
      st.write(senti_pipeline(statement)) #identifies statement's sentiment
