import numpy as np
# 4 documents for 1 query
X = np.array([
    [0.9, 5.0],   # Doc A
    [0.6, 3.0],   # Doc B
    [0.2, 1.0],   # Doc C
    [0.4, 2.0]    # Doc D
])
y = np.array([3, 2, 0, 1])
w = np.array([0.1, 0.1])
def softmax(z):
    z = z - np.max(z)
    e = np.exp(z)
    return e / np.sum(e)
# One training step (listwise)
scores = X @ w
P_y = softmax(y)
P_s = softmax(scores)
loss = -np.sum(P_y * np.log(P_s + 1e-12))
print("True dist:", np.round(P_y, 3))
print("Pred dist:", np.round(P_s, 3))
print("Listwise loss:", round(loss, 3))
