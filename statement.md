# Problem Statement

The goal of this project is to develop a content-based movie recommendation system that suggests movies to users based on their preferences for genre, minimum rating, and popularity.
The dataset contains movie metadata such as title, genre, rating, popularity, and runtime, and the system must intelligently filter or cluster movies to return the most relevant results.

A key challenge is that not all genres have enough data or may not satisfy strict filters. To address this, the system must fall back to a machine learning–based K-Means clustering model to identify similar movies and still provide meaningful recommendations.

# Scope Of The Project

Included in Scope

Reading and validating a movie dataset (movies.csv)

Preprocessing:

Label Encoding of genres

Min-Max scaling of numerical features

Unsupervised clustering using K-Means (5 clusters)

Dual recommendation logic:

1. Rule-based filtering using:

Genre

Rating

Popularity

2. Cluster-based fallback when results are insufficient

Clean command-line interface for input and output

Display of top recommended movies sorted by rating and popularity

 Out of Scope (Not Included)

No database or storage system

No GUI or mobile app

No deep learning or collaborative filtering

No personalised user history or profiling

No deployment (web/server)

The scope is deliberately focused on creating a simple, functional ML-backed recommender using your given dataset.


# Target Users

The system is designed for:

 1. Movie Enthusiasts

People looking for good movies within a particular genre, rating range, or popularity level.

 2. Students Learning Machine Learning

Those who want to understand preprocessing, clustering, and recommendation logic.

 3. Developers or Researchers

Anyone needing a lightweight content-based recommendation tool for experimentation.

 4. Academic Evaluation

Students (like you) submitting a practical ML project for coursework or GitHub documentation.


# High-Level Features

Based strictly on your code and dataset, the system provides:

 1. Dataset Loading & Validation

Ensures movies.csv exists

Validates required columns

Extracts:

title

genre

rating

popularity

runtime

 2. Data Preprocessing

Label Encoding for the genre column

Min-Max Scaling for rating, popularity, and runtime

Feature matrix constructed for clustering

 3. Machine Learning (K-Means Clustering)

Clusters movies into 5 groups based on their encoded genre + numeric features

Used when rule-based filtering gives too few results

 4. Intelligent Recommendation Engine

The heart of your project:

A. Rule-Based Filtering

Filters by:

Genre

Minimum rating

Minimum popularity

B. Cluster-Based Recommendation

If fewer than 5 movies match:

The system identifies the dominant cluster for that genre

Returns movies from that cluster

 5. User Input Interface

The system:

Prints available genres

Accepts runtime inputs from the user

Validates inputs indirectly

Displays results in a clean tabular format

 6. Modular Design

The recommend_movies() function is reusable, allowing future expansion with minimal changes.
