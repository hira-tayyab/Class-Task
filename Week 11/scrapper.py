import requests
from bs4 import BeautifulSoup
import csv

def get_cars_data(car):
    
    url=f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    response=requests.get(url, headers=headers)

    cars=[]
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        tables=soup.find_all('table')
        if not tables:
            print("No tables found on the webpage.")
        for table in tables:
            rows=table.find_all('tr')
            for row in rows:
                cols=row.find_all('td')
                if len(cols)>= 2:
                    name=cols[0].get_text()
                    price=cols[1].get_text()
                    cars.append({'name': name, 'price': price})
                  
            
    else:
        print("Failed to retrieve the webpage.")    
        
    return cars


#create a function to scrape data from the webpage, the above code can be used inside the function
def scrapper(car):
     data = get_cars_data(car)
     return data 


# create a function to save data to a csv file
def save_to_file(data, filename):
    if not data: print("No data to save!")
 return with open(filename, "w", newline="", encoding="utf-8") as file: writer = csv.writer(file)
 # headers
writer.writerow(["Name", "Price"])
  # data rows
 for item in data: 
    writer.writerow([item['name'], item['price']])
 print("Data saved successfully in", filename) data = scrapper("toyota") save_to_file(data, "cars.csv") print("Done")

def testing():
     data = scrapper("toyota")

    print("Total Cars Found:", len(data))

    for car in data[:5]:  # Show first 5 records
        print(car)


# Main Program
data = scrapper("toyota")
save_to_file(data, "cars.csv")

print("Done")

testing()