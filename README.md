
# Quantitative Analysis of ANA HEp-2 Cell Images via Edge Detection Techniques

## Description
This project implements traditional edge detection techniques on fluorescing cell images and evaluates their performance against ground truth data using the F1 score.


## Project Overview

Serological testing for anti-nuclear antibodies (ANAs) is critical for diagnosing autoimmune diseases. This project focuses on detecting fluorescing cells in images obtained using indirect immunofluorescence (IIF) on HEp-2 cells. The primary aim is to evaluate various edge detectors to analyze and identify nuclear components in the images, reducing subjective bias in interpretation. The tested each detector includes 
1. Robinson
2. Sobel
3. Prewitt
4. Kirch
5. Guassian
6. Canny

**F1 score** was used as a metric for evaluation.

$$
F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}
{\text{Precision} + \text{Recall}}
$$

## Methods

### Preprocessing Steps  

#### 1. Loading Data  
- Images and their **ground truths** were loaded using **scikit-image**.  

#### 2. Grayscale Conversion  
- Original images were converted to grayscale to simplify processing and focus on intensity information.  

#### 3. Noise Reduction  
- Applied Gaussian Filtering to reduce high-frequency noise while preserving important structures.  

#### 4. Ground Truth Preparation  
- Converted **ground truth images** to **binary format** (black & white) for accurate edge comparison.  
---

### Modular Edge Detection Function  

To streamline experimentation with multiple edge detectors,  
a modular edge detection function was implemented:  

- Purpose  
  - Allows easy substitution of different convolution kernerls of each edge detector.  
  - Simplifies threshold-based edge extraction.
  - Supports quick comparison between detectors.  

- **Workflow:**  
  1. Convolve the image in both **X** and **Y** directions using the selected detector kernels.
  2. Compute the **magnitude** of gradients.  
  3. **Normalize** the resulting edges for uniform intensity scaling using **OpenCV**.
  4. Apply a **threshold** to produce a binary edge map.

---

## Results

### Picture 1
| Operator | Threshold | F1      |
|----------|-----------|---------|
| Robinson | 80        | 0.58544 |
| Sobel    | 75        | 0.58579 |
| Prewitt  | 80        | 0.58667 |
| Kirsch   | 75        | 0.58446 |
| Gaussian | 85        | 0.58980 |
*Table 1: Highest F1 scores and their corresponding highest threshold of different edge detectors for Picture 1.*


### Picture 2
| Operator | Threshold | F1      |
|----------|-----------|---------|
| Robinson | 60        | 0.66206 |
| Sobel    | 65        | 0.66568 |
| Prewitt  | 65        | 0.66494 |
| Kirsch   | 65        | 0.66222 |
| Gaussian | 70        | 0.65303 |
*Table 2: Highest F1 scores and their corresponding highest threshold of different edge detectors for Picture 2.*

### Picture 3
| Operator | Threshold | F1      |
|----------|-----------|---------|
| Robinson | 25        | 0.55983 |
| Sobel    | 25        | 0.56442 |
| Prewitt  | 25        | 0.56503 |
| Kirsch   | 25        | 0.56261 |
| Gaussian | 25        | 0.56630 |
*Table 3: Highest F1 scores and their corresponding highest threshold of different edge detectors for Picture 3.*

### Canny Edge Detector
| | 9343 AM | 10905JL | 43590AM |
|---|---|---|---|
| Low Threshold | 0.1 | 0.1 | 0.1 |
| High Threshold (2*Low Threshold) | 0.2 | 0.2 | 0.2 |
| F1 score | 0.3814 | 0.4682 | 0.1383 |
*Table 4: F1 scores and highest threshold of Canny Edge Detector on three pictures.*


## Acknowledgments
- **University of Birmingham and School of Computer Science**: For providing the assignment and dataset.
- **Module Instructor and Teachig Assistants**: For guidance and support throughout the project.


