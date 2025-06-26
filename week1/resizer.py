from PIL import Image
import os

directory = "datasets"
size = (300, 300)

for subdir in os.listdir(directory):
    if subdir != "Cid_Kagenou":
        folder = os.path.join(directory, subdir)
        print(folder)
        for character in os.listdir(folder):
            img_path = os.path.join(folder, character)
            img_desc = img_path.split("\\")[-1]
            original_image = Image.open(img_path)
            resized_path = os.path.join(folder, f"resized_{img_desc}")
            if "resized_" not in img_path:
                converted_image = original_image.convert("RGB")
                resized_image = converted_image.resize(size)
                resized_image.save(resized_path)
                print(f"Successfully resized {img_desc}")
                os.remove(img_path)