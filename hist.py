# Importing Important libraries
from tkinter import filedialog
from tkinter import *
import cv2


# Helper functions
def open_file1():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    img_path_1 = root.filename
    print("Image 1 : ", img_path_1)
    f = open("file.txt", "w")
    f.write(str(img_path_1) + '\n')
    f.close()


def open_file2():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    img_path_2 = root.filename
    print("Image 2 : ", img_path_2)
    f = open("file.txt", "a")
    f.write(str(img_path_2) + '\n')
    f.close()


def cal():
    print("\nRunning...")


# Function to return the similarity index between teo histograms
def compare_histogram(histogram1, histogram2):
    similarity_index = cv2.compareHist(histogram1, histogram2, cv2.HISTCMP_BHATTACHARYYA)
    return similarity_index


# Function to return the histogram of an image
def get_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    return histogram


# Simple Graphical user interface
root = Tk()
root.geometry('355x140')
root.title("Image similarity calculator")
btn1 = Button(root, text="Select Image 1", command=open_file1)
btn1.grid(row=2, column=1, padx=20, pady=20)
btn2 = Button(root, text="Select Image 2", command=open_file2)
btn2.grid(row=2, column=3, padx=20, pady=20)
btn3 = Button(root, text="Calculate", command=cal)
btn3.grid(row=4, column=2, padx=20, pady=20)
root.mainloop()

# Initialise path for images
f = open("file.txt", "r")
img_path_1 = f.readline().strip()
img_path_2 = f.readline().strip()
f.close()

# Reading image 1
image1 = cv2.imread(img_path_1)

histogram1 = get_histogram(image1)

# Reading image 2
image2 = cv2.imread(img_path_2)

histogram2 = get_histogram(image2)

# Get the similarity index
similarity_index = 1 - compare_histogram(histogram1, histogram2)

similarity_index = round(similarity_index * 100, 4)

print("\nThe calculated similarity index between the images is", str(similarity_index) + "%")
