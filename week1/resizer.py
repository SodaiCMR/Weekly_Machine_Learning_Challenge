from PIL import Image
import os

directory = "datasets"
size = (300, 300)

for dir in os.listdir(directory):
    if dir != "Cid_Kagenou":
        folder = os.path.join(directory, dir)
        print(folder)
        for character in os.listdir(folder):
            img_path = os.path.join(folder, character)
            img_desc = img_path.split("\\")[-1]
            original_image = Image.open(img_path)
            resized_path = os.path.join(folder, f"resized_{img_desc}")
            if "resized_" not in img_path:
                resized_image = original_image.resize(size)
                resized_image.save(resized_path)
                print(f"Successfully resized {img_desc}")
                os.remove(img_path)