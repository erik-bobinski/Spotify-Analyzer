# Author: Ryan Connolly
# December 10, 2024
# Description: This modules defines the DataProcessor class that handles the Spotify data upload and preprocesses features to be suitable for K-Means Clustering and cosine similarity calculations. 


import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans

class DataProcessor:
    def __init__(self, file_path):
        '''
        Constructor to initialize the DataProcessor with the file path to the dataset
        params: file_path(str) 
        '''
        self.file_path = file_path   # path to dataset
        self.data = None             # placeholder for loaded dataset
        self.cluster_model = None    # placeholder for k-means model
        
    def loadData(self):
        '''
        Load dataset from csv into pandas data frame
        returns: pd.DataFrame = the loaded dataset
        '''
        self.data = pd.read_csv(self.file_path)  
        required_columns = ['id', 'name', 'artists', 'valence', 'danceability', 'energy', 'tempo', 'acousticness']
        missing_columns = [col for col in required_columns if col not in self.data.columns]

        if missing_columns:
            raise ValueError(f"The dataset is missing required columns: {', '.join(missing_columns)}")
        return self.data
    
    def clean(self):
        '''
        Cleans dataset to handle missing values and duplicates
        returns: pd.DataFrame = cleaned dataset
        '''
        self.data = self.data.drop_duplicates()  # remove duplicate entries
        
        important = ['name', 'id', 'artists']              # important columns for analysis
        self.data = self.data.dropna(subset=important)            # drop rows with missing critical values
        
        feature_cols = ['valence', 'danceability', 'energy', 'tempo', 'acousticness']
        for col in feature_cols:
            if col in self.data.columns:
                self.data[col] = self.data[col].fillna(self.data[col].mean())    # fills in missing values in feature columns with column mean
        
        
    def preprocessData(self):
        '''
        Normalizing relevant features for clustering and similarity calculations
        
        returns: pd.DataFrame = preprocessed dataset with normalized features
        '''
        
        # detect feature columns to normalize for similarity
        feature_cols = ['valence', 'danceability', 'energy', 'tempo', 'acousticness']
        features = [col for col in feature_cols if col in self.data.columns]
        
        # normalize each feature to have mean 0 and std 1.
        self.data[features] = self.data[features].apply(lambda x: x - x.mean() / x.std())
        return self.data
        
    def clusterData(self, n_clusters=10):
        '''
        Cluster songs using K-Means and add cluster labels to dataset
        params: n_clusters(int) = number of clusters
        returns: pd.DataFrame = dataset with cluster labels added
        '''
        
        feature_cols = ['valence', 'danceability', 'energy', 'tempo', 'acousticness']
        features = [col for col in feature_cols if col in self.data.columns]
        
        if not features:
            raise ValueError("No features available for clustering.")
        
        self.cluster_model = KMeans(n_clusters=n_clusters, random_state=42)
        self.data['cluster'] = self.cluster_model.fit_predict(self.data[features])
        return self.data 
