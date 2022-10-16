"""Batch convert videos to greyscale .
Install dependencies:
  pip install pillow docopt
Note: If you do not provide an output path, the generated files will be saved
in a folder named "Converted"
Usage:
  greyscale.py <in_path> [<out_path>]
  greyscale.py -h | --help
  greyscale.py --version
Arguments:
  <in_path>   Input directory
  <out_path>  Output directory [default: ./Converted]
Options:
  -h, --help  Show this help screen.
  --version     Show version.
"""

import docopt
import cv2 as cv
import os
import time
import matplotlib.pyplot as plt
import glob
import sys


def process_video(video_inpath, video_outpath):
    name, ext = os.path.splitext(video_inpath)
    # name = name + "_grey1"
    # gray_video_path = name + ext
    # use extension .avi for xvid
    # gray_video_path = 'output.avi'
    # print(gray_video_path)
    cap = cv.VideoCapture(video_inpath)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'mp4v')  # use xvid for .avi
    # enter appropriate fps and frame size
    out = cv.VideoWriter(video_outpath, fourcc, 23.98, (1280, 720), False)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # write the flipped frame
        out.write(frame)
        # cv.imshow('frame', frame)
        # key = cv.waitKey(1)
        # if key == ord('q'):
        # break
        # if key % 256 == 27:    # pressing escape key will exit
        # break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()


def main(in_path, out_path):
    if not os.path.isdir(in_path):
        print('Error: <in_path> must be a directory', file=sys.stderr)
        return

    if out_path is None:
        dirname = os.path.dirname(in_path)
        out_path = dirname + 'Converted'

    if not os.path.exists(out_path):
        print('Creating directory', out_path)
        os.mkdir(out_path)

    x = []  # number of files
    y = []  # time taken to process number if files in x
    i = 0  # file counter
    start_time = time.time()
    x.append(i)  # marking origin
    end_time = time.time()
    y.append(end_time - start_time)  # marking origin time for better graph view

    for in_file in glob.glob(in_path + '/*'):
        filename = os.path.basename(in_file)
        out_file = out_path + '/' + filename
        process_video(in_file, out_file)
        if i in [1, 2, 3, 4, 5, 6, 7, 8]:
            x.append(i)
            end_time = time.time()
            y.append(end_time - start_time)
        i += 1
    plt.plot(x, y, 'ko-')
    plt.xlabel('Number of files -> ')
    plt.ylabel('Time taken (s) ->')
    plt.title(label="using openCV", fontsize=15, color="red")
    plt.show()


if __name__ == '__main__':
    args = docopt.docopt(__doc__, version='Greyscale converter v2.0')
    main(args['<in_path>'], args['<out_path>'])
