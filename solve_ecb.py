import struct
from PIL import Image

with open('aes.bmp.enc', 'rb') as f:
    data = f.read()

total_pixels = len(data) // 3
print(f"Total pixels: {total_pixels}")
print(f"Square root: {total_pixels ** 0.5:.2f}")
print()

# Since 307218 doesn't factor nicely, try common image dimensions
# and use only the data we need

dimensions = [
    (554, 554),  # Square-ish
    (555, 553),
    (553, 555),
    (600, 512),
    (512, 600),
    (640, 480),
    (480, 640),
    (768, 400),
    (400, 768),
    (606, 507),
    (507, 606),
]

def create_bmp_header(width, height, data_size):
    header = bytearray()
    header += b'BM'
    header += struct.pack('<I', 54 + data_size)
    header += struct.pack('<H', 0)
    header += struct.pack('<H', 0)
    header += struct.pack('<I', 54)
    header += struct.pack('<I', 40)
    header += struct.pack('<i', width)
    header += struct.pack('<i', -height)
    header += struct.pack('<H', 1)
    header += struct.pack('<H', 24)
    header += struct.pack('<I', 0)
    header += struct.pack('<I', data_size)
    header += struct.pack('<i', 0)
    header += struct.pack('<i', 0)
    header += struct.pack('<I', 0)
    header += struct.pack('<I', 0)
    return bytes(header)

print("Creating BMPs with approximate dimensions...\n")

for width, height in dimensions:
    needed_pixels = width * height
    needed_bytes = needed_pixels * 3
    
    if needed_bytes <= len(data):
        # Use only what we need
        pixel_data = data[:needed_bytes]
        
        header = create_bmp_header(width, height, len(pixel_data))
        complete_bmp = header + pixel_data
        
        filename = f'approx_{width}x{height}.bmp'
        with open(filename, 'wb') as f:
            f.write(complete_bmp)
        
        pixels_used = needed_pixels
        pixels_wasted = total_pixels - pixels_used
        
        print(f"{filename}")
        print(f"  Used: {pixels_used} pixels ({pixels_wasted} leftover)")
    else:
        print(f"{width}x{height} - too big")

print("")
print(f"To Open images:")
print("open approx_*.bmp")

