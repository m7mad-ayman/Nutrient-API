import requests
from bs4 import BeautifulSoup as bs
from app.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'This command makes WebScraping to install database'

    def handle(self, *args, **kwargs):
        urls =["https://www.fatsecret.com/calories-nutrition/food/vegetables",
        "https://www.fatsecret.com/calories-nutrition/food/fruit",
        "https://www.fatsecret.com/calories-nutrition/food/beans",
        "https://www.fatsecret.com/calories-nutrition/food/fish",
        "https://www.fatsecret.com/calories-nutrition/food/nuts",
         "https://www.fatsecret.com/calories-nutrition/food/cheese",
         "https://www.fatsecret.com/calories-nutrition/food/fried-rice",
         "https://www.fatsecret.com/calories-nutrition/food/macaroni",
        "https://www.fatsecret.com/calories-nutrition/food/bread",
        "https://www.fatsecret.com/calories-nutrition/food/egg-whites"]
        print('processing ...')

        for url in urls:
            # Send a GET request to the website
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content
                soup = bs(response.content, 'html.parser')
                tables=soup.find_all('table', {"class":"generic nutrition"})
                category = url.split('/')[-1]
                for table in tables:

                    items = table.find_all('td')
                
                    for item in items:
                        if "subtitle" in str(item):
                            continue
                        elif 'class="prominent"' in str(item):
                            i=0
                            data = Food()
                            if item.get_text().endswith('cup') or item.get_text().endswith('large') or item.get_text().endswith(' oz'):
                                data.name =item.get_text()+" Egg White"
                            else:
                                data.name =item.get_text()
                        elif 'nutrient' in str(item):
                            if i==0:
                                
                                data.category=category
                                if item.get_text() =="-":
                                    data.fat = 0
                                else:
                                    data.fat= float(item.get_text())
                                i+=1
                            elif i==1 :
                                if item.get_text() =="-":
                                    data.carb = 0
                                else:
                                    data.carb= float(item.get_text())
                                i+=1
                            elif i==2:
                                if item.get_text() =="-":
                                    data.protein = 0
                                else:
                                    data.protein= float(item.get_text())
                                i+=1
                            elif i==3:
                                data.cal = float(item.get_text())
                                data.save()
                                print("[{0} ] saved ".format(data.name))
