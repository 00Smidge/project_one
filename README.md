# Project 1: Analyzing Flight Behavior Patterns

<div style="text-align: center;">
    <img src="images/airplane.jpeg" alt="Airplane" width="500" />
</div>

---

## Table of Contents

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Data Sources](#data-sources)
- [Quickstart Guide](#quickstart-guide)
- [Tech Stack Setup](#tech-stack-setup)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Interactive Map Features](#interactive-map-features)
- [Results and Insights](#results-and-insights)
- [Conclusion](#conclusion)
- [How to Use](#how-to-use)
- [References and Credits](#references-and-credits)
- [Deployment Workflow](#deployment-workflow)
- [Branch Discipline](#branch-discipline)
- [Team Members](#team-members)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This project is part of an AI boot camp that focuses on advanced data analysis. We explore and analyze flight behavior patterns, with a primary focus on uncovering trends related to flight delays. Using datasets from Kaggle and the OpenSky API, our objective is to identify significant patterns and correlations that can help airlines and stakeholders make informed decisions.

Through this analysis, we develop insights that highlight trends and anomalies in flight behavior, such as delays by airlines, airports, and time of day. This project serves as a practical application of our data analysis skills, demonstrating the techniques and methodologies we have learned throughout the AI boot camp.

---

## Objectives

- Analyze overall flight delay distribution to understand delay trends.
Examine delays by airlines and airports to identify underperforming entities.
- Investigate delays by time of day and day of the week to pinpoint peak delay periods.
- Perform correlation analysis to explore relationships between flight delays and factors such as distance and flight time.
- Provide actionable insights and recommendations for airlines and airports to optimize operations and reduce delays.

---

## Data Sources 

### Kaggle Flight Data
- [Kaggle Dataset](https://www.kaggle.com/datasets/mahoora00135/flights) The dataset from Kaggle includes historical flight data with over 1 million records. Key columns include:

| Column         | Description                                                  |
|----------------|--------------------------------------------------------------|
| `id`           | Unique flight identifier                                     |
| `dep_time`     | Actual departure time (24-hour format)                       |
| `arr_time`     | Actual arrival time (24-hour format)                         |
| `dep_delay`    | Departure delay in minutes                                   |
| `arr_delay`    | Arrival delay in minutes                                     |
| `carrier`      | Two-letter airline carrier code                              |
| `origin`       | Origin airport code                                          |
| `dest`         | Destination airport code                                     |
| `distance`     | Distance traveled (miles)                                    |
| `air_time`     | Total time in the air (minutes)

### OpenSky API Data
- [OpenSky API](https://github.com/openskynetwork/opensky-api) The OpenSky API provides real-time flight tracking. This data can be used to compare with historical data to enhance predictions or validate findings.

---

## Quickstart Guide

### 1. **Install Project Dependencies**

**All required dependencies are stored in [requirements.txt](requirements.txt)**

- Open the terminal (VS Code terminal shortcut: macOS `Control + tilde` | Windows `Ctrl + backtick`).
- Ensure you are in the project root directory, then run:

     ```bash
     pip install -r requirements.txt
     ```

### 2. **Download Flight Data from Kaggle**

   **(Note: Data is already included; skip unless necessary.)**  

- Steps to download the data:
     1. Create a free [Kaggle account](https://www.kaggle.com/account/login).
     2. In Kaggle's settings, generate an API key and download `kaggle.json`.
     3. Copy `kaggle.json` to the project root and set permissions (Linux/macOS/WSL):

        ```bash
        chmod 600 kaggle/kaggle.json
        ```

     4. Download the dataset:

        ```bash
        kaggle datasets download -d mahoora00135/flights
        ```

     5. Unzip and move the `flights.csv` file to the `data` folder.

### 3. **Install OpenSky API**

**(Optional: Use the OpenSky API if additional features are needed after completing tasks with the Kaggle data.)**

- Install OpenSky API dependencies:

     ```bash
     pip install src/python3/python
     ```

- If you encounter issues with `python3`, use `python`.

---

## Tech Stack Setup

This project utilizes a dynamic tech stack to run the web application and generate interactive maps in real-time. Here’s a breakdown of the stack:

- **Flask:** The backend web framework handling routing and server-side logic.
- **Folium:** For dynamic map creation, allowing us to visualize flight paths and data on the map.
- **Pyodide:** Runs Python code directly in the browser, enabling client-side execution for future expansion.
- **Jinja2 Templating:** Used in Flask for rendering dynamic content on the web pages.
- **DigitalOcean Droplet:** Our deployment platform, providing a serverless experience for running the Python project.
- **Gunicorn:** A WSGI HTTP server used to serve the Flask application in production.

## Exploratory Data Analysis (EDA)

In this section, we present statistical summaries and visualizations derived from the flight behavior data. These insights help us understand key performance indicators related to flight operations.

### Key Insights from Flight Data

- **Overall Delay Trends:** Most flights experience minimal delays, but certain airlines and airports show consistently higher delays.
- **Airline Performance:** Frontier Airlines and AirTran Airways were identified as underperforming in terms of on-time arrivals, while Alaska Airlines consistently arrives early.
- **Airport Efficiency:** Newark Liberty International Airport (EWR) had the highest average delays, while smaller regional airports tended to perform better.
- **Time-Based Delays:** Flights scheduled during late-night hours (12 AM to 3 AM) and afternoon peak times (5 PM to 7 PM) were more likely to be delayed.
- **Correlation Findings:** Distance and flight time showed weak correlations with delays, indicating that other factors (such as weather or operational inefficiencies) are likely contributing to delays.

### Sample Visualizations

#### Visualization 1 
![XXXXXX](images/XXXX.png)
Explanation:

#### Visualization 2 
![XXXXXX](images/XXXX.png)
Explanation:

- **Recommendation:** Add info here.... (Offer any recommendations based on your analysis.)

---

## Results and Insights

- Add info here.... (Describe the results you obtained, highlighting any important findings related to flight delays or predictions.) 

---

## Conclusion

Add info here... (Summarize the overall findings and the value of the analysis.)

### Future Work:
- Add info here... (List any areas for improvement or further analysis, such as incorporating weather data or expanding the dataset.) 

---

## How to Use

1. **Download Flight Data:** The dataset is available in the `data/` folder. You can also download the latest data from Kaggle as mentioned in the [Quickstart Guide](#quickstart-guide).
2. **Run the Jupyter Notebook:** Navigate to the `notebooks/` folder and open `flight_analysis.ipynb`. The notebook includes all code and explanations for the data analysis and machine learning models.
3. **View Visualizations:** All visualizations are saved in the `images/` folder.

## References and Credits
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [OpenSky Network API](https://openskynetwork.github.io/opensky-api/)
- [Kaggle Dataset](https://www.kaggle.com/datasets/mahoora00135/flights)

---

## Deployment Workflow

### 1. **Branching and Git Commands**

- Create a new branch for each task.
- If not on `main`, switch to it:

     ```bash
     git switch main
     git pull origin main
     git checkout -b <branch-name>
     ```

- Commit and push frequently:

     ```bash
     git status
     git add .
     git commit -m 'commit message'
     git push
     ```

- For the first push of a new branch:

     ```bash
     git push --set-upstream origin <branch-name>
     ```
---

## Branch Discipline

- **Protected Branch:** `main` – Managed by the project manager. No direct pushes allowed.
- **Testing Branch:** `stage` – All code contributions are merged into `stage` .
- Once `stage` is stable and conflict-free, it will be merged into `main`.

--- 

## Team Members

- **Steven Midgley**
- **Dane Larsen**
- **Leslie Barrera Dorantes**

--- 

## Acknowledgments

We would like to express our sincere gratitude to the following individuals and organizations for their invaluable contributions to this project:

- **Firas Obeid**: For providing guidance and support throughout the project.
- **Kaggle**: For the dataset that served as a foundation for our analysis.
- **OpenSky API**: For providing essential data to enhance our understanding of flight behavior.

Additionally, we appreciate the collaborative environment fostered by our AI boot camp, which enabled us to work together effectively and learn from each other.

Thank you to everyone who has contributed to this project’s success! 