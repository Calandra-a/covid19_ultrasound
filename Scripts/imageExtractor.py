
import cv2
import os


# Function to extract frames
def FrameCapture(path,name):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # checks whether frames were extracted
    success = 1

    #number of images you want from video
    #todo implement a sleep to get image per time increment
    for i in range(1):
        
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
  
        # Saves the frames with frame-count
        cv2.imwrite("%s.jpg" % name, image)        
  
# Driver Code
if __name__ == '__main__':
  
    # Calling the function
    directory = "C:\\Users\\calan\\Documents\\CSI-6998\\covid19_ultrasound\\data\\pocus_videos\\linear\\container"
    for filename in os.listdir(directory):
        FrameCapture(os.path.join(directory, filename),os.path.splitext(filename)[0])