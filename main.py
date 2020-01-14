import cv2
import numpy as np
import glob
import os
import sys
import argparse


def main():
    # Argument parser
    parser = argparse.ArgumentParser(
        description="Calculate mean for dataset for each channel.")
    parser.add_argument('-i', '--image_directory',
                        help="Directory of the image dataset", required=True)
    parser.add_argument('-if', '--image_format',
                        help="Format of the image dataset. Ex. png", required=False, default='png')

    args = parser.parse_args()
    image_folderdir = args.image_directory
    image_format = args.image_format

    blue_mean_container = []
    green_mean_container = []
    red_mean_container = []

    # Check for each image dataset
    for filename in os.listdir(image_folderdir):
        if filename.endswith("." + image_format):
            # print(os.path.splitext(filename)[0])
            image = cv2.imread(os.path.join(image_folderdir, filename))
            if image is None:
                sys.exit("Image " + filename + " malfunction")
            image = np.transpose(image, (2, 0, 1))
            blue_mean_one_image = np.mean(image[0])
            green_mean_one_image = np.mean(image[1])
            red_mean_one_image = np.mean(image[2])
            blue_mean_container.append(blue_mean_one_image)
            green_mean_container.append(green_mean_one_image)
            red_mean_container.append(red_mean_one_image)

    blue_mean = np.mean(blue_mean_container)
    green_mean = np.mean(green_mean_container)
    red_mean = np.mean(red_mean_container)

    # Print mean average
    print("Blue: " + str(blue_mean))
    print("Green: " + str(green_mean))
    print("Red: " + str(red_mean))


if __name__ == "__main__":
    main()
