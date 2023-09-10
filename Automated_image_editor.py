# Import necessary modules from PIL (Python Imaging Library).
from PIL import Image, ImageEnhance, ImageFilter
import os

# Define the input and output directories.
path = './imgs'      # Input directory containing images to be processed.
pathout = '/editedimgs'  # Output directory to save the edited images.

# Loop through the files in the input directory.
for filename in os.listdir(path):
    # Open the current image file for processing.
    img = Image.open(f"{path}/{filename}")

    # Apply a sharpening filter to the image and convert it to grayscale (L mode).
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    # Define a factor for enhancing contrast.
    factor = 1.5

    # Create an ImageEnhance object for contrast enhancement.
    enhancer = ImageEnhance.Contrast(edit)

    # Enhance the contrast of the grayscale image using the defined factor.
    edit = enhancer.enhance(factor)

    # Extract the clean name of the file without the extension.
    clean_name = os.path.splitext(filename)[0]

    # Save the edited image with a new filename in the output directory.
    edit.save(f'{pathout}/{clean_name}_edited.jpg')

# End of the loop.
