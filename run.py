#!/usr/bin/env python3

import subprocess
import argparse
from PIL import Image, ImageChops

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("th_fded", type=float)
ap.add_argument("rho", type=float)
ap.add_argument("sigma", type=float)
ap.add_argument("n", type=int)
ap.add_argument("tzc", type=float)
ap.add_argument("sigma2", type=float)
ap.add_argument("n2", type=int)
ap.add_argument("tzc2", type=float)
ap.add_argument("inv", type=int)

args = ap.parse_args()

subprocess.run(["edges", "-r", str(args.th_fded), "-p", str(args.th_fded),"-s", str(args.th_fded),
                     "-m", str(args.sigma), str(args.n), str(args.tzc), "-l", str(args.sigma2), str(args.n2), str(args.tzc2),
                    "-h", str(args.rho), "input_0.png"])

# Invert output images
files = ["out_roberts", "out_prewitt", "out_sobel", "out_mh", "out_mhl", "out_haralick"]
if args.inv == 1:
    for filename in files:
        im = Image.open(filename + '.png')
        inv_im = ImageChops.invert(im)
        im.save(filename + '.png')
