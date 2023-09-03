import os
import platform
import win32api  # type: ignore

# Check the operating system
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

# Get the directory of the current script
src = os.path.dirname(os.path.realpath(__file__))
# Get a list of available drives on the Windows system
get_drives = win32api.GetLogicalDriveStrings()
list_of_drives = get_drives.split("\x00")
drive_list = []

# Filter out empty drive names and create a list of available drives
for drive in list_of_drives:
    if drive != "":
        drive_list.append(drive)

# Iterate through the list of drives
for drive in drive_list:
    # Check if the drive is a directory
    if os.path.isdir(drive):
        # Recursively walk through the directory and its subdirectories
        for src, dirs, files in os.walk(drive):
            # Create a file path for the "payload.txt" file in the current directory
            file_path = os.path.join(src, f"payload.txt")
            
            # Check if the file exists
            if os.path.exists(file_path):
                try:
                    # Attempt to delete the "payload.txt" file
                    win32api.DeleteFile(file_path)
                    print(f"Success! {file_path} deleted")
                except win32api.error as e:
                    # Ignore errors and continue to the next file or directory
                    pass
            else:
                # If the file doesn't exist in the current directory, print a message
                print(f"No file found in {src}")
    else:
        # If the drive is not a directory, skip it
        pass
