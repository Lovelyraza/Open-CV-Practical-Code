# import cv2

# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
# eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml") 
# smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml") 
# cap = cv2.VideoCapture(0) 
# while True: 
#     ret, frame = cap.read() 
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
#     faces=face_cascade.detectMultiScale(gray,1.3,5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h,x:x+w]
#         roi_color = frame[y:y+h,x:x+w]
#         eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10)
#         if len(eyes)>0:
#             cv2.putText(frame,"Eyes Detected",(x,y-50),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
#         smiles=smile_cascade.detectMultiScale(roi_gray,1.7,20)
#         if len(smiles)>0:
#             cv2.putText(frame,"Smiling",(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
#     cv2.imshow("Smart Face Detector", frame) 
#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break 
# cap.release() 
# cv2.destroyAllWindows()
# import cv2

# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
# smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]

#         # --- EYES ---
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
#         if len(eyes) > 0:
#             cv2.putText(frame, "Eyes Detected", (x, y-50),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

#         # --- MOUTH REGION ONLY ---
#         mh = h // 2   # mouth starts halfway down the face
#         mouth_gray = roi_gray[mh:h, 0:w]

#         smiles = smile_cascade.detectMultiScale(
#             mouth_gray,
#             scaleFactor=1.7,
#             minNeighbors=22,
#             minSize=(25, 25)
#         )

#         if len(smiles) > 0:
#             cv2.putText(frame, "Smiling", (x, y-20),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

#     cv2.imshow("Smart Face Detector", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)

def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, _ = frame.shape

    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face in result.multi_face_landmarks:
            # Mouth landmark points
            # Upper Lip = 13 , Lower Lip = 14
            # Left Mouth Corner = 61 , Right Mouth Corner = 291

            p13 = face.landmark[13]
            p14 = face.landmark[14]
            p61 = face.landmark[61]
            p291 = face.landmark[291]

            lip_top = (int(p13.x * w), int(p13.y * h))
            lip_bottom = (int(p14.x * w), int(p14.y * h))
            left_corner = (int(p61.x * w), int(p61.y * h))
            right_corner = (int(p291.x * w), int(p291.y * h))

            # Distances
            mouth_width = euclidean(left_corner, right_corner)
            mouth_height = euclidean(lip_top, lip_bottom)

            smile_ratio = mouth_width / mouth_height

            # Threshold experimentally (best value ≈ 2.0)
            if smile_ratio > 2.0:
                cv2.putText(frame, "Smiling", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            else:
                cv2.putText(frame, "Not Smiling", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Smile Detector (MediaPipe)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
