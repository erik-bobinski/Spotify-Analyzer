# Author: Ryan Connolly
# December 10, 2024
# Description: This modules handles the Spotify data upload and preprocesses features to be suitable for Singular Value Decomposition. 


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
        load dataset from csv into pandas data frame
        returns: pd.DataFrame = the loaded dataset
        '''
        self.data = pd.read_csv(self.file_path)  
        return self.data
    
    def preprocessData(self):
        '''
        normalizing relevant features for similarity calculations
        
        returns: pd.DataFrame = preprocessed dataset with normalized features
        '''
        # features to normalize for similarity
        features = ['valence', 'danceability', 'energy', 'tempo', 'acoustics']
        
        # normalize each feature to have mean 0 and std 1.
        self.data[features] = self.data[features].apply(lambda x: x - x.mean() / x.std())
        return self.data
        