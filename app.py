import tkinter as tk
import pyautogui
import time
import random

def main():
    start_page()
    main_loop()

def start_page():
    app = tk.Tk()
    app.title("AFK App")
    x = 1920 // 5
    y = 1080 // 2
    app.geometry(f"{x}x{y}")

    label = tk.Label(app, text="AFK App\nRunning!\n\nclose to start...", font=("Arial", 30))
    label.pack(expand=True)

    app.mainloop()
    
def main_loop():
    print("starting")

    count = 0
    old_position_x, old_position_y = pyautogui.position()

    while(True):
        new_position_x, new_position_y = pyautogui.position()
        #print(old_position_x, old_position_y)
        #print(new_position_x, new_position_y)
        
        if new_position_x == old_position_x and new_position_y == old_position_y:
            count += 1
            #print(f"count: {count}")
            if count >= 2:
                #print("afk")
                AFK_function(new_position_x, new_position_y)
                continue
        else:
            count = 0
            #print("moved")

        old_position_x, old_position_y = new_position_x, new_position_y
        
        #print("sleeping")
        time.sleep(30)
    
    

def AFK_function(old_x, old_y):
    #pyautogui.moveTo(1920 // 2, 1080 // 2)
    #time.sleep(1)

    print("moving")

    random_x = random.randrange(0, 1920)
    random_y = random.randrange(0, 1080)

    pyautogui.moveTo(random_x, random_y)
    pyautogui.moveTo(old_x, old_y)
    time.sleep(30)

main()