# Task Automation Script - Move all .jpg files from one folder to another
# CodeAlpha Internship - Task 3

import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print("❌ Source folder does not exist.")
        return
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"📁 Created destination folder: {destination_folder}")
    
    moved_count = 0
    
    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            
            shutil.move(source_path, destination_path)
            moved_count += 1
            print(f"✅ Moved: {filename}")
    
    print(f"\n📦 Total .jpg files moved: {moved_count}")

if __name__ == "__main__":
    print("📂 JPG File Mover Automation Script")
    src = input("Enter source folder path: ").strip()
    dest = input("Enter destination folder path: ").strip()
    move_jpg_files(src, dest)
