import sys
import glob
import PIL
from PIL import Image


def resize_aspect(im, fixed_width='', fixed_height=''):
    if fixed_height != '':
        height_percent = (fixed_height / float(im.size[1]))
        width_size = int((float(im.size[0]) * float(height_percent)))
        im = im.resize((width_size, fixed_height), PIL.Image.NEAREST)
        return im
    elif fixed_width != '':
        width_percent = (fixed_width / float(im.size[0]))
        height_size = int((float(im.size[1]) * float(width_percent)))
        im = im.resize((fixed_width, height_size), PIL.Image.NEAREST)
        return im
    else:
        return im


def smart_crop(im, width, height):
    if height > width:
        im = resize_aspect(im, height)
    else:
        im = resize_aspect(im, width)
    # paste the thumbnail into the full sized image
    left = int(im.size[0]/2-width/2)
    upper = int(im.size[1]/2-height/2)
    #upper = 0
    right = left + width
    lower = upper + height
    im_cropped = im.crop((left, upper, right, lower))
    #bg = Image.new('RGB', (right - left, lower - upper), (255, 255, 255))
    #bg.paste(im, (-left, -upper))
    # bg.save('temp.jpg')
    #bg = Image.open('temp.jpg')
    return im_cropped


smart_crop(img, width, height)

# Create the frames
frames = []
imgs = glob.glob("/Users/Nick/Downloads/ImageGif/*.jpg")
total_duration = (frame_duration * len(imgs)) * 100

for i in imgs:
    new_frame = Image.open(i)
    #im = Image.open(i)
    new_frame = smart_crop(new_frame, 200, 200)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=total_duration, loop=0)
