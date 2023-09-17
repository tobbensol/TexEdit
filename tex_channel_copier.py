from pathlib import Path
from src.tex import Tex
import numpy as np
import scipy.misc as smp
from PIL import Image

def tex_channel_copier(directory: str, target : str, source : str):
    '''copies the source channel of a given TEX file into the target channel, '''

    if target not in channels.keys() or source not in channels.keys():
        raise TypeError(f'{target} or {source} is not a valid channel, please use "r", "g", "b" or "a"')

    folder = Path(directory)
    # may need to change this check since naming doesnt necisarily have "--" in it
    grabber = list(folder.glob('**/*s.tex'))

    for file in grabber:
        with open(file, "rb") as f:
            new_bytes = bytearray(f.read())

        tex = Tex.from_file(file)
        num_pixels = tex.hdr.height * tex.hdr.width
        pixel_size = 4    # 4 bytes per pixel (32 bits)
        
        offset = 80
        channels = {"b":0, "g":1, "r":2, "a":3}

        # Copy the alpha channel into the blue channel for each pixel
        try:
            for _ in range(tex.hdr.mip_levels):
                for i in range(offset, offset:= offset + num_pixels * pixel_size, pixel_size):
                    new_bytes[i + channels[target]] = new_bytes[i + channels[source]]
                num_pixels = num_pixels//4 

            with open(file, "wb") as f:
                f.write(new_bytes)
        except:
            print(file)

def get_tex(file: str):
    return Tex.from_file(file)

def get_data(tex: Tex):
    contents = tex.bdy.data
    pixel_size = 4

    return np.array(contents).reshape((len(contents)//pixel_size, pixel_size))

def get_image(data: np.array, height: int, width: int):
    image = data[:height * width, :].reshape([height, width, 4])
    image[:, :, [0, 2]] = image[:, :, [2, 0]]

    return Image.fromarray(image, mode="RGBA")

def copy_channel(file: str, target : str, source : str):
    tex = Tex.from_file(file)
    pixel_size = 4    # 4 bytes per pixel (32 bits)
    
    channels = {"b":0, "g":1, "r":2, "a":3}

    body = tex.bdy.data
    print(tex._root)
    '''
        np.array(contents).reshape((len(contents)//pixel_size, pixel_size))

    # Copy the alpha channel into the blue channel for each pixel
    try:
        for _ in range(tex.hdr.mip_levels):
            for i in range(offset, offset:= offset + num_pixels * pixel_size, pixel_size):
                new_bytes[i + channels[target]] = new_bytes[i + channels[source]]
            num_pixels = num_pixels//4 

        with open(file, "wb") as f:
            f.write(new_bytes)
    except:
        print(file)
    '''

if __name__ == "__main__":
    copy_channel("target.tex", "b", "r")
    #tex = get_tex("target.tex")
    #data = get_data(tex)
    #image = get_image(data, tex.hdr.height, tex.hdr.width)
    #image.show()




# +0 = Blue
# +1 = Green
# +2 = Red
# +3 = Alpha