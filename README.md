# Facebook page SCRAPER using FastAPI (a python frameworks), MongoDB (for database), Docker Compose (for deployment), Selenium (for scraping)
## How to start the application

**The commands:**

First you have to git clone the files by entering in your terminal:
```
$ git clone https://github.com/Cherni-Oussama/facebook-page-scraper
```  
Then start the application:
```
$ docker-compose up -d
```
The above command will both create the images and start the containers (2 images and 2 containers - one for the FastAPI application and one for the MongoDB database).

For starting the scraper, open up your browser and enter:

* http://127.0.0.1/

To display all the scraped pages, enter :

* http://127.0.0.1/list
