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
df['Percentage_DIFFERENCE'] = 100*(df.Cash_Advantage / df.Combined_Disbursement)
only_advantage = df.query("Percentage_DIFFERENCE >= 0")
advantage = px.scatter(only_advantage, 
           y="Percentage_DIFFERENCE", x = "win_pct", 
           hover_data = ["name", "district", "party", "tipping"], 
           color = "Won?",
           labels={
                     "Percentage_DIFFERENCE": "Percentage cash advantage",
                     "win_pct": "Win percentage",
                     "Won?": "Won race?"
                 },
          title = "Candidates with percentage cash advantage usually win")



# Confit
st.set_page_config(page_title='Blog', page_icon=':book:', layout='wide')
with st.expander("Case study: Marie Gluesenkamp Perez"):

           # Title
           st.title('A look into Marie Gluesenkamp Perez')
           st.subheader("Overview")
           st.plotly_chart(advantage,theme=None,use_container_width=True)

           st.write(
               """
              As proven with our motivation for the website, candidates who spend more money on their election campaigns tend to be more likely to win their races. Specifically, when candidates have a cash advantage over their opponent, they are far more likely to win that race. The chart below tells this story as the majority of the winners had a significant cash advantage over their opponents. On the other hand, candidates who have a small advantage, highlighted in the red box, are far less likely to win their races. However, in the midterms elections of 2022, there was a single blue dot that stood out in the red zone. That is the story of Marie Gluesenkamp Perez.
               """
           )

           image1 = Image.open("streamlit/cash_advantage.png")
           st.image(image1)



           st.subheader("Against the Odds")
           st.write(
               """
              Marie Gluesenkamp Perez (D) ran against Joe Kent (R) in the 3rd district of Washington. Perez came from humble backgrounds. Her father was a Mexican immigrant who worked as a salesperson and her mother came from a generational family who worked in the state’s stone-cutting and logging industry. Following her mother’s family legacy, Perez went on to run her own auto repair shop small business with her husband. In total, the couple made under $80,000 per year.
               """
           )
           

           st.write("""On the other hand, Perez’s counterpart, Joe Kent, is a well-established political figure within the Republican voting population as he frequently guested on Tucker Carlson Tonight. Kent also has been politically active as he served on the Military Veterans advisory board for former president Donald Trump. As a result, his campaign in 2022 was endorsed by Trump and other prominent figures from the same party. According to OpenSecrets, Kent self-financed almost $250,000 while Perez spent none. 
                    """
                   )
           image2 = Image.open("streamlit/cash_adv_MGP.png")
           st.image(image2)
           st.write("""FiveThirtyEight predicted Perez to only have a 15% winning chance due to Kent’s established presence within the Republican party. Despite her odds, Perez managed to barely raise 2% more than her opponent. As a result, Perez narrowly won the race with 50.14% of the votes with solely donations. 
                    """
                   )
           st.subheader('Looking Forward')
           st.write(
               """
               The case study of Marie Gluesenkamp Perez is one of many that inspires and motivates the purpose of our website. Even on the federal level, there exists stories where the smallest amount of donation to a political candidate could make a huge difference. It is our goal to make it easier for the voting population to find candidates like Perez where the smallest donation of money could bring unexpected results. For now, Perez’s case is a rarity, but hopefully, it could become a norm to create a space for disadvantaged political candidates to have a better chance.
               """
           )
