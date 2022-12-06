import cv2
import pytesseract
import webbrowser

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

img = cv2.imread("face.png",1) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

visage = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),   
)

print("Found {0} visage!".format(len(visage)))

for (x, y, m, n) in visage:
    cv2.rectangle(img, (x, y), (x+m, y+n), 
                  (0, 0, 255), 2)      
    visage = img[y:y + n, x:x + m]
    cv2.imshow("face",visage)
    cv2.imwrite('srinivas.jpg', visage)
cv2.imwrite('identified.jpg', img)

t_old = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
r_k = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

dil = cv2.dilate(t_old, r_k, iterations = 1)
con, des = cv2.findContours(dil, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)
 
image2 = img.copy() 

f = open("info.txt", "m+")
f.write("")
f.close()

for count in con:
    
    x, y, m, n = cv2.boundingRect(count)
    Rect = cv2.rectangle(image2, (x, y), (x + m, y + n), (0, 255, 0), 2)
    cropimg = image2[y:y + n, x:x + m]
    text = pytesseract.image_to_string(cropimg)

    f = open("info.txt", "a")
    f.write(text)
    f.close

identify = cv2.QRCodeDetector()
url_data, bbox, straight_qrcode = identify.detectAndDecode(img)
if url_data:
    webbrowser.open(url_data)