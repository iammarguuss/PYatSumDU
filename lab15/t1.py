import pandas as pd

data = {
    "Vitaly_Prikhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10],
    "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4],
    "Mikhail_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4],
    "Maxim_Derizemlya": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7],
    "Victoria_Zhuk": [10, 10, 10, 9, 10, 9, 10, 8, 7, 12],
    "Andrey_Kuryanov": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8],
    "Oksana_Dubovets": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10],
    "Nikita_Stroganov": [6, 7, 8, 9, 10, 10, 10, 10, 10, 9],
    "Karina_Nikolaenko": [2, 3, 5, 4, 5, 4, 3, 3, 5, 8]
}
df = pd.DataFrame(data)

print("Initial DataFrame:\n", df)

mean_scores = df.mean() 
median_scores = df.median()
max_scores = df.max()  
min_scores = df.min()  

print("\nMean Scores:\n", mean_scores)
print("\nMedian Scores:\n", median_scores)
print("\nMax Scores:\n", max_scores)
print("\nMin Scores:\n", min_scores)