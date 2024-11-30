# cs210project

## Description

Sabanci University CS210 Introduction to Data Science Course Fall 2023-2024 Term Project.  
This project analyzes the relationship between menstrual cycle phases and music preferences by examining whether there is a noticeable shift in the tempo and energy of music listened to during the luteal phase compared to the follicular phase.

Using Spotify's extended streaming history and my menstrual cycle data from the Health app from my phone, it explores potential patterns and correlations between physiological changes and musical preferences.

(It is obviously short since this is just the **project proposal**, with time the necessary parts will be added such as: used **tools, data visualization, limitations, findings** ect.

## Content Overview
**[Hypothesis](#hypothesis)**

**[Motivation](#motivation)**  

**[Data Source](#data-source)** 

**[Data Processing](#data-processing)**


## Hypothesis

Hypothesis: During the luteal phase of the menstrual cycle, there is a noticeable preference for slow-tempo music compared to the follicular phase, where high-energy, fast-tempo music is more frequently listened to.

## Motivation

The interaction between physiological states and behavioral patterns is a compelling area of study, particularly in understanding how hormonal changes across the menstrual cycle influence daily preferences. This project aims to explore whether there is a difference in music preferences, specifically tempo and energy levels, during the luteal and follicular phases of the cycle. 

This study provides an opportunity to investigate potential correlations and gain insights into the subtle effects of biological rhythms on everyday behaviors. This approach not only allows for the application of data science techniques to real-world, multidimensional data but also provides a framework for exploring personalized patterns in an empirical and scientifically grounded manner.


## Data Source

Data sources:

-   Extended streaming data that is directly exported from Spotify with a personal data request.
-   Menstural cycle data directly exported from Apple Health app.
-   Spotify Web API for obtaining empo or energy information of each song.

## Data Processing

The requested and exported data include many information.
- **The Spotify data:** exported as a JSON file, includes information such as the timestamp of when each song was played, track name, artist, and Spotify track URI.
- **The menstrual cycle data:** downloaded as a PDF, provides calendar-based visualizations indicating the dates of menstrual and other cycle phases.
- Here is a summary of the how will the process proceed:

- To enrich the Spotify data with features like tempo and energy, the Spotify Web API will be used. By extracting the spotify_track_uri from the JSON file, audio features for each song (e.g., tempo and energy levels) will be retrieved programmatically. For the menstrual cycle data, relevant phase intervals (e.g., follicular, luteal, menstrual) will be extracted either manually or through PDF parsing tools. These intervals will then be aligned with the Spotify data by matching timestamps, enabling analysis of music preferences during different phases of the cycle.


