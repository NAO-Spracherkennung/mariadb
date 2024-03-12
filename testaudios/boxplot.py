import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Modellvergleich Zeit
data = {
    'Tiny (Labor)': [0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    'Tiny (Laut)': [0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    'Base (Labor)': [0.5, 0.5, 0.6, 0.7, 0.6, 0.5, 0.6, 0.5, 0.5, 0.5],
    'Base (Laut)': [0.6, 0.6, 0.6, 0.5, 0.6, 0.5, 0.6, 0.5, 0.5, 0.5],
    'Small (Labor)': [1.7, 1.5, 1.5, 1.5, 1.5, 1.4, 1.5, 1.3, 1.3, 1.3],
    'Small (Laut)': [1.4, 1.5, 1.5, 1.5, 1.5, 1.7, 1.6, 1.4, 1.3, 1.3],
    'Medium (Labor)': [5.1, 4.4, 4.8, 4.4, 4.6, 5.1, 5.1, 4.3, 4.5, 4.6],
    'Medium (Laut)': [4.8, 4.4, 4.8, 5.0, 4.5, 4.3, 4.8, 4.0, 4.2, 4.1],
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
df.boxplot(grid=False, vert=False)
plt.grid(axis='x')
plt.xlabel("Länge in Sekunden", loc="right")
plt.xticks(np.arange(0, 5.1, 0.5))
plt.show()

# Whisper vs Choregrpahe Zeit
data = {
    'Tiny (Labor)': [7.4, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3],
    'Tiny (Laut)': [7.4, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3],
    'Base (Labor)': [7.5, 7.5, 7.6, 7.7, 7.6, 7.5, 7.6, 7.5, 7.5, 7.5],
    'Base (Laut)': [7.6, 7.6, 7.6, 7.5, 7.6, 7.5, 7.6, 7.5, 7.5, 7.5],
    'Small (Labor)': [8.7, 8.5, 8.5, 8.5, 8.5, 8.4, 8.5, 8.3, 8.3, 8.3],
    'Small (Laut)': [8.4, 8.5, 8.5, 8.5, 8.5, 8.7, 8.6, 8.4, 8.3, 8.3],
    'Medium (Labor)': [12.1, 11.4, 11.8, 11.4, 11.6, 12.1, 12.1, 11.3, 11.5, 11.6],
    'Medium (Laut)': [11.8, 11.4, 11.8, 12.0, 11.5, 11.3, 11.8, 11.0, 11.2, 11.1],
    'Choregraphe (Labor)': [18, 23, 19, 17.5, 11.5, 10, 9.5, 16, 16, 16],
    'Choregraphe (Laut)': [16, 22.5, 21, 18.5, 11.5, 11, 10.5, 16, 20, 16.5],
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
df.boxplot(grid=False, vert=False)
plt.grid(axis='x')
plt.xlabel("Länge in Sekunden", loc="right")
plt.xticks(np.arange(0, 24, 1))
plt.show()

# Whisper vs Choregrpahe WER
data = {
    'Tiny (Labor)': [0, 29, 11, 33, 17, 33, 25, 0, 0, 33],
    'Tiny (Laut)': [29, 43, 11, 50, 50, 50, 100, 0, 0, 33],
    'Base (Labor)': [0, 14, 0, 0, 33, 0, 0, 0, 0, 0],
    'Base (Laut)': [14, 43, 0, 50, 33, 17, 50, 0, 0, 33],
    'Small (Labor)': [0, 0, 0, 0, 0, 0, 13, 0, 0, 0],
    'Small (Laut)': [14, 14, 0, 50, 17, 17, 13, 0, 0, 0],
    'Medium (Labor)': [14, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Medium (Laut)': [0, 29, 33, 0, 0, 17, 13, 0, 0, 0],
    'Choregraphe (Labor)': [33.5, 22.5, 12.5, 16.7, 0, 0, 0, 16.7, 16.7, 16.7],
    'Choregraphe (Laut)': [16.7, 22.2, 29, 16.7, 0, 0, 0, 33.3, 0, 33.3],
}
df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
df.boxplot(grid=False, vert=False)
plt.grid(axis='x')
plt.xlabel("WER in Prozent", loc="right")
plt.xticks(np.arange(0, 101, 10))
plt.show()