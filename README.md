# 🌦️ Weather Forecast Desktop App (PySimpleGUI + OpenWeatherMap API)

This is a simple desktop weather forecasting application built with Python using **PySimpleGUI** for the interface and **Matplotlib** for visualizing the 5-day forecast. It fetches real-time weather information and forecast data from the **OpenWeatherMap API**.

---

## 🔧 Features

- 🌍 Detects your current city using your IP address.
- 🏙️ Allows manual entry of any city name.
- 🌤️ Displays current weather data:
  - Temperature
  - Humidity
  - Pressure
  - Wind speed
  - Weather description
- 📈 Plots a 5-day forecast with:
  - Temperature
  - Humidity
  - Wind speed
- 🎨 Matplotlib integration for graphs inside PySimpleGUI window.

---

## 🧰 Technologies Used

- Python 3
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [Matplotlib](https://matplotlib.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [IP-API](http://ip-api.com/) for location detection

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```
### Install dependencies

```bash
pip install -r requirements.txt
```
### 🔑 Setup
Get your free API key from OpenWeatherMap.

Replace the value of API_KEY in the script with your own:

```python
API_KEY = "your_api_key_here"
```

### ▶️ Usage
Run the app:

```bash
python weather_app.py
```

Click "Use My Location" to fetch weather data for your current city.

Or manually enter a city name and click "Get Weather".