import os
import shutil

# specify the path to your Downloads folder
downloads_path = os.path.expanduser("~") + "/Downloads/"

# create a folder named "Categories" in Downloads folder
categories_folder = downloads_path + "Categories"
if not os.path.exists(categories_folder):
    os.mkdir(categories_folder)

# define categories based on file extensions
file_categories = {
    ".pdf": "PDFs",
    ".doc": "Docs",
    ".docx": "Docs",
    ".xlsx": "Spreadsheets",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".exe": "Applications",
    ".svg": "Images",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z" : "Archives",
}

# iterate through the files in Downloads folder
for file_name in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file_name)
    # check if the file is not a folder and has an extension
    if os.path.isfile(file_path) and os.path.splitext(file_path)[1] in file_categories:
        # create a subfolder in Categories folder based on the file extension
        category_folder = os.path.join(categories_folder, file_categories[os.path.splitext(file_path)[1]])
        if not os.path.exists(category_folder):
            os.mkdir(category_folder)
        # move the file to the appropriate subfolder
        shutil.move(file_path, os.path.join(category_folder, file_name))
