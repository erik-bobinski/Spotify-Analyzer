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
    
    recommender = Recommender(pp_data)

    uiLogin(recommender).run_server(debug=True)
    
    # this point on is for basic testing. comment out once GUI is integrated.
    
    user_targetID = input("What is your favorite song ID? : ")
    
    recs = recommender.recommend(user_targetID, top=5)
    
    print("Top 5 Recommendations: ")
    print(recs)
    

if __name__ == "__main__":
    main()
