import cv2
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
image = cv2.imread('Bs.jpeg')
cv2.imshow("Anime", image)
cv2.waitKey(0)

import matplotlib.pyplot as plt 

# Convertir l'image de BGR à RGB 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
 
# AEicher l'image dans le notebook 
plt.imshow(image_rgb) 
plt.axis('oE')  # Optionnel : pour ne pas aEicher les axes 
plt.show()