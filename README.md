# Unit-10-SQLAlchemy-challenge
<img src="/Images/Hawaii2020.jpg" width="1080">

This is a two part challenge, the first one is Climate Analysis and Exploration with SQL Alchemy and Jupyter Notebook and the second one is creating Climate Apps with Flask and SQL Alchemy  

## PART 1 : Climate Analysis and Exploration
SQL Alchemy Homework - Hawaii Weather!
### Precipitation Analysis
Looking at the table below, we can conclude that Hawaii, is a low precepitation area with only a few high precepitation days. 

These are the last 12 months (up to 23 October 2017) figure of the percipitation in Hawaii 
<img src="/Graphs/Unit10-1.png" width="600">

### Stations Analysis
There are 9 Weather Stations in Hawaii, with the most active station is USC00519281 Weather Station
The normal temperature data in USC00519281 are Min Temp = 54.0, Avg Temp = 71.7, Max Temp = 85.0

As can be seen in the graph below, most of the days in Station are in the comfortable weather between 70 - 80 degree F
<img src="/Graphs/Unit10-2.png" width="600">

## Temperature Analysis I
Both the graph and the statistical analysis below, it can be seem that Hawaii enjoy moderate temperature all year long, 
with average temperature difference between June and December only about 4 degrees F.<br>
<img src="/Graphs/Unit10-4.png" width="720">   <img src="/Graphs/Table3.png" width="180"> 

However to my surprise, when I perform the Ttest, the pvalue of result is very low at 4.193529835915755e-187 

## Temperature Analysis II
This part analysing the temperature of a certain future holiday date, which I put as '2021-10-15' to '2021-11-05'
This challenge has 3 parts :
### Trip Average Temperature
Which calculate the average temperature (and the max and min) for the duration of the trip from the lastest year of the data   
 <img src="/Graphs/Unit10-5.png" width="300"> 

### Daily Normal Temperature
Which show the Max, Avg, and Min temperatures for each dates during the duration of the trip from the data.
Our analaysis shown that the Maximum, Average, and Minimum temperatures for the duration of the trip are 68.0 F, 76.4 F, 81.0 F. 
<img src="/Graphs/Unit10-6.png" width="600"> 

### ### Daily Rainfall Average
Which calculate the rainfall for each weather stations for the duration of the trip using the previous year's matching dates.
<img src="/Graphs/Table2.png" width="620">
<img src="/Graphs/barchart.png" width="600">


## PART 2 : Climate App
For this part we created [app.py](https://github.com/vivisantosa/Unit-10-SQLAlchemy-challenge/blob/master/app.py) codes for static and dynamic queries
Here are the screenshoots of the queries
- Landing page <br/>
  <img src="/Images/p1.png" width="600"> 
- Static queries <br/>
  <img src="/Images/p2.png" width="600"> 
- Dynamic queries<br/>
  <img src="/Images/p3.png" width="600"> 


