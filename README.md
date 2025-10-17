# ECB Encrypted Image Challenge

**Lab 06:** Breaking AES-ECB encryption on bitmap images

**Author:** Deeksha Bharadwaj  
**Course:** [Your Course Name]  
**Date:** [Date]

## Overview

This project demonstrates the vulnerability of AES-ECB mode encryption. By exploiting ECB's pattern-preservation weakness, we extracted a hidden flag from an encrypted bitmap image without the decryption key.

## Files

- `solve.py` - Reconstructs BMP files from encrypted data
- `flip.py` - Corrects image orientation

## Usage
```bash
pip install pillow
python3 solve_ecb.py
python3 flip_image.py
open ANSWER.bmp
```

## Result

**Flag:** `TROLL`

## Lesson

ECB mode is insecure for images. Always use CBC, CTR, or GCM modes.