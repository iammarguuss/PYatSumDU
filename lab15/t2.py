import pandas as pd
import matplotlib.pyplot as plt

file_path = 'BUBUBU.csv'

try:
    bike_data = pd.read_csv(
        file_path,
        sep=',',
        encoding='latin1',
        parse_dates={'DateTime': [0, 1]},
        dayfirst=True, 
        index_col='DateTime',
        na_values=['']
    )
    bike_data = bike_data.apply(pd.to_numeric, errors='coerce')
    print("Данные успешно загружены")
except Exception as e:
    print(f"Ошибка при загрузке файла: {e}")

plt.figure(figsize=(15, 10))

for column in bike_data.columns:
    bike_data[column].dropna().plot(label=column)

plt.title('Daily Bicycle Traffic by Track')
plt.xlabel('Date') 
plt.ylabel('Number of Bicyclists') 
plt.legend(loc='upper left') 
plt.grid(True)
plt.show()