from PIL import Image

def hide_data(image_file, data_to_hide, output_file):
    image = Image.open(image_file)
    data = iter(data_to_hide.encode('utf-8'))

    pixels = list(image.getdata())
    if len(data_to_hide) * 8 > len(pixels):
        raise ValueError("Not enough pixels in the image to hide the data.")

    for i in range(len(data_to_hide)):
        pixel = pixels[i]
        pixels[i] = (pixel[0], pixel[1], pixel[2], data.__next__())

    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    new_image.save(output_file)

def reveal_data(image_file):
    image = Image.open(image_file)
    pixels = list(image.getdata())

    data = ""
    for pixel in pixels:
        data += chr(pixel[3])
        if pixel[3] == 0:
            break

    return data
