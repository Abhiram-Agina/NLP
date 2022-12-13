# Team Analytics

import streamlit as st
import pandas as pd
from PIL import Image

st.title("Homepage: **Natural Language Processing**")

#make an index of services offered
#list metrics, along with importance & limitations
#predict/analyze game outcome per Team metrics

st.sidebar.markdown(
"""
About Me:
* I am a Senior at Oak Park High School in Oak Park, CA. I absolutely love Computer Science. I developed this app as a tool and portfolio of my early work in Artificial Intelligence & Linguistics.
* [**My Github**](https://github.com/Abhiram-Agina)
* [**My LinkedIn**](https://www.linkedin.com/in/abhiram-agina/)
"""
)

nav = st.sidebar.radio("Navigation",["Summary", "Spell Checker", "Sentiment Analyzer", "Context Questions"])


if nav == "Home":
    st.markdown(
    """
    ***Natural Language Processing?***
    * **There is a new player** 
    * "Natural Language Processing (NLP) is a field of study that focuses on how computers can understand and generate human language. It involves developing algorithms and models that enable computers to process and analyze natural language data, such as speech and text. NLP has many applications, including language translation, text summarization, and sentiment analysis."
    * As states by ChatGPT OpenAI
    
    ***My Goal***
    * This website aims to chart and display my growth into the World of Artificial Intelligence & NLP.  
    * ***Please Explore and Enjoy :)***\n
    """
    )
    
    
if nav == "Spell Checker":
    st.header("*Spell Check*")
    st.markdown(
    '''
    * [Spell Check](https://abhiram-agina-nlp-spellcheck-nt232o.streamlit.app/)
    '''
    )
    
if nav == "Sentiment Analyzer":
    st.header("*Sentiment Analyzer*")
    st.markdown(
    '''
    * [Sentiment Analyzer](https://abhiram-agina-nlp-simplesentiment-ehagi9.streamlit.app/)
    '''
    )
    
if nav == "Context Questions":
    st.header("*Context Questions*")
    st.markdown(
    '''
    * [Context Questions](https://abhiram-agina-nlp-questionanswer-transformers-45gs5y.streamlit.app/)
    '''
    )
    
