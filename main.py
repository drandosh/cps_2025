from models import SensorData
from data_storage_service import DataStorageService

def main():
    try:
        run()
    except:
        print('An unknown error occurred, shutting down')
        input('Press any key to exit')

def run() -> None:
    data_storage_service = DataStorageService()


def print_sensor_data(data: SensorData) -> None:
    print(f'============={data.timestamp}=============')
    print(f'Temperatur (Celsius): {data.temperature_celsius}')
    print(f'Temperatur (Fahrenheit): {data.temperature_fahrenheit}')
    print(f'Luftdruck: {data.pressure}')
    print(f'Luftfeuchtigkeit: {data.humidity}')
    print()
mock_data = SensorData(27790.0000, 25216.7968700, 100.92763)
DataStorageService.store(mock_data)

