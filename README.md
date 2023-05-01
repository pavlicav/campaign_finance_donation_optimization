# Campaign Finance
### Thao Nguyen, John Okoniewski, Vivian Pavlica, Ben Ramsey, Gregory Zavalnitskiy
![Image failed to load, please click here to view the image instead](flowchart.jpg?raw)
## Background
In a democratic society, it is important for citizens to participate in the political process by making informed decisions when voting for candidates who will represent them. However, it can be challenging for voters to navigate the complex landscape of politics, particularly when it comes to understanding which candidates are most likely to win an election and which issues are most important to them. 

Moreover, election campaigns are often expensive, and candidates who are struggling to fund their campaigns may be less likely to win, even if they have strong beliefs and policies that align with voters' interests. This presents a challenge for both candidates and voters, as it limits the diversity of perspectives that can be represented in government. 

The purpose of this project is to address these challenges by providing a platform that helps users to make informed decisions when voting for candidates. Specifically, the project aims to highlight candidates who are struggling to fund their campaigns and would benefit the most from donations. By doing so, the project seeks to level the playing field and ensure that candidates with strong beliefs and policies have a better chance of winning, regardless of their financial resources. It should also be noted this project would not have be possible without the mentorship of Dr. Randy Olson and Dr. Dirk Colbry.
## Streamlit
[![Launch our Streamlit!]()](https://pavlicag-campaign-finance-donation-optimiz-streamlitmain-iuzsxf.streamlit.app/)

## Visual Explanation
<img src="https://youtu.be/GvZMf1gddpg" width="100%">

## IP Agreement
This repository includes the group's Intellectual Property (IP) Agreement which specifies the distribution of rights to the contents of this repository. 

## Dataset
https://github.com/fivethirtyeight/data/tree/master/election-forecasts-2022

The dataset that is being used to build the application includes information of the top 50 closest races between House of Repsentatives candidates during the race in 2022 with 100 rows and 9 columns. The columns specifies information about the candidates' last names, their party, the districts they ran in, and predicted win percentage from FiveThirtyEight in 2022. Additionally, the dataset also includes information on ideology that corresponds with each candidates and their stances. The values for each ideology is as follow:

**gun_control:** <br />
 0 = stricter gun control <br />
 1 = easy access to guns <br />

**healthcare:** <br /> 
  0 = private healthcare <br />
  1 = goverment sponsored healthcare <br />

**abortion:**
  0 = pro-life <br /> 
  1 = pro-choice <br />

**climate_change:** <br />
  0 = do not support imposing taxes of carbon emissions <br />
  1 = support imposing taxes on carbon emissions <br />

**immigration_daca:** <br />
  0 = support requiring unlawful immigrants to return to country of origin <br />
  1 = does not support requiring unlawful immigrants to return to country of origin <br />

For candidates who do not have stances on any of the above ideologies or information could not be found, the values are -1 for each corresponding candidates and ideologies.
