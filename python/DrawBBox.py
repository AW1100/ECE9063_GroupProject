import cv2
import xml.etree.ElementTree as ET

image_path = 'D:/ECE9063/Project/Data/images/raw/'
annotation_path = 'D:/ECE9063/Project/Data/annotations/'
file_name = 'BikesHelmets2'
image = cv2.imread(image_path+file_name+'.png')

tree = ET.parse(annotation_path+file_name+'.xml')
root = tree.getroot()
for obj in root.findall('object'):
    x1 = int(obj.find('bndbox/xmin').text)
    y1 = int(obj.find('bndbox/ymin').text)
    x2 = int(obj.find('bndbox/xmax').text)
    y2 = int(obj.find('bndbox/ymax').text)
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 1)

cv2.imwrite(file_name+'BBox'+'.png', image)
# Display the image with the bounding box
cv2.imshow('Bounding Box Example', image)
cv2.waitKey(0)
cv2.destroyAllWindows()