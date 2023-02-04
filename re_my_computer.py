# import modules
import psutil
import socket
import platform
import requests
import webbrowser
import tkinter as tk


from playsound import playsound
from tkinter import messagebox


def main():
    # get my computer information
    cpu, built_in_vga, dedicated_vga, ram, full_drive, free_drive, os, mainboard_chipset, mainboard_manufacturer = get_my_computer_info()

    # get ip address
    ip = get_user_ip_address()

    # send my computer information to server
    sendHardwareInfo(ip, cpu, mainboard_manufacturer,
                     dedicated_vga, built_in_vga, ram, full_drive, os)

    # open my computer gamelist website
    open_website()

    # open alert window
    open_alert()


# get cpu information
def get_cpu_name():
    return platform.processor()


# get vga information
def get_vga_name():
    # how to get built-in graphics card name in windows with python
    def get_built_in_vga_name():
        return platform.processor()

    # how to get dedicated graphics card name in windows with python
    def get_dedicated_vga_name():
        return platform.processor()

    return get_built_in_vga_name(), get_dedicated_vga_name()


# get ram information
def get_ram_size():
    return str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"


# get drive information
def get_drive_size():
    # how to get drive size in windows with python
    def get_full_drive_size():
        return str(round(psutil.disk_usage('/').total / (1024.0 ** 3))) + " GB"

    # how to get free drive size in windows with python
    def get_free_drive_size():
        return str(round(psutil.disk_usage('/').free / (1024.0 ** 3))) + " GB"

    return get_full_drive_size(), get_free_drive_size()


# get os information
def get_os_name():
    return platform.system()


# get mainboard information
def get_mainboard_name():
    # how to get mainboard chipset in windows with python
    def get_mainboard_chipset():
        return platform.processor()

    # how to get mainboard manufacturer in windows with python
    def get_mainboard_manufacturer():
        return platform.processor()

    return get_mainboard_chipset(), get_mainboard_manufacturer()


# get my computer information
def get_my_computer_info():
    cpu = get_cpu_name()  # get cpu information
    built_in_vga, dedicated_vga = get_vga_name()  # get vga information
    ram = get_ram_size()  # get ram information
    full_drive, free_drive = get_drive_size()  # get drive information
    os = get_os_name()  # get os information
    board_chipset, board_manufacturer = get_mainboard_name()  # get mainboard information

    # print my computer information
    print("CPU: " + cpu)
    print("Built-in VGA: " + built_in_vga)
    print("Dedicated VGA: " + dedicated_vga)
    print("RAM: " + ram)
    print("Full Drive: " + full_drive)
    print("Free Drive: " + free_drive)
    print("OS: " + os)
    print("Mainboard Chipset: " + board_chipset)
    print("Mainboard Manufacturer: " + board_manufacturer)

    return cpu, built_in_vga, dedicated_vga, ram, full_drive, free_drive, os, board_chipset, board_manufacturer


# get my ip address
def get_user_ip_address():
    ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
    print("IP: " + ip)
    return ip


# send my computer information to my computer hardware database
def sendHardwareInfo(ip, cpu, mainboard_manufacturer, dedicated_vga, built_in_vga, ram, full_drive, os):
    # url = "http://xn--220br78cbrb12f.com/api/setHardware"
    url = "http://localhost:3000/api/setHardware"

    data = {
        "ip": ip,
        "cpu": cpu,
        "mainboard_manufacturer": mainboard_manufacturer,
        "external_vga": dedicated_vga,
        "internal_vga": built_in_vga,
        "ram": ram,
        "full_drive": full_drive,
        "os": os,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)


# open my computer gamelist website
def open_website():
    webbrowser.open("http://xn--220br78cbrb12f.com/myHardware")


# open messagebox
def open_alert():
    root = tk.Tk()
    root.withdraw()

    # background music
    playsound("sound.mp3")

    messagebox.showinfo(
        "내컴퓨터.com", "사양 스캔이 완료되었습니다.\n다운받은 프로그램을 삭제하여도 추후 사양을 다시 확인할 수 있습니다.")

    root.destroy()


# run main function
if __name__ == "__main__":
    main()
