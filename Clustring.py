import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")

print(df.head())
print()
print(df.columns)
print()
print(df.isnull().sum())
print()
print(df.duplicated().sum())
print()
print(df.info())
print()

# Use 2 features for clustring
x = df[["Annual Income (k$)", "Spending Score (1-100)"]]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled[:5])

inertia = []

for k in range(1, 11):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(x_scaled)

    inertia.append(kmeans.inertia_)

# Visualization
plt.figure(figsize=(8, 5))

plt.plot(range(1, 11), inertia, marker="o")

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()

# I've identified K ≈ 5, Final K-Means model
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(x_scaled)

# Add clusters to dataset
df["Cluster"] = clusters

print("Dataset with Cluster Labels:")
print(df.head())

# Cluster Visualization
plt.figure(figsize=(8, 6))

plt.scatter(
    x["Annual Income (k$)"],
    x["Spending Score (1-100)"],
    c=clusters,
    s=50
)

# Plot cluster centroids
centers = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means")
plt.legend()

plt.show()

# Display cluster clounts
print("CUSTOMER CLUSTER COUNTS")
print(df["Cluster"].value_counts().sort_index())

# Cluster Analysis
cluster_summary = df.groupby("Cluster")[
    ["Annual Income (k$)", "Spending Score (1-100)"]
].mean()

print(cluster_summary)

print("\nCLUSTER CENTERS")

centers = scaler.inverse_transform(kmeans.cluster_centers_)

centers_df = pd.DataFrame(
    centers,
    columns=["Annual Income (k$)", "Spending Score (1-100)"]
)

print(centers_df)




