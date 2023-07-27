# This is Python script.

from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
from bs4 import BeautifulSoup


#opening json file to write the scraped data into it
with open("data.json","w")as f:
   json.dump([],f)
def write_json(new_data,filename='data.json'):
   with open(filename,'r+') as file:
      file_data=json.load(file)
      file_data.append(new_data)
      file.seek(0)
      json.dump(file_data,file,indent=4)

driver =webdriver.Chrome()

#default url
url='https://www.kayak.co.in/flights/HYD-DOH/2023-01-30?sort=bestflight_a'

#userdefined input url
#source=input("enter the source")
#destination=input("enter your destination")
#url='https://www.kayak.co.in/flights/HYD-DOH/2023-01-30?sort=bestflight_a'


driver.get(url)
sleep(4)


#Scraping Flight fares
flight_rows=driver.find_elements(By.XPATH,'//div[@class="inner-grid keel-grid"]')
print(len(flight_rows))


lst_prices=[]
for webelement in flight_rows:
   elementHTML=webelement.get_attribute('outerHTML')
   elementsoup=BeautifulSoup(elementHTML,'html.parser')

   temp_price=elementsoup.find("div",{"class":"col-price result-column js-no-dtog"})
   price=temp_price.find("span",{"class":"price-text"})
   lst_prices.append(price.text)

print(lst_prices)


#Scraping source and destination airport names
airport=[]
flight_rows=driver.find_elements(By.CLASS_NAME, 'airport-name')
for j in flight_rows:
   print("AirPort_names:"+ j.text)
   airport.append(j.text)

s_airport=[]
d_airport=[]
for i in range(len(airport)):
   if i%2==0:
      s_airport.append(airport[i])
   else:
      d_airport.append(airport[i])


#Scraping no of stops
stops=[]
flight_stops=driver.find_elements(By.CLASS_NAME, 'stops-text')
for k in flight_stops:
   print("Stops:"+ k.text)
   stops.append(k.text)



#Scraping departure time of the flight
depart=[]
depart_time=driver.find_elements(By.CLASS_NAME, 'depart-time')
for r in depart_time:
   print("depart_time:"+ r.text)
   depart.append(r.text)



#Scraping arrival time of the flight
arrival=[]
arrival_time=driver.find_elements(By.CLASS_NAME, 'arrival-time')
for s in arrival_time:
   print("arrival_time:"+ s.text)
   arrival.append(s.text)



#Scraping the flight details
f_details=[]
duration=driver.find_elements(By.XPATH, '//div[@class="top"]')
for t in duration:
   print("duration"+ t.text)
   f_details.append(t.text)


#allocating Details of the flight
timings=[]
y=[]
f_duration=[]
for i in range(0,len(f_details),3):
   timings.append(f_details[i])
   y.append((f_details[i+1]))
   f_duration.append(f_details[i+2])

#Scraping Airline name
f_airline=[]
airline=driver.find_elements(By.CLASS_NAME,"codeshares-airline-names")
for u in airline:
   print("airline"+ u.text)
   f_airline.append(u.text)
print(len(f_airline))




#Writing the flight details in json file

for i in range(len(stops)):
   write_json({
      "from":s_airport[i],
      "to":d_airport[i],
      "stops":stops[i],
      "depart-time":depart[i],
      "arrival-time":arrival[i],
      "Timings":timings[i],
      "two":y[i],
      "flightduration":f_duration[i],
      "Airline":f_airline[i],
      "cost":lst_prices[i]
   })


