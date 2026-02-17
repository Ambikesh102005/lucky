import sys
from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("VEGETA EGO LIVE WALLPAPER 4K.jpg") as img:
        img = img.rotate(360)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("out.jpeg")


main()
