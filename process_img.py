import cv2
import os
#from pathlib import Path


def view_images():

    dir = 'test_frames/sturgeon_vid_01.m4v' # get frames directory

    for entry in os.scandir(dir):
        if entry.is_file():  # check if it's a file

            img = cv2.imread(dir + '/' + entry.name) # load the image

            cv2.namedWindow('image', cv2.WINDOW_NORMAL) # name the window

            cv2.resizeWindow('image', 900, 700) # resize the window

            cv2.imshow('image', img) # display the image in the window

            cv2.waitKey(0) # close the window

    cv2.destroyAllWindows() # close all windows

def extract_object_frame():
    # TODO - use object recognition algorithm to identify frame segments with sturgeon
    pass

if __name__ == '__main__':
    view_images()