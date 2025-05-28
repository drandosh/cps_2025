import csv


class DataStorage:
    _file_name = 'messung.csv'

    @staticmethod
    def store(data):
        with open(DataStorage._file_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
