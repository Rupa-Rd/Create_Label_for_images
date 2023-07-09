import os
from os import listdir

file_with_labels = {}
folder_dir = 'E:\Git Repositories\Create_Label_for_images\pet_images'

for images in os.listdir(folder_dir) :
    label = ''
    if (images.endswith('.jpg')) :
        image = images.removesuffix('.jpg')
        image = image.lower()
        for char in image:
            if char == '_':
                label += ' '
            elif char not in '0123456789':
                label += char
        file_with_labels[images] = label

with open('result.txt','w') as file :

    file.write("{:36s} {}\n".format("Image","Label"))
    file.write("-------------------------------------------------------------------\n")
    for key, values in file_with_labels.items() :
        file.write(f"{key:36s}:{values}\n")
    file.close()
print("Successfully! reported the results into result.txt")