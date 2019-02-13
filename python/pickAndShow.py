def pickAndShow():
  myPicFile = pickAFile()
  myPict = makePicture(myPicFile)
  show(myPict)
  mySoundFile = pickAFile()
  mySound = makeSound(mySoundFile)
  play(mySound)
