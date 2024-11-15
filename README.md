# SpaceY - Predicting Rocket Launch Prices and Reusability

## Project Overview

In this capstone project, I’ll take the role of a data scientist working for **SpaceY**, a new rocket company aiming to compete with SpaceX. The goal is to **predict launch prices** by gathering data on **SpaceX's Falcon 9 rocket launches** and building dashboards to estimate launch costs. Additionally, I will predict if SpaceX will **reuse the first stage** of the rocket using machine learning models.

## Objectives
1. **Gather SpaceX Launch Data**  
   Use the **SpaceX REST API** and **web scraping** techniques to collect data on past rocket launches, including rocket specifications, payload mass, launch site, and more.

2. **Data Wrangling**  
   Clean and preprocess the data by handling null values, filtering out Falcon 1 launches, and performing necessary transformations.

3. **Predict Reusability**  
   Use machine learning to predict if SpaceX will successfully land and reuse the rocket's first stage.

## Data Sources

- **SpaceX REST API**  
  I will use the SpaceX API to gather data on past launches. This data includes rocket specifications, payloads, and landing outcomes. The main endpoint used is:  
  `api.spacexdata.com/v4/launches/past`
  
- **Web Scraping**  
  In addition to the API, I will scrape **Falcon 9 launch data** from Wikipedia tables using Python’s **BeautifulSoup** package.

## Key Tasks Completed
All Jupyter Notebook files have been uploaded to this repository
1. **API Data Collection**  
   Collected data using the SpaceX API and transformed it into a Pandas DataFrame for analysis.

2. **Web Scraping for Launch Records**  
   Scraped launch tables from Wiki pages and converted them into structured datasets.

3. **Data Wrangling**  
   Cleaned the data by filtering out Falcon 1 launches and handling missing values in the **PayloadMass** column using mean imputation.
