# AIML VITyarthi project


# Overview of the Project

This project is a Movie Recommendation System built using Python and machine learning techniques.
It recommends movies to users based on their preferred genre, minimum rating, and popularity threshold.
If too few movies match the filters, the system automatically uses K-Means clustering to find similar movies and provide fallback recommendations.

The system operates on a CSV dataset containing movie titles, genres, ratings, popularity scores, and runtime.
It includes preprocessing, feature scaling, genre encoding, clustering, and final recommendation generation through a simple command-line interface.


# Features

1. Genre-based movie filtering

Users can choose a genre, and the system returns movies from that category.

 2. Rule-based filtering

Filters results by:

Minimum rating

Minimum popularity

 3. Automatic fallback using K-Means clustering

If filtered results are fewer than 5:

The system identifies the dominant cluster for the chosen genre

And shows similar movies based on cluster grouping

 4. Preprocessing Pipeline

Includes:

Label Encoding for categorical genres

Min-Max scaling for numeric features

Feature selection for clustering

 5. User-Friendly CLI Interface

The system:

Displays available genres

Takes user input

Shows clean tabular output of recommendations

 6. Works with custom datasets

As long as the dataset has:

title, genre, rating, popularity, runtime


…it will run smoothly.


# Technologies/Tools Used

Programming Language

Python 3.x

Libraries

Pandas – data loading, cleaning, and manipulation

NumPy – numerical operations

scikit-learn

LabelEncoder for genre encoding

MinMaxScaler for feature scaling

KMeans for clustering

Development Tools

Any Python IDE: VS Code / PyCharm / Jupyter Notebook

CSV dataset

Command-line interface to run the script


# Steps to Install & Run the Project

1 Install Python

Ensure Python 3.7+ is installed.

Check using:

python --version

2️ Install Required Libraries

Run this in your terminal:

pip install pandas numpy scikit-learn

3️ Place the Dataset

Save your dataset file as:

movies.csv


Place it in the same folder as your .py script.

4️ Run the Program

Navigate to the folder where your file is saved and run:

python movie_recommender.py

5️ Provide Inputs When Prompted

The program will ask:

Enter preferred genre:
Enter minimum rating (0–10):
Enter minimum popularity:


Enter values accordingly.

6️ View Recommendations

The system prints the top movie recommendations in a well-formatted table.


# Instructions for Testing

Here’s how to test your project based on the code:

1️ Test with Valid Inputs

Choose genres that exist in the dataset, such as:

Drama

Sci-Fi

Action

Comedy

Provide reasonable rating and popularity values:

rating: 7
popularity: 20

2️ Test Fallback Cluster Logic

Enter strict filters that return fewer than 5 movies.

Example:

Genre: Comedy
Rating: 9
Popularity: 90


This will trigger:

“Not enough movies match your filters”

Cluster-based recommendations

3️ Test Invalid Genre Input

Enter a genre not in the dataset:

Fantasyy


Expected output:

 Genre not found in dataset!
Available genres: [...]

4️ Test Boundary Values

Examples:

rating = 0

popularity = 0

runtime edge cases (though runtime is not user-input)

5️ Test Dataset Integrity Errors

Rename or remove the CSV file.
Expected:

Error: Please make sure 'movies.csv' is in the same folder.


Remove a required column and test:

Error: Missing column 'genre' in dataset!
