# pyinstaller exe detected as virus
import base64
# import modules
import os
import psutil
import platform
import requests
import webbrowser
import wmi
import subprocess
import ctypes
import playsound


msg_title = "내컴퓨터.com"
msg_content = "사양 스캔이 완료되었습니다.\n다운받은 프로그램을 삭제하여도 추후 사양을 다시 확인할 수 있습니다."


your_code = base64.b64encode(b"""
def main():
    # get my computer information
    cpu, built_in_vga, dedicated_vga, ram, full_drive, free_drive, os, mainboard_chipset, mainboard_manufacturer = get_my_computer_info()

    # get ip address
    ip = get_user_ip_address()

    # send my computer information to server
    sendHardwareInfo(ip, cpu, mainboard_manufacturer, mainboard_chipset,
                    dedicated_vga, built_in_vga, ram, full_drive, os)

    # open my computer gamelist website
    open_website()

    # open alert window
    open_alert()


# get cpu information
def get_cpu_name():
    return subprocess.check_output("wmic cpu get name", shell=True).decode("utf-8").split("\\n")[1].strip()


# get vga information
def get_vga_name():
    built_in_vga = None
    dedicated_vga = None
    w = wmi.WMI()
    for gpu in w.Win32_VideoController():
        if "Intel" in gpu.Name:
            built_in_vga = gpu.Name
        else:
            dedicated_vga = gpu.Name

    return str(built_in_vga), str(dedicated_vga)


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
    return platform.platform()


# get mainboard information
def get_mainboard_name():
    chipset = subprocess.check_output(
        "wmic baseboard get manufacturer", shell=True).decode("utf-8").split("\\n")[1].strip()
    manufacturer = subprocess.check_output(
        "wmic baseboard get product", shell=True).decode("utf-8").split("\\n")[1].strip()

    return chipset, manufacturer


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
    ip = requests.get("https://ifconfig.me/ip").text.strip()
    print("IP: " + ip)
    return ip


# get sound file path
def find_sound_file_path():
    sound_file_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "sound.mp3").replace("\\", "/")
    return sound_file_path


# send my computer information to my computer hardware database
def sendHardwareInfo(ip, cpu, mainboard_manufacturer, mainboard_chipset, dedicated_vga, built_in_vga, ram, full_drive, os):
    url = "http://xn--220br78cbrb12f.com/api/setHardware"
    # url = "http://localhost:3000/api/setHardware"

    data = {
        "ip": ip,
        "cpu": cpu,
        "mainboard_manufacturer": mainboard_chipset + ", " + mainboard_manufacturer,
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
    from playsound import playsound
    playsound(find_sound_file_path())

    ctypes.windll.user32.MessageBoxW(0, msg_content, msg_title, 0)


# run main function
if __name__ == "__main__":
    main()
""")

exec(base64.b64decode(your_code))
