# Set the variable "collage" to the image "collage.png", which is stored in memory.
collage = makePicture("/Users/keithharrison/Google Drive/GCU/CST-111/Week7/collage.png")

# Set the variable "messageToEncode" to the image "messageToEncode.png", which is stored in memory.
messageToEncode = makePicture("/Users/keithharrison/Google Drive/GCU/CST-111/Week7/messageToEncode.png")

# Set the variable "encodedCollage" to the image "encodedCollage.png", which is stored in memory.
encodedCollage = makePicture("/Users/keithharrison/Google Drive/GCU/CST-111/Week7/encodedCollage.png")


def main():
  # Welcomes the user and prompts the user to select "encrypt" or "decrypt".
  print("Welcome to the secret message encoder/decoder!\nThis program will take a text message in image format and encrypt it in a collage so it is hidden and will take the encrypted image, decrypt it and reveal the hidden message!\nPlease choose the option number you want.\n[1] Encrypt Message\n[2] Decrypt Message")
  option = raw_input("Please select '1' or '2':")  # Variable "option" equal to the user's selection.
  # if/else statements to select the appropriate option
  if option == "1":  # If the user's input is equal to "1":
    print("You selected Option 1: Encrypt Message!\n")  # Inform the user of their choice.
    encryptKey()  # Call the "encryptKey()" function.
  elif option == "2":  # If the user's input is equal to "2":
    print("You selected Option 2: Decrypt Message!\n")  # Inform the user of their choice.
    decryptKey()  # Call the "decryptKey()" function.
  else:  # If the user's input is not a "1" or a "2":
    print("Sorry, I didn't understand your selection. Please try again:\n")  # Inform the user of their invalid choice.
    main() # Call the "main()" function to start the process over again.


# Function that asks for the correct encryption key, calls the function that encrypts the message image into the collage image, shows the encrypted image and saves it to file.
def encryptKey():
  response = raw_input("Now, please enter the correct encryption key: ") # Variable "respone" equal to the user's input of the encryption key.
  if response == "LopesUp!":  # If the user's input is equal to "LopesUp!", the correct encryption key:
    print("Encrypting now! Please wait ... once done, the encrypted image will appear!")  # Print a "please wait" message to console.
    encrypt(messageToEncode, collage)  # Calls the "encrypt" function, passing the "messageToEncode" argument for the "message" parameter and the "collage" argument for the "src" parameter.
    print("Encryption completed successfully!")    
    explore(collage) # Show the encrypted image.
    writePictureTo(collage, "/Users/keithharrison/Google Drive/GCU/CST-111/Week7/encodedCollage.png") # Write the encrypted image's value to "encodedCollage.png".
  else:  # If the user's response is NOT "LopesUp!":
    print("You have entered an incorrect encryption key, please try again:") # Print to the console that the user's encryption key was incorrect.
    encryptKey() # Call the "encryptKey()" function to restart the process over again.


# Function that asks for the correct encryption key and calls the function that decrypts the message hidden in the encrypted image.        
def decryptKey():
  response = raw_input("Now, please enter the correct encryption key:") # Variable "respone" equal to the user's input of the encryption key.
  if response == "LopesUp!":  # If the user's input is equal to "LopesUp!", the correct encryption key:
    print("Decrypting now! Please wait ... once done, the decrypted message will appear!")  # Print a "please wait" message to console.
    decrypt(encodedCollage)  # Calls the "deencrypt" function, passing the "encodedCollage" argument for the "encodedImage" parameter.  
  else:  # If the user's response is NOT "LopesUp!":
    print("You have entered an incorrect encryption key, please try again:")  # Print to the console that the user's encryption key was incorrect.
    decryptKey()  # Call the "dencryptKey()" function to restart the process over again.


# Function that makes all source image red pixels even, then hides the secret message in the source image.
def encrypt(message, src): # Function "encrypt()" that takes two parameters, "message", which is the secret message image and "src", which is the collage that the message will be hidden within.
  # for loop that ensures each red pixel value for "src" is even numbered.
  for pix in getPixels(src):  # for each index "pix" in each pixel from "src":
    if (getRed(pix) % 2) == 1:  # if the red pixel value is odd or pix divided by two has a remainder of 1, indicating an odd value:
      setRed(pix, getRed(pix) - 1)  # set the red pixel's value to pix minus 1, making that red pixel's value even.
  # for loop that ranges through the width and height of the source image, evaluates how close to black are the message image pixels and if the message image pixel is black, make its red pixel's value odd.
  for srcImageX in range(0, getWidth(src)):  # for each index "srcImageX" in range from 0 to the width of the source image. Represents the pixel position of X in the source image.
    for srcImageY in range(0, getHeight(src)):  # AND for each index "srcImageY" in range from 0 to the height of the source image. Represents the pixel position of Y in the source image.
      msg_px = getPixel(message, srcImageX, srcImageY) # Set variable "msg_px" to the value of each pixel of the message image, at the X and Y indexes of the source image.
      src_px = getPixel(src, srcImageX, srcImageY) # Set variable "src_px" to the value of each pixel of the source image, at the X and Y indexes of the source image.
      if (distance(getColor(msg_px), black) < 100.0): # If the distance between the color value of the message image's pixel is less than 100, meaning if the pixel is black.
        setRed(src_px, getRed(src_px) + 1) # Then set the red value of the source image's pixel to an odd number by adding one to the value.


# Function that creates an empty image, decrypts the encoded image, that shows the revealed message and saves the revealed message to a file.        
def decrypt(encodedImage): # Function "decrypt()" that takes one parameter, "encodedImage", which is the collage image with the secret message hidden within it.
  messageDecoded = makeEmptyPicture(getWidth(encodedImage), getHeight(encodedImage)) # Creates an empty image, the same size as the encoded image, setting its values to the variable "messageDecoded".
  for encodedX in range(0, getWidth(encodedImage)): # for each index "encodedX" in range from 0 to the width of the encoded image. Represents the pixel position of X in the encoded image.
    for encodedY in range(0, getHeight(encodedImage)): # for each index "encodedY" in range from 0 to the height of the encoded image. Represents the pixel position of Y in the encoded image.
      encoded_px = getPixel(encodedImage, encodedX, encodedY) # Set variable "encoded_px" to the value of each pixel of the encoded image, at the X and Y indexes of the encoded image.
      message_px = getPixel(messageDecoded, encodedX, encodedY) # Set variable "message_px" to the value of each pixel of the empty image, at the X and Y indexes of the encoded image.
      if (getRed(encoded_px) % 2) == 1: # if the red pixel value is odd or encoded_pix divided by two has a remainder of 1, indicating an odd value:
        setColor(message_px, black) # Set the empty image's pixel's color to black.
  print("Decryption completed successfully!")
  show(messageDecoded) # Show the decoded message image.
  writePictureTo(messageDecoded, "/Users/keithharrison/Google Drive/GCU/CST-111/Week7/decodedMessage.png") # Write the decoded message image's value to "decodedMessage.png".
  return messageDecoded  # Return the decoded image's value.

                      
main()  # Calls the "main()" function and starts the program.