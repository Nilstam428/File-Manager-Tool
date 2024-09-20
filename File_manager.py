import os
import shutil
import subprocess

def list_directory():
    """List contents of the current directory."""
    current_dir = os.getcwd()
    print(f"Contents of {current_dir}:")
    for item in os.listdir(current_dir):
        print(item)

def change_directory(path):
    """Change directory to the given path."""
    try:
        os.chdir(path)
        print(f"Changed directory to {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found!")
    except PermissionError:
        print("Permission denied!")

def create_file(file_name):
    """Create a new file."""
    try:
        subprocess.run(['touch', file_name])
        print(f"File '{file_name}' created.")
    except PermissionError:
        print("Permission denied!")

def create_directory(dir_name):
    """Create a new directory."""
    try:
        subprocess.run(['mkdir', dir_name])
        print(f"Directory '{dir_name}' created.")
    except PermissionError:
        print("Permission denied!")

def delete_file(file_name):
    """Delete a file."""
    try:
        if os.path.isfile(file_name):
            subprocess.run(['rm', file_name])
            print(f"File '{file_name}' deleted.")
        else:
            print("File not found!")
    except PermissionError:
        print("Permission denied!")

def delete_directory(dir_name):
    """Delete a directory."""
    try:
        if os.path.isdir(dir_name):
            subprocess.run(['rm', '-r', dir_name])
            print(f"Directory '{dir_name}' deleted.")
        else:
            print("Directory not found!")
    except PermissionError:
        print("Permission denied!")

def rename_file(old_name, new_name):
    """Rename a file or directory."""
    try:
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"Renamed '{old_name}' to '{new_name}'")
        else:
            print(f"'{old_name}' not found!")
    except PermissionError:
        print("Permission denied!")
    except FileExistsError:
        print(f"File '{new_name}' already exists!")

def move_file(src, dest):
    """Move a file or directory."""
    try:
        if os.path.exists(src):
            shutil.move(src, dest)
            print(f"Moved '{src}' to '{dest}'")
        else:
            print(f"'{src}' not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(f"Error: {e}")

def copy_file(src, dest):
    """Copy a file to a new location."""
    try:
        if os.path.isfile(src):
            shutil.copy(src, dest)
            print(f"Copied '{src}' to '{dest}'")
        else:
            print(f"'{src}' not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(f"Error: {e}")

def paste_file(copied_file, dest):
    """Paste the copied file into a new location."""
    try:
        if os.path.isfile(copied_file):
            shutil.copy(copied_file, dest)
            print(f"Pasted '{copied_file}' to '{dest}'")
        else:
            print(f"'{copied_file}' not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(f"Error: {e}")

def file_details(file_name):
    """Get file details like size and last modification time."""
    try:
        if os.path.isfile(file_name):
            file_stats = os.stat(file_name)
            print(f"File: {file_name}")
            print(f"Size: {file_stats.st_size} bytes")
            print(f"Last Modified: {os.path.getmtime(file_name)}")
        else:
            print("File not found!")
    except PermissionError:
        print("Permission denied!")

def display_file_content(file_name):
    """Display the content of a file."""
    try:
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
                print(content)
        else:
            print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(f"Error: {e}")

def main_menu():
    """Main menu of the file manager."""
    clipboard = None
    while True:
        print("\nEnhanced File Manager:")
        print("1. List Directory")
        print("2. Change Directory")
        print("3. Create File")
        print("4. Create Directory")
        print("5. Delete File")
        print("6. Delete Directory")
        print("7. Rename File/Directory")
        print("8. Move File/Directory")
        print("9. Copy File")
        print("10. Paste File")
        print("11. File Details")
        print("12. Display File Content")
        print("13. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            list_directory()
        elif choice == '2':
            path = input("Enter directory path: ")
            change_directory(path)
        elif choice == '3':
            file_name = input("Enter file name: ")
            create_file(file_name)
        elif choice == '4':
            dir_name = input("Enter directory name: ")
            create_directory(dir_name)
        elif choice == '5':
            file_name = input("Enter file name to delete: ")
            delete_file(file_name)
        elif choice == '6':
            dir_name = input("Enter directory name to delete: ")
            delete_directory(dir_name)
        elif choice == '7':
            old_name = input("Enter current name: ")
            new_name = input("Enter new name: ")
            rename_file(old_name, new_name)
        elif choice == '8':
            src = input("Enter source file/directory: ")
            dest = input("Enter destination directory: ")
            move_file(src, dest)
        elif choice == '9':
            src = input("Enter file to copy: ")
            dest = input("Enter destination path: ")
            copy_file(src, dest)
            clipboard = src  # Store copied file in clipboard for paste
        elif choice == '10':
            if clipboard:
                dest = input("Enter destination path: ")
                paste_file(clipboard, dest)
            else:
                print("Clipboard is empty. Copy a file first.")
        elif choice == '11':
            file_name = input("Enter file name for details: ")
            file_details(file_name)
        elif choice == '12':
            file_name = input("Enter file name to display content: ")
            display_file_content(file_name)
        elif choice == '13':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
