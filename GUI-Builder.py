import tkinter as tk
import serial
import time

try:
    arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=0.1)
    time.sleep(2)
except:
    print("Arduino not found!")

def trigger_Flash():
    try:
        arduino.write(bytes("FLASH\n", 'utf-8'))
    except: print("Error sending FLASH")

def trigger_Start():
    try:
        arduino.write(bytes("START\n", 'utf-8'))
    except: print("Error sending START")

def trigger_Get():
    try:
        arduino.write(bytes("GET\n", 'utf-8'))
    except: print("Error sending GET")

def update_log():
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').rstrip()
        log_box.insert(tk.END, line + "\n")
        log_box.see(tk.END)
    root.after(100, update_log)

root = tk.Tk()
root.title("UHD Control Panel v1.0")
root.geometry("800x480")

label = tk.Label(root, text="Ultimate Hacking Device", font=("Arial", 20))
label.pack(pady=10)

log_box = tk.Text(root, height=10, width=70, bg="black", fg="lime")
log_box.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="FLASH", command=trigger_Flash, bg="green", fg="white", width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="START SNIFF", command=trigger_Start, bg="blue", fg="white", width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="GET DATA", command=trigger_Get, bg="orange", fg="white", width=15).grid(row=0, column=2, padx=5)

update_log()
root.mainloop()
