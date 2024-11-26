import os
import cv2
from tkinter import Tk
from tkinter.filedialog import askdirectory

# folder selection
def select_image_directory():
    Tk().withdraw()
    folder = askdirectory(title="Select Folder Containing Images")
    if not folder:
        print("No folder selected. Exiting...")
        exit()
    return folder

def main():
    image_directory = select_image_directory()
    print(f"Selected directory: {image_directory}\n")
    image_file_names = os.listdir(image_directory)

    for filename in image_file_names:
        if filename.endswith(".png"):
            image_path = os.path.join(image_directory, filename)

            image = cv2.imread(image_path)
            if image is None:
                print(f"Could not read {filename}. Skipping...")
                continue

            cv2.imshow("Image", image)
            print(f"Image: {filename}")

            label = input("Enter the label for this image: ")

            cv2.destroyAllWindows()

            gt_filename = os.path.splitext(filename)[0] + ".gt.txt"
            gt_filepath = os.path.join(image_directory, gt_filename)

            with open(gt_filepath, "w", encoding="utf-8") as gt_file:
                gt_file.write(label)

            print(f"Saved label '{label}' to {gt_filename}\n")

    print("Finished processing.")

if __name__ == "__main__":
    main()
