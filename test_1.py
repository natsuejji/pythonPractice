import numpy as np
import sys
from PIL import Image
import numpy as np

input_file = '04A.png'

im = Image.open(input_file)
data = np.array(im)
rotated_data = np.flip(np.flip(data,axis=0),axis=1)

new_im = Image.fromarray(rotated_data)
new_im.save("image/ans2.png")