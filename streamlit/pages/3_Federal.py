# Libraries

import streamlit as st
import streamlit.components.v1 as components
# from streamlit_custom_slider import st_custom_slider
import pandas as pd
from PIL import Image
import numpy as np
# from streamlit_card import card
# from IPython.core.display import HTML


# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'
# if 'key' not in st.session_state:
#     st.session_state.key = 'value1'
    
# st.write(st.session_state)
    
# st.write(st.session_state.key)
issues=["abortion","gun_control", "climate_change",  "immigration", "healthcare"]
checked=[]
party=''
st.set_page_config(
    page_icon="📈",
    layout="wide")
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



def get_icons(vallist):
    temp=""""""
    template="""<span class="fa-stack fa-2x">
        <i class="fa fa-idea fa-stack-1x"></i>
        <i class="fas fa-ban fa-stack-2x" style="color:Tomato"></i>
        </span>
        """

#     vallist=list(file.iloc[name][4:9])
    vals=['gun_control','healthcare','abortion','climate_change', 'immigration' ]
    idea={'abortion':'suitcase-medical', 'gun_control':'gun', 'climate_change':"leaf", 
           'immigration':"child", 'healthcare':"stethoscope"}
    for i,val in zip(vallist,vals):
        #missing/dont know
#         print(j,idea[j])
        

        #pro guns
        if i == 0:
            pass
        elif i==1:
            t1=template.replace("idea",idea[val])
            t1=t1.replace("Tomato","#ffffff00")
            temp = temp + t1

        elif i ==-1:
            

            t1=template.replace("idea",idea[val])
#             t1=t1.replace("Tomato","#ffffff00")
            temp = temp + t1

    return temp



