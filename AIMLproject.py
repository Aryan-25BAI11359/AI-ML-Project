import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 1. Load a sample dataset (or your own CSV)
data = {
    'title': ['The Dark Knight', 'Avengers: Endgame', 'The Godfather', 'Joker', 'Toy Story'],
    'genres': ['Action Crime Drama', 'Action Adventure Sci-Fi', 'Crime Drama', 'Crime Drama Thriller', 'Animation Children Comedy']
}
df = pd.DataFrame(data)

# 2. Initialize the TF-IDF Vectorizer to turn text into math
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genres'])

# 3. Compute the Cosine Similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# 4. Function to get recommendations
def get_recommendations(movie_title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = df.index[df['title'] == movie_title].tolist()[0]
    
    # Get pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 2 most similar movies (excluding itself)
    movie_indices = [i[0] for i in sim_scores[1:3]]
    
    return df['title'].iloc[movie_indices]

# Test it out!
print("If you liked 'The Dark Knight', you might also like:")
print(get_recommendations('The Dark Knight'))