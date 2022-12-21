# import modules
from tkinter import *
import tkinter as tk
from flask import Flask, make_response
import platform
import psutil
import subprocess
import webbrowser
import time

root = Tk()
root.title("내컴퓨터.com")
root.geometry("300x200")
root.resizable(False, False)

# create a label
label = Label(root, text="버튼을 눌러 사용자의\n컴퓨터 정보를 확인하세요.")
label.place(x=80, y=50)

# create a button
button = Button(root, text="내 컴퓨터 스펙 확인하기")
button.bind("<Button-1>", lambda e: clicked_button())
button.place(x=70, y=100)


# in mac
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


# send info to cookie
def get_computer_hardware():
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

    return os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity


# localhost:5000/get_info
app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/get_info', methods=['POST'])
def get_info():
    # get info wait to send
    os, cpu, ram, graphic_card, bios, mainboard_manufacturer, drive_capacity = get_computer_hardware()

    resp = make_response({
        'os': os,
        'cpu': cpu,
        'ram': ram,
        'graphic_card': graphic_card,
        'bios': bios.split("\n")[0],
        'mainboard_manufacturer': mainboard_manufacturer,
        'drive_capacity': drive_capacity
    })
    return resp,


def clicked_button():
    label.destroy()
    button.destroy()

    finishLabel = Label(root, text="컴퓨터 정보를 확인했습니다.\n웹사이트로 이동하겠습니다.")
    finishLabel.place(x=70, y=60)

    webbrowser.open_new('http://localhost:8080/gameList')
    app.run(debug=True, port=10000)


if __name__ == '__main__':
    root.mainloop()
