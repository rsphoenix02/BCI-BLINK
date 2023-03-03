import threading
import demo_thread


# Create a thread
def create_thread():
    thread = threading.Thread(target=demo_thread.read_serial)
    # Start the thread
    thread.start()
