import threading
import pynput
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

running = False
program_running = True
def Worker():
    """Worker Function runs in the background waiting till the running conition is true"""
    mouse = pynput.mouse.Controller()
    while program_running:
        if running:
            mouse.click(Button.left, 1)
            time.sleep(0.1)
        time.sleep(0.01)

def on_press(key):
    """This fucntion captures the key and does checks to see if the key 
    matches a condition needed to start the clicking or end the program """
    global running, program_running

    if hasattr(key, "char") and key.char == "s":
        print(f"[STATUS] Clicking: {running}")
        running = not running

    elif key == pynput.keyboard.Key.esc:
        program_running = False
        print(f"[STATUS] Exiting program...")
        return False

threading.Thread(target=Worker).start()



with Listener(on_press=on_press) as listener:
    listener.join()


