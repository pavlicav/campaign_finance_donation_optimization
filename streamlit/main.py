# Libraries
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Confit
st.set_page_config(page_title='About Us', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Home Page')
st.subheader("About us")
st.write(
    """
   The Olson Campaign Finance consists of five undergraduate data science students from Michigan State University assembled by Dr. Dirk Colbry and mentored by Dr. Randy Olson. The team was formed with the common goal of creating a website that will allow users to donate to political candidates who need funding the most.  
    """
)




st.subheader("Why we did it")
st.write(
    """
   Using data from the FEC (Federal Election Commission) for the 2022 House of Representatives elections, there was a clear trend between win percentage and amount of money that each candidate spent on their campaigns. In the figure below, the combined disbursement is the total amount of money that both candidates spent in one race. The percentage of combined disbursement, seen on the y-axis, the portion of the combined disbursement that each candidate spent. In this case, it is apparent that the more money that a candidate spends, the more likely they are to win. 

    """
)
image = Image.open("streamlit/combined_disbursement.png")
st.image(image, caption="test")

st.write("""As a result, the idea for the website was developed with the intention of bringing awareness to candidates that have less funding for their campaigns. Furthermore, we hope that bringing this information to light will allow users to gain more influence with their donations as they could pinpoint candidates that need money the most through this website. 
         """
        )

st.subheader('How it works')
st.write(
    """
    The website currently allows users to select political issues that are important to them. These issues include Gun Control, Public or Private healthcare, Immigration (DACA), Access to Abortion, and Severity of Climate change. After selection, profiles of 2022 House of Representative candidates are shown to the user. The order presented is sorted based off a combination of shared ideologies and closest race, based upon fivethirtyeight.org. After the user finds a candidate, they will have the option to continue to the candidate's website and support them.
    """
)

#st.info('**Ben the Best: [@benramsey](https://www.linkedin.com/in/ben-ramsey-7b70671bb/)**')
