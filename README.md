# CMSE 495 - Campaign Finance Project
![Image failed to load, click here to see](flowchart.pdf?raw=true "Optional Title")


Sponsor - Dr. Randal Olsen

Team Members - Thao Nguyen, John Okoniewski, Vivian Pavlica, Ben Ramsey, Gregory Zavalnitskiy

## Web App
https://pavlicag-campaign-finance-donation-optimiz-streamlitmain-iuzsxf.streamlit.app/

# Project Video
[[Watch video](https://youtu.be/0gkptmWfgPM)]
<img src="https://youtu.be/sITk6x0mjf8/maxresdefault.jpg" width="30%">



## Objective
The purpose of the application is to allow users of the website to be able to select political issues that are important to them and match with candidates that could benefit the most from their donation.

## IP Agreement
This repository includes the group's Intellectual Property (IP) Agreement which specifies the distribution of rights to the Olsen Finance Application. 

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
