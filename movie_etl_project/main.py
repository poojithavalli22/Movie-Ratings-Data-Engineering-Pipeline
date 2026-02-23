import pandas as pd

# Step 1: Extract
df = pd.read_csv("movies.csv")

print("Raw Data:")
print(df.head())

# Step 2: Transform

# Remove missing values
df.dropna(inplace=True)

# Convert rating to float
df["Rating"] = df["Rating"].astype(float)

# Remove invalid ratings
df = df[(df["Rating"] >= 0) & (df["Rating"] <= 10)]

# Remove duplicate movies
df.drop_duplicates(subset="Movie", inplace=True)

print("\nCleaned Data:")
print(df)


genre_avg = df.groupby("Genre")["Rating"].mean()

print("\nAverage Rating per Genre:")
print(genre_avg)


import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PoojithaValli@3372!",  # change this
    database="movie_db"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO movies (movie, genre, rating, year)
        VALUES (%s, %s, %s, %s)
    """, (row["Movie"], row["Genre"], row["Rating"], row["Year"]))

conn.commit()
conn.close()

print("\nData Loaded Successfully!")


import matplotlib.pyplot as plt

genre_avg = df.groupby("Genre")["Rating"].mean()

genre_avg.plot(kind="bar")
plt.title("Average Rating per Genre")
plt.ylabel("Average Rating")
plt.xlabel("Genre")
plt.show()