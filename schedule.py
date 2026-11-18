#import required modules
import os
import shutil
from pathlib import Path
from datetime import datetime

#Target folder to organize
TARGET_FOLDER = Path.home() / "Desktop"
# You can change this to Downloads if needed:
# TARGET_FOLDER = Path.home() / "Downloads"

#File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js", ".json"]
}

# Counter for summary
moved_files = 0

# Counter for number of folders used
used_folders = set()

#Organize files
for file in TARGET_FOLDER.iterdir():

    # Ignore folders
    if file.is_dir():
        continue

    # Get file extension
    extension = file.suffix.lower()

    destination_folder = None

    # Find matching category
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            destination_folder = TARGET_FOLDER / category
            break

    # Skip unknown file types
    if destination_folder is None:
        continue

    # Create destination folder if it doesn't exist
    destination_folder.mkdir(exist_ok=True)

    used_folders.add(destination_folder.name)

    destination = destination_folder / file.name

    # Handle duplicate filenames
    if destination.exists():

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        destination = destination_folder / f"{file.stem}_{timestamp}{file.suffix}"

    # Move file
    shutil.move(str(file), str(destination))

    moved_files += 1


# Print Summary

print("---------- SUMMARY ----------")
print(f"Moved {moved_files} files")
print(f"Created/Used {len(used_folders)} folders")
print("Organization Complete!")