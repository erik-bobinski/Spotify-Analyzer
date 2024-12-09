# Author: Ryan Connolly
# Date: December 10, 2024
# Description: This module manages the recommendation logic using cosine similarity.

import numpy as np 

class Recommender:
    def __init__(self, data):
        '''
        Constructor initializes recommender with preprocessed data
        params: data(pd.DataFrame) = dataset with normalized features
        '''
        self.data = data  #dataset for recommendations
        
    def cosineSimilarity(self, targetID):
        '''
        Calculates cosine similarity between target song and all other songs
        params: targetID (str) = ID of target song for comparison
        returns: np.ndarray: array of similarity scores between target song and others
        '''
        
        # features to consider
        features = ['valence', 'danceability', 'energy', 'tempo', 'acoustics']
        
        # extract features of target
        target_features = self.data.loc[self.data['id'] == targetID, features].values[0]
        
        # features for the reat of the songs
        total_features = self.data[features].values
        
        #cosine similarity calculation
        dot_product = np.dot(total_features, target_features)  # dot product
        norm_target = np.linalg.norm(target_features)  # magnitude of target features
        norm_all = np.linalg.norm(total_features, axis=1)  # magnitudes of all features
        similarity = dot_product / (norm_all * norm_target)  # cosine similarity formula
        
        return similarity
    
    