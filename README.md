# Customer Segmentation using K-Means

## 📌 Overview

This project uses **K-Means Clustering** to segment customers based on their **Annual Income** and **Spending Score**.

## 🛠️ Technologies

- Python
- Pandas
- Scikit-learn
- Matplotlib

## 🔄 Steps

1. Load and inspect the dataset
2. Check missing values and duplicates
3. Select Annual Income and Spending Score
4. Scale the features using StandardScaler
5. Find the optimal number of clusters using the Elbow Method
6. Apply K-Means Clustering
7. Visualize the customer clusters
8. Analyze the customer segments

## 📊 Model

**Algorithm:** K-Means Clustering

**Number of Clusters:** 5

## 👥 Customer Segments

| Cluster | Income | Spending | Segment |
|---|---:|---:|---|
| 0 | 55.30k | 49.52 | Average Income / Average Spending |
| 1 | 86.54k | 82.13 | High Income / High Spending |
| 2 | 25.73k | 79.36 | Low Income / High Spending |
| 3 | 88.20k | 17.11 | High Income / Low Spending |
| 4 | 26.30k | 20.91 | Low Income / Low Spending |

## 💡 Business Insights

- **Cluster 1:** High-value customers who can be targeted with premium offers and loyalty programs.
- **Cluster 2:** High-spending customers who may respond well to discounts and attractive offers.
- **Cluster 3:** High-income customers with low spending who can be targeted with personalized marketing.
- **Cluster 4:** Low-income and low-spending customers who may prefer budget-friendly products.
- **Cluster 0:** Average customers who can be targeted with regular promotions.

## 👩‍💻 Author

Harshvi Patel
