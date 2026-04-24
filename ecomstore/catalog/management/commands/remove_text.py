# brew install tesseract
# pip install pytesseract opencv-python pillow
# run as:  python manage.py remove_text /path/to/your/image.jpg --threshold 15
import cv2
import pytesseract
from PIL import Image
import numpy as np
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Remove small text from the provided image file and replace it with the background.'

    def add_arguments(self, parser):
        parser.add_argument('image_path', type=str, help='Path to the image file')
        parser.add_argument('--threshold', type=int, default=20, help='Threshold height for small text (in pixels) to be removed')

    def handle(self, *args, **kwargs):
        image_path = kwargs['image_path']
        threshold = kwargs['threshold']

        image = cv2.imread(image_path)
        if image is None:
            self.stdout.write(self.style.ERROR(f"Image file not found: {image_path}"))
            return

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Increase contrast for better text detection
        alpha = 1.5  # Contrast control
        contrast_image = cv2.convertScaleAbs(gray, alpha=alpha, beta=0)

        # Apply adaptive thresholding
        threshold_image = cv2.adaptiveThreshold(contrast_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # Use Tesseract with custom config for small text detection
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
        custom_config = r'--oem 3 --psm 6'  # Custom config to adjust Tesseract sensitivity

        h, w, _ = image.shape
        boxes = pytesseract.image_to_boxes(Image.fromarray(threshold_image), config=custom_config)

        mask = np.zeros_like(gray)
        for b in boxes.splitlines():
            b = b.split(' ')
            x, y, w_b, h_b = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            y = h - y
            h_b = h - h_b
            text_height = y - h_b

            if text_height <= threshold:
                cv2.rectangle(mask, (x, h_b), (w_b, y), 255, -1)

        result = cv2.inpaint(image, mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)
        output_path = image_path.replace(".jpg", "_small_text_removed.jpg")
        cv2.imwrite(output_path, result)
        self.stdout.write(self.style.SUCCESS(f"Processed image saved as: {output_path}"))
