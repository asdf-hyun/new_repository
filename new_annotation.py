
import cv2
import numpy as np

# Parameters for drawing
drawing = False  # True if the mouse is pressed
ix, iy = -1, -1  # Initial x, y coordinates of the region

# List to store annotations as (x, y, height, width)
annotations = []

# Mouse callback function to draw rectangles and store (x, y, height, width)
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y  # Start point of the rectangle

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Draw the rectangle as the mouse moves
            temp_image = image.copy()
            cv2.rectangle(temp_image, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Image Segmentation", temp_image)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Calculate width and height of the rectangle
        width = x - ix
        height = y - iy
        # Store the rectangle as (x, y, height, width)
        annotations.append((ix, iy, height, width))

# Function to display the image and collect annotations
def segment_image(image_path):
    global image
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found!")
        return

    # Create a clone of the image for annotation display
    annotated_image = image.copy()
    cv2.namedWindow("Image Segmentation")
    cv2.setMouseCallback("Image Segmentation", draw_rectangle)

    while True:
        # Show the annotations on the cloned image
        temp_image = annotated_image.copy()
        for rect in annotations:
            x, y, height, width = rect
            cv2.rectangle(temp_image, (x, y), (x + width, y + height), (0, 255, 0), 2)

        # Display the image with annotations
        cv2.imshow("Image Segmentation", temp_image)
        
        # Press 's' to save annotations, 'c' to clear, and 'q' to quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
            # Save annotations in (x, y, height, width) format
            with open("annotations.txt", "w") as f:
                for rect in annotations:
                    f.write(f"{rect}\n")
            print("Annotations saved to annotations.txt")
        elif key == ord("c"):
            # Clear annotations
            annotations.clear()
            annotated_image = image.copy()
            print("Annotations cleared")
        elif key == ord("q"):
            break

    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    PathNames = r"C:\Users\cic\Desktop\Online_Repo-main\Image_dataset"
    segment_image(PathNames + "//000000000139.jpg")