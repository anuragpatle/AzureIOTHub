import os
from tkinter import *
import sys

# Without below lines this error will come
# by crontab
#
# self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use) _tkinter.TclError: no display name and no $DISPLAY environment variable
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


class Dashboard(Tk):

    last_mtime = None
    root_path = '/home/pi/MyProjects/AzureIOTHub/RaspberryPiApp/Files'
    sensor_data_file = root_path + '/SensorData.txt'

    def __init__(self):
        super().__init__()
        self.geometry("1024x768")
        # self.geometry("800x480")

        self.attributes('-fullscreen', True)
        self.resizable(True, True)

    def createHeaders(self):
        temperatureLbl = Label(
            self, bg="white", text="Temperature", fg='#676362', padx=5, pady=5, font=('URW Gothic L','25','bold'))
        temperatureLbl.place(x=430, y=210)

        moistureLbl = Label(
            self, bg="white", text="Soil Moisture", fg='#676362', padx=5, pady=5, font=('URW Gothic L','25','bold'))
        moistureLbl.place(x=430, y=300)

        humidityLbl = Label(
             self, bg="white", text="Air Humidity", fg='#676362', padx=5, pady=5, font=('URW Gothic L','25','bold'))
        humidityLbl.place(x=430, y=390)

    def background(self):
        self.backGroundImage = PhotoImage(file= self.root_path + "/bg.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

    def monitor_file_change(self):
        temprature_label = Label(
            self, bg="white", fg='#6a0038', pady=5, font="bold 60")
        temprature_label.place(x=655, y=180)

        soil_moisture_label = Label(
            self, bg="white", fg='#6a0038', pady=5, font="bold 60")
        soil_moisture_label.place(x=655, y=270)

        humidity_label = Label(
            self, bg="white", fg='#6a0038', pady=5, font="bold 60")
        humidity_label.place(x=655, y=360)

        mtime = os.path.getmtime(self.sensor_data_file)
        if Dashboard.last_mtime is None or mtime > Dashboard.last_mtime:
            with open(self.sensor_data_file) as f:
                values = f.read()
                separatedValues = values.split(";")
                # Temperature
                temprature_label['text'] = separatedValues[0] + "°C"
                soil_moisture_label['text'] = separatedValues[1]  # Moisture
                humidity_label['text'] = separatedValues[2]  # Humidity
            Dashboard.last_mtime = mtime
        self.after(1000, self.monitor_file_change)


if __name__ == "__main__":

    Dashboard = Dashboard()
    Dashboard.background()
    Dashboard.createHeaders()
    Dashboard.monitor_file_change()
    Dashboard.mainloop()

