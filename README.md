# 🎬 Movie Ratings ETL Pipeline

An end-to-end Data Engineering project that demonstrates how to build a complete ETL (Extract, Transform, Load) pipeline using Python, Pandas, MySQL, and Matplotlib.

---

## 📌 Project Overview

This project automates the process of:

- Extracting movie data from a CSV file
- Cleaning and transforming the dataset
- Loading structured data into a MySQL database
- Performing SQL-based analytics
- Visualizing insights using Matplotlib

It simulates a real-world data engineering workflow for analytical reporting.

---

## 🛠 Tech Stack

- Python  
- Pandas  
- MySQL  
- mysql-connector-python  
- Matplotlib  

---

## 📂 Project Structure

movie_etl_project/
│
├── movies.csv
├── main.py
└── README.md

---

## 🔄 ETL Workflow

### 1️⃣ Extract
- Read movie dataset using Pandas

### 2️⃣ Transform
- Remove missing values  
- Convert rating to float  
- Filter invalid ratings  
- Remove duplicate records  
- Compute average rating per genre  

### 3️⃣ Load
- Insert cleaned data into MySQL database  

### 4️⃣ Analyze
- Retrieve highest rated movies  
- Calculate average rating per genre  
- Filter movies by release year  

### 5️⃣ Visualize
- Generate bar chart of average rating per genre  

---

## 🗄 Database Schema

```sql
CREATE DATABASE movie_db;
USE movie_db;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie VARCHAR(100),
    genre VARCHAR(50),
    rating FLOAT,
    year INT
);
```

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install pandas mysql-connector-python matplotlib
```

### Step 2: Configure MySQL Credentials

Update this section inside `main.py`:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="movie_db"
)
```

### Step 3: Run the Script

```bash
python main.py
```

---

## 📊 Sample Analytical Queries

### 🔹 Top Rated Movies

```sql
SELECT movie, rating
FROM movies
ORDER BY rating DESC
LIMIT 5;
```

### 🔹 Average Rating per Genre

```sql
SELECT genre, AVG(rating)
FROM movies
GROUP BY genre;
```

### 🔹 Movies Released After 2010

```sql
SELECT movie, rating
FROM movies
WHERE year > 2010;
```

---

## 🎯 Key Learnings

- Practical implementation of ETL pipeline  
- Data cleaning and preprocessing using Pandas  
- SQL-based aggregation and reporting  
- Database connectivity using Python  
- Data visualization with Matplotlib  

---

## 📌 Resume Description

Designed and implemented an end-to-end ETL pipeline using Python and MySQL to automate data ingestion, transformation, and analytical reporting on movie rating data.

---

## 🚀 Future Improvements

- Add automated scheduling  
- Integrate dashboard using Streamlit  
- Implement logging system  
- Use PostgreSQL instead of MySQL  
- Deploy on cloud platform  

---

## 👨‍💻 Author

Your Name
