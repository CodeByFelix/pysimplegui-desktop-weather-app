import PySimpleGUI as sg
import requests
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def getMyLocation () -> str:
    response = requests.get (GEOLOCATE_URL)
    return response.json()['city']

def getWeather (location: str) -> dict:
    params = {'q': location, 'appid': API_KEY, 'units': 'metric'}
    try:
        #print (params)
        response = requests.get (BASE_URL, params=params)
    except:
        raise Exception ("Couldnt Complet Request")
    else:
        data = response.json()
        if data['cod'] != 200:
            raise Exception ("Incomplete Response")
        else:
            return {
                'country': data['sys']['country'],
                'city': data['name'],
                'description': data['weather'][0]['description'],
                'temp': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data ['main']['pressure'],
                'wind': data['wind']['speed']
            }

def daysForcast (location: str, canvas):
    params = {'q': location, 'appid': API_KEY, 'units': 'metric'}
    try:
        #print (params)
        response = requests.get (FORECAST_URL, params=params)
    except:
        raise Exception ("Couldnt Complet Request")
    else:
        data = response.json()
        if int(data['cod']) != 200:
            print (data['cod'])
            raise Exception ("Incomplete Response")
        else:
            dates = []
            temps = []
            humidity = []
            pressure = []
            wind = []
            for d in data['list']:
                dates.append(d['dt_txt'])
                temps.append (d['main']['temp'])
                humidity.append (d['main']['humidity'])
                pressure.append (d['main']['pressure'])
                wind.append (d['wind']['speed'])
            
            fig, ax = plt.subplots (figsize=(18, 6))
            ax.plot (dates, temps, label='Temperature (°C)', color='orange', marker='o')
            ax.plot (dates, humidity, label='Humidity (%)', color='blue', marker='o')
            #ax.plot (dates, pressure, label='Pressure (hPa)', color='green', marker='o')
            ax.plot (dates, wind, label='Wind (m/s)', color='red', marker='o')
            ax.set_title (f"5 Day Weather Focast of {data['city']['name']}", fontsize=14, fontweight='bold')
            ax.set_xlabel("Date and Time", fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.legend()
            plt.grid(True)
            plt.tight_layout()

            figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
            figure_canvas_agg.draw ()
            figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        
GEOLOCATE_URL = "http://ip-api.com/json/"
API_KEY = "Open Weather API Key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"

#R1 = [sg.Text ("City:")]
#R2 = [sg.Input ('City', key='_city_'), sg.Button ("Get Weather", '_get_weather_')]

CC = [
    [sg.Text ("City:")],
    [sg.Input (key='_city_'), sg.Button ("Get Weather", key='_get_weather_')]
]

layout = [
    [sg.Push(), sg.Column(CC, element_justification='left'), sg.Push()],
    [sg.Text (key='_text_', font=('Any', 12, 'bold'))],
    [sg.Canvas (key='_canvas_')],
    [sg.VPush()],
    [sg.Push(), sg.Button ("Use My Location", key='_my_location_'), sg.Push()]
]

window = sg.Window ("Weather App", layout, resizable=True, size=(1280, 960))

while True:
    event, values = window.read ()

    if event == sg.WIN_CLOSED:
        break

    if event == '_my_location_':
        location = getMyLocation()
        print (location)
        try:
            weather = getWeather (location)
        except Exception as e:
            sg.popup_error (e)
        else:
            data = f"""
                    Weather Description of {weather['city']}.
                    Country: {weather['country']}
                    City: {weather['city']}
                    Weather Description: {weather['description']}
                    Temperature: {weather['temp']}°C
                    Humidity: {weather['humidity']}%
                    Preasure: {weather['pressure']}hPa
                    Wind Speed: {weather['wind']}m/s
                    
                    """
            window ['_text_'].update(value=data)
               
            try:
                daysForcast (location, window['_canvas_'].TKCanvas)
            except Exception as e:
                sg.popup_error (e)

    if event == '_get_weather_':
        location = values['_city_']
        if location == '':
            sg.popup_error ("City Field cannot be Empty")
        else:
            try:
                weather = getWeather (location)
            except Exception as e:
                sg.popup_error (e)
            else:
                data = f"""
                        Weather Description of {weather['city']}.
                        Country: {weather['country']}
                        City: {weather['city']}
                        Weather Description: {weather['description']}
                        Temperature: {weather['temp']}°C
                        Humidity: {weather['humidity']}%
                        Preasure: {weather['pressure']}hPa
                        Wind Speed: {weather['wind']}m/s
                        
                        """
                window ['_text_'].update(value=data)
                #print ("Yes")
            try:
                daysForcast (location, window['_canvas_'].TKCanvas)
            except Exception as e:
                sg.popup_error (e)
            else:
                pass
window.close ()
