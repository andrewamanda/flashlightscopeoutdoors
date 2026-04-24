# brew install tesseract
# pip install pytesseract opencv-python pillow


import cv2
import pytesseract
from PIL import Image
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'Task to interact with the model'

    def handle(self, *args, **kwargs):

        # Load image using OpenCV
        image_path = '/Users/wangmingye/Downloads/20220715152544_74311.jpg'
        image = cv2.imread(image_path)

        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use Tesseract to detect text
        # Make sure Tesseract is installed and pytesseract is properly configured
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Update with your Tesseract path

        # Get bounding boxes of detected text
        h, w, _ = image.shape
        boxes = pytesseract.image_to_boxes(Image.fromarray(gray))

        # Blur the text instead of drawing a white box
        for b in boxes.splitlines():
            b = b.split(' ')
            x, y, w_b, h_b = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            y = h - y
            h_b = h - h_b

            # Extract the region of interest (ROI) where the text is located
            roi = image[h_b:y, x:w_b]

            # Apply Gaussian blur to the ROI
            blurred_roi = cv2.GaussianBlur(roi, (15, 15), 0)

            # Replace the original ROI with the blurred version
            image[h_b:y, x:w_b] = blurred_roi

        cv2.imwrite('/Users/wangmingye/Downloads/blurred_image.jpg', image)
