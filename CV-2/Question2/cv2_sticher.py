import numpy as np
import cv2

imagepath1=["Test-1/Img1.jpeg","Test-1/Img2.jpeg","Test-1/Img3.jpeg"]

imagepath2=["Test-2/Img1.jpeg","Test-2/Img2.jpeg","Test-2/Img3.jpeg"]

imagepath3=["Test-3/Img1.jpeg","Test-3/Img2.jpeg","Test-3/Img3.jpeg"]

imagepath4=["Test-4/Img1.jpeg","Test-4/Img2.jpeg","Test-4/Img3.jpeg"]

imagepath5=["Test-5/Img1.jpeg","Test-5/Img2.jpeg","Test-5/Img3.jpeg"]

imagepathArray = [imagepath1,imagepath2,imagepath3,imagepath4,imagepath5]

ns=1
for i in imagepathArray:	
	images = []
	for path in i:
		image = cv2.imread(path)
		images.append(image)
	print(len(images))
	stitcher = cv2.Stitcher_create()
	(status, stitched) = stitcher.stitch(images)

	if status == 0:
		print("Images are successfully stitched")
		cv2.imshow("Stitched Image", stitched)
		cv2.imwrite("stichedSet" + str(ns) +  ".png",stitched)
	else:
		print("[INFO] Failed Image Stitching ({})".format(status))
	ns=ns+1

