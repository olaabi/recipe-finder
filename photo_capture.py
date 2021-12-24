'''
Main Activity file (Taking photos of ingredients file)
First Stage: Take photo from webcam, write to a file then read into ingredient_classifier.py
'''

# Imports
import cv2 as cv

# Video capture from webcam
cam = cv.VideoCapture(0)
ingredient_photos = [] # empty list that will contain the current set of ingredients (consider using dictionary)

while True:
    retVal, img = cam.read()
    cv.imshow("Capturing new photo...", img)
    
    # press c for taking photo; saves to folder (for testing) + list
    # consider classifying photos after pressing c
    if cv.waitKey(1) & 0xFF == ord('c'):
        ingredient_photos.append(img)
        cv.imwrite("ingredient" + str(len(ingredient_photos)) + ".jpg", img)
        print("Ingredient added.")
    
    # press q to stop taking photos
    elif cv.waitKey(1) & 0xFF == ord('q'):
        print("Done!")
        break

cam.release()
cv.destroyAllWindows()

