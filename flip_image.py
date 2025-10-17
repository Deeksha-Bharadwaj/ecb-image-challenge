import struct
from PIL import Image

img = Image.open('640x480.bmp')
img.transpose(Image.FLIP_TOP_BOTTOM).save('ANSWER.bmp')

print("\n📖 Open ANSWER.bmp to read the flag!")
print("\nCommand: open ANSWER.bmp")