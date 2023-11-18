import os
from PIL import Image

input_folder = '../Data/images/cropped'


desired_width = 50  # Adjust to your preferred width
desired_height = 50  # Adjust to your preferred height

output_folder = '../Data/images/cropped_' + desired_width

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):  # Adjust file extensions as needed
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, filename)
        try:
            with Image.open(input_image_path) as img:
                # # Calculate new dimensions while maintaining the aspect ratio
                # img.thumbnail((desired_width, desired_height))
                # # Create a blank background image with the desired dimensions and black color
                # new_img = Image.new("RGB", (desired_width, desired_height), (0, 0, 0))
                # # Calculate the position to paste the resized image in the center
                # position = ((desired_width - img.width) // 2, (desired_height - img.height) // 2)
                # # Paste the resized image onto the center of the blank background
                # new_img.paste(img, position)
                # # Save the modified image to the output folder
                new_img = img.resize((desired_width, desired_height))
                new_img.save(output_image_path)
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

