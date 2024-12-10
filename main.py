# Author: Ryan Connolly
# Date: December 10, 2024
# Description: This module contains the main function that implements the DataProcessor and Recommender classes.

from DataProcessor import DataProcessor
from Recommender import Recommender
from uiLogin import uiLogin

def main():
    processor = DataProcessor("data.csv")
    data = processor.loadData()
    clean = processor.clean()
    pp_data = processor.preprocessData()
    clustered = processor.clusterData(n_clusters=10)
    
    recommender = Recommender(clustered)
    
    app = uiLogin(recommender, clustered)
    app.run_server(debug=False)
    
    # this point on is for basic testing. comment out once GUI is integrated.
    
    # user_targetID = input("Enter target song ID : ")
    
    # features = ['valence', 'danceability', 'energy', 'tempo', 'acousticness']  # default
    # top = 5
    # recs = recommender.recommend(user_targetID, features, top=top, cluster_priority=True)
    
    # print("Top 5 Recommendations: ")
    # print(recs)
    

if __name__ == "__main__":
    main()
