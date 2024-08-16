import numpy as np
import cv2
import imutils
from skimage.filters import threshold_local
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    maxWidth = max(int(np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))),
                   int(np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))))
    maxHeight = max(int(np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))),
                    int(np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))))
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


def ocr(im):
  
    image = remove_shadow(im)
    text = pytesseract.image_to_string(image)

    return text

def edgeDetection(image):
    image = imutils.resize(image, height = 500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.array([[0, -1, 0],
                       [-1,  5, -1],
                       [0, -1, 0]])
    
    sharpened = cv2.filter2D(gray, -1, kernel)
    blurred = cv2.GaussianBlur(sharpened, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 90)
    return edged

def findContour(edged):
    screenCnt = np.array([])
    cnts = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
       
        if len(approx) == 4:
            screenCnt = approx
            break
    return screenCnt


def scan(screenCnt, image):
    ratio = image.shape[0] / 500.0
    warped = four_point_transform(image, screenCnt.reshape(4, 2) * ratio)
   
    return warped

def remove_shadow(image):
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
  
  
    median_blur = cv2.medianBlur(gray, 21)
    
  
    diff = cv2.absdiff(median_blur, gray)
    
   
    _, inverse_diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    inverse_diff = 255 - inverse_diff
    
    
    return inverse_diff


def convert_to_binary(img):

    image = remove_shadow(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


    return binary
    
def enhance_saturation(image, saturation_factor=1.05):
   
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

 
    h, s, v = cv2.split(hsv)

  
    s = np.clip(s * saturation_factor, 0, 255).astype(np.uint8)

  
    enhanced_hsv = cv2.merge([h, s, v])

   
    enhanced_image = cv2.cvtColor(enhanced_hsv, cv2.COLOR_HSV2BGR)

    return enhanced_image

def main():
    image = cv2.imread("image9.jpg")
    EdgedImage = edgeDetection(image)  
    screenCnt = findContour(EdgedImage)
    newImage = image
    
    print(screenCnt)
    if screenCnt.size > 0:
        newImage = scan(screenCnt,image)   
        
    ProcessedImage = remove_shadow(newImage)
    ocr(ProcessedImage) 
   
    
    cv2.imshow("Scanned", imutils.resize(ProcessedImage, height = 650))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
