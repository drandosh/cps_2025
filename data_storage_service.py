import csv
import os

from models import SensorData


class DataStorageService:
    __file_name = 'measurement.csv'
    __file_headers = ['Timestamp', 'Temperatur (Celsius)', 'Temperatur (Fahrenheit)', 'Luftfeuchtigkeit', 'Luftdruck']
    __sensor_path = '/sys/bus/iio/devices/iio:\\device0'
    __temp_file_path = '/in_temp_input'
    __humidity_file_path = '/in_humidityrelative_input'
    __pressure_file_path = '/in_pressure_input'

    def store(self, data: SensorData):
        self.__append(data)

    def read(self) -> SensorData:
        humidity = self.__get_humidity()
        temp = self.__get_temp()
        pressure = self.__get_pressure()
        return SensorData(temp, humidity, pressure)

    def __append(self, data: SensorData):
        with open(self.__file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            if os.path.exists(self.__file_name):
                writer.writerow(self.__file_headers)
            writer.writerow(data.to_array())
            print(f'data written to {self.__file_name}')

    def __get_humidity(self) -> float:
        try:
            with open(self.__sensor_path + self.__humidity_file_path, 'r') as file:
                content = file.read()
                value = float(content) / 1000
                return value
        except (FileNotFoundError, PermissionError, OSError, ValueError):
            print('Error while reading humidity from file')

    def __get_pressure(self) -> float:
        try:
            with open(self.__sensor_path + self.__pressure_file_path, 'r') as file:
                content = file.read()
                value = float(content) / 1000
                return value
        except (FileNotFoundError, PermissionError, OSError, ValueError):
            print('Error while reading pressure from file')

    def __get_temp(self) -> float:
        try:
            with open(self.__sensor_path + self.__temp_file_path, 'r') as file:
                content = file.read()
                value = float(content) / 1000
                return value
        except (FileNotFoundError, PermissionError, OSError, ValueError):
            print('Error while reading temperature from file')
