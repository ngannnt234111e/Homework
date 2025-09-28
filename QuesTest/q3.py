items = {"Apple": 3, "Banana": 1, "Orange": 4}
# Pairwise comparisons
pairs = [("Apple","Banana"), ("Apple","Orange"), ("Banana","Orange")]
wins = {item:0 for item in items}
for a,b in pairs:
    if items[a] > items[b]:
        wins[a] += 1
    else:
        wins[b] += 1
# Final ranking
ranking = sorted(wins.items(), key=lambda x: -x[1])
print("Ranking:", ranking)
