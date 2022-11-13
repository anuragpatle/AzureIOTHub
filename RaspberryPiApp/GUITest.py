import os
from tkinter import *

# For 5 inch display the resolution will be: 800×480

# root = Tk()

# Label(text='Watch Log of COW').pack()
# log = Label(text='abc')
# log.pack()

# last_mtime = None
# cow = './Files/SensorData.txt'

# def monitor_file_change():
#     global last_mtime
#     mtime = os.path.getmtime(cow)
#     if last_mtime is None or mtime > last_mtime:
#         with open(cow) as f:
#             log['text'] = f.read()
#         last_mtime = mtime
#     root.after(1000, monitor_file_change)

# monitor_file_change()
# root.mainloop()


class Dashboard(Tk):

    last_mtime = None
    sensor_data_file = './Files/SensorData.txt'

    def __init__(self):
        super().__init__()
        self.geometry("800x480")
        self.resizable(False, False)

    def createHeaders(self):
        temperatureLbl = Label(
            self, bg="white", text="Temperature", fg='#676362', padx=5, pady=5, font=('URW Gothic L','25','bold'))
        temperatureLbl.place(x=330, y=110)

        moistureLbl = Label(
            self, bg="white", text="Soil Moisture", fg='#676362', padx=5, pady=5, font=('URW Gothic L','25','bold'))
        moistureLbl.place(x=330, y=200)

        humidityLbl = Label(
             self, bg="white", text="Air Humidity", fg='#676362', padx=5, pady=5, font=('URW Gothic L','25','bold'))
        humidityLbl.place(x=330, y=290)

    def background(self):
        self.backGroundImage = PhotoImage(file="./Files/bg.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

    def monitor_file_change(self):
        temprature_label = Label(
            self, bg="white", fg='#6a0038', pady=5, font="bold 60")
        temprature_label.place(x=555, y=80)

        soil_moisture_label = Label(
            self, bg="white", fg='#6a0038', pady=5, font="bold 60")
        soil_moisture_label.place(x=555, y=170)

        humidity_label = Label(
            self, bg="white", fg='#6a0038', pady=5, font="bold 60")
        humidity_label.place(x=555, y=260)

        mtime = os.path.getmtime(self.sensor_data_file)
        if Dashboard.last_mtime is None or mtime > Dashboard.last_mtime:
            with open(self.sensor_data_file) as f:
                values = f.read()
                separatedValues = values.split(";")
                # Temperature
                temprature_label['text'] = separatedValues[0] + "°C"
                humidity_label['text'] = separatedValues[1]  # Humidity
                soil_moisture_label['text'] = separatedValues[2]  # Moisture
            Dashboard.last_mtime = mtime
        self.after(1000, self.monitor_file_change)


if __name__ == "__main__":

    Dashboard = Dashboard()
    Dashboard.background()
    Dashboard.createHeaders()
    Dashboard.monitor_file_change()
    Dashboard.mainloop()


# root = Tk()

# Label(text='Watch Log of COW').pack()
# log = Label(text='abc')
# log.pack()

# last_mtime = None
# cow = './Files/SensorData.txt'

# def monitor_file_change():
#     global last_mtime
#     mtime = os.path.getmtime(cow)
#     if last_mtime is None or mtime > last_mtime:
#         with open(cow) as f:
#             log['text'] = f.read()
#         last_mtime = mtime
#     root.after(1000, monitor_file_change)

# monitor_file_change()
# root.mainloop()
