import queue
import serial

data_queue = queue.Queue()
n = 0


def read_serial():
    arduino = serial.Serial('COM4', 115200, timeout=1)

    while True:
        data = arduino.readline()
        if data:
            string = data.decode()
            s = string.strip()
            arr = s.split(',')
            if len(arr) == 2 and arr[1] != '':
                inp = int(arr[1])
                # print(n)
                data_queue.put(inp)
            else:
                continue
