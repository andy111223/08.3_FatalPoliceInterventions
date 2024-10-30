# Fatal Police Interventions Analysis
This repository contains a script that analyzes data on fatal police interventions in the USA. The analysis explores various aspects, including the relationship between race and mental health signs, the frequency of incidents by day of the week, and the number of interventions per 1,000 residents for each state. This repository is intended for the author's educational purposes only.

## Features
The script performs the following analysis steps:
1. Load Dataset
    - Load a dataset containing details on fatal police shootings in the USA.
2. Data Preparation
    - Fill missing values in the 'race' column with 'Unknown'.
    - Group the data by 'race' and 'signs_of_mental_illness' and count the combinations.
3. Percentage Calculation
    - Calculate the total number of victims per race.
    - Calculate the percentage of victims who showed signs of mental illness for each race.
    - Use .map() to add a column indicating the percentage of cases involving signs of mental illness.
4. Day of the Week Analysis
    - Add a column to the dataset indicating the day of the week on which each intervention occurred.
    - Count the interventions per day of the week and plot them to visualize the trends.
5. State Population Analysis
    - Load data on US states' populations and abbreviations from Wikipedia.
    - Clean and filter the data to match the state-level information in the intervention dataset.
    - Merge this data with the interventions dataset to calculate the number of interventions per 1,000 residents in each state.
## Installation
1. Clone the repository:

    `git clone https://github.com/andy111223/08.3_FatalPoliceInterventions.git`
2. Navigate to the project directory:

    `cd 08.3_FatalPoliceInterventions`
2. Install the necessary Python packages:

    `pip install pandas matplotlib`
## Usage
To run the analysis, execute the following command:

`python3 main.py` 

This will load the dataset, perform data analysis, and generate plots showing insights about the interventions.
## Requirements
    - Python 3
    - Pandas
    - Matplotlib