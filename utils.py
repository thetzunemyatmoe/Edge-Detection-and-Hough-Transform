from matplotlib import pyplot as plt

import cv2
import numpy as np

import scipy
import scipy.signal
# Function 1


def display_original_and_gt(original_image, ground_truth_image, title):
    # Create a 1x2 grid for side-by-side display
    plt.figure(figsize=(12, 6))

    # Display original image
    plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
    plt.imshow(original_image)
    plt.title(f'{title} -- Original')
    plt.axis('off')  # Turn off axis

    # Display ground truth image
    plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
    plt.imshow(ground_truth_image)
    plt.title(f'{title} -- Ground Truth')
    plt.axis('off')  # Turn off axis

    # Show the images
    plt.tight_layout()
    plt.show()

# Function 2


def display_single(image, title=None, is_gray=True):

    plt.imshow(image, cmap='gray')
    if title:
        plt.title(title)
    plt.axis('off')
    plt.show()

# Function 3


def display_filtered_edge_results(image_name, filter_type, images, edge_results):
    """
    Display the original image and results of edge detection using a specified filter.

    Parameters:
        image_name (str): Name of the image to be displayed.
        filter_type (str): Type of filter ('mean' or 'gaussian').
        original_images (dict): Dictionary of original images keyed by name.
        edge_results (dict): Dictionary of edge detection results.
                             Format: {filter_type: {detector_name: [image1_result, image2_result, ...]}}
    """
    # Find the index of the image in the provided data
    if image_name not in image_names:
        print(f"Error: Image '{image_name}' not found.")
        return

    image_idx = image_names.index(image_name)
    print(image_idx)

    # Define the detectors in display order
    detectors = ['sobel', 'prewitt', 'kirch', 'robinson', 'gaussian']

    # Create a 2x3 grid for visualization
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    fig.suptitle(
        f'{filter_type.capitalize()} Filtered Edge Detection Results for {image_name}', fontsize=16)
    axes = axes.flatten()

    # Display the original image in the first subplot
    axes[0].imshow(images[image_idx], cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    # Display edge detection results for each detector
    for i, detector in enumerate(detectors):
        if i + 1 < len(axes):  # Ensure we're within grid bounds
            edge_image = edge_results[filter_type][detector][image_idx]
            axes[i + 1].imshow(edge_image, cmap='gray')
            axes[i +
                 1].set_title(f'{filter_type.capitalize()} - {detector.capitalize()}')
            axes[i + 1].axis('off')

    # Turn off any unused subplots
    for j in range(len(detectors) + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout for the title
    plt.show()


def edge_detection(image, detector):
    # Convoling the image (X direction)
    convolve_x = scipy.signal.convolve2d(
        image, detector['x'], mode='same', boundary='symm')
    convolve_y = scipy.signal.convolve2d(
        image, detector['y'], mode='same', boundary='symm')

    # Calculating magnitude
    m = abs(np.sqrt(np.square(convolve_x) + np.square(convolve_y)))

    # Normalize
    normalized_edge = cv2.normalize(
        m, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    return normalized_edge
