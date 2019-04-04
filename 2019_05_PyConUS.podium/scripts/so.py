
from PIL import Image
im = Image.open("image.png")

# create palette from raw data
# colours: Red, Green, Blue, Black, and White (5 total)
RGBBW = [(255,0,0), (0,255,0), (0,0,255), (0,0,0), (255,255,255)]
data = sum([list(x) for x in RGBBW], [])[:256]
pimg = Image.new("P",(16,16))
pimg.putpalette(data)


im.convert("RGB")
cim_ = im.im.convert("P", 0, pimg.im)
cim = im._new(cim_).convert("RGB")

def colors(im):
    cs = []
    for x in range(im.width):
        for y in range(im.height):
            cs.append(im.getpixel((x,y)))
    return list(set(cs))

print("Original: %s" % colors(im))
print("Palette: %s" % RGBBW)
print("Convert: %s" % colors(cim))

def scopecreep(im,pal):
    creep = []
    cs = colors(im)
    for c in cs:
        if c not in pal:
            creep.append(c)

    return list(set((creep)))

print(scopecreep(cim, RGBBW))
