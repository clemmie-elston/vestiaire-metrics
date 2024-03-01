# **Vestiaire Metrics**


## Project Overview

`vestiaire-metrics` is a comprehensive analytics project designed to extract, process, and visualize data from a PostgreSQL database hosted on ElephantSQL. The project aims to provide insightful metrics about customer interactions, preferences, and behaviors on the Vestiaire Collective platform.


### Architecture

The project architecture is structured around several key components:

- **Data Source:** Raw data is stored in a PostgreSQL database managed through ElephantSQL, ensuring robustness and scalability.
- **Analysis Queries:** A series of SQL queries were developed to extract meaningful insights from the data, focusing on customer interactions and product listings. 
- **Python Automation:** A Python script was implemented to automate the execution of SQL queries, fetching results directly from the database.
- **Visualization:** Further analysis was pursued through additional SQL queries, with the aim of visualizing the results in a slide deck for easier interpretation and sharing.


## 1. Data Injection


### Database Setup on ElephantSQL

The PostgreSQL database was set up on ElephantSQL, a cloud-hosted PostgreSQL service offering. The process involved:

1. **Creating a New Instance:** A new database instance was initialized on ElephantSQL, which provided a URL used to connect to the PostgreSQL database.
2. **Schema Creation:** Tables were created to store data related to customer listings, product attributes, and interactions.
3. **Data Import:** CSV files containing extracts of data were imported into the database, involving careful management of data types and integrity.


### Challenges Encountered

Throughout this task, several challenges were encountered, including:

**Encoding issues**: At first, there was an encoding issue that wasn't reading western european accents, which we can find in the brands file. I used the `iconv` tool within the command line to creat and encode all the files in UTF-8 encoding in a new directory called `csv_encoded`.
**Null Characters**: Importing data from CSV files revealed the presence of null characters within text fields, which required cleaning before successful import. I had to do some manual research to replace the null values in the text fields to get the closest outcome possible to what I could see on the website. 
**Null Values**: Handling null values in data, required adapting the `CREATE TABLE` query. 
**Best practice & room for improvement**: Given more time, I would have cleaned up the database a bit more, considered changing some of the types of the columns and remove some null fields. But I wanted to stay as true as possible to the file I had been given. It would be interesting to get a take on how you would handle this internally. Knowing general best practices and format rules could allow good decision making.


### Extra step

If I had more time, I would have deployed the database on Heroku to make it accessible, but chose to highlight other sections of this project. 


## 2. Data Analysis


**Exercise Queries and Python Automation**
The project included the development of 5 initial SQL queries (referred to in this project as "exercise queries") designed to analyze listings and customer activity. These queries were automated through a Python script (`run_exercise_queries.py` in the `script` directory of the project), which ran each SQL file and printed the results in a specific directory (/vestiaire-metrics/data/results_csv/exercise_results_csv). 


## 3. Data insights 

**Expanding the Analysis**
To deepen the insights into the customer database, an additional set of 8 SQL queries was created (referred to here as `extra_queries`). These queries aimed to uncover more detailed aspects of customer behavior, brand preferences, and engagement metrics. They are stored in the `sql` directory under `extra_analysis`, the python script used to run these queries and populate the `extra_results_csv` is stored in the `script` directory. The new queries explored areas such as popular brands and categories, time spent on listings, frequent usage by customers, listing success rates by brand, customer engagement by category, and conversion rates by category.

To push analysis further I put together a deck of slides. You can find them here : https://docs.google.com/presentation/d/1GykvBheNl01vhw4VzPDCqdAgRo9vrzzj/edit?usp=sharing&ouid=104631056619292904131&rtpof=true&sd=true.

The slides have 4 main contents.

1. Our numbers 
2. Brand analysis
3. Category analysis
4. What's next?

It's used to visualise the results better and give more insights on how to act on our analysis. The *What's next?* section offers 3 propositions on how to action the results: 

- Maximize listing counts 
- Reduce listing time
- Promote succesful categories & brands 

**Best practice and future suggestions** 

Given more time, we could put together an interactive dashboard using our newly created database (wih redash or databricks for instance), or no code platforms could also be used such as Google Looker. Finally, creating an interactive dashboard from scratch using a python library and hosting it on Heroku could also be considered. 


## Retro 

We would much appreciate if you could quickly answer the following: 

1. How much time did you spend answering those questions?

2h to 3h

2. How proud are you of your work? 

Very proud

3. What did you find challenging in this task?

Cleaning the database was quite challenging, I would have liked to do it a bit more. 

4. Is there anything missing that you think would be relevant to ask to candidates in the context of Skills Test?

It could be interesting to ask candidates what they think the product team of vestiaire collective should prioritise given the results of the case study.