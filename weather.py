import requests, json, os
def getWeather():
    while(True):
        print('Please enter your city')
        city = str(input())
        key = '2cb48673ee9b6ef320872f2e77e2f226'

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, key)
        request = requests.get(url)
        data = json.loads(request.text)
        returnCheck = len(data)
        if(returnCheck==2):
            getWeather()
        #get locatoin
        location = data['name']

        #get desc
        desc = data['weather'][0]['description']

        #get feels like
        getFeel = data['main']['feels_like']
        feels = int((getFeel - 273.15)*9/5+32)

        #gets and parses temp
        getTemp = data['main']['temp']
        temp = int((getTemp - 273.15)*9/5+32)

        #gets humidity
        humidity = data['main']['humidity']

        #gets temp low
        getLow = data['main']['temp_min']
        low = int((getLow - 273.15)*9/5+32)

        #gets high
        getHigh = data['main']['temp_max']
        high = int((getHigh - 273.15)*9/5+32)

        #get pressure
        pressure = data['main']['pressure']

        print('Current Weather For', location,)
        print("-----------------------------------")
        print(desc.title())
        print("Feels like:", feels, "F")
        print("Current Temp:", temp, "F")
        print("Humidity:", humidity, "%")
        print("Low:", low, "F")
        print("High:", high, "F")
        print("Pressure:", pressure)
        print("\nEnter 'yes' to enter another location.")
        decision = str(input())
        if decision == 'no' or decision == 'No':
            break
      
getWeather()
