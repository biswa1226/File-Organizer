import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            ext = file_name.split('.')[-1].lower()
            if ext:
                target_folder = os.path.join(folder_path, ext.upper() + "_Files")
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file_name))
                print(f"Moved: {file_name} -> {target_folder}")

if __name__ == "__main__":
    path = input("Enter the path of the folder to organize: ")
    organize_files(path)
    print("\n✅ All files organized successfully!")
