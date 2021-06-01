def invert(path):
    from PIL import Image

    pic = Image.open('img.jpg')
    pic_width, pic_height = pic.size

    for x in range(pic_width):
        for y in range(pic_height):
            cur_color = pic.getpixel( (x, y) )
            new_color = tuple( [255 - value for value in cur_color] )
            pic.putpixel( (x, y), new_color )

    pic.save('reversed.jpg')

if __name__ == '__main__':
    PATH = 'img.jpg'
    invert(PATH)
