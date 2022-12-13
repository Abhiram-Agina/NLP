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
* I am a Junior at Oak Park High School in Oak Park, CA. I absolutely love Basketball & the NBA. I developed this app as a tool and portfolio of my early work in Basketball Analytics.
* [**My Github**](https://github.com/Abhiram-Agina)
* [**My LinkedIn**](https://www.linkedin.com/in/abhiram-agina/)
"""
)

nav = st.sidebar.radio("Navigation",["Summary", "Spell Checker", "Sentiment Analyzer", "Context Questions"])


if nav == "Summary":
    st.markdown(
    """
    ***Data Science + Sports? ***
    * **Our world is changing, and sports are no exception.** 
    * Data Science and Analytics can now be implemented into every facet of a game from **Team** and **Player** Analysis all the way to aspects such as **Ticketing** and **Marketing**.
    * More Info: [How Data Analysis In Sports Is Changing The Game](https://www.forbes.com/sites/forbestechcouncil/2019/01/31/how-data-analysis-in-sports-is-changing-the-game/?sh=3c2f0b883f7b)\n
    
    ***My Goal***
    * This website aims to chart and display my growth into the World of Data Analytics. I begin with my favorite sport, a game I continue to love playing, watching, and learning about. 
    * ***Please Explore and Enjoy :)***\n
    """
    )
    
    
if nav == "Spell Checker":
    st.header("*Spell Check*")
    st.markdown(
    '''
    * [Spell Check](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Four_Factor_Analysis.py)
    '''
    )
    
if nav == "Sentiment Analyzer":
    st.header("*Sentiment Analyzer*")
    st.markdown(
    '''
    * [Spell Check](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Four_Factor_Analysis.py)
    '''
    )
    
if nav == "Context Questions":
    st.header("*Context Questions*")
    st.markdown(
    '''
    * [Spell Check](https://share.streamlit.io/abhiram-agina/basketball_analytics_main/main/Four_Factor_Analysis.py)
    '''
    )
    
