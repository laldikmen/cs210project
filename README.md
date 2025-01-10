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



