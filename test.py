import os
import cv2
import pytesseract
import shutil

# Set path to Tesseract OCR (modify if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Paths
input_folder = "folder-2"  # Folder containing images
face_folder = "faces (Output)"
other_folder = "others (Output)"

# Create directories if they don’t exist
os.makedirs(face_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

# Load OpenCV’s Haar cascade face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def detect_face(image_path):
    """Detects faces in an image."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    return len(faces) > 0  # Returns True if a face is detected


def contains_text(image_path):
    """Detects if an image contains readable text."""
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    return len(text.strip()) > 5  # Returns True if non-empty text is found


# Process each image
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        has_face = detect_face(img_path)
        has_text = contains_text(img_path)
        if has_face:
            shutil.move(img_path, os.path.join(face_folder, filename))
            print(f"Moved {filename} to 'faces'")
        elif has_text:
            shutil.move(img_path, os.path.join(other_folder, filename))
            print(f"Moved {filename} to 'others'")
print("Image classification complete!")
