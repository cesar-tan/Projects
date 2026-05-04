# Google-Data-Analytics-Capstone

## Introduction

### Overview
For this case study, I played the role as a junior data analyst working in the marketing analytics team at Cyclistic, a bike-share company in Chicago. The director of marketing believed the company’s future success depends on maximizing the number of annual memberships. The marketing analytics team wanted to understand how casual riders and annual members use Cyclistic bikes differently. The team will then create a marketing strategy aimed towards the casual members, and it will aim to convert these casual members into annual members. However, before going through with the marketing campaign, it must be approved by the executive team, so the proposed marketing strategies must be backed up with data insights.

### **Characters and Teams**

**Cyclistic** - a bike-share program with over 5800 bicycles and 600 docking systems. They offer reclining bikes, hand tricycles, and cargo bikes, making bike-share more inclusive to people with disabilities and riders who cannot use a standard two-wheeled bike. The majority of riders use traditional bikes; about 8% of users use the accessible options. Most riders use Cyclistic's bikes for leisure, but about 30% use them for daily commutes.

**Marketing director** - responsible for the development of campaigns and initiatives to promote the bike-share program. These may include email, social media, and other channels.

**Cyclistic marketing analytics team** - a team of data analysts who are responsible for collecting, analyzing, and reporting data that helps guide Cyclistic marketing strategy. In this scenario, you joined this team six months ago and have been busy learning about Cyclistic's mission and goals - as well as how you, as a junior data analyst, can help Cyclistic achieve them.

**Cyclistic executive team** - the detail-oriented executive team that will decide whether to approve the recommended marketing program.

### **About the Company**

Founded in 2016, Cyclistic rapidly became a popular bike-share company in Chicago. The company owns 5824 geotracked bicycles in a network of 692 stations across the city. Riders can unlock a bike from any one station, and return it at any other station in the network at any time.

Cyclistic offers 3 different pricing plans: single-ride passes, day passes, and annual memberships. People who purchase the single-ride or day passes are called casual riders, while thos who order the annual memberships are annual members.

Cyclistic's financial analysts have found that annual memberships are more profitable compared to the single-ride and full day passes. The marketing director believes that Cyclistic can grow more in the future if the company aims to convert casual riders into annual members. Instead of aiming a marketing campaign to new consumers, the director thinks there is a good chance to convert existing casual riders to annual members. It is up to the marketing analytics team to look through Cyclistic's historical data to find patterns, insights, and understand the differences between casual riders and annual members. The team will then use these insights to create a marketing strategy aimed towards the casual members in hopes of converting them into annual riders.

## Data Sources

The data can be found and downloaded from [here](https://divvy-tripdata.s3.amazonaws.com/index.html). The data is formatted as CSV files, each containing one month's trip data. For analysis, I used data from November 2024 to October 2025. Each file has 13 columns containing the following information:

- A ride's distinct ride ID
- The type of bike used
- The start and end times for the trip
- Information regarding the starting and ending locations (station names, station IDs, latitude and longitude values)
- The type of user, either defined as "member" (with an annual membership) or "casual" (for casual users)

## Cleaning and Transformations

For the data cleaning process, I did the following steps:

- Removed duplicate trips, rows with empty values, rows with errors. This involved removing trips with duplicate ride IDs, and removing trips with missing information. Also removed trips that started outside of the specified date range (some trips started on October 2024, and those were removed).
- Converting the start and end times to datetime format (initially stored as strings).
- Added extra time columns to examine data (by month, day, hour).
- Added a column for a trip's duration.
- Removed trips with negative trip duration, i.e., trips where start times occur earlier than the end times.

## Analysis and Summary

For the analysis, I did the following tasks using Python:

- Examined the number of trips by members and casual riders.
- Viewed the percentage of trips by bike type, and the breakdown of bike types used in both groups.
- Looked at the average trip duration by both rider groups.
- Examined the number of trips for both groups by hour, month, and day.
- Looked at starting and ending stations that saw the most activity from both groups.

The code and results from the analysis can be found in [case-study-code.ipynb](case-study-code.ipynb). From the analysis, we can conclude the following about how casual riders and annual members use the bike share service:

- About 64.23% of bike trips in the last 12 months were from annual members; the other 35.77% of trips were from casual riders.
- About 53.52% of all trips were done with classic bikes, 46.48% of trips used electric bikes. When looking at both respective groups, the percentage of bike trips by bike type was similar (member: 54.76% classic vs. 45.24% electric, casual: 51.29% classic vs. 48.71% electric)
- The average ride duration for annual members was 12m 11s; the average ride duration for casual riders was 22m 19s.
- Both groups experienced similar trends when looking at number of rides by month. From November 2025 to January 2025, the number of rides decreased. The number of rides then increased from January to August 2025. For annual members, the number of trips increased in September before falling in October. On the other hand, the number of rides from casual users experienced a sharp decline from August to October.
- When counting trips by days, for annual members, the days with the least amount of bike trips were Saturday and Sunday, but these were the most popular days for casual members to go on bike trips.
- When looking at trips by starting hour, the peak hour is 5pm for both casual riders and members. For members, there is a spike in usage from 7-9am.
- Both groups have different start and end stations for their trips.

In addition to Python, I used Power BI to make a simple [report](PBIReport.png) to show the findings from the data in an easy-to-read format. With Power BI, I was also able to use map visuals to plot the most popular starting stations for both rider groups. When looking at ending stations and comparing to starting stations, the maps looked identical, so I decided to leave out the map for ending stations. From the map visual, I saw that usage for members was more popular in the inner city areas, while for casual riders, usage was focused more in areas closer to the city's waterfront.

## Recommendations

Based on the results from the analysis, I can give the following recommendations on how Cyclistic can deliver effective advertisements:

- Run advertisements focusing on benefits of Cyclistic's annual membership.
- Offer additional benefits to members over casual riders at peak usage times.
- Run ads that encourage the usage of bikes during off-peak hours, pushing casual riders to bike more frequently to the point where a membership feels worth it to them.
- If possible, add a trial membership to casual riders so they can see the benefits of the membership. Additionally, add promotions for subscriptions to entice the casual riders.
