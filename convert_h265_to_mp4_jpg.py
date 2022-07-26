import ffmpeg
import cv2
import os

def get_jpg_from_h265(fn,sn,scale):
    fn_split_l = fn.rsplit('.')[0]
    try:
        os.remove(fn_split_l+".mp4")
    except:
        pass
    stream = ffmpeg.input(fn)
    stream = ffmpeg.output(stream, fn_split_l + '.mp4')
    ffmpeg.run(stream)
    vidcap = cv2.VideoCapture(fn_split_l + '.mp4')
    success,image = vidcap.read()
    if scale != 1:
        h,w = int(image.shape[0]*scale),int(image.shape[1]*scale)
        image = cv2.resize(image,(w,h))
    cv2.imwrite(sn, image) 


if __name__=="__main__":
    get_jpg_from_h265("stream.h265","stream.jpg")
