import cv2,dropbox,time,random

startTime=time.time()

def snap_shot():
    num = random.randint(1,200)
    #video capture object from cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(num) + ".png"
        cv2.imwrite(img_name,frame)
        #start_time = time()
        result = False
        return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_img(img):
    access_token="sl.BBBD-W9DfJmKQUsEG2iNQHqbz4shgEXhv_B9sy-Qv5VWQRXcsSZrzq84Yeqf6WizS6UB1yvCJHORe9RXdLKu7ALMe8eKnSqIxLoKUPx51kN7c0gRUA049TeyERtnliog0JDIQ0Y"
    file_from = img
    file_to = "/Python/" + img
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=300):
            name=snap_shot()
            upload_img(name)

main()