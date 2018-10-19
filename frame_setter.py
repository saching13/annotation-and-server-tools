import cv2


#def fps_modifier():






vid_cap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
success,image = vid_cap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vid_cap.read()
  print('Read a new frame: ', success)
  count += 1




