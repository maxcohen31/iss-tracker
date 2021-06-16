# Internation Space Station tracker
# Author: Emanuele

import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# Startint the Tracker Class
class Tracker:
    def __init__(self):
        self.url =  requests.get('http://api.open-notify.org/iss-now.json').json() # get the url 
        self.df = pd.DataFrame.from_dict(self.url) # making a dataframe using pandas
        self.people_url = requests.get('http://api.open-notify.org/astros.json').json()   
        
    
    # Method to get the ISS latitude    
    def get_latitude(self):
        self.df = self.df.transpose()
        return f"Latitude: {self.df['latitude'][0]}"
    
    # Method to get the ISS longitude      
    def get_longitude(self):
        self.df = self.df.transpose()
        return f"Longitude: {self.df['longitude'][0]}"
     
    # Method to get the number of astronauts living in the ISS    
    def get_people(self):
        self.df_people = pd.DataFrame.from_dict(self.people_url).transpose()
        return self.df_people.loc['number'][0])
    
    # Method to get the names of the astronauts 
    def get_names(self):
        self.df_people = pd.DataFrame.from_dict(self.people_url) # New dataframe
        for key, value in self.df_people['people'][0:].items(): # A for loop to get the names
            return value['name']
    
    # At least the method to plot the ISS on a map    
    def show_position(self):
        self.df['latitude'] = self.df.loc['latitude', 'iss_position'] # Creating a new column named latitude   
        self.df['longitude'] = self.df.loc['longitude', 'iss_position'] # Creating a new column named longitude 
        self.df.reset_index(inplace=True) # We change the original dataframe
        iss_pos = px.scatter_geo(self.df, lat='latitude', lon='longitude') # Setting up the plot
        iss_pos.show() # Show
        



