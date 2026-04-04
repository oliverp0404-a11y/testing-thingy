import tkinter as tk
import serial
import time

try:
    # Standard Arduino port for Raspberry Pi
    arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=0.1)
    time.sleep(2)
except:
    print("Arduino not found! Check the USB cable.")

def trigger_flash():
    try:
        arduino.write(bytes("FLASH\n", 'utf-8'))
        print("Command Sent: FLASH")
    except:
        print("Error: Could not send to Arduino")

# Setup Window
root = tk.Tk()
root.title("UHD Control Panel v1.0")
root.geometry("800x480") # Fits your 7" screen

# Big Title
label = tk.Label(root, text="Ultimate Hacking Device", font=("Arial", 30))
label.pack(pady=40)

# Big Easy-to-Touch Button
flash_button = tk.Button(root, text="FLASH STRIP", command=trigger_flash, 
                         bg="green", fg="white", font=("Arial", 25), 
                         height=3, width=20)
flash_button.pack(pady=20)

root.mainloop()
