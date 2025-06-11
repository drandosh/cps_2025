from fan import Fan
from models import SensorData
from data_storage_service import DataStorageService
import time

def print_sensor_data(data: SensorData) -> None:
    print(f'============={data.timestamp.strftime("%d-%m-%Y %H:%M:%S")}=============')
    print(f'Temperatur (Celsius): {data.temperature_celsius}')
    print(f'Temperatur (Fahrenheit): {data.temperature_fahrenheit}')
    print(f'Luftdruck: {data.pressure}')
    print(f'Luftfeuchtigkeit: {data.humidity}')
    print()

def kick_watchdog():
    with open( '/dev/watchdog', 'w') as wd:
        wd.write( '1' )
        wd.flush()

def run():
    data_storage_service = DataStorageService()
    #fan = Fan()
    temp = 19
    print('Running...')
    while True:
        data = data_storage_service.read()
        data_storage_service.store(data)
        print_sensor_data(data)
        #fan.control(temp)
        #temp = temp + 1
        #print(temp)
        #kick_watchdog()
        time.sleep(10)


def main():
    try:
        run()
    except Exception as e:
        print(f'An unknown error occurred, shutting down. Exception: {e}')
        input('Press any key to exit')


if __name__ == "__main__":
    main()