def create_card_update(person,dis,party,full,v):
    
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
      <img src="https://raw.githubusercontent.com/ramseybe/campaign_prototype/main/pages/person.jpeg" alt="person" width="100%" height="300">
      <h1>full</h1>
      <p class="title"> district, party</p>
      <p></p>
      <div style="margin: 24px 0;">
        {}
        </span>
      </div>
      <p ><button onclick="location.href='http://www.stackoverflow.com/'" type="button">Contact</button></p>
    </div>
    </body>
    </html>"""
#     st.write(name)
#     st.write(i)
    temp=get_icons(v)
    a=a.replace("{}",temp)
    
    name=person.lower()
    name=name.replace("-","_")
    name=name.replace(" ","_")
    name=name.replace("'","")
    a=a.replace("person",name)
#     st.write(list(data.iloc[i])[0])
    a=a.replace("district",dis)
    a=a.replace("party",party)
    a=a.replace("full",full)
    
    return a

with left_column:
    states = [ 'N/A','AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

    option = st.selectbox(
        'Do you want to only see results from a certain state?',
        states)

    #make numpy
    np_vals=np.arange(-1, 1, 0.02).tolist()
    np_vals[50]=0.0
    np_vals[99]=1.0
    #make list
    mid=[" "*i for i in range(98)]
    mid[49]="Neutral"
#     'abortion':'suitcase-medical', 'gun_control':'gun', 'climate_change':"leaf", 
#            'immigration':"child", 'healthcare':"stethoscope"
    #abortion
    temp_list=["Pro-Choice"]+mid+["Pro-Life"]
    abortion = st.select_slider('Stance on Abortion',temp_list,value="Neutral")
    abortion = np_vals[temp_list.index(abortion)]
    abr= """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
        <span class="fa-stack fa-2x">
         <i class="fa fa-suitcase-medical fa-stack-1x"></i>
        <i class="fas fa-ban fa-stack-2x" style="color:Tomato"></i>
        </span>
        """
    components.html(abr,width=200, height=200)
    abr= """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css">
        <span class="fa-stack fa-2x">
         <i class="fa fa-suitcase-medical fa-stack-1x"></i>
        <i class="fas fa-ban fa-stack-2x" style="color:#ffffff00"></i>
        </span>
        """
    components.html(abr)
    #guns
    temp_list=["Gun Control"]+mid+["Gun Rights"]
    guncontrol = st.select_slider('Stance on Guns',temp_list,value="Neutral")
    guncontrol= np_vals[temp_list.index(guncontrol)]
    #climate
    temp_list=["Believes in Climate Change"]+mid+["Disputes Climate Change"]
    climate = st.select_slider('Stance on Climate Change',temp_list,value="Neutral")
    climate= np_vals[temp_list.index(climate)]
    #immigration
    temp_list=["Open Border"]+mid+["Closed Border"]
    immigration = st.select_slider('Stance on Immigration',temp_list,value="Neutral")
    immigration= np_vals[temp_list.index(immigration)]
    #healthcare
    temp_list=["Socalized Healthcare"]+mid+["Private Healthcare"]
    healthcare = st.select_slider('Stance on healthcare',temp_list,value="Neutral")
    healthcare= np_vals[temp_list.index(healthcare)]
    issues = [abortion,guncontrol,climate,immigration,healthcare]
    #st.write(issues)
    

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


#     return list(sorted_match)[-6:]
def get_scores(user_position, df):
    # Inputs:
    # User Positions - iterable length 5 of user's positions
    # positions - pandas dataframe containing columns 
    #           "gun_control", "healthcare","abortion", 'climate_change', 'immigration_daca'
    #
    # return: np array of how close each candidate is to user's position
    
    # Convert to numpy
    position_array = df[["gun_control", "healthcare","abortion", 'climate_change', 'immigration_daca']].to_numpy()
    # sets NA to 0, positions to 1 or -1
    position_array[position_array == 0] = -2
    position_array[position_array == -1] = 0
    position_array[position_array == -2] = -1
    
    # make array with same shape as position array, with user's positions
    p = np.array(user_position)
    p = np.expand_dims(p,0)
    tile = np.tile(p, (len(position_array),1))
    scores = abs((tile - position_array))
    sums = 10-np.sum(scores, 1)
    filter_vals = np.unique(np.sort(sums)[0:6])
    
    return sums

def get_top_6(user_preferences,state="N/A"):
    
    finance_data = "538_FEC_Won_Opponent_Combined_Dataset.csv"
    position_data = "files/top100_top5.csv"
    save_as = "filter_results.csv"
    
    df = pd.read_csv(finance_data)
    positions = pd.read_csv(position_data)
    df.index = list(df["Unnamed: 0"])
    # Setting the "Universal Index"
    positions.index = ["-".join([positions["district"].iloc[i], positions["party"].iloc[i]]) for i in range(len(positions))]
    positions.head()
    positions = positions.join(df, rsuffix="_")
    sums = get_scores(user_preferences, positions)
    positions["score"] = sums
    if state == "N/A":
        top_6 = positions.sort_values(by = ["score", "tipping"], ascending = True).iloc[0:6:].reset_index(drop = True)
#     top_6.to_csv(save_as)
    else:
        temp = positions[positions["district"].str.contains(state)]
        top_6 = temp.sort_values(by = ["score", "tipping"], ascending = True).iloc[0:6].reset_index(drop = True)
    return top_6


tempdf=get_top_6(issues,option)
# if st.button('Submit'):
#     tempdf=get_top_6(issues)
    
with right_column:
    #st.dataframe(tempdf)
    st.subheader('Candidates that best align with your views:')
    with st.container():

        for i,row in tempdf.iterrows():
            #st.write(row['name'], row['district'],row['party'],row['name_'],[row['gun_control'],row['healthcare'],row['abortion'],row[ 'climate_change'],row['immigration_daca']])
            t=row['name']
            t=t.replace(" ","_")
            t=t.lower()
            if row['party'] == 'R':
                party = 'Republican'
            elif row['party'] == 'D':
                party = 'Democrat'

#                 image = Image.open(f'streamlit/pages/can_pics/{t}.jpeg')
            try:
                l=[row['gun_control'],row['healthcare'],row['abortion'],row[ 'climate_change'],row['immigration_daca']]
                st.write()
                components.html(create_card_update(row['name'],row['district'],row['party'],row['name_'],l),width=300, height=700)

            except:
                st.write(create_card_update(row['name'],row['district'],row['party'],row['name_'],[1,0,-1,-1,-1]))
                #st.write(f"Click here to donate to their campaign [{t} campaign](http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html)")

