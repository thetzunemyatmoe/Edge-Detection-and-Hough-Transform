
# Cell Detection using Edge Detection and Hough Transform

This repository contains the implementation for the "Cell Detection" assessed assignment as part of the Computer Vision and Imaging module. The assignment involves implementing and analyzing various edge detection algorithms and the Hough Transform for detecting features in fluorescing cell images.


## Project Overview

Serological testing for anti-nuclear antibodies (ANAs) is critical for diagnosing autoimmune diseases. This project focuses on detecting fluorescing cells in images obtained using indirect immunofluorescence (IIF) on HEp-2 cells. The primary aim is to evaluate various edge detection algorithms to analyze and identify nuclear components in the images, reducing subjective bias in interpretation.

### Objectives
1. Evaluate the performance of edge detection algorithms (Robinson, Sobel, Prewitt, Kirsch, Gaussian).
2. Implement an additional edge detection algorithm for comparison.
3. Use the Canny edge detector and Hough Transform to detect lines in a specific image.

---

## Tasks

### Task 1: Edge Detection
- **Description**: Apply the Robinson, Sobel, Prewitt, Kirsch, and Gaussian (5x5 kernel) edge detection algorithms to three fluorescing cell images.
- **Steps**:
  - Preprocess images (Load the images and apply Guassian Blur).
  - Apply each filter in horizontal and vertical directions.
  - Combine the results and compare against the provided ground truth edges (using F1 score).

### Task 2: Advanced Edge Detection
- **Description**: Implement an additional edge detection algorithm (Canny Edge Detection on the same images and compare it with those used in Task 1.
- **Steps**:
  - Implement and apply the algorithm to the images.
  - Evaluate performance and discuss its strengths and weaknesses (using F1 score).

### Task 3: Hough Transform
- **Description**: Use the Canny edge detector on `Bhamimage.jpeg` to identify edge points, then apply the Hough Transform to detect lines.
- **Steps**:
  - Apply the Canny edge detector.
  - Use the Hough Transform to detect and visualize lines.
  - Analyze the detected lines and discuss observations.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**: OpenCV, NumPy, Matplotlib, SciImage

---

## Acknowledgments
- **University of Birmingham and School of Computer Science**: For providing the assignment and dataset.
- **Module Instructor and Teachig Assistants **: For guidance and support throughout the project.

Feel free to contribute or report any issues! 🚀
