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

def data_row_to_dict(row, type, url):
    return {
        f'{row[0]}': f'{url}/{type}/{row[1]}'
    }

if __name__ == '__main__':
    api_url = 'https://raw.githubusercontent.com/minhdq1998/AusUniversityLogoApi/main'
    root_folder = 'api/'

    tafe_data = read_data_csv('tafe.csv')
    uni_data = read_data_csv('uni.csv')

    schools = {}

    for tafe in tafe_data:
        # schools.append(data_row_to_dict(tafe, type='TAFE', url=api_url))
        schools[f'{tafe[0]}'] = f'{api_url}/"TAFE"/{tafe[1]}'

    for uni in uni_data:
        # schools.append(data_row_to_dict(uni, type='UNI', url=api_url))
        schools[f'{uni[0]}'] = f'{api_url}/"TAFE"/{uni[1]}'
    
    # for school in schools:
    #     with open(f'{root_folder}/{school["name"]}.json', 'w') as jsonfile:
    #         json.dump(school, jsonfile)

    with open(f'{root_folder}/all.json', 'w') as jsonfile:
        json.dump(schools, jsonfile, indent=4)
    