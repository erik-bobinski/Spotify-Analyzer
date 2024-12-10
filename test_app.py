import pytest
import pandas as pd
import numpy as np
from DataProcessor import DataProcessor
from Recommender import Recommender

InputData = pd.DataFrame({
    'id': ['1', '2', '3'],
    'name': ['Song1', 'Song2', 'Song3'],
    'artists': ['Artist1', 'Artist2', 'Artist3'],
    'valence': [0.5, 0.7, 0.6],
    'danceability': [0.8, 0.9, 0.7],
    'energy': [0.6, 0.85, 0.75],
    'tempo': [120.0, 130.0, 140.0],
    'acoustics': [0.2, 0.3, 0.4]
})

def test_load_data(tmp_path):
    """Test loading data from CSV file."""
    Path = tmp_path / "test_data.csv"
    InputData.to_csv(Path, index=False)
    processor = DataProcessor(Path)
    Data = processor.loadData()
    assert not Data.empty, "Data should load correctly."
    assert list(Data.columns) == list(InputData.columns), "Columns should match."

def test_cosine_similarity():
    """Test cosine similarity calculation."""
    recommender = Recommender(InputData)
    Similarities = recommender.cosineSimilarity('1')
    assert len(Similarities) == len(InputData), "Similarity scores should match the number of songs."
    assert np.isclose(Similarities[0], 1, atol=1e-6), "Target song should have a similarity of 1 with itself."

def test_recommend():
    """Test song Recommendations."""
    recommender = Recommender(InputData)
    Recommendations = recommender.recommend('1', top=2)
    assert len(Recommendations) == 2, "Number of Recommendations should match the 'top' parameter."
    assert 'name' in Recommendations.columns, "Recommendations should include song names."
    assert 'similarity' in Recommendations.columns, "Recommendations should include similarity scores."

def test_data_integrity():
    """Test that data integrity is preserved after processing."""
    processor = DataProcessor(None)
    processor.data = InputData.copy()
    processor.preprocessData()
    assert set(processor.data.columns) == set(InputData.columns), "All original columns should remain."

def test_invalid_song_id():
    """Test behavior with an invalid song ID."""
    recommender = Recommender(InputData)
    with pytest.raises(IndexError):
        recommender.recommend('invalid_id', top=5)
