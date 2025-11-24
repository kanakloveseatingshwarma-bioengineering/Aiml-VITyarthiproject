# ------------------------------------------------------------
# MOVIE RECOMMENDATION SYSTEM (FULL WORKING VERSION)
# ------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.cluster import KMeans

print("\n🎬 MOVIE RECOMMENDATION SYSTEM\n")

# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------
try:
    df = pd.read_csv("movies.csv")
    print("Dataset loaded successfully!")
except:
    print("Error: Please make sure 'movies.csv' is in the same folder.")
    exit()

# Keep only required columns
required_cols = ['title', 'genre', 'rating', 'popularity', 'runtime']

for col in required_cols:
    if col not in df.columns:
        print(f"Error: Missing column '{col}' in dataset!")
        exit()

df = df[required_cols]

# ------------------------------------------------------------
# 2. PREPROCESSING
# ------------------------------------------------------------

# Encode the genre column
le = LabelEncoder()
df['genre_encoded'] = le.fit_transform(df['genre'])

# Select numerical features for clustering
features = ['genre_encoded', 'rating', 'popularity', 'runtime']
X = df[features]

# Scale features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# ------------------------------------------------------------
# 3. K-MEANS CLUSTERING
# ------------------------------------------------------------

kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

print("Clustering completed!\n")

# ------------------------------------------------------------
# 4. RECOMMENDATION FUNCTION
# ------------------------------------------------------------

def recommend_movies(genre_preference, min_rating=6.0, min_popularity=20):

    # Convert genre name into encoded number
    try:
        genre_encoded = le.transform([genre_preference])[0]
    except:
        print("\n❌ Genre not found in dataset!")
        print("Available genres:", list(df['genre'].unique()))
        return pd.DataFrame()

    # Rule-based filtering
    filtered = df[
        (df['genre_encoded'] == genre_encoded) &
        (df['rating'] >= min_rating) &
        (df['popularity'] >= min_popularity)
    ]

    # If too few results → use cluster-based recommendations
    if len(filtered) < 5:
        print("\n⚠ Not enough movies match your filters.")
        print("Showing similar movies based on clusters instead...\n")

        # Find cluster for this genre
        user_cluster = df[df['genre_encoded'] == genre_encoded]['cluster'].mode()[0]
        filtered = df[df['cluster'] == user_cluster]

    return filtered[['title', 'genre', 'rating', 'popularity', 'runtime']].sort_values(
        by=["rating", "popularity"], ascending=False
    )


# ------------------------------------------------------------
# 5. USER INPUT
# ------------------------------------------------------------

print("Available Genres:", list(df['genre'].unique()))

genre_input = input("\nEnter preferred genre: ")
rating_input = float(input("Enter minimum rating (0–10): "))
popularity_input = float(input("Enter minimum popularity: "))

# ------------------------------------------------------------
# 6. GENERATE RECOMMENDATIONS
# ------------------------------------------------------------

recommendations = recommend_movies(genre_input, rating_input, popularity_input)

# ------------------------------------------------------------
# 7. DISPLAY RESULTS
# ------------------------------------------------------------

if recommendations.empty:
    print("\nNo recommendations found.")
else:
    print("\n🎬 TOP RECOMMENDATIONS FOR YOU:\n")
    print(recommendations.head(10).to_string(index=False))

print("\nDone!")