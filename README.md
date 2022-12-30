# API with SQLite

The project consists of ingesting data from various sources, subsequently applying the relevant transformations, and then providing the clean data for consultation through an API. The API is create with FastAPI, the functions for the consult are made with SQLite and then a virtual environment with docker was created for its use with mogenius.

---

### Step 1:

The datasets found in \Datasets_original were loaded and cleaning, column and data type changes were performed. These changes are detailed in Create_database.ipynb

The four modified datasets were inserted into tables and saved in the Database.db file using the sqlite library.

### Step 2:

The main.py file is configured to be able to create the application with FastAPI, this file in turn contains the functions where the queries will be made. The functions were made using the SQLite library which takes the data from the Database.db file.

### Step 3:

A dockerfile is created with the configuration to create the docker image, then the command to create the docker image is executed, in this case called "sql_api"

```
Docker build -t sql_api .
```

### Step 4:

The image is run using `docker run -d --name container -p 8000:8000 sql_api `and opened in the `localhost:8000/docs` browser to run the required queries. This step was done to verify that the container and the app are working.

### Step 5:

The github repository is connected to mogenius, from where the dockerfile is executed. It is verified that all the app works by entering from the link provided by mongenius, which in my case is this [Link](https://fastapi-docker-prod-api-with-sqlite-lf0bdt.mo5.mogenius.io/docs)

---



## Conclusions

For this API I chose to use SQLite to facilitate the queries and basic python functions to avoid adding more complexity to tools like FastAPI or Docker, which is the first time i used them, and to avoid future errors. Still, with this project I learned the basic use of these tools, how to use them together and their usefulness for future APIs.
