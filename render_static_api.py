import csv

def read_data_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

if __name__ == '__main__':
    read_data_csv('tafe.csv')
    read_data_csv('uni.csv')