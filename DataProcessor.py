# Author: Ryan Connolly
# December 10, 2024
# Description: This modules defines the DataProcessor class that handles the Spotify data upload and preprocesses features to be suitable for cosine similarity calculations. 


import pandas as pd 
import numpy as np 

class DataProcessor:
    def __init__(self, file_path):
        '''
        Constructor to initialize the DataProcessor with the file path to the dataset
        params: file_path(str) 
        '''
        self.file_path = file_path   # path to dataset
        self.data = None             # placeholder for loaded dataset
        
    def loadData(self):
        '''
        Load dataset from csv into pandas data frame
        returns: pd.DataFrame = the loaded dataset
        '''
        self.data = pd.read_csv(self.file_path)  
        
        if self.data is None:
            raise FileNotFoundError("Data not found.")
        return self.data
    
    def clean(self):
        '''
        Cleans dataset to handle missing values and duplicates
        returns: pd.DataFrame = cleaned dataset
        '''
        self.data = self.data.drop_duplicates()  # remove duplicate entries
        
        important = ['name', 'id', 'artists']      # important columns for analysis
        self.data = self.data.dropna(subset=important)            # drop rows with missing critical values
        
        cols = ['valence', 'danceability', 'energy', 'tempo', 'acousticness']
        self.data[cols] = self.data[cols].apply(lambda x: x.fillna(x.mean()), axis=0)  # fills in missing values in feature columns with column mean
        
        
    def preprocessData(self):
        '''
        Normalizing relevant features for similarity calculations
        
        returns: pd.DataFrame = preprocessed dataset with normalized features
        '''
        
        # features to normalize for similarity
        features = ['valence', 'danceability', 'energy', 'tempo', 'acousticness']
        
        # normalize each feature to have mean 0 and std 1.
        self.data[features] = self.data[features].apply(lambda x: x - x.mean() / x.std())
        return self.data
        
