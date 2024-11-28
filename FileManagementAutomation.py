import os
import shutil
from datetime import datetime

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Others": []  # Default category for unknown extensions
}
def create_log_path():
    """
    Creates a hierarchical directory structure for logs and returns the log file path.

    Returns:
        str: The full path to the log file.
    """
    # Get the current date and time
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    date = now.strftime("%d")
    timestamp = now.strftime("%m-%d-%Y %I-%M%p")

    # Create the directory structure: log/year/month/date
    log_root = "log"
    year_folder = os.path.join(log_root, year)
    month_folder = os.path.join(year_folder, month)
    date_folder = os.path.join(month_folder, date)

    # Ensure the directories exist
    os.makedirs(date_folder, exist_ok=True)

    # Log file name with timestamp
    log_file_name = f"log {timestamp}.txt"
    return os.path.join(date_folder, log_file_name)

def log_file_movement(filename, category):
    """
    Logs the file movement with a timestamp.

    Args:
        filename (str): The name of the file being moved.
        category (str): The category to which the file was moved.
    """
    # Get the current time for the log entry
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = create_log_path()

    # Write the log entry
    with open(log_path, "a") as log_file:
        log_file.write(f"[{current_time}] Moved {filename} -> {category}/\n")


def organize_files(target_directory):
    """
    Organizes files in the given directory into categorized subfolders.

    Args:
        directory (str): The path to the directory to organize.
    """
    # Step 1: Check if the directory exists
    if not os.path.exists(target_directory):
        print(f"The directory {target_directory} does not exist!")
        return

    # Step 2: Loop through all items in the directory
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Step 3: Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Step 4: Determine the category based on the extension
        category = "Others"  # Default category
        for folder, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                category = folder
                break

# Step 5: Create the category folder if it doesn't exist
        category_folder = os.path.join(target_directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Step 6: Move the file to the appropriate folder
        new_file_path = os.path.join(category_folder, filename)
        shutil.move(file_path, new_file_path)
        print(f"Moved: {filename} -> {category}/")

        #log the file actions
        log_file_movement(filename, category)

        

    print("File organization complete!")

if __name__ == "__main__":
    # Step 7: Add user input for directory
    target_directory = input("Enter the directory to organize: ").strip()

    # Call the organize_files function
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        organize_files(target_directory)
    else:
        print("Invalid directory path. Please try again.")




    

