#!/usr/bin/env python3
#
# copy.py
#
# Copy CCSAE files from image_src dir to a fixed format in image_dest dir.
#

import os.path as op
import shutil as su

image_src = '../ccsae-explainer-graphics/'  # image source directory
image_dest = '../images/'                   # image destination directory
image_base = 'fseicdace'                    # base filename of destination images
image_ext = '.png'                          # destination image filename extension

# A list of 16 files in order.
# - The 1st corresponds to f"{image_base}-a{ext}" 
# - The 2nd corresponds to f"{image_base}-b{ext}"
# ...
# - The 16th corresponds to f"{image_base}-p{ext}" 
files = [ l for l in """
1CO2.png
2warm-air.png
3acidification.png
4warmer-water.png
5water-vapor.png
6glaciers.png
7salinity.png
8clouds.png
9rising-sea.png
10density.png
11oxygen.png
12algal-bloom.png
13weather.png
14atlantic.png
15marine-life.png
16human-life.png
""".split('\n') if l ]
# print(files)

# Copy the files accordingly
src_dir = op.realpath(op.join(op.dirname(op.realpath(__file__)), image_src))
dest_dir = op.realpath(op.join(op.dirname(op.realpath(__file__)), image_dest))
# print(image_src, image_dest)

for i, name in enumerate(files):
    from_path = op.join(src_dir, name)
    to_path = op.join(dest_dir, f"{image_base}-{chr(ord('a') + i)}{image_ext}")
    print(f"  {from_path}\n\u2192 {to_path}")
    su.copy(from_path, to_path)
