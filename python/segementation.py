import numpy as np
import os
from PIL import Image
import xml.etree.ElementTree as ET

input_annotation_folder = '../Data/annotations'
input_image_folder = '../Data/images/raw'

output_segemented_image_folder = '../Data/images/cropped'
if not os.path.exists(output_segemented_image_folder):
    os.makedirs(output_segemented_image_folder)

for filename in os.listdir(input_image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):  # Adjust file extensions as needed
        input_image_path = os.path.join(input_image_folder, filename)
        output_image_path = os.path.join(output_segemented_image_folder, filename)
        input_annotation_path = os.path.join(input_annotation_folder, filename[0:-4]+'.xml')
        try:
            tree = ET.parse(input_annotation_path)
            root = tree.getroot()

            with Image.open(input_image_path) as img:
                object_index = 0
                for obj in root.findall('object'):
                    name = obj.find('name').text
                    if(name == 'With Helmet'):
                        name = 'T'
                    else:
                        name = 'F'

                    x1 = int(obj.find('bndbox/xmin').text)
                    y1 = int(obj.find('bndbox/ymin').text)
                    x2 = int(obj.find('bndbox/xmax').text)
                    y2 = int(obj.find('bndbox/ymax').text)
                    # print(filename[:-4])
                    # print(name)
                    # print(x1, y1, x2, y2)
                    if x2 < x1:
                        temp = x1
                        x1 = x2
                        x2 = temp
                    elif y2 < y1:
                        temp = y1
                        y1 = y2
                        y2 = temp
                    cropped_img = img.crop((x1, y1, x2, y2))
                    fname = filename[12:-4] + '_' + str(object_index) + '_' + name + '.png'
                    object_index = object_index + 1
                    cropped_img.save(f"{output_segemented_image_folder}/{fname}")

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")