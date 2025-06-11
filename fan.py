import subprocess

class Fan:
    def __init__(self):
        command = ["raspi-gpio set", "18", "op"]
        try:
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            print("Command output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error executing command:", e.stderr)

    def start(self):
        command = ["raspi-gpio set", "18", "dh"]
        try:
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            print("Command output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error executing command:", e.stderr)
    def stop(self):
        command = ["raspi-gpio set", "18", "dl"]
        try:
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            print("Command output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error executing command:", e.stderr)

    def control(self, temp :float):
        if temp < 20:
            self.stop()
        if temp >= 20:
            self.start()