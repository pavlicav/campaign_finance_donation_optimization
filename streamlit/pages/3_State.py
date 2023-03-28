# Libraries
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
#from streamlit_card import card
# from IPython.core.display import HTML
issues=["abortion","gun_control", "climate_change",  "immigration", "healthcare"]
checked=[]
party=''
st.set_page_config(
    page_icon="📈",
    layout="wide",)
DATA_URL='https://raw.githubusercontent.com/ramseybe/hackathon_campaign/main/50_toss_up1.csv'
st.header("Make a Difference This Election!", )
left_column, right_column = st.columns([3,5])

@st.cache

def load_data(file):
    data = pd.read_csv(file)
    data=data.drop(["Unnamed: 0"],axis=1)
    dict = data.to_dict()
    return dict

thing = load_data(DATA_URL)
for key, val in thing.items():
    needed = val
    break

def create_card(name):
    file = pd.read_csv('https://raw.githubusercontent.com/ramseybe/hackathon_campaign/main/50_toss_up1.csv')
    file=file.drop(["Unnamed: 0"],axis=1)
    
    tempname=name.title()
    name=name.lower()

    person=file.iloc[file.index[file["name"] == tempname].values[0]]

    card="""<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 500px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}



button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>



<div class="card">
  <img src="https://github.com/pavlicag/campaign_finance_donation_optimization/blob/main/streamlit/pages/can_pics/person.jpeg" alt="person" style="width:100%">
  <h1>person</h1>
  <p class="title">district, party</p>
  <p>Harvard University</p>
  <div style="margin: 24px 0;">
  </div>
  
  
  <p><button>Donate!</button></p>
</div>

</body>
</html>"""
    #name
    card=card.replace("person",name)
    #district
    card=card.replace("district",person["district"])
    #party
    card=card.replace("party",person["party"])
    return card
def get_icons(name,file):
    temp=""""""
    template="""<span class="fa-stack fa-2x">
        <i class="fa fa-idea fa-stack-1x"></i>
        <i class="fas fa-ban fa-stack-2x" style="color:Tomato"></i>
        </span>
        """

    vallist=list(file.iloc[0][4:9])

    idea={'abortion':'suitcase-medical', 'gun_control':'gun', 'climate_change':"leaf", 
           'immigration':"child", 'healthcare':"stethoscope"}
    for i,j in zip(vallist,idea):
        #missing/dont know
        #print(j,idea[j])
        if i==0:
            pass

        #against 
        #need icon
        #color= clear
        #change to -1
        if i == -1:
            t1=template.replace("idea",idea[j])
            t1=t1.replace("Tomato","#ffffff00")
            temp = temp + t1
        #pro
        #need icon
        #color= tomato
        elif i ==1:

            t1=template.replace("idea",idea[j])
            temp = temp + t1
    return temp

def create_card_update(name):
    a="""<html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
    <style>
    .card {
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
      max-width: 400px;
      margin: auto;
      text-align: center;
      font-family: arial;
    }

    .title {
      color: grey;
      font-size: 18px;
    }

    button {
      border: none;
      outline: 0;
      display: inline-block;
      padding: 8px;
      color: white;
      background-color: #000;
      text-align: center;
      cursor: pointer;
      width: 100%;
      font-size: 18px;
    }

    a {
      text-decoration: none;
      font-size: 22px;
      color: black;
    }

    button:hover, a:hover {
      opacity: 0.7;
    }
    </style>
    </head>
    <body>



    <div class="card">
      <img src="https://raw.githubusercontent.com/ramseybe/campaign_prototype/main/pages/person.jpeg" alt="person" style="width:100%">
      <h1>person</h1>
      <p class="title">CEO & Founder, Example</p>
      <p></p>
      <div style="margin: 24px 0;">
        {}
      </div>
      <p><button>Donate!</button></p>
    </div>

    </body>
    </html>"""
    temp=get_icons(name,data)
    a=a.replace("{}",temp)
    
    name=name.lower()
    name=name.replace("-","_")
    name=name.replace(" ","_")
    name=name.replace("'","")

    a=a.replace("person",name)
    return a
# def checkbox_container(data):
#     st.subheader('Check the important issues to you:')
#     age = st.select_slider('How old are you?',["Pro","Neutral","Anti"])

#     for i in data:
#         st.checkbox(i.replace("_"," "), key='dynamic_checkbox_' + i)

