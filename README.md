# Nutrient API
#### A basic Django Nutrient API is a backend service built using the Django RestFramework to handle the core functionalities of a Web Scraping for food from a website.
#### Returns Fats , Carbs , Proteins and Calories for any item .

## Tools :
- Django
- RestFramework
- BeautifulSoup
- Requests
  
## Featues :
- RESTful API Endpoints :
  [ "/food" (all) , "/vegetables" , "/fruit" , "/beans" , "/fish" ,  "/nuts" , "/cheese" , "/fried-rice" , "/macaroni" , "/bread" , "/egg-whites" ]
- Returns Fats , Carbs , Proteins and Calories

## Installation :
  ### Requirements
  - Python (3.x.x)
  ### SetUp
  To install required packages 
  
  ```
  pip install -r requirements.txt
  ```
    
  Create admin user
  
  ```
    python manage.py createsuperuser
  ```
    
  Create database
  
  ```
    python manage.py makemigrations
    python manage.py migrate
  ```
    
  To run  Web Scraping file app/management/commands/scrap.py
  
  ```
    python manage.py scrap
  ```

  To run the server

  ```
    python manage.py runserver
  ```

