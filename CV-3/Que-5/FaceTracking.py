import cv2

face_detector_model = cv2.CascadeClassifier("facefrontal.xml")

capture = cv2.VideoCapture(0)

while capture.isOpened():
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector_model.detectMultiScale(gray,1.1, 4 )
    for (x,y, w, h) in faces:
        cv2.putText(frame, "Srinivas Narne", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.rectangle(frame, pt1 = (x,y),pt2 = (x+w, y+h), color = (255,0,0),thickness =  3)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv2.imshow("window", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break