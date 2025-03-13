import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
import folium
import webbrowser
import requests
import geocoder

# Define your OpenChargeMap API key
API_KEY = "1d19829e-df08-4bf3-8096-1ddca709833e"

def get_user_location():
    try:
        # Use geocoder library to automatically detect the user's location
        location = geocoder.ip('me')
        return location.latlng  # Returns a tuple of (latitude, longitude)
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching user location: {e}")
        return None, None


def get_charging_stations(latitude, longitude):
    try:
        url = f"https://api.openchargemap.io/v3/poi/?output=json&latitude={latitude}&longitude={longitude}&distance=10&distanceunit=KM&maxresults=10&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching charging stations: {e}")
        return []

def show_map_with_charging_stations():
    latitude, longitude = get_user_location()
    if latitude is not None and longitude is not None:
        charging_stations = get_charging_stations(latitude, longitude)
        if charging_stations:
            # Create map centered at user's location
            map = folium.Map(location=[latitude, longitude], zoom_start=15)
            
            # Add marker for user's location
            folium.Marker([latitude, longitude], popup="Your Location", icon=folium.Icon(color="blue")).add_to(map)
            
            # Add markers for charging stations
            for station in charging_stations:
                folium.Marker([station['AddressInfo']['Latitude'], station['AddressInfo']['Longitude']], popup=station['AddressInfo']['Title']).add_to(map)
            
            # Save the map to an HTML file
            map.save("charging_stations_map.html")
            
            # Open the HTML file in the default web browser
            webbrowser.open("charging_stations_map.html")
        else:
            messagebox.showinfo("No Charging Stations", "No charging stations found nearby.")

root = tk.Tk()
root.title("Charging Station Finder")

button = tk.Button(root, text="Show Map with Charging Stations", command=show_map_with_charging_stations)
button.pack()

root.mainloop()