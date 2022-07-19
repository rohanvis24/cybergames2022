# picture size: 62x62

from PIL import Image

orig = Image.open("./ciphertext.png")

width = 5456
height = 7936

img_size = 62

img_counter = 0

for i in range(int(height / img_size)):
    for j in range(int(width / img_size)):
        tmp = orig.crop((j * img_size, i * img_size, j * img_size + img_size, i * img_size + img_size))
        tmp.save(f"./img/{img_counter}.png")
        img_counter += 1
