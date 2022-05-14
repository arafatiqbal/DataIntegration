from calendar import day_abbr
from itertools import count
import pandas as pd
from regex import E

county_info = pd.read_csv('acs2017_census_tract_data.csv',usecols=['State','County','TotalPop','Poverty','IncomePerCap'])
cf = county_info.groupby(['State','County']).sum()

state = county_info.loc(county_info["State"] == "Oregon")
percent = state.loc[county_info["County"] == "Melheur County"]
print(percent)

#Cunties
# result = county_info[county_info["County"] == "Malheur County"].groupby(['State','County']).sum()
# print(result)

#Poverty %
count = percent["Poverty"].div(100)
per = (count.sum() / count.count()) * 100
print ("% Poverty", per)