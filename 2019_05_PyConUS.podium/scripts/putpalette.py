from PIL import Image

# NOTE: 
# Mojave Pillow install
# sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
# example with quantize and dither feature not yet cut, requires install from source, requires above to install

RGBBW = [(255,0,0), (0,255,0), (0,0,255), (0,0,0), (255,255,255)]
data = sum([list(x) for x in RGBBW], [])[:256]

BW = [(0,0,0), (255,255,255)]
bwdata = sum([list(x) for x in BW], [])[:256]

pimg = Image.new("P",(16,16))
pimg.putpalette(data)

def colours(im):
    cs = []
    for x in range(im.width):
        for y in range(im.height):
            cs.append(im.getpixel((x,y)))
    return list(set(cs))

def scopecreep(im,pal):
    creep = []
    cs = colours(im) 
    for c in cs:
        if c not in pal:
            creep.append(c)

    return list(set((creep)))

def analyze(img, data=RGBBW):
    img = img.convert("RGB")
    print("colors: %s" % len(colours(img)))
    for x in scopecreep(img, data):
        print(x)
    print("\n\n")
    

im = Image.open("3x3.png")

im.convert("RGB")


imp2_ = im.im.convert("P", 0, pimg.im)
imp2 = im._new(imp2_).convert("RGB")
imp2.save("3x3_imp2.png")
print("image 2: native convert with palette")
analyze(imp2)


imp3 = im.convert("P", palette=pimg.im)
imp3.save("3x3_imp3.png")
print("image 3: wrapped convert with palette")
analyze(imp3)

imrgb = im.convert("RGB")
imp4 = imrgb.quantize(palette=pimg)
imp4.save("3x3_imp4.png")
print("image 4: native quantize")
analyze(imp4)

imp5 = imrgb.quantize(palette=pimg) #, dither=0)
imp5 = imp5.convert("RGB")
imp5.save("3x3_imp5.png")
print("image 5: quantize dither 0")
analyze(imp5)

imp6 = imrgb.convert("P", palette=Image.ADAPTIVE)
imp6.save("3x3_imp6.png")
print("image 6: adaptive palette")
analyze(imp6)
