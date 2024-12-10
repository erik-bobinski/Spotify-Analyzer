# Spotify-Analyzer

## **Project Description**

Spotify Analyzer is a Python-based tool that recommends songs similar to a given track using cosine similarity. Users can upload their Spotify data, explore recommendations, and interact with the system through an intuitive GUI. The application leverages `pandas` and `numpy` for data processing and Dash for a graphical user interface.

---

## **Features**

- Login and Dashboard for a seamless user experience.
- Song recommendation system based on cosine similarity.
- Data preprocessing with normalization of key features (e.g., valence, energy, tempo).
- Dynamic, interactive GUI with:
  - Dropdowns for song selection.
  - Buttons to process data and generate recommendations.
  - Graphical display of song recommendations.
- Advanced Python module integration (`pandas`, `numpy`).

---

## **Installation**

### Prerequisites

1. Python 3.12 or later.
2. Recommended to use a virtual environment (e.g., `venv` or `conda`).

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/erik-bobinski/Spotify-Analyzer.git
   cd Spotify-Analyzer
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

4. Run the test suite (optional):

   ```bash
   pytest test_app.py
   ```

---

## **Usage**

### Login Page

- Enter your email and password (no validation; for navigation only).
- Click "Submit" to navigate to the dashboard.

### Dashboard

1. Login to the webapp via the GUI.
2. Select a target song from the dropdown menu.
3. Click the "Recommend" button to generate a list of similar tracks.
4. View the recommendations dynamically in the dashboard.

---

## **Project Architecture**

### File Overview

- **`DataProcessor.py`**:
  - Handles data loading and preprocessing (normalization).
- **`Recommender.py`**:
  - Contains the cosine similarity logic and recommendation generation.
- **`uiLogin.py`**:
  - Implements the GUI using Dash.
- **`test_app.py`**:
  - Contains pytest cases to validate data processing and recommendation logic.
- **`main.py`**:
  - Brings everything together and runs the code.

### Dependencies

- Dash: For the graphical user interface.
- Pandas: For data manipulation and analysis.
- Numpy: For numerical operations.
- Pytest: For testing the functionality.

## getSpotify.py

getSpotify.py was our initial project idea utilizing the Spotify API to pull a user's actual song/playlist history. While the file ran and successfully pulled the logged in user's data, we elected against using this file in our final design as it left too much risk for runtime errors or bugs that will disqualify the rest of the project due to inability to run.
