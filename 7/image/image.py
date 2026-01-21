from PIL import Image, ImageFilter


def main():
    with Image.open("image.jpg") as img:
        print(img.size)
        print(img.format)

        img = img.rotate(180)

        imgBlur = img.filter(ImageFilter.BLUR)
        imgEdges = img.filter(ImageFilter.FIND_EDGES)

        img.save("out.jpg")
        imgBlur.save("outBlur.jpg")
        imgEdges.save("outEdges.jpg")



main()