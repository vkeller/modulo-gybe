### PART B

model.save('image.classifier.keras')
# Saves the trained model as 'image.classifier.keras'

model = models.load_model('image.classifier.keras')
# This simply loads in the trained model we just made in part A

img = cv.imread('horse-image.jpg')  
# img loads an image file (in this case, horse-image.jpg). 
# The cv.imread() function from OpenCV reads the image in the default BGR (Blue-Green-Red) color format.

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# This line converts the image from BGR to RGB format, which is the standard color format for most libraries, including Matplotlib.
# OpenCV reads images in BGR, while Matplotlib expects images in RGB. This step ensures the colors display correctly.

plt.imshow(img, cmap=plt.cm.binary)
# This parameter is optional, if you want the image in its original color, you can remove this line. 
plt.show()
