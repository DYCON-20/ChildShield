import cv2

import cv2

  

# Charger l'image insert le nom de ton image içi 
image = cv2.imread('lena.jpg', 1)

# Charger le classificateur de cascade de visage
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Détecter les visages dans l'image
faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dessiner des rectangles autour des visages détectés
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Afficher l'image avec les rectangles
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# teste pour definir si le visage est detecter, et pour verifier la presance du fichier haarascade_frontalface_default.xml
print(face_cascade)

image_test = cv2.imread('lena.jpg')
gray = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) > 0:
    print("Visage détecté !")
else:
    print("Aucun visage détecté.")
