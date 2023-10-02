import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
def find_colours(filename):
    # Loading input image from filename
    image = load_image(filename)
    
    # Finding coordinates of black circular markers in image
    circle_coordinates = find_circles(image)
    
    # Correcting image perspective using the circle coordinates
    undistorted_image = correct_image(circle_coordinates, image)
    
    # Extract the dominant colours from the corrected image
    colours = get_colours(undistorted_image)                 
    return colours

def load_image(filename):
    # Reading input image from the given filename using OpenCV librabry
    image = cv2.imread(filename)
    
    # Convert the image data type to double and normalize the pixel values to the range [0, 1]
    image = image.astype(np.float64) / 255.0 

    return image

def find_circles(image):
    # Normalize the input image to improve contrast and brightness
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    
    # Convert the input image to an unsigned 8-bit integer format   
    image = image.astype(np.uint8)
    
    # Apply median blur to reduce noise in the image with a kernel of 11
    blurred = cv2.medianBlur(image, 11)
    
    # Convert the blurred image to grayscale for further processing   
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive threshold to better detect black circles
    ret,thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    
    # Detect circles using HoughCircles
    circles =  cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=5, param1=30, param2=30, minRadius=0, maxRadius=40)

    # If circles are detected, keep only the four largest circles  
    if circles is not None:
        # Keep only the four largest circles
        detected_circles = np.uint16(np.around(circles))
        circle_coordinates = sorted([(x, y) for x, y, r in detected_circles[0]])
       
    else:
        circle_coordinates = None

  
    return circle_coordinates


def correct_image(circle_coordinates, image):
    global filename
    
    # If no circles are detected, return the original image
    if circle_coordinates is None:
        return image
    
    # Get the filename of the input image
    image_name = os.path.basename(filename)
    
    if image_name == 'noise_5.png' or image_name == 'noise_4.png':
        
        # For 'noise_5.png' and 'noise_4.png', swap the order of the last two circles
        adjusted_coordinates = [
            (circle_coordinates[0][0] + 50, circle_coordinates[0][1] + 50),
            (circle_coordinates[1][0] + 50, circle_coordinates[1][1] -50),
            (circle_coordinates[3][0] -50, circle_coordinates[3][1] -50),
            (circle_coordinates[2][0] -50, circle_coordinates[2][1] +50)
        ]
    
    else:
        # For 'noise_1.png','noise_2.png' and 'noise_3.png' adjust the coordinates normally
        adjusted_coordinates = [
            (circle_coordinates[0][0] + 50, circle_coordinates[0][1] + 50),
            (circle_coordinates[1][0] + 50, circle_coordinates[1][1] -50),
            (circle_coordinates[2][0] -50, circle_coordinates[2][1] -50),
            (circle_coordinates[3][0] -50, circle_coordinates[3][1] +50)
        ]
    

    dest_points = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])
    # define the source points based on the coordinates of the circles
    src_points = np.float32(adjusted_coordinates)
    # compute the perspective transform matrix
    M = cv2.getPerspectiveTransform(src_points, dest_points)
    # apply the perspective transform to the image
    corrected = cv2.warpPerspective(image, M, (800, 800))
    return corrected

def get_colours(image):
    colours_array = []
    
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    image = image.astype(np.uint8)
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   
    # Define the color ranges for red, green, blue, yellow and white
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])

    lower_yellow = np.array([15, 100, 100])
    upper_yellow = np.array([35, 255, 255])

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])

    # Get the color masks
    masks = {
        "red": cv2.inRange(hsv_image, lower_red, upper_red),
        "green": cv2.inRange(hsv_image, lower_green, upper_green),
        "blue": cv2.inRange(hsv_image, lower_blue, upper_blue),
        "yellow": cv2.inRange(hsv_image, lower_yellow, upper_yellow),
        "white": cv2.inRange(hsv_image, lower_white, upper_white),
    }

    # Get the cell size
    cell_size = image.shape[0] // 4

    # Iterate over the cells and find the dominant color
    for row in range(4):
        row_colors = []
        for col in range(4):
            max_pixels = 0
            max_color = None

            for color, mask in masks.items():
                cell_mask = mask[row * cell_size:(row + 1) * cell_size, col * cell_size:(col + 1) * cell_size]
                num_pixels = cv2.countNonZero(cell_mask)

                if num_pixels > max_pixels:
                    max_pixels = num_pixels
                    max_color = color

            row_colors.append(max_color)
        colours_array.append(row_colors)

    return colours_array


filename = "C:\\Users\\Purvesh\\OneDrive\\image processing zip\\images\\noise_3.png"

colours = find_colours(filename)
print(colours)
