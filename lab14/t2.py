import numpy as np
import matplotlib.pyplot as plt

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
world_exports = np.array([23.6, 23.0, 23.2, 24.0, 25.9, 27.2, 28.8, 29.8, 31.0, 26.4, 28.7, 30.5, 30.3, 30.3, 29.9, 28.3, 27.4, 28.3, 29.2, 28.3, 26.4])
ukraine_exports = np.array([60.3, 50.6, 50.1, 52.5, 58.7, 47.7, 43.2, 41.3, 43.3, 42.9, 46.5, 49.4, 47.4, 42.9, 48.6, 52.6, 49.3, 48.1, 45.2, 41.2, 38.8])

#1.1
plt.figure(figsize=(12, 6))
plt.plot(years, world_exports, label='World', color='blue', marker='o')
plt.plot(years, ukraine_exports, label='Ukraine', color='green', marker='o')
plt.title('Exports of goods and services (% of GDP) Over Years', fontsize=15)
plt.xlabel('Year', fontsize=12, color='blue')
plt.ylabel('Exports (% of GDP)', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()

#1.2
country = input("Enter country name (World/Ukraine): ").strip()
data_dict = {'World': world_exports, 'Ukraine': ukraine_exports}

if country in data_dict:
    plt.figure(figsize=(12, 6))
    plt.bar(years, data_dict[country], color='orange')
    plt.title(f'Exports of goods and services (% of GDP) for {country}', fontsize=15)
    plt.xlabel('Year', fontsize=12, color='red')
    plt.ylabel('Exports (% of GDP)', fontsize=12, color='red')
    plt.grid(True, linestyle='--')
    plt.show()
else:
    print("Incorrect country name. Please enter 'World' or 'Ukraine'.")