# ImageProcessing-ColorRecognition

This repository contains a Python implementation for automated color recognition in images, specifically designed for Lego's Life of George game. The goal is to read a color pattern in the image from the hard disk and return an array representing the color pattern.

## Problem Statement

Lego’s Life of George is a game where an image is displayed on the screen for a number of seconds before being blanked. For this project, the objective is to write software that automatically reads a color pattern image from the hard disk and returns an array representing the color pattern. The images may have black circles for finding the edge, but there is no correct orientation.

## File Structure

- **images:** Contains problem images.
- **noise_images.py:** Code solution for noisy images.
- **org_images.py:** Code solution for original images.
- **rot_images.py:** Code solution for rotated images.

## Problem Solution Overview

### Noisy Images

#### `find_colours(filename)`
- **Input:** Image filename
- **Output:** 4x4 array representing the dominant colors in each cell of the given image.

#### `load_image(filename)`
- **Input:** Image filename
- **Output:** Normalized double data type image.

#### `find_circles(image)`
- **Input:** Image
- **Output:** Coordinates of the four black circles.

#### `correct_image(circle_coordinates, image)`
- **Input:** Circle coordinates, Image
- **Output:** Corrected perspective of the image.

#### `get_colours(image)`
- **Input:** Image
- **Output:** Array with the dominant colors from the image.

#### Performance Assessment
- Overall accuracy for noisy images: 100%

#### Areas for Improvement
1. The fixed radius range in `find_circles()` could be adaptive for better results.
2. `get_colours()` could use a more adaptive method to detect color ranges.

### Original Images

- Implementation and functions are similar to noisy images, with differences in kernel size and coordinate adjustments.

#### Performance Assessment
- Overall accuracy for original images: 100%

#### Areas for Improvement
1. Better code organization for readability and maintainability.
2. Proper error handling for robustness.

### Rotated Images

#### `find_colours(filename)`
- **Input:** Image filename
- **Output:** 4x4 array representing the dominant colors in each cell of the rotated image.

#### Performance Assessment
- Overall accuracy for rotated images: 93.75%

#### Areas for Improvement
- Further optimization or tuning needed for handling various image variations.

## Conclusion

The implemented solution successfully recognizes colors in noisy, original, and rotated images with high accuracy. Areas for improvement have been identified to enhance adaptability and robustness.

## How to Use

1. Clone the repository.
2. Run `noise_images.py`, `org_images.py`, or `rot_images.py` based on the type of image.


## Report

The detailed report can be found in the project directory, providing insights into each function's workings, design decisions, performance assessments, and suggestions for improvements.
