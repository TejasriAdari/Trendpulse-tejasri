import pandas as pd
import numpy as np

# Load data from CSV
df = pd.read_csv("cleaned_data.csv")

# Finding Average score
avg_score = np.mean(df['score'])
print("Average Score:", avg_score)

# Finding Top 5 posts from reddit
top_posts = df.sort_values(by='score', ascending=False).head(5)
print(top_posts)

# Most active authors
authors = df['author'].value_counts().head(5)
print(authors)

# Correlation of data
correlation = df['score'].corr(df['comments'])
print("Score vs Comments correlation:", correlation)