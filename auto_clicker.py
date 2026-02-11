import threading
import pynput
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

running = False
programme_running = True
def Worker():
    mouse = pynput.mouse.Controller()
    while programme_running:
        if running:
            mouse.click(Button.left, 1)
            time.sleep(0.1)
        time.sleep(0.01)

def on_press(key):
    global running, programme_running
    try:
        if key.char == "s":
            running = not running
    except AttributeError:
        pass

threading.Thread(target=Worker).start()



with Listener(on_press=on_press) as listener:
    listener.join()

