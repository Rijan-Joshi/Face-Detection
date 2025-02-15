import os
import shutil

# Set the source directory (where your subfolders are located)
source_dir = "lfw-deepfunneled"  # Replace with your actual source directory

# Set the destination directory where all images will be moved
destination_dir = "images"  # Replace with your actual destination folder
os.makedirs(destination_dir, exist_ok=True)

# Supported image extensions (you can add more if needed)
image_extensions = (".png", ".jpg", ".jpeg", ".bmp")

# Walk through all subdirectories and files in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.lower().endswith(image_extensions):
            src_file = os.path.join(root, file)
            dst_file = os.path.join(destination_dir, file)
            # Handle duplicate file names by renaming
            if os.path.exists(dst_file):
                base, ext = os.path.splitext(file)
                counter = 1
                new_file = f"{base}_{counter}{ext}"
                dst_file = os.path.join(destination_dir, new_file)
                while os.path.exists(dst_file):
                    counter += 1
                    new_file = f"{base}_{counter}{ext}"
                    dst_file = os.path.join(destination_dir, new_file)
            shutil.move(src_file, dst_file)
            print(f"Moved: {src_file} -> {dst_file}")

print("All images have been moved to the destination folder.")
