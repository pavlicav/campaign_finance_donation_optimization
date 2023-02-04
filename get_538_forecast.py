# Script to get latest forecast from 538 to dataframe
# Vivian Pavlica 2/1/22

# Import Pandas
import pandas as pd

# Download data from 538 github on close races
datas = pd.read_csv("https://projects.fivethirtyeight.com/2022-general-election-forecast-data/house_district_toplines_2022.csv",
                     low_memory=False)

# Filter to latest forecast date and choose lite model
latest_date = max(datas.forecastdate.unique())
datas = datas.query('forecastdate == @latest_date').query('expression == "_lite"')

# Drop unneccecary columns
sum_data = datas[['branch', 'district', 'forecastdate', 'name_D1',
       'name_R1','winner_D1', 'winner_R1', 'tipping', 'timestamp']]

sum_data = sum_data.dropna() # Drops rows that are non-contested

# Export to CSV
sum_data.to_csv("latest_forecast.csv", index=False)
