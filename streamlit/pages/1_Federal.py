# # Libraries
# import streamlit as st
# import pandas as pd
# from PIL import Image
# issues=["abortion","gun_control", "climate_change",  "immigration", "healthcare"]
# checked=[]
# party=''
# st.set_page_config(
#     page_icon="📈",
#     layout="wide",)
# DATA_URL='https://raw.githubusercontent.com/ramseybe/hackathon_campaign/main/50_toss_up1.csv'
# st.header("Make a Difference This Election!", )
# left_column, right_column = st.columns([3,5])

# @st.cache
# def load_data(file):
#     data = pd.read_csv(file)
#     data=data.drop(["Unnamed: 0"],axis=1)
#     dict = data.to_dict()
#     return dict

# thing = load_data(DATA_URL)
# for key, val in thing.items():
#     needed = val
#     break


# def checkbox_container(data):
#     st.subheader('Check the important issues to you:')
#     for i in data:
#         st.checkbox(i.replace("_"," "), key='dynamic_checkbox_' + i)

# def get_selected_checkboxes():
#     return [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]

# def checked_to_list(data):
#     for i in data.columns():
#         st.write(i)
# with left_column:
#     checkbox_container(issues)
#     # st.write('You selected:')
#     # st.write(get_selected_checkboxes())

# checked = get_selected_checkboxes()

# # st.write(checked)
# def read_file():
#     data = pd.read_csv(DATA_URL)
#     data = data.drop(["Unnamed: 0"], axis=1)
#     data = data.sort_values(by=['percent'])
#     data['percent'].to_list()
#     new = []
#     for i in data['percent'].to_list():
#         new.append(abs(i - 50))
#     data['percent'] = new

#     return data

# def match(df,values):
#     match = {}
#     for index, row in df.iterrows():
#         diff = 0
#         for can_ideology, user_ideology in zip(row[4:].to_dict().values(), values):
#             diff += abs(int(can_ideology) - int(user_ideology))
#         match[index] = diff
#     sorted_match = dict(sorted(match.items(), key=lambda item: item[1]))
#     return list(sorted_match)[-6:]

# if st.button('Submit'):
#     with right_column:
#         st.subheader('Candidates that best align with your views:')
#         with st.container():
#             data = read_file()
#             good=[]
#             for i in data.columns:
#                 if i in checked:
#                     good.append(1)
#                 else:
#                     good.append(0)
#             good=good[4:]
#             # st.write(good)
#             matches= match(data,good)
#             # st.write(matches)

#             newdf=data.loc[data.index[matches]]
#             for i,row in newdf.iterrows():

#                 t=row['name']
#                 t=t.replace(" ","_")
#                 t=t.lower()
#                 if row['party'] == 'R':
#                     party = 'Republican'
#                 elif row['party'] == 'D':
#                     party = 'Democrat'
#                 if t=='budzinski' or t=='daniels':
#                     image = Image.open(f'pages/can_pics/{t}.jpg')
#                     st.subheader(t.title()+', ' +party)
#                     st.subheader(row['district'])
#                     st.image(image)

#                 else:
#                     image = Image.open(f'pages/can_pics/{t}.jpeg')
# #                     st.image(Image.open(f'can_pics/{t}.png'))
#                     st.subheader(t.title()+', '+ party)
#                     st.subheader(row['district'])
#                     st.image(image)

                    
#                 cls=['district', 'name', 'percent', 'party', 'abortion', 'gun_control', 'climate_change', 'gender_identity',
#                  'pro_marijuana', 'captial_punishment', 'fracking', 'defense_spending', 'immigration',
#                  'net_neutrality']
#                 for j in cls:
#                     if row[j] == 1:
#                         b=j.replace("_"," ")
#                         st.write(f"Pro-{b.title()}", end=" ")
#                 st.write(
#                     f"Click here to donate to their campaign [{t} campaign](http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html)")

#                 # st.write("canidate url")
