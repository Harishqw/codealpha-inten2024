import os
import shutil

def organize_files(directory):
    """Organize files in a directory based on their types."""
    file_categories = {
        "image": ["jpg", "jpeg", "png", "gif"],
        "video": ["mp4", "mkv", "avi"],
        "document": ["pdf", "doc", "docx"],
    }

    # Create directories for each category
    for category in file_categories:
        os.makedirs(os.path.join(directory, category), exist_ok=True)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith("."):
            continue

        # Determine the category of the file based on its extension
        file_extension = os.path.splitext(filename)[1].lower()[1:]
        category = None
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                break

        # Move the file to its category directory
        if category:
            shutil.move(file_path, os.path.join(directory, category, filename))
        else:
            print(f"Unrecognized file extension: {filename}")

# Example usage
organize_files("E:\decoumentof pyo")