import customtkinter as ctk
import serial

try:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)
except:
    print("Arduino not found, running in demo mode")

def trigger_flash():
    try:
        arduino.write(bytes("FLASH\n", 'utf-8'))
        print("Command Sent: FLASH")
    except:
        print("Error: Could not send to Arduino")

app = ctk.CTk()
app.geometry("400x240")
app.title("UHD Control Panel v1.0")

label = ctk.CTkLabel(app, text="Ultimate Hacking Device", font=("Roboto", 20))
label.pack(pady=20)

flash_button = ctk.CTkButton(app, text="FLASH STRIP", command=trigger_flash, fg_color="green")
flash_button.pack(pady=10)

app.mainloop()
