import sys
import PIL
import glob
from PIL import Image
import resize_img as rimg

frame_duration = .5
width = 200
height = 400

# Create the frames
frames = []
imgs = glob.glob("Image_Input/*.jpg")
total_duration = (frame_duration * len(imgs)) * 100

for i in imgs:
    new_frame = Image.open(i)
    new_frame = rimg.smart_crop(new_frame, width, height)
    frames.append(new_frame)

# Save into a GIF file that loops forever
export_file_name = F"gif_slideshow_{str(width)}_{str(height)}.gif"
frames[0].save(export_file_name, format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=total_duration, loop=0)
