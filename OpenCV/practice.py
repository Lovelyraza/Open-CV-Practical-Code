import cv2
import numpy as np

# #1 Camera open karne ke liye 
# camera=cv2.VideoCapture(0)

# #2 Frame ki width our height set karne ke liye
# frame_width  = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# #3 Codec define karne ke liye jis se video ka size boht kaam ho jaye ga or quality bhi same rah gi
# codec=cv2.VideoWriter_fourcc(*'XVID')

# #4 video writer object create karne ke liye
# output_file=cv2.VideoWriter('output.avi',codec,20,(frame_width,frame_height))

# # Video starting
# while True:
#     success,frame=camera.read()
#     if not success:
#         print("Camera se frame ni mila")
#         break
#     else:
#         #5 frame ko output file me write karne ke liye
#         output_file.write(frame)
#         cv2.imshow('Camera Frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('d'):
#             break
# #6 resources ko release karne ke liye
# camera.release()
# output_file.release()
# cv2.destroyAllWindows()



# import cv2

# cap = cv2.VideoCapture("output.avi")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     cv2.imshow("Video", frame)

#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# kernel = np.array([[0, -1, 0],
#                    [-1, 5,-1],
#                    [0, -1, 0]])

# image=cv2.imread("C:\\Users\\Ali Raza\\OneDrive\\Desktop\\OpenCV\\pexels-fmaderebner-869258.jpg")

# image=cv2.resize(image,(600,400))
# # gimage=cv2.GaussianBlur(image,(9,9),0)
# # mimage=cv2.medianBlur(image,9)
# simage=cv2.filter2D(image,-1,kernel)
# cv2.imshow("Original Image",image)
# # cv2.imshow("Gaussian Blur",gimage)
# # cv2.imshow("Median Blur",mimage)
# cv2.imshow("Sharpened Image",simage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img=cv2.imread("pexels-fmaderebner-869258.jpg")
img=cv2.resize(img,(300,300))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(img,150,200)
ret,thresh=cv2.threshold(img,150,255,cv2.THRESH_BINARY)
cv2.imshow("Original Image",img)
# cv2.imshow("Canny Edge Detection",canny)
cv2.imshow("Thresholding",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
# import cv2
# import numpy as np

# img1 = np.zeros((300,300), dtype="uint8")
# img2 = np.zeros((300,300), dtype="uint8")

# cv2.circle(img1, (150,150), 100, 255, -1)
# cv2.rectangle(img2, (50,50), (250,250), 255, -1)

# cv2.imshow("Circle", img1)
# cv2.imshow("Rectangle", img2)
# bitwise_and = cv2.bitwise_and(img1, img2)
# bitwise_or = cv2.bitwise_or(img1, img2)
# bitwise_not = cv2.bitwise_not(img1)
# cv2.imshow("Bitwise AND", bitwise_and)
# cv2.imshow("Bitwise OR", bitwise_or)
# cv2.imshow("Bitwise NOT", bitwise_not)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# img = cv2.imread("C:\\Users\\Ali Raza\\OneDrive\\Desktop\\OpenCV\\circle.png") #path to the image
# img = cv2.resize(img, (600, 400))   # As image was too large so resizing it to display properly
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converting to grayscale as countour function works on single channel images
# _, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # Applying thresholding less then 200 will be black else white
# counters, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, counters, -1, (255, 0,0),5)  # Drawing all contours in blue color with thickness of 5
# cv2.imshow("Threshold Image", threshold)  # Displaying the threshold image
# cv2.imshow("Contours", img)
# # cv2.imshow("Original Image", img)   # Displaying the original image
# cv2.waitKey(0)         
# cv2.destroyAllWindows()