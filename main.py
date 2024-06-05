import sys
import PIL
import os
from PIL import Image
import PIL.Image

image_path = sys.argv[1]
path, extension = os.path.splitext(image_path)

s = path.rsplit("\\")

saving_path = ""
saving_path = saving_path.join([word + "\\" for word in s if word != s[-1]])

# print(saving_path)
# print(path)
# print(extension)

with Image.open(image_path) as image:
  print("The original size of Image is: ", round(len(image.fp.read())/1024,2), "KB")
  image = image.resize((image.width, image.height), PIL.Image.NEAREST)
  image.save(f"{saving_path}compressed_image{extension}")

  with Image.open(f'{saving_path}compressed_image{extension}') as compresed_image:
    print("The size of compressed image is: ", round(len(compresed_image.fp.read())/1024,2), "KB")
