# **Vestiaire Metrics**


## Project Overview

`vestiaire-metrics` is a comprehensive analytics project designed to extract, process, and visualize data from a PostgreSQL database hosted on ElephantSQL. The project aims to provide insightful metrics about customer interactions, preferences, and behaviors on the Vestiaire Collective platform.

### Architecture

The project architecture is structured around several key components:

- **Data Source:** Raw data is stored in a PostgreSQL database managed through ElephantSQL, ensuring robustness and scalability.
- **Analysis Queries:** A series of SQL queries were developed to extract meaningful insights from the data, focusing on customer interactions and product listings. 
- **Python Automation:** A Python script was implemented to automate the execution of SQL queries, fetching results directly from the database.
- **Visualization:** Further analysis was pursued through additional SQL queries, with the aim of visualizing the results on a dashboard for easier interpretation and sharing.


## 1. Data Injection


### Database Setup on ElephantSQL

The PostgreSQL database was set up on ElephantSQL, a cloud-hosted PostgreSQL service offering. The process involved:

1. **Creating a New Instance:** A new database instance was initialized on ElephantSQL, which provided a URL used to connect to the PostgreSQL database.
2. **Schema Creation:** Tables were created to store data related to customer listings, product attributes, and interactions.
3. **Data Import:** CSV files containing extracts of data were imported into the database, involving careful management of data types and integrity.


### Challenges Encountered

Throughout the project, several challenges were encountered, including:

**Encoding issues**: At the first there was an encoding issue that wasn't reading western european accents, which we can find in the brands file. I used the `iconv` tool within the command line to creat and encode all the files in UTF-8 encoding in a new directory called `csv_encoded`.
**Null Characters**: Importing data from CSV files revealed the presence of null characters within text fields, which required cleaning before successful import. I had to do some manual research to replace the null values in the text fields to get the closest outcome possible to what I could see on the website. 
**Null Values**: Handling null values in data, required adapting the `CREATE TABLE` query. 
**Best practice & room for improvement**: Given more time, I would have cleaned up the database a bit more, considered changing some of the types of the columns and remove some null fields. But I wanted to stay as true as possible to the file I had been given. It would be interesting to get a take on how you would handle this internally. Knowing general best practices and format rules could allow good decision making.


## 2. Data Analysis


Exercise Queries and Python Automation
The project included the development of 5 initial SQL queries (referred to as "exercise queries") designed to analyze listings and customer activity. These queries were automated through a Python script (run_queries.py), which executed the SQL files and handled the results. This setup streamlined the analysis process, making it reproducible and efficient.


### 3. Data insights 

Expanding the Analysis
To deepen the insights into the customer database, an additional set of 7 SQL queries was created. These queries aimed to uncover more detailed aspects of customer behavior, brand preferences, and engagement metrics. The new queries explored areas such as popular brands and categories, time spent on listings, frequent usage by customers, listing success rates by brand, customer engagement by category, and conversion rates by category.

Conclusion
The vestiaire-metrics project represents a comprehensive effort to leverage SQL and Python for data analysis and visualization. Despite facing challenges related to data cleaning and type compatibility, the project successfully derived meaningful insights from the Vestiaire Collective customer database. The subsequent expansion of the analysis through additional queries underscored the project's commitment to understanding customer dynamics at a deeper level.

### Retro 

We would much appreciate if you could quickly answer the following: 

1. How much time did you spend answering those questions?

2h to 3h

Think also about what additional queries would you run and what kind of data will you need to continue your analysis?
💡
[Skills Test] Product Data Analyst 3



2. How proud are you of your work? 

Very proud


3. What did you find challenging in this task?
4. Is there anything missing that you think would be relevant to ask to candidates in the context of Skills Test?