#!/usr/bin/env python3

# Bot token from @botfather
Token = "Your token"

# Start message
Start = "Welcome {0}!\nJust send me the city name in any language"
Error = "City not found!"

# Request url
URL = "http://api.openweathermap.org/data/2.5/weather?"

# API key (get it from openweathermap.org by creating an accout)
APIKey = "Your api key"

# Weater function
def GetWeather(city):
    global Error, URL, APIKey
    
    response = requests.get(f"{URL}appid={APIKey}&q={city}")

    result = response.json()
    
    if result["cod"] != "404":

        # Coord report 
        try:
            coord = result["coord"]
        except:
            coord = "No data"

        try:
            longitute = coord["lon"]
        except:
            longitute = "No data"
        
        try:
            latitute = coord["lat"]
        except:
            latitute = "No data"

        # Weather report 
        try:
            weather = result["weather"]       
        except:
            weather = "No data"

        try:
            weatherDiscription = weather[0]["description"]
        except:
            weatherDiscription = "No data"

        try:
            weatherMain  = weather[0]["main"]
        except:
            weatherMain = "No data"

        try:
            weatherID = weather[0]["id"]
        except:
            weatherID = "No data"

        # Base report 
        try:
            base = result["base"]
        except:
            base = "No data"

        # Main report 
        try:
            main = result["main"]
        except:
            main = "No data"

        try:
            temperature = main["temp"]
        except:
            temperature = "No data"

        try:
            feelsLlike = main["feels_like"]
        except:
            feelsLlike = "No data"

        try:
            MinTemp = main["temp_min"]
        except:
            MinTemp = "No data"

        try:
            MaxTemp = main["temp_max"]        
        except:
            MaxTemp = "No data"

        try:
            pressure = main["pressure"]
        except:
            pressure = "No data"

        try:
            humidity = main["humidity"]
        except:
            humidity = "No data"

        try:
            sea_level = main["sea_level"]
        except:
            sea_level = "No data"
        
        try:
            grnd_level = main["grnd_level"]
        except:
            grnd_level = "No data"

        # Visibility report 
        try:
            visibility = result["visibility"]
        except:
            visibility = "No data"

        # Wind report
        try: 
            wind = result["wind"]
        except:
            wind = "No data"

        try:    
            windSpeed = wind["speed"]
        except:
            windSpeed = "No data"

        try:        
            windDeg = wind["deg"]
        except:
            windDeg = "No data"

        try:
            gust = wind["gust"]
        except:
            gust = "No data"

        # Cloud report 
        try:
            clouds = result["clouds"]
        except:
            clouds = "No data"

        try:    
            cloudsAll = clouds["all"]
        except:
            cloudsAll = "No data"

        # SYS report 
        try:
            sys = result["sys"]
        except:
            sys = "No data"

        try:
            country = sys["country"]
        except:
            country = "No data"

        try:    
            sunrise = sys["sunrise"]
        except:
            sunrise = "No data"

        try:    
            sunset = sys["sunset"]
        except:
            sunset = "No data"    

        # Other reports
        try:
            timezone = result["timezone"]
        except:
            timezone = "No data"

        try:
            name = result["name"]
        except:
            name = "No data"

        wheatherText = f"""
〚{name}, {country}〛
↳ Geo coords: {latitute}, {longitute}
↳ timezone: {timezone}
↳ Sunrise: {sunrise}
↳ Sunset: {sunset}
↳ Base: {base}
↳ Visibility: {visibility}

〚Temperature〛 (Celsius)
↳ Temperature: {temperature - 273.15 :.2f} °C
↳ feelsLlike: {feelsLlike - 273.15 :.2f} °C
↳ Minimum: {MinTemp - 273.15 :.2f} °C
↳ Maximum: {MaxTemp - 273.15 :.2f} °C
↳ Pressure: {pressure}
↳ Humidity: {humidity}
↳ Sea level: {sea_level}
↳ Ground level: {grnd_level}

〚Weather〛
↳ Main: {weatherMain}
↳ Discription: {weatherDiscription}

〚Cloud〛
↳ Cloud: {cloudsAll}

〚Wind〛
↳ Wind Speed: {windSpeed}
↳ Wind Degree: {windDeg} °
↳ gust: {gust}

"""
        return wheatherText
    else:
        return Error
