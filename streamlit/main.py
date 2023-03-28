# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='About Us', page_icon=':bar_chart:', layout='wide')

# Title
st.title('About Us')




st.subheader("Why we did it")
st.write(
    """
    Every election cycle, there are thousands of competitive races that lack financial information that voters could find whether it is on the federal, state, or local level. 
    As a result, the goal of the website is to provide voters with not only the finance for each candidates’ campaigns but allow users to narrow down the campaigns that need money the most. We believe that through this idea, voters will have more access to this information which will allow them to have more choices to vote for. Additionally, candidates who have more funding tend to have more recognition which may affect the voter’s pool of choice. 
    We hope that through this website, candidates with less funding can be made more aware to the voting population.
    """
)

st.subheader('Methodology')
st.write(
    """
    The website currently allows users to select political issues that are important to them. These issues include Gun Control, Public or Private healthcare, Immigration (DACA), Access to Abortion, and Severity of Climate change. After selection, profiles of 2022 House of Representative candidates are shown to the user. The order presented is sorted based off a combination of shared ideologies and closest race, based upon fivethirtyeight.org. After the user finds a candidate, they will have the option to continue to the candidate's website and support them.
    """
)

#st.info('**Ben the Best: [@benramsey](https://www.linkedin.com/in/ben-ramsey-7b70671bb/)**')
