import csv
import json
import os

def read_data_csv(filename):
    result = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result.append(row)
    return result

def data_row_to_dict(row, type):
    return {
        'name': row[0],
        'logo': f'/{type}/{row[1]}'
    }

if __name__ == '__main__':
    root_folder = 'api/'
    tafe_data = read_data_csv('tafe.csv')
    uni_data = read_data_csv('uni.csv')

    schools = []

    for tafe in tafe_data:
        schools.append(data_row_to_dict(tafe, type='TAFE'))

    for uni in uni_data:
        schools.append(data_row_to_dict(uni, type='UNI'))
    
    for school in schools:
        with open(f'{root_folder}/{school["name"]}.json', 'w') as jsonfile:
            json.dump(school, jsonfile)

    with open(f'{root_folder}/all.json', 'w') as jsonfile:
        json.dump(schools, jsonfile, indent=4)
    