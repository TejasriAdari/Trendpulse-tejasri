import pandas as pd
import matplotlib.pyplot as plt

# Loading data
df = pd.read_csv("cleaned_data.csv")

# Top 5 posts bar chart
top = df.sort_values(by='score', ascending=False).head(5)

plt.barh(top['title'], top['score'])
plt.xlabel("Score")
plt.title("Top 5 Reddit Posts")
plt.show()

# Converting to Histogram
plt.hist(df['score'], bins=10)
plt.title("Score Distribution")
plt.show()

# Scatter plot
plt.scatter(df['score'], df['comments'])
plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.show()