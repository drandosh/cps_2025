from datetime import datetime, UTC


class SensorData:
    def __init__(self,
                 raw_temperature_celsius: float,
                 humidity: float,
                 pressure: float):
        self.timestamp = datetime.now(UTC)
        self.temperature_celsius = (raw_temperature_celsius / 1000)
        self.temperature_fahrenheit = raw_temperature_celsius * 1.8 + 32
        self.humidity = humidity
        self.pressure = pressure

    def to_array(self):
        return [
            self.timestamp,
            self.temperature_celsius,
            self.temperature_fahrenheit,
            self.humidity,
            self.pressure,
        ]
