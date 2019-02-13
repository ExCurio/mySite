    
# Function that takes two different sound files and splices them together to make a single sound file.
def spliceSounds():
  print "Select the first wav sound file: "  # Prompts the user for the first sound file.
  firstFile = pickAFile()  # Select the first sound file.
  print "Select the second wav sound file: "  # Prompts the user for the second sound file.
  secondFile = pickAFile()  # Select the second sound file.
  firstSound = makeSound(firstFile)  # Load the first sound file into memory.
  secondSound = makeSound(secondFile)  # Load the second sound file into memory.
  splicedSound = makeEmptySoundBySeconds(5, 22050)  # Create an empty sound file, 5 secs long, at a sampling rate of 22,050, to hold the new, spliced sound file.
  
  print "The first file Sampling Rate is ", getSamplingRate(firstSound)  # Prints to the console the sampling rate of the first sound file.
  print "The second file Sampling Rate is ", getSamplingRate(secondSound)  # Prints to the console the sampling rate of the second sound file.
  
  # For loop that iterates through the firstSound file and secondSound file and makes the splicedSound file equal to the two sound files.
  for i in range(0, 40000):  # For loop that will iterate through the code 40,000 times, incrementing the index (i) by 1 each time.
    firstSample = getSampleValueAt(firstSound, i)  # Get sample of first sound file at index = i
    secondSample = getSampleValueAt(secondSound, i)  # Get sample of second sound file at index = i
    splicedSample = firstSample + secondSample * 10  # splice together the two samples into a sample called splicedSample, increasing the volume of secondSample.
    setSampleValueAt(splicedSound, i, splicedSample)  # splice together the splicedSamples into the splicedSound file at index = i.
    

  play(splicedSound)  # Play the splicedSound file for the user to hear.
  return splicedSound  # Returns to the console total number of samples of the splicedSound file.

    