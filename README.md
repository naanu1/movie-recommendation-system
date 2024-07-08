# Movie Recommender System
In today’s fast-paced world, where time is a scarce resource, recommendation systems play a crucial role. These systems assist users in making informed choices without overwhelming them with too many options. They achieve this by predicting and suggesting content that aligns with individual preferences based on various factors such as browsing history, user profiles, and similarities with other users.

# Types of Recommendation Systems

1) Content-Based Filtering
Definition: Content-based systems focus on the attributes of items (movies, music, etc.) and recommend items with similar attributes to those the user has liked before.

Examples: Platforms like Twitter and YouTube use content-based recommendations to suggest videos or tweets based on your previous interactions.

Implementation: They create item profiles and user profiles, predicting that users who liked certain items in the past will likely enjoy similar items in the future.

Challenges: Content-based systems can sometimes make predictable recommendations and may struggle to suggest items outside a user's established preferences.

2) Collaborative Filtering
Definition: Collaborative filtering systems recommend items based on user interactions and similarities between users.

Examples: Recommending books on Amazon based on what other users with similar reading habits have liked.

Implementation: They use user-item interaction data to find patterns and recommend items liked by users with similar preferences.

Challenges: Scalability issues with large datasets and the tendency to recommend only popular items, potentially overlooking new or less-known items.

3) Hybrid Recommendation Systems
Definition: Hybrid systems combine both content-based and collaborative filtering approaches to provide more accurate and diverse recommendations.

Examples: Modern platforms like Spotify and Netflix use hybrid systems to balance the strengths of both approaches.

Implementation: They leverage techniques like word embeddings and machine learning models to offer personalized recommendations that address the limitations of individual methods.

Advantages: Hybrid systems can overcome the limitations of single-method approaches and deliver more relevant and personalized recommendations.

# About this Project
*This project is a Streamlit web application that recommends movies based on user preferences. It utilizes a machine learning model trained on a dataset of movie metadata from TMDB.

*Dataset Used
The project uses the TMDB 5000 Movie Dataset available on Kaggle.
Concept Used: Cosine Similarity
Cosine Similarity: This metric measures the similarity between documents or items by calculating the cosine of the angle between their feature vectors.

*Implementation: In this project, cosine similarity is used to measure the similarity between movies based on their attributes.

*Application: By comparing feature vectors (often represented as numpy arrays), cosine similarity helps in recommending movies that are most similar to a user's interests.

*Scoring: The similarity score ranges from 0 to 1, where 1 indicates identical items and 0 indicates completely dissimilar items.
