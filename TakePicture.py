import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time=time.time()

def takePicture():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time=time.time()
        result = False
    return img_name
    print("Picture Taken :(")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.BIDr9xvVV_rhYuxM1bVmbY9kcIouptmy9Q-fexFmHQ20rtip_ybORap6c1bTG6yVNVX8mRcyGJ9JnO10THzWp3IFBV_FDQHRsu-2v3blKhju6yRElmKeTWf56xT15HbgxavFgRk"
    file = img_name
    file_from = file
    file_to = "/webcamePictures/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = takePicture()
            upload_file(name)

main()
