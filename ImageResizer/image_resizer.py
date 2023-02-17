# install pillow if you havent
# import pillow
from PIL import Image


def resize_image(size1, size2):
    # open up the image we want to resize using python
    image = Image.open('qrimg.png')

    # print the current size of that image
    print(f"Current size: {image.size}")

    # specify the size we wanna change it to
    resized_image = image.resize((size1, size2))

    # save the new resized image
    print(f"Your {size1} x {size2} image is ready!")
    resized_image.save(f"ImageResizer/qrcode-{size1}x{size2}.png")


size1 = int(input("Enter Width: "))
size2 = int(input("Enter Lenght: "))
resize_image(size1, size2)
