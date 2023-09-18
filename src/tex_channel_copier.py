from pathlib import Path
from tex import Tex
import numpy as np
from PIL import Image

def tex_channel_copier(directory: str, array: np.array):
    '''copies the source channel of a given TEX file into the target channel, '''

    folder = Path(directory)
    # may need to change this check since naming doesnt necisarily have "--" in it
    grabber = list(folder.glob('**/*s.tex'))

    for file in grabber:
        tex = Tex.from_file(file)
        array = np.array([[0,0,0,0], [0,1,0,0], [0,0,1,0], [1,0,0,1]])
        tex.bdy.from_bytes(array)
        tex._write()

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

def byte_to_int(byte):
    return int.from_bytes(byte, byteorder='big')

def int_to_byte(number):
    max_byte, min_byte = 255, 0
    return int.to_bytes(max(min(int(number), max_byte), min_byte))

def copy_channel(tex: Tex, modification_matrix : np.array):
    data = get_data(tex)

    vectorized_byte_to_int = np.vectorize(byte_to_int)
    int_array = vectorized_byte_to_int(data)

    modified_array = np.matmul(int_array, modification_matrix)

    vectorized_int_to_byte = np.vectorize(int_to_byte)
    byte_array = b''.join(vectorized_int_to_byte(modified_array).reshape(-1))

    return byte_array

    

if __name__ == "__main__":
    array = np.array([[1,0,0,0], [0,2,0,0], [0,0,1,0], [0,0,0,1]])
    tex = get_tex("src/data/target.tex")
    copy_channel(tex, array)
    #data = get_data(tex)
    #image = get_image(data, tex.hdr.height, tex.hdr.width)
    #image.show()




# +0 = Blue
# +1 = Green
# +2 = Red
# +3 = Alpha