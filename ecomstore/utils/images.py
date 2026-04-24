from PIL import Image

def get_content_type(file_path):
    try:
        with Image.open(file_path) as img:
            if img.format == 'PNG':
                return 'image/png'
            elif img.format == 'JPEG':
                return 'image/jpeg'
            else:
                return None  # Handle other formats if needed
    except Exception as e:
        print(f"Error: {e}")
        return None

from PIL import Image
import os

def convert_to_jpeg(file_path):
    try:
        # Open the image file
        with Image.open(file_path) as img:
            # Check the format of the image
            if img.format != 'JPEG':
                # Convert to JPEG
                rgb_img = img.convert('RGB')  # JPEG doesn't support transparency, so convert to RGB
                # Create new file name with .jpg extension
                new_file_path = os.path.splitext(file_path)[0] + '.jpg'
                rgb_img.save(new_file_path, 'JPEG')
                print(f"Converted to JPEG and saved as: {new_file_path}")
                return new_file_path
            else:
                print("File is already in JPEG format.")
                return file_path
    except Exception as e:
        print(f"Error: {e}")
        return None
