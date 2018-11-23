# Add python code in this file

import csv

cities = []
with open('cities.csv') as citiesFile:
    reader = csv.DictReader(citiesFile)
    for row in reader:
        cities.append(row)

with open('output_points.csv', 'w', newline='') as outputFile:
    fieldnames = ['ID', 'X', 'Y', 'City']
    writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
    writer.writeheader()

    with open('points.csv') as pointsFile:
        reader = csv.DictReader(pointsFile)
        for row in reader:
            status = 'None'
            for city in cities:
                if int(city['TopLeft_X']) <= int(row['X']) <= int(city['BottomRight_X']) and \
                        int(city['TopLeft_Y']) <= int(row['Y']) <= int(city['BottomRight_Y']):
                    status = city['Name']
            writer.writerow({'ID': row['ID'], 'X': row['X'], 'Y': row['Y'], 'City': status})
        print('output_points.csv file is ready in project folder.')




