import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Sample dataset
data = pd.DataFrame({
    "query": ["comedy", "comedy", "action", "action"],
    "item": ["MovieA", "MovieB", "MovieC", "MovieD"],
    "sim_score": [0.8, 0.6, 0.4, 0.9],   
    "popularity": [100, 50, 30, 120],
    "rating": [4.5, 3.2, 2.0, 4.8]
})

X = data[["sim_score", "popularity"]]
y = data["rating"]

# Train a pointwise model
model = GradientBoostingRegressor()
model.fit(X, y)

# Predict scores for candidates
data["pred_score"] = model.predict(X)

# Rank within each query
ranked = data.sort_values(by=["query", "pred_score"], ascending=[True, False])
print(ranked[["query", "item", "pred_score"]])
