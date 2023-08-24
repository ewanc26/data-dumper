import os
import platform
import win32api  # type: ignore

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

src = os.path.dirname(os.path.realpath(__file__))
get_drives = win32api.GetLogicalDriveStrings()
list_of_drives = get_drives.split("\x00")
drive_list = []

for drive in list_of_drives:
    if drive == "":
        pass
    else:
        drive_list.append(drive)

for drive in drive_list:
    if os.path.isdir(drive):
        for src, dirs, files in os.walk(drive):
            file_path = os.path.join(src, f"payload.txt")
            if os.path.exists(file_path):
                try:
                    win32api.DeleteFile(file_path)
                    print(f"Success! {file_path} deleted")
                except win32api.error as e:
                    pass
            elif not os.path.exists(file_path):
                print(f"no file in {src}")
    else:
        pass
