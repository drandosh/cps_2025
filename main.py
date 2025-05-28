import models


def print_sensor_data(data: models.SensorData) -> None:
    print(f'============={data.timestamp}=============')
    print(f'Temperatur (Celsius) {data.temperature_celsius}')
    print(f'Temperatur (Fahrenheit) {data.temperature_fahrenheit}')
    print(f'Luftdruck: {data.pressure}')
    print(f'Luftfeuchtigkeit: {data.humidity}')

