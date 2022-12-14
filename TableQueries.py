import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("Cancer Death - Data.csv")

from tableqa.agent import Agent
agent = Agent(df)

st.title("Answers questions about this table")

st.table(df)

question = st.text_input("Question on data in this table?")

answer = agent.query_db(question)
st.write(answer)
