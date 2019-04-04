from PIL import Image
im = Image.open("3x3.png")

for x in range(im.width):
    for y in range(im.height):
        print(x, y, im.getpixel((x, y)))

print(im.getpixel((0,2)))


