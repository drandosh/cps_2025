import csv
import os

from models import SensorData


class DataStorageService:
    _file_name = 'messung.csv'
    _file_headers = ['Timestamp', 'Temperatur (Celsius)', 'Temperatur (Fahrenheit)', 'Luftfeuchtigkeit', 'Luftdruck']
    _sensor_path = '/sys/bus/iio/devices/iio:\\device0'
    _temp_file_path = '/in_temp_input'
    _humidity_file_path = '/in_humidityrelative_input'
    _pressure_file_path = '/in_pressure_input'

    def store(self, data: SensorData):
        self.__append(data)

    def read(self) -> SensorData:
        humidity = self.__get_humidity()
        temp = self.__get_temp()
        pressure = self.__get_pressure()
        return SensorData(temp, humidity, pressure)

    @staticmethod
    def __append(data: SensorData):
        file_exists = os.path.isfile(DataStorageService._file_name)
        with open(DataStorageService._file_name, mode='a', newline='') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(DataStorageService._file_headers)
            writer.writerow(data.to_array())
            print('data written to csv')

    def __get_humidity(self) -> float:
        try:
            with open(self._sensor_path + self._humidity_file_path, 'r') as file:
                content = file.read()
                return float(content) / 1000
        except(FileNotFoundError, PermissionError, OSError, ValueError):
            print('Error while reading humidity from file')

    def __get_pressure(self) -> float:
        try:
            with open(self._sensor_path + self._pressure_file_path, 'r') as file:
                content = file.read()
                return float(content) / 1000
        except(FileNotFoundError, PermissionError, OSError, ValueError):
            print('Error while reading pressure from file')

    def __get_temp(self) -> float:
        try:
            with open(self._sensor_path + self._temp_file_path, 'r') as file:
                content = file.read()
                return float(content) / 1000
        except(FileNotFoundError, PermissionError, OSError, ValueError):
            print('Error while reading temperature from file')
