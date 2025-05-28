import csv
import os

from models import SensorData


class DataStorageService:
    _file_name = 'messung.csv'
    _file_headers = ['Timestamp', 'Tempereatur (celsius)', 'Tempereatur (fahrenheit)', 'Luftfeuchte', 'Luftdruck']
    _sensor_path = '/sys/bus/iio/devices/iio:\device0'
    _temp_file_path = '/in_temp_input'
    _humidity_file_path = '/in_humidityrelative_input'
    _pressure_file_path = '/in_pressure_input'


    #def __init__(self):

    def store(self ,data: SensorData):
        if DataStorageService.storage_file_exists():
            DataStorageService.append_data_to_file(self, data)
        else:
            DataStorageService.create_file(self, data)


    def create_file(self, data : SensorData):
        with open(DataStorageService._file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(DataStorageService._file_headers)
            writer.writerow(data.to_array())



    def append_data_to_file(self, data):
        with open('data_with_headers.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data.to_array())


    @staticmethod
    def storage_file_exists() -> bool:
        if os.path.exists(DataStorageService._file_name):
            return True
        else:
            return False

    def read(self) -> SensorData:
        humidity = self._get_humidity()
        temp = self._get_temp()
        pressure = self._get_pressure()
        return SensorData(temp, humidity, pressure)

    def _get_humidity(self) -> float:
        with open(self._sensor_path + self._humidity_file_path, 'r') as file:
            content = file.read()
            return float(content)
    def _get_pressure(self) -> float:
        with open(self._sensor_path + self._pressure_file_path, 'r') as file:
            content = file.read()
            return float(content)
    def _get_temp(self) -> float:
        with open(self._sensor_path + self._temp_file_path, 'r') as file:
            content = file.read()
            return float(content)