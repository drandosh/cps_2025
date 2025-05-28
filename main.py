import models

DataStorageService = DataStorageService()

def print_sensor_data(data: models.SensorData) -> None:
    print(f'============={data.timestamp}=============')
    print(f'Temperatur (Celsius) {data.temperature_celsius}')
    print(f'Temperatur (Fahrenheit) {data.temperature_fahrenheit}')
    print(f'Luftdruck: {data.pressure}')
    print(f'Luftfeuchtigkeit: {data.humidity}')
mock_data = SensorData(27790.0000, 25216.7968700, 100.92763)
DataStorageService.store(mock_data)

