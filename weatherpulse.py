import requests

# Function to get weather data from the API
def get_weather_data(city_name, api_key):
    # The API URL we will use to get the weather data
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    # Make the HTTP GET request to the API
    response = requests.get(api_url)
    
    # If the response was successful (status code 200), return the data
    if response.status_code == 200:
        return response.json()  # The response data in JSON format
    else:
        # If there's an error (e.g., city not found), return None
        print(f"Error: Unable to get data for {city_name}. Please check the city name or API key.")
        return None

# Function to display the weather data
def display_weather(data):
    # Extracting data from the JSON response
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    # Display the data
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

# Main function to run the app
def main():
    # Your OpenWeatherMap API key (replace with your actual key)
    api_key = "becffb74bde8e0d3b3217b85d004c7da"
    
    # Get the city name from the user
    city_name = input("Enter the city name: ")
    
    # Get the weather data
    weather_data = get_weather_data(city_name, api_key)
    
    # If we successfully got the data, display it
    if weather_data:
        display_weather(weather_data)

# Entry point of the script
if __name__ == "__main__":
    main()
