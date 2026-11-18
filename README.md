# SMART DESKTOP FILE ORGANIZER

-A python automation script that organizes your files by automatically sorting them into categorized folders based on their extension

-This project helps keep you workspace clean and organized

## Features

- Scans a target directory(_Desktop by default_)**Can change if you want to**

-Automatically sorts file into following categories:
    -Images
    -Documents
    -Archives
    -Code
    __You can add your categories__

-Prevents file overwriting by automatically renaming duplicate files using timestamps
-It also provides a summary
-Easy to customize by adding more file extensions or categories

## Project Structure

```
PY_FILE_ORGANIZER/
|
|--schedule.py
|--README.md

```
## Requirements

-Python 3.8+
-I used no external libraries...Only used:
    ```

    -os

    -shutil

    -pathlib

    -datetime

    
## How it works

The script performs the following steps:

    -Opens the target folder (Desktop by default).

    -Reads every file in the folder.

    -Determines the file type based on its extension.

    -Creates a matching category folder if it does not already exist.

    -Moves the file into the appropriate folder.

    -Checks for duplicate filenames before moving files.

    -Renames duplicate files using a timestamp.

    -Prints a summary of the operation.

**Example:**

Before:
```

Desktop/
│
├── photo.jpg
├── report.pdf
├── project.py
├── archive.zip

```

After:
```

Desktop/
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── report.pdf
│
├── Code/
│   └── project.py
│
└── Archives/
    └── archive.zip
```

## Running a program

-Open a terminal or command prompt inside the project folder and run:

```python schedule.py```

-If Python 3 is required on your system:

```python3 schedule.py``` _Linux_

## Example output

```
---------- SUMMARY ---------- 

-Moved 14 files 

-Created/Used 4 folders 

-Organization Complete!

```

## Automating the script

Instead of running the script manually, you can schedule it to execute automatically once every day.

### Windows(Task Scheduler)

    -Press Windows + S and search for Task Scheduler.

    -Open Task Scheduler.

    -Click Create Basic Task.

    -Enter a task name (for example, Desktop File Organizer).

    -Select Daily as the trigger.

    -Choose your preferred execution time.

    -Select Start a Program.

    -Browse to your Python executable (python.exe).

    -In Add arguments, enter the full path to your script.

Example:

```
C:\Users\YourName\Documents\SmartDesktopFileOrganizer\schedule.py
```
Click Finish.

The script will now run automatically every day at the selected time.

### Linux and MacOS (Cron)

Open the terminal and type:

```crontab -e```

Add the following line to run the organizer every day at 8:00 PM:

```0 20 * * * /usr/bin/python3 /home/$USER/SmartDesktopFileOrganizer/schedule.py```

Save and exit.

Cron will now execute the script automatically every day.

## License

-This project is intended for educational and learning purposes. Feel free to modify and extend it to suit your own needs.
