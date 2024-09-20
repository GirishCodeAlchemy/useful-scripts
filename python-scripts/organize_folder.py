from pathlib import Path


def alchemy_organize(path: str) -> None:
    directory = Path(path)

    # Define directories for different file types
    file_type_dirs = {
        'audios': directory / 'audios',
        'images': directory / 'images',
        'documents': directory / 'documents',
        'videos': directory / 'videos',
        'others': directory / 'others'
    }

    # File extensions grouped by type
    EXTENSIONS = {
        'audios': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
        'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.md', '.html'],
    }

    # Create the directories if they don't exist
    for folder in file_type_dirs.values():
        folder.mkdir(exist_ok=True)

    # Get all the files in the directory
    file_names = [f for f in directory.iterdir() if f.is_file()]

    # Iterate through files and move them to appropriate directories
    for file in file_names:
        extension = file.suffix.lower()
        moved = False

        # Check if the file belongs to any of the defined categories
        for category, ext_list in EXTENSIONS.items():
            if extension in ext_list:
                new_folder = file_type_dirs[category]
                moved = True
                break
        
        # If the file doesn't match any category, move it to 'others'
        if not moved:
            new_folder = file_type_dirs['others']

        # Move the file to the new folder
        new_path = new_folder / file.name
        file.rename(new_path)


if __name__ == '__main__':
    path = input(r'PATH: ')
    alchemy_organize(path)
