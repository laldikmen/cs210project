# cs210project

## Description

Sabanci University CS210 Introduction to Data Science Course Fall 2023-2024 Term Project.  
This project analyzes the relationship between menstrual cycle phases and each phases hormonal effects on listening activity by examining whether there is a noticeable shift in the skipped track count during the luteal phase compared to the follicular phase.

Using Spotify's extended streaming history and my menstrual cycle data from the Health app from my phone, it explores potential patterns and correlations between physiological effects of hormonal changes and musical listening habits.


## Content Overview
**[Hypothesis](#hypothesis)**

**[Motivation](#motivation)**  

**[Data Source](#data-source)** 

**[Data Processing](#data-processing)**


## Hypothesis

Hypothesis: The number of skipped songs on Spotify increases during the luteal phase of the menstrual cycle compared to the follicular phase within same menstrual cycle.

## Motivation

The interaction between physiological states and behavioral patterns is a compelling area of study, particularly in understanding how hormonal changes across the menstrual cycle influence daily preferences. This project aims to explore whether there is a difference in song skipping frequency, during the luteal and follicular phases of the cycle. 

Audial sensitivity and irritability are higher in the luteal phase due to declining estrogen and serotonin levels, which may lead to increased indecisiveness or dissatisfaction with chosen songs, might make users less satisfied with song choices, leading to frequent skipping. This study provides an opportunity to investigate potential correlations and gain insights into the subtle effects of biological rhythms on everyday behaviors. This approach not only allows for the application of data science techniques to real-world, multidimensional data but also provides a framework for exploring personalized patterns in an empirical and scientifically grounded manner.


## Data Source

Data sources:

-   Extended streaming data that is directly exported from Spotify with a personal data request.
-   Menstural cycle data directly exported from Apple Health app.

## Data Processing

The requested and exported data include many information.
- **The Spotify data:** exported as a JSON file, includes information such as the timestamp of when each song was played, track name, artist, information on skipping and shuffle as well as Spotify track URI.
- **The menstrual cycle data:** downloaded as a PDF, provides calendar-based visualizations indicating the dates of menstrual and other cycle phases.
- Here is a summary of the how the process proceeded:

- first I cleaned the menstrual cycle data to ensure correct phase assignment for each day.
- Data Collection and Preprocessing:
Menstrual Cycle Data:
Menstrual cycle records were transformed from PDF to CSV format.
Phase intervals (follicular, ovulation, luteal) were clarified by identifying specific start and end dates for each phase.
Spotify Streaming History:
Streaming history was collected in JSON format and converted to CSV.
Key metrics, such as timestamps (ts) and whether songs were skipped (skipped), were extracted for analysis.
High Volume Notifications Data:
Apple Health data (HKQuantityTypeIdentifierHeadphoneAudioExposure) was also converted to CSV and analyzed for notifications during each phase.Methodology:
Visualization of High-Volume Notifications:
By Cycle Phases: A bar chart was created to visualize the number of high-volume notifications across each menstrual cycle phase.
Comparison of Follicular vs. Luteal Phases: A separate bar chart compared the total high-volume notifications between the follicular and luteal phases.
Daily Notifications: A daily bar chart highlighted trends in notifications over time.
Skipped Songs Analysis:
By Phase Intervals: The number of skipped songs was calculated for each phase interval, and a bar chart was generated to visualize the counts.
Comparison of Averages: The average number of skipped songs for follicular and luteal phases was calculated and visualized using a comparative bar chart.
Statistical Validation:
Scientific and data science methodologies were applied to validate the hypothesis. The statistical significance of the difference in skipped song counts between luteal and follicular phases was tested using appropriate methods (e.g., t-tests, ANOVA).Results:
High-Volume Notifications:
Notifications were found to vary across phases, with distinct patterns emerging in daily and phase-specific comparisons.
A clear distinction was observed in notification counts between follicular and luteal phases.
Skipped Songs:
The analysis revealed a statistically significant increase in skipped song counts during the luteal phase compared to the follicular phase.
The difference was validated through scientific testing, confirming the hypothesis.

-> The findings support the hypothesis that the number of skipped songs on Spotify increases during the luteal phase of the menstrual cycle compared to the follicular phase. This research highlights a potential link between physiological changes associated with menstrual phases and behavioral tendencies in music consumption. These insights pave the way for further interdisciplinary studies exploring the intersection of health, psychology, and digital behavior analytics.



Notes: it was a different prject during the proposal time but i had to change/update it due to a update on spotify web api. apparently now it is not posibble to fetch tempo and energy info from web api usin uri.



