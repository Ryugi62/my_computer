import tkinter as tk
import platform
import psutil
import subprocess
import webbrowser
import requests


def createGUI():
    root = tk.Tk()
    root.title("Hello World")
    root.geometry("300x200")

    # create a label
    label = tk.Label(root, text="버튼을 눌러 사용자의\n컴퓨터 정보를 확인하세요.")
    label.place(x=80, y=40)

    # create a button
    button = tk.Button(root, text="Click Me")
    button.bind("<Button-1>", lambda e: clicked_button())
    button.place(x=105, y=90)


def clicked_button():
    os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity = getHardwareInfo()

    ip = getIP()

    sendHardwareInfo(ip, os, cpu, ram, graphic_card, bios,
                     mainboard_manufacturer, drive_capacity)

    webbrowser.open("http://localhost:3000/myHardware")

    # stop tk.mainloop() and close window
    tk._exit()


def getIP():
    # get ip
    ip = requests.get("https://api.ipify.org").text
    return ip


def mac():
    # get os
    os = platform.platform()

    # get cpu
    cpu = platform.processor()

    # get ram
    ram = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"

    # get graphic card
    graphic_card = subprocess.check_output(
        "/usr/sbin/system_profiler SPDisplaysDataType | grep 'Chipset Model:'", shell=True).decode("utf-8").split(":")[1].strip()

    # get bios version
    bios_version = subprocess.check_output(
        "/usr/sbin/system_profiler SPHardwareDataType | grep 'Version:'", shell=True).decode("utf-8").split(":")[1].strip()

    # get drive capacity
    drive_capacity = str(
        round(psutil.disk_usage('/').total / (1024.0 ** 3)))+" GB"

    # print
    # return os, cpu, ram, graphic_card, bios_version, mainboard_manufacturer, drive_capacity
    return os, cpu, ram, graphic_card, bios_version, drive_capacity


# in windows
def windows():
    # get os
    os = platform.platform()

    # get cpu
    cpu = platform.processor()

    # get ram
    ram = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"

    # get graphic card
    graphic_card = subprocess.check_output(
        "wmic path win32_VideoController get name", shell=True).decode("utf-8").split("\n")[1].strip()

    # get bios version
    bios_version = subprocess.check_output(
        "wmic bios get smbiosbiosversion", shell=True).decode("utf-8").split("\n")[1].strip()

    # get mainboard manufacturer
    mainboard_manufacturer = subprocess.check_output(
        "wmic baseboard get manufacturer", shell=True).decode("utf-8").split("\n")[1].strip()

    # get drive capacity
    drive_capacity = str(
        round(psutil.disk_usage('C:\\').total / (1024.0 ** 3)))+" GB"

    # print
    return os, cpu, ram, graphic_card, bios_version, mainboard_manufacturer, drive_capacity


def getHardwareInfo():
    # get info
    if platform.system() == "Windows":
        # os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity = windows()
        os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity = windows()
    elif platform.system() == "Darwin":
        # os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity = mac()
        os, cpu, ram, graphic_card, bios, drive_capacity = mac()
        mainboard_manufacturer = "Can't found"
    else:
        print("Sorry, your system is not supported yet.")
        return False

    return os, cpu, ram, graphic_card, bios.split("\n")[0], mainboard_manufacturer, drive_capacity


def sendHardwareInfo(ip, os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity):
    url = "http://localhost:3000/api/setHardware"

    data = {
        "ip": ip,
        "os": os,
        "cpu": cpu,
        "ram": ram,
        "graphic_card": graphic_card,
        "bios": bios,
        "mainboard_manufacturer": mainboard_manufacturer,
        "drive_capacity": drive_capacity
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)


def main():
    createGUI()
    tk.mainloop()


if __name__ == "__main__":
    main()
