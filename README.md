# CMSE 495 - Campaign Finance Project

Sponsor - Dr. Randal Olsen

Team Members - Thao Nguyen, John Okoniewski, Vivian Pavlica, Ben Ramsey, Gregory Zavalnitskiy

[[Watch the proposal video](https://youtu.be/0gkptmWfgPM)]


<img src="https://img.youtube.com/vi/0gkptmWfgPM/maxresdefault.jpg" width="30%">

The purpose of the application is to allow users of the website to be able to select political issues that are important to them and match with candidates that could benefit the most from their donation.

This repository includes thr group's Intellectual Property (IP) Agreement which specifies the distribution of rights to the Olsen Finance Application. 

The dataset that is being used to build the application includes information of the top 50 closest races between House of Repsentatives candidates during the race in 2022 with 100 rows and 9 columns. The columns specifies information about the candidates' last names, their party, the districts they ran in, and predicted win percentage from FiveThirtyEight in 2022. Additionally, the dataset also includes information on ideology that corresponds with each candidates and their stances. The values for each ideology is as follow:

gun_control: 
  0 = stricter gun control
  1 = easy access to guns

healthcare: 
  0 = private healthcare
  1 = goverment sponsored healthcare

abortion:
  0 = pro-life 
  1 = pro-choice

climate_change:
  0 = do not support imposing taxes of carbon emissions 
  1 = support imposing taxes on carbon emissions

immigration_daca: 
  0 = support requiring unlawful immigrants to return to country of origin 
  1 = does not support requiring unlawful immigrants to return to country of origin

For candidates who do not have stances on any of the above ideologies or information could not be found, the values are -1 for each corresponding candidates and ideologies.
