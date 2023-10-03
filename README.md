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


## Important
# Image Processing Coursework Assignment

This repository contains my solution for a image processing coursework assignment as part of the Image Processing module in Msc. Data Science at University of Sussex. The assignment was completed during the 2022-2023 year.

## Disclaimer
**Note to Course Instructors and Evaluators:**
This project represents my individual effort and understanding of the coursework requirements. It is submitted in fulfillment of the academic requirements for the Image Processing module. The code and documentation are provided for educational purposes and as a showcase of my learning progress.

**Academic Integrity:**
I have adhered to the principles of academic integrity throughout the completion of this assignment. Any external resources, code snippets, or references used are appropriately cited in the code and documentation.

## Important Notice to Future Students
**Attention:** This project, including its code, documentation, and any associated materials, is the result of my individual effort and understanding. Future students are hereby informed not to copy or reproduce any part of this project. Such actions may be considered a violation of academic integrity policies, which could lead to severe consequences, including but not limited to disciplinary action by the university. I, the original author, will not be held responsible for any repercussions resulting from the misuse of this work by others. It is strongly advised to adhere to the principles of academic integrity and conduct your own work independently.

**Note:** Always refer to your university's policies on academic integrity and honor codes.


*Note: This README is designed to be transparent about the nature of the project and to comply with academic honesty policies.*
