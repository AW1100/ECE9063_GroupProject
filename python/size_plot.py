import os
from PIL import Image
import matplotlib.pyplot as plt

# Folder path containing images
folder_path = '../Data/images/bgRemoved'

# Lists to store image widths and heights
image_widths = []
image_heights = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):  # Adjust file extensions as needed
        image_path = os.path.join(folder_path, filename)
        try:
            # Open the image and get its dimensions
            with Image.open(image_path) as img:
                width, height = img.size
                image_widths.append(width)
                image_heights.append(height)
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

# Create a scatter plot of image dimensions
plt.scatter(image_widths, image_heights, alpha=0.5)
plt.xlabel('Width')
plt.ylabel('Height')
plt.title('Image Width vs. Height')
plt.grid(True)
plt.show()