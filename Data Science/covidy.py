#pip  install plotly
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("covid_data.csv")
data.set_index('OBJECTID')

print(data.head(5))

data = data[['Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths', 'Active']]
data.columns = ('State','Country','Last Update','Lat','Long','Confirmed','Recovered','Deaths','Active')

print(data.head(10))
data['State'].fillna(value = '', inplace = True)

print(data.head(10))

import datetime as dt

def convertTime(t):
  t = int(t)
  return dt.datetime.fromtimestamp(t)

data = data.dropna(subset = ['Last Update'])
data['Last Update'] = data['Last Update'] / 1000
data['Last Update'] = data['Last Update'].apply(convertTime)


print(data.head(10))

# # Top 10 most affected countries (Bubble Plot)

top10_confirmed = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().nlargest(10).sort_values(ascending = False))

print(top10_confirmed)


# fig1 = px.scatter(top10_confirmed, x = top10_confirmed.index, y = 'Confirmed', size = 'Confirmed', size_max = 120, color = top10_confirmed.index, title = "Top 10 Countries by Confirmed Cases" )
# fig1.write_html('first_figure.html', auto_open=True)

# # Top 10 most affected countries (Bubble Plot)

# top10_deaths = pd.DataFrame(data.groupby('Country')['Deaths'].sum().nlargest(10).sort_values(ascending = False))

# # #print(top10_confirmed)


# fig2 = px.scatter(top10_deaths, x = top10_confirmed.index, y = 'Deaths', size = 'Deaths', size_max = 120, color = top10_confirmed.index, title = "Top 10 Countries by Deaths" )
# fig2 = px.bar(top10_deaths, x = 'Deaths', y = top10_deaths.index, height = 600, color = 'Deaths', orientation = 'h',
#             color_continuous_scale = ['deepskyblue','red'], title = 'Top 10 Death Cases Countries')
# fig2.write_html('second_figure.html', auto_open=True)

# # # c. Top 10 recovered countries (Bar plot)

# top10_recovered = pd.DataFrame(data.groupby('Country')['Recovered'].sum().nlargest(10).sort_values(ascending = False))
# fig3 = px.bar(top10_recovered, x = top10_recovered.index, y = 'Recovered', height = 600, color = 'Recovered',
#              title = 'Top 10 Recovered Cases Countries', color_continuous_scale = px.colors.sequential.Viridis)
# fig3.write_html('third_figure.html', auto_open=True)
# """

# USA

topstates_us = data['Country'] == 'US'
topstates_us = data[topstates_us].nlargest(5, 'Confirmed')
# Brazil
topstates_brazil = data['Country'] == 'Brazil'
topstates_brazil = data[topstates_brazil].nlargest(5, 'Confirmed')
# India
topstates_india = data['Country'] == 'India'
topstates_india = data[topstates_india].nlargest(5, 'Confirmed')
# Russia
topstates_russia = data['Country'] == 'Russia'
topstates_russia = data[topstates_russia].nlargest(5, 'Confirmed')

# # # USA 
fig5 = go.Figure(data = [
    go.Bar(name = 'Active Cases', x = topstates_us['Active'], y = topstates_us['State'], orientation = 'v'),
    go.Bar(name = 'Death Cases', x = topstates_us['Deaths'], y = topstates_us['State'], orientation = 'v')
])
fig5.update_layout(title = 'Most Affected States in USA', height = 600)
fig5.write_html('fifth_figure.html', auto_open=True)

# fig6 = go.Figure(data = [
#     go.Bar(name = 'Recovered Cases', x = topstates_brazil['State'], y = topstates_brazil['Recovered']),
#     go.Bar(name = 'Active Cases', x = topstates_brazil['State'], y = topstates_brazil['Active']),
#     go.Bar(name = 'Death Cases', x = topstates_brazil['State'], y = topstates_brazil['Deaths'])
# ])
# fig6.update_layout(title = 'Most Affected States in Brazil', barmode = 'stack', height = 600)
# fig6.write_html('sixth_figure.html', auto_open=True)()

# time_series = pd.read_csv('WHO-COVID-19-global-data.csv', encoding = 'ISO-8859-1')
# time_series.columns = ("Date_reported","Country_code","Country","WHO_region","New_cases","Cumulative_cases","New_deaths","Cumulative_deaths")

# time_series.head()

# time_series["Date_reported"] = pd.to_datetime(time_series["Date_reported"])

# time_series_dates = time_series.groupby('Date_reported').sum()
# print(time_series_dates)

# fig11 = go.Figure()
# fig11.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['Cumulative_cases'], fill = 'tonexty',
#                           line_color = 'blue'))
# fig11.update_layout(title = 'Cumulative Cases Worldwide')
# fig11.write_html('secent_figure.html', auto_open=True)


# fig12 = go.Figure()
# fig12.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['Cumulative_deaths'], fill = 'tonexty',
#                           line_color = 'red'))
# fig12.update_layout(title = 'Cumulative Deaths Worldwide')
# fig12.write_html('secent1_figure.html', auto_open=True)

# fig13 = go.Figure()
# fig13.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['New_cases'], fill = 'tonexty',
#                           line_color = 'gold'))
# fig13.update_layout(title = 'Daily New Cases Worldwide')
# fig13.write_html('secent2_figure.html', auto_open=True)


# fig14 = go.Figure()
# fig14.add_trace(go.Scatter(x = time_series_dates.index, y = time_series_dates['New_deaths'], fill = 'tonexty',
#                           line_color = 'hotpink'))
# fig14.update_layout(title = 'Daily Death Cases Worldwide')
# fig14.write_html('secent3_figure.html', auto_open=True)



