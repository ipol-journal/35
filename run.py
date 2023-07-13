#!/usr/bin/env python3

import subprocess
import argparse
import cv2

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
files = ["out_roberts.png", "out_prewitt.png", "out_sobel.png", "out_mh.png", "out_mhl.png", "out_haralick.png"]
if args.inv == 1:
    for filename in files:
        image = cv2.imread(filename)
        image = ~image
        cv2.imwrite(filename, image)