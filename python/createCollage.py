# Function used to copy a source image to a target image, pixel by pixel. Called in the imageCollage() function.
def imageCopy(src, tar, tarX, tarY): # The function takes 4 parameters.
  tarImageX = tarX  # Sets the tarImageX variable equal to the tarX imageCopy() function parameter.
  for srcImageX in range(0,getWidth(src)):  # For loop that iterates through the range from 0 to the width of the source (src) image.
    tarImageY = tarY  # Sets the tarImageY variable equal to the tarY imageCopy() function parameter.
    for srcImageY in range(0,getHeight(src)):  # Nested for loop that iterates through the range from 0 to the height of the source (src) image.
      src_px=getPixel(src,srcImageX,srcImageY)  # getPixel function called on the source (src) image with the srcImageX and scrImageY indexes.
      tar_px=getPixel(tar,tarImageX,tarImageY)  # getPixel function called on the target (tar) image with the tarImageX and tarImageY indexes.
      setColor(tar_px,getColor(src_px))  # Sets the color of the target pixel (tar_px) to that of the source pixel (src_px).
      tarImageY += 1  # Increments the tarImageY variable by 1 to iterate through the entire image along the Y-axis as the loop runs.
    tarImageX += 1  # Increments the tarImageX variable by 1 to iterate through the entire image along the X-axis as the loop runs.

# Function used to specifically copy a part of an image from a larger image, pixel by pixel, for the antelope's horns. Called in the imageCollage() function.
def copyHorns(src, tar, tarX, tarY): # The function takes 4 parameters.
  tarImageX = tarX  # Sets the tarImageX variable equal to the tarX imageCopy() function parameter.
  for srcImageX in range(10, 130):  # For loop that iterates through the range from 10 to 130, the start and stop X coordinates in the source image.
    tarImageY = tarY  # Sets the tarImageY variable equal to the tarY imageCopy() function parameter.
    for srcImageY in range(15, 115):  # Nested for loop that iterates through the range from 15 to 115, the start and stop Y cooridinates in the source image.
      src_px=getPixel(src,srcImageX,srcImageY)  # getPixel function called on the source (src) image with the srcImageX and scrImageY indexes.
      tar_px=getPixel(tar,tarImageX,tarImageY)  # getPixel function called on the target (tar) image with the tarImageX and tarImageY indexes.
      setColor(tar_px,getColor(src_px))  # Sets the color of the target pixel (tar_px) to that of the source pixel (src_px).
      tarImageY += 1  # Increments the tarImageY variable by 1 to iterate through the entire image along the Y-axis as the loop runs.
    tarImageX += 1  # Increments the tarImageX variable by 1 to iterate through the entire image along the X-axis as the loop runs.    

# Function used to specifically copy a part of an image from a larger image, pixel by pixel, for the rabbit's ears. Called in the imageCollage() function.
def copyEars(src, tar, tarX, tarY): # The function takes 4 parameters.
  tarImageX = tarX  # Sets the tarImageX variable equal to the tarX imageCopy() function parameter.
  for srcImageX in range(5, 120):  # For loop that iterates through the range from 5 to 120, the start and stop X coordinates in the source image.
    tarImageY = tarY  # Sets the tarImageY variable equal to the tarY imageCopy() function parameter.
    for srcImageY in range(5, 95):  # Nested for loop that iterates through the range from 5 to 95, the start and stop Y cooridinates in the source image.
      src_px=getPixel(src,srcImageX,srcImageY)  # getPixel function called on the source (src) image with the srcImageX and scrImageY indexes.
      tar_px=getPixel(tar,tarImageX,tarImageY)  # getPixel function called on the target (tar) image with the tarImageX and tarImageY indexes.
      setColor(tar_px,getColor(src_px))  # Sets the color of the target pixel (tar_px) to that of the source pixel (src_px).
      tarImageY += 1  # Increments the tarImageY variable by 1 to iterate through the entire image along the Y-axis as the loop runs.
    tarImageX += 1  # Increments the tarImageX variable by 1 to iterate through the entire image along the X-axis as the loop runs.

# Function that opens the source and target images and calls the copy() function to create the collage.
def imageCollage():

  # Gets the GCU Arena image, loads it into memory, and prints out the image statistics to the console.
  # The GCU Arena image is used as the background and the canvas in which other images are copied onto.
  gcu=makePicture("/Users/keithharrison/Google Drive/GCU/CST-111/Week6/gcuArena.jpg")
  print gcu
  
  # Gets the antelope image, loads it into memory, and prints out the image statistics to the console.
  antelope=makePicture("/Users/keithharrison/Google Drive/GCU/CST-111/Week6/antelope.jpg")
  print antelope
  
  # Gets the jackrabbit image, loads it into memory, and prints out the image statistics to the console.
  jackrabbit=makePicture("/Users/keithharrison/Google Drive/GCU/CST-111/Week6/jackrabbit.jpg")
  print jackrabbit
  
  # Copies the antelope image and places it 25 pixels from the left side of the GCU image and to the height of the GCU image minus the height of the antelop image minus 15 pixels.
  imageCopy(antelope,gcu,25,getHeight(gcu)-getHeight(antelope)-15)
  
  # Copies the jackrabbit image and places it 775 pixels from the left side of the GCU image and to the height of the GCU image minus the height of the rabbit image minus 15 pixels..
  imageCopy(jackrabbit,gcu,775,getHeight(gcu)-getHeight(jackrabbit)-15)
  
  # Copies the antelope horns and places them on the GCU Arena image on top of the jackrabbit at x = 780 and y = 495.
  copyHorns(antelope,gcu,780,495)
  
  # Copies the jackrabbit ears and places them on the GCU Arena image on top of the antelope at x = 42 and y = 382.
  copyEars(jackrabbit,gcu,42,382)
  
  # Shows the collage.
  show(gcu)
  # Writes collage to file.
  writePictureTo(gcu, "/Users/keithharrison/Google Drive/GCU/CST-111/Week6/collage.png")
  # Returns the collage.
  return gcu