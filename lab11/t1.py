import csv

input_file_path = 'raw.csv'
output_file_path = 'cooked.csv'

try:
    with open(input_file_path, mode='r', encoding='utf-8') as file:
        print(file.read()) #not sure that was that a good idea

        reader = csv.reader(file)
        headers = next(reader) 
        
        year_indices = [headers.index(f"{year} [YR{year}]") for year in range(1991, 2019)]
        
        gdp_data = []
        for row in reader:
            if row and row[0] == 'GDP per capita (current US$)':
                gdp_data = [row[i] for i in year_indices]
                break
        
        min_gdp = min(gdp_data)
        max_gdp = max(gdp_data)

    with open(output_file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Min GDP', 'Max GDP'])
        writer.writerow([min_gdp, max_gdp])

except Exception as e:
    print(f"Err: {e}")
