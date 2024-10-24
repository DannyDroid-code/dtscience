LifeExpectancy.csv dataset contains life expectancy data and health factors for 193 countries from the year 2000-2015 which was collected from the WHO data repository website and its corresponding economic data was collected from the United Nation website. It consists of 22 columns and 2938 rows.
Field
Description
Country
Country
Year
Year
Status
Developed or Developing
Life expectancy
Life Expectancy in years
Adult Mortality
Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)
infant deaths
Number of Infant Deaths per 1000 population
Alcohol
Alcohol, recorded per capita (15+) consumption
percentage expenditure
Expenditure on health as a percent of GDP per capita (%)
Hepatitis B
Hepatitis B (HepB) immunization coverage among 1-year-olds (%)
Measles
Measles - number of reported cases per 1000 population
BMI
Average Body Mass Index of the entire population
under-five deaths
Number of under-five deaths per 1000 population
Polio
Polio (Pol3) immunization coverage among 1-year-olds (%)
Total expenditure
General government expenditure on health (%)
Diphtheria
Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)
HIV/AIDS
Deaths per 1000 live births HIV/AIDS (0-4 years)
GDP
Gross Domestic Product per capita (in USD)
Population
Population of the country
thinness 1-19 years
Prevalence of thinness among children and adolescents for Age 10 to 19 (%)
thinness 5-9 years
Prevalence of thinness among children for Age 5 to 9 (%)
Income composition of resources
Productive use of resources
Schooling
Number of years of Schooling(years)


Rename some columns if they contain leading and trailing spaces (by removing spaces).
Which columns in the dataset have missing values and how many?
Drop all the columns from the DataFrame containing more than 15% percent of the missing values.
Replace the missing values in the remaining columns with the median 
Create a bar plot to find out whether the average age of death had increased globally in a period of 15 years i.e. between 2000 and 2015.
In which year, the average life expectancy was maximum?
Create a barplot for yearly life expectancy of developing and developed countries in a single bar chart.
You are provided with a video game sales dataset vgsales.csv. It consists of the following features:
Rank - Rank based on the number of units sold of a game. The most sold game is ranked 1.
Name - The name of a video game.
Platform - The platform (PC, PS4, XBox etc.) for which a game is released.
Year - The release year of a video game.
Genre - The genre of a video game.
Publisher - The publisher of a video game.
NA_Sales - Approximately, the total number of units sold (in millions) of a video game in North America.
EU_Sales - Approximately, the total number of units sold (in millions) of a video game in Europe.
JP_Sales - Approximately, the total number of units sold (in millions) of a video game in Japan.
Other_Sales - Approximately, the total number of units sold (in millions) of a video game in the rest of the world.
Global_Sales - Approximately, the total number of units sold (in millions) of a video game all over the world.

The Year and Publisher columns contain a few missing values. Treat them accordingly.
Convert the values contained in the Year column into integer values.
Find the top 10 best publishers of video games sold in North America.
Also, create publisher-wise line plots for the total number of units sold across different regions and the world.
Which video game publisher sells the most number of units globally and how much?
