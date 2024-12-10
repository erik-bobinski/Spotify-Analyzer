# Author: Ryan Connolly
# Date: December 10, 2024
# Description: This module defines the Recommender class that manages the recommendation logic using K-Means clustering and cosine similarity.

import numpy as np 
import pandas as pd

class Recommender:
    def __init__(self, data):
        '''
        Constructor initializes recommender with preprocessed data
        params: data(pd.DataFrame) = dataset with normalized features
        '''
        self.data = data  #dataset for recommendations
        
    def cosineSimilarity(self, targetID, features):
        '''
        Calculates cosine similarity between target song and all other songs
        params: targetID (str) = ID of target song for comparison, features = features user wants to consider for similarity
        returns: np.ndarray: array of similarity scores between target song and others
        '''
        
        # extract features of target
        target_features = self.data.loc[self.data['id'] == targetID, features].values[0]
        
        # features for the reat of the songs
        total_features = self.data[features].values
        
        # avoid dividing by 0
        norm_target = np.linalg.norm(target_features) or 1  # default to 1 if magnitude is 0
        norm_all = np.linalg.norm(total_features, axis=1)
        norm_all[norm_all == 0] = 1  # replace zero magnitudes with 1 to avoid division errors

        
        #cosine similarity calculation
        dot_product = np.dot(total_features, target_features)  # dot product
        norm_target = np.linalg.norm(target_features)  # magnitude of target features
        norm_all = np.linalg.norm(total_features, axis=1)  # magnitudes of all features
        similarity = dot_product / (norm_all * norm_target)  # cosine similarity formula
        
        sim_perc = similarity * 100  # convert similarity to percentage for better user understanding
        
        return sim_perc
    
    def recommend(self, targetID, features, top=5, cluster_priority=True):
        '''
        Recommends songs similar to the target based on similarity scores, optionally using clustering.
        params: targetID(str): ID of target song, top(int): number of recommendations to return, features(): features to consider
        returns: pd.DataFrame = top n recommended songs with details and similarity scores
        '''
    
        # if user wants to prioritize recs in same cluster as target
        if cluster_priority and 'cluster' in self.data.columns:
            target_cluster = self.data.loc[self.data['id'] == targetID, 'cluster'].values[0]     # cluster of target song 
            cluster_songs = self.data[self.data['cluster'] == target_cluster].copy()             # filter data to only include songs in the same cluster
            
        else:
            cluster_songs = self.data.copy() # use entire dataset
        
        cluster_songs = cluster_songs[cluster_songs['id'] != targetID] # exclude target song
        
        # calculate similarity scores
        cluster_features = cluster_songs[features].values
        target_features = self.data.loc[self.data['id'] == targetID, features].values[0]
        
        # cosine similarity for the filtered dataset
        dot_product = np.dot(cluster_features, target_features)
        norm_target = np.linalg.norm(target_features) or 1
        norm_cluster = np.linalg.norm(cluster_features, axis=1)
        norm_cluster[norm_cluster == 0] = 1                              # avoid division by zero
        similarity = (dot_product / (norm_cluster * norm_target)) * 100  # convert to percentage

        # assign similarity scores to the filtered songs
        cluster_songs['similarity'] = similarity
        
        # sort by similarity
        recs = cluster_songs.sort_values(by='similarity', ascending=False)
        
        # Fallback to global dataset if needed
        if len(recs) < top:
            remaining = top - len(recs)
            global_songs = self.data[~self.data['id'].isin(recs['id'])]
            global_songs = global_songs[global_songs['id'] != targetID]  # Exclude the target song
            global_features = global_songs[features].values

            # Global similarity calculation
            dot_product_global = np.dot(global_features, target_features)
            norm_global = np.linalg.norm(global_features, axis=1)
            norm_global[norm_global == 0] = 1
            global_similarity = (dot_product_global / (norm_global * norm_target)) * 100
            global_songs['similarity'] = global_similarity

            # Sort global songs by similarity and append to recommendations
            global_recs = global_songs.sort_values(by='similarity', ascending=False).head(remaining)
            recs = pd.concat([recs, global_recs])

        # add percent sign to similarity
        recs['similarity'] = recs['similarity'].apply(lambda x: f"{x:.2f}%")
        recs = recs.head(top)

        # Conditionally include 'cluster' in the result if it exists
        columns_to_return = ['name', 'artists', 'similarity']
        if 'cluster' in recs.columns:
            columns_to_return.append('cluster')

        return recs[columns_to_return]

