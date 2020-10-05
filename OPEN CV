import cv2
def main():
    imgpath="D:\\for development purpose only\\python\\openCV\\img database\\standard_test_images\\lena_color_512.tif"
    img=cv2.imread(imgpath, 0)
    savepath="D:\\for development purpose only\\python\\openCV\\output\\ReadAndWriteOperation\\lena_grayscale_512.jpg"
    cv2.namedWindow('lena',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('lena',img)
    cv2.imwrite(savepath,img)
    cv2.waitKey(0)
    cv2.destroyWindow('lena')
if __name__=="__main__":
    main()