# def get_selected_checkboxes():
#     return [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]

# def checked_to_list(data):
#     for i in data.columns():
#         pass
with left_column:
    abortion = st.select_slider('Stance on Abortion',["Pro","Neutral","Anti"],value="Neutral")
    guncontrol = st.select_slider('Stance on Guns',["Pro","Neutral","Anti"],value="Neutral")
    climate = st.select_slider('Stance on Climate Change',["Pro","Neutral","Anti"],value="Neutral")
    immigration = st.select_slider('Stance on Immigration',["Pro","Neutral","Anti"],value="Neutral")
    healthcare = st.select_slider('Stance on healthcare',["Pro","Neutral","Anti"],value="Neutral")
    issues = [abortion,guncontrol,climate,immigration,healthcare]

# checked = get_selected_checkboxes()

# st.write(checked)
def read_file():
    data = pd.read_csv(DATA_URL)
    data = data.drop(["Unnamed: 0"], axis=1)
    data = data.sort_values(by=['percent'])
    data['percent'].to_list()
    new = []
    for i in data['percent'].to_list():
        new.append(abs(i - 50))
    data['percent'] = new

    return data

def match(df,values):
    match = {}
    for index, row in df.iterrows():
        diff = 0
        for can_ideology, user_ideology in zip(row[4:].to_dict().values(), values):
            diff += abs(int(can_ideology) - int(user_ideology))
        match[index] = diff
    sorted_match = dict(sorted(match.items(), key=lambda item: item[1]))
    return list(sorted_match)[-6:]

if st.button('Submit'):
    
    with right_column:
#         create_card("patti")
#         components.html(create_card("aadland"),width=200, height=400)
        #st.markdown(create_card("aadland"))
#         image = Image.open(f'https://raw.githubusercontent.com/ramseybe/campaign_prototype/main/pages/can_pics/barrett.jpeg')
#         st.image(image)
#         st.image(
#             "https://raw.githubusercontent.com/ramseybe/campaign_prototype/main/pages/can_pics/barrett.jpeg",
#             width=400, # Manually Adjust the width of the image as per requirement
#         )


        html_string = "<h3>this is an html string</h3>"

        st.markdown(html_string, unsafe_allow_html=True)

        st.subheader('Candidates that best align with your views:')
        with st.container():
            data = read_file()
            good=[]
            for i in data.columns:
                if i in checked:
                    good.append(1)
                else:
                    good.append(0)
            good=good[4:]
            # st.write(good)
            matches= match(data,good)
            # st.write(matches)

            newdf=data.loc[data.index[matches]]
            for i,row in newdf.iterrows():

                t=row['name']
                t=t.replace(" ","_")
                t=t.lower()
                if row['party'] == 'R':
                    party = 'Republican'
                elif row['party'] == 'D':
                    party = 'Democrat'
                components.html(create_card_update(t),width=400, height=700)
#                 if t=='budzinski' or t=='daniels':
# #                     image = Image.open(f'pages/can_pics/{t}.jpg')
# #                     st.subheader(t.title()+', ' +party)
# #                     st.subheader(row['district'])
# #                     st.image(image)
#                     hasClicked = card(
#                           title=f"{t.title()} {party}",
#                           text="row['district']",
#                           image=f'can_pics/{t}.jpg'

#                         )

#                 else:
# #                     image = Image.open(f'pages/can_pics/{t}.jpeg')
# # #                     st.image(Image.open(f'can_pics/{t}.png'))
# #                     st.subheader(t.title()+', '+ party)
# #                     st.subheader(row['district'])
# #                     st.image(image)
#                         hasClicked = card(
#                           title=f"{t.title()} {party}",
#                           text="row['district']",
#                           image=f'can_pics/{t}.jpeg'

#                         )
                        
#                         st.write(hasClicked)
    

                    
                cls=['district', 'name', 'percent', 'party', 'abortion', 'gun_control', 'climate_change', 'gender_identity',
                 'pro_marijuana', 'captial_punishment', 'fracking', 'defense_spending', 'immigration',
                 'net_neutrality']
#                 for j in cls:
#                     if row[j] == 1:
#                         b=j.replace("_"," ")
#                         st.write(f"Pro-{b.title()}", end=" ")

                st.write(
                    f"Click here to donate to their campaign [{t} campaign](http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html)")

                # st.write("canidate url")
