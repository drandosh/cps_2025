from datetime import datetime, UTC


class SensorData:
    def __init__(self,
                 temperature_celsius: float,
                 humidity: float,
                 pressure: float):
        self.timestamp = datetime.now(UTC)
        self.temperature_celsius = temperature_celsius
        self.temperature_fahrenheit = temperature_celsius * 1.8 + 32
        self.humidity = humidity
        self.pressure = pressure
