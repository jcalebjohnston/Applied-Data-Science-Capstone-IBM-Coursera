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
   Classifying all Success as "1" and all Failures as "0" by introducing a new column.

4. **Exploratory Data Analysis**  
   Performed EDA with SQL, and visualization techniques and later implemented one hot encoding on dataset.

5. **Interactive Visual Analysis and Dashboarding**  
   Visualized Launch Sites on maps for further analysis with Foilum and built interactive dashboads using Ploty Dash to gather further insights into dataset.

6. **Predictive Modeling**  
   Implemented various Machine Learning Techniques, evaluated them and selected the best fir fro the problem at hand.

## Installation
1. Clone this repository to your local machine:
   `https://github.com/jcalebjohnston/Applied-Data-Science-Capstone-IBM-Coursera.git`
2. Install the necessary libraries, All necessary libraries are listed in the Jupyter notebooks:
```pip install requests beautifulsoup4 pandas scikit-learn```
3. Run the Jupyter notebooks for data collection, cleaning, and modeling. In the format of the ** Key Tasks Completed** Section
