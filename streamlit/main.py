# Libraries
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly

df = pd.read_csv("538_FEC_Won_Opponent_Combined_Dataset.csv")
district_sum = pd.DataFrame(df.groupby(["district"])["Total_Disbursement"].sum()).reset_index()
district_sum.rename(columns = {'Total_Disbursement':'Combined_Disbursement'}, inplace = True)
df = pd.merge(df, district_sum, how='left')
df['Percentage_USED_TOTAL'] = 100*(df.Total_Disbursement / df.Combined_Disbursement)
combined = px.scatter(df, 
           y="Percentage_USED_TOTAL", x = "win_pct", 
           hover_data = ["name", "district", "party"], 
           color = "Won?",
           labels={
                     "Percentage_USED_TOTAL": "Percentage of combined disbursement spent",
                     "win_pct": "Win percentage",
                     "Won?": "Won race?"
                 },
          title = "Candidates who spend more money usually win")

st.plotly_chart(combined,theme="streamlit")
html_string = plotly.io.to_html(combined)

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
# image = Image.open("streamlit/combined_disbursement.png")
components.html(html_string, height = 400, width = 800)

st.write("""As a result, the idea for the website was developed with the intention of bringing awareness to candidates that have less funding for their campaigns. Furthermore, we hope that bringing this information to light will allow users to gain more influence with their donations as they could pinpoint candidates that need money the most through this website. 
         """
        )

st.subheader('How it works')
st.write(
    """
    The website currently allows users to select their stance on political issues that are important to them. These issues include gun control, public or private healthcare, immigration (DACA), access to abortion, and severity of climate change. After selection, profiles of 2022 House of Representative candidates are shown to the user. The order presented is sorted based on a combination of shared ideologies and tipping point percentages for each candidate. In politics, the tipping point is the percentage chance that a seat decides control of the House. The data of ideologies of each candidate is collected by our team and the tipping point percentages are from fivethirtyeight.org. After the user finds a candidate, they will have the option to continue to the candidate's website and support them. 

    """
)

st.info('**Ben the Best: [@benramsey](https://www.linkedin.com/in/ben-ramsey-7b70671bb/)**')
st.info('**Thao the Tiny: [@thaonguyen](https://www.linkedin.com/in/thaonguyenmsu/)**')
