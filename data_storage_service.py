import csv
import os
import string

import sensor_data
from sensor_data import SensorData


class DataStoraService:
    _file_name = 'messung.csv'
    _file_headers = ['Timestamp', 'Tempereatur (celsius)', 'Tempereatur (fahrenheit)', 'Luftfeuchte', 'Luftdruck']
    _sensor_path = '/sys/bus/iio/devices/iio:\\device0'
    _temp_file_path = '/in_temp_input'
    _humidity_file_path = 'in_humidityrelative_input'
    _pressure_file_path = 'in_pressure_input'


    def __init__(self):

    def store(self ,data: SensorData):
        if DataStoraService.file_exists():
            DataStoraService.append_data_to_file(data)
        else:
            DataStoraService.create_file(data)


    def create_file(self, data : SensorData):
        with open(DataStoraService._file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(DataStoraService._file_headers)
            writer.writerow(data)



    def append_data_to_file(self, data):
        with open('data_with_headers.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)


    def file_exists(self) -> bool:
        if os.path.exists(DataStoraService._file_name):
            return True
        else:
            return False

    def read(self) -> SensorData:
        humidity = self._get_humidity()
        temp = self._get_temp()
        pressure = self._get_pressure()
        return SensorData(humidity, 0 ,temp, pressure)

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