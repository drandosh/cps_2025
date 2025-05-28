from models import SensorData
from data_storage_service import DataStorageService


def print_sensor_data(data: SensorData) -> None:
    print(f'============={data.timestamp.strftime("%d-%m-%Y %H:%M:%S")}=============')
    print(f'Temperatur (Celsius): {data.temperature_celsius}')
    print(f'Temperatur (Fahrenheit): {data.temperature_fahrenheit}')
    print(f'Luftdruck: {data.pressure}')
    print(f'Luftfeuchtigkeit: {data.humidity}')
    print()


def run():
    print('Running...')
    data_storage_service = DataStorageService()
    mock_data = SensorData(27790.0000, 25216.7968700, 100.92763)
    data_storage_service.store(mock_data)
    print_sensor_data(mock_data)


def main():
    try:
        run()
    except Exception as e:
        print(f'An unknown error occurred, shutting down. Exception: {e}')
        input('Press any key to exit')


if __name__ == "__main__":
    main()
