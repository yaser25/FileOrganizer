import os
import shutil
FILE_TYPES = {
    "Images": ("jpg", "jpeg", "png"),
    "Videos": ("mp4", "avi"),
    "Music": ("mp3",),
    "Documents": ("pdf", "txt")
}

moved_files = {
    "Images": 0,
    "Documents": 0,
    "Videos": 0,
    "Music": 0,
    "Others": 0
}

OTHER_FOLDER = "Others"


def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    print(f"\nFolder found:\n{folder_path}")
    files = os.listdir(folder_path)
    print(files)
    print("\nFiles:")  
    for file in files:
        filename = file.lower()
        source = os.path.join(folder_path , file)
        """"  Ignore folders and process only regular files """
        if not os.path.isfile(source):
            continue
        destination_folder = None
        destination_category = OTHER_FOLDER
        for category, extensions in FILE_TYPES.items():
            if filename.endswith(extensions):
                destination_category = category
                break
        #if not destination_category:
            #destination_category = OTHER_FOLDER  
        print("DEBUG:", destination_category)        
        destination_folder = os.path.join(folder_path , destination_category)
        os.makedirs(destination_folder , exist_ok=True)

        destination_file = os.path.join(destination_folder , file)
        counter = 1
        if os.path.exists(destination_file):
           
           base_name, ext = os.path.splitext(file)
           while True:
                new_name = f"{base_name}_{counter}{ext}"
                new_destination = os.path.join(destination_folder, new_name)
                if not os.path.exists(new_destination):
                    destination_file = new_destination
                    break
                counter +=1
                
        shutil.move(source , destination_file)
        print(f"{os.path.basename(destination_file)} moved to {destination_category}")
        moved_files[destination_category] += 1

        
                
        


