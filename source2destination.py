import os
import shutil
import sys

def move_files_to_usb():
    print("📂 File Mover Tool 📂")
    
    # Get source directory
    source_dir = input("Enter the source directory path: ").strip()
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' doesn't exist!")
        return
    
    # Get destination directory (USB)
    dest_dir = input("Enter the USB destination path: ").strip()
    if not os.path.exists(dest_dir):
        create_dir = input(f"Destination '{dest_dir}' doesn't exist. Create it? (y/n): ").lower()
        if create_dir == 'y':
            try:
                os.makedirs(dest_dir)
                print(f"Created directory: {dest_dir}")
            except Exception as e:
                print(f"Error creating directory: {e}")
                return
        else:
            print("Operation cancelled.")
            return
    
    # Get files from source directory
    files = os.listdir(source_dir)
    if not files:
        print(f"No files found in '{source_dir}'")
        return
    
    print(f"\nFound {len(files)} files/folders in source directory.")
    
    # Ask if user wants to move all files or select specific ones
    move_all = input("Move all files? (y/n): ").lower()
    
    files_to_move = []
    if move_all == 'y':
        files_to_move = files
    else:
        print("\nAvailable files/folders:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        
        selections = input("\nEnter file numbers to move (comma-separated) or 'all': ").strip()
        if selections.lower() == 'all':
            files_to_move = files
        else:
            try:
                indices = [int(x.strip()) - 1 for x in selections.split(',')]
                files_to_move = [files[i] for i in indices if 0 <= i < len(files)]
            except:
                print("Invalid selection. Please enter numbers separated by commas.")
                return
    
    # Move the files
    moved_count = 0
    errors = []
    
    print("\nMoving files...")
    for file in files_to_move:
        source_path = os.path.join(source_dir, file)
        dest_path = os.path.join(dest_dir, file)
        
        try:
            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
                shutil.rmtree(source_path)
            else:
                shutil.move(source_path, dest_path)
            moved_count += 1
            print(f"✅ Moved: {file}")
        except Exception as e:
            errors.append(f"❌ Error moving {file}: {str(e)}")
    
    # Summary
    print(f"\nOperation complete! Moved {moved_count} of {len(files_to_move)} files/folders.")
    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(error)

if __name__ == "__main__":
    try:
        move_files_to_usb()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    input("\nPress Enter to exit...")
