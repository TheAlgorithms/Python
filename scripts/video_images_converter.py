import cv2
import os

def convert_images_to_video(image_folder, image_extension, video_name):
    '''
    Converts images into a video. Given a folder name, the images located in there will be converted into a video file.

    Parameters
    ----------
    image_folder : str
        Path where the images are stored.
    image_extension: str
        The search for images will be performed by searching the files by their extension.
    video_name : str
        Path where the video will be created.
    '''
    images = [img for img in os.listdir(image_folder) if img.endswith(image_extension)]
    images.sort(key= lambda f: int(''.join(filter(str.isdigit, f))))

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 25, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

def convert_video_to_images(image_folder, video_path, image_extension = ".jpg"):
    '''
    Converts video into images. Given a video folder name, the video will be converted into images and stored at given folder location.

    Parameters
    ----------
    image_folder : str
        Path where the images will be stored.
    video_path : str
        Path where the video are store.
    image_extension: str
        The frames obtained from the video will be stored at given extension. JPG by default.
    '''
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 1

    while success:
        cv2.imwrite(f"{image_folder}{count}{image_extension}", image)     
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

# convert_video_to_images("teste/", "teste.mp4")