# import modules
import psutil
import socket
import platform
import requests
import webbrowser
import tkinter as tk


# create gui window for my computer information
def create_gui_window():
    # create window
    window = tk.Tk()

    # set window title
    window.title("Hello World")

    # set window size
    window.geometry("300x200")

    # create a label
    label = tk.Label(window, text="버튼을 눌러 사용자의\n컴퓨터 정보를 확인하세요.")
    label.place(x=80, y=40)

    # create a button
    button = tk.Button(window, text="Click Me", command=click_button)
    button.place(x=105, y=90)

    # can't resize window
    window.resizable(False, False)


# if click button
def click_button():
    # # send my computer information to server
    # sendHardwareInfo(get_user_ip_address(), get_my_computer_info())

    # open my computer information page
    webbrowser.open("http://xn--220br78cbrb12f.com/myHardware")

    # stop tk.mainloop() and close window
    tk._exit()


# get user ip address in windows with python
def get_user_ip_address():
    return socket.gethostbyname(socket.gethostname())


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


# send my computer information to my computer hardware database
def sendHardwareInfo(ip, cpu, built_in_vga, dedicated_vga, ram, full_drive, free_drive, os, board_chipset, board_manufacturer):
    url = "http://xn--220br78cbrb12f.com/api/setHardware"

    data = {
        "ip": ip,
        "cpu": cpu,
        "built_in_vga": built_in_vga,
        "dedicated_vga": dedicated_vga,
        "ram": ram,
        "full_drive": full_drive,
        "free_drive": free_drive,
        "os": os,
        "board_chipset": board_chipset,
        "board_manufacturer": board_manufacturer
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)


# open my computer gamelist website
def open_browser():
    pass


def open_my_computer_gamelist_website():
    pass


# main function
def main():
    # create gui window
    create_gui_window()

    # start gui window
    tk.mainloop()


# run main function
if __name__ == "__main__":
    main()
