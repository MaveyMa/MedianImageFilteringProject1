#NAME: MAVEY MA
#DUE: FRIDAY, FEBRUARY 12, 2016
#CST205: AVNER, PROJECT 1, GROUP 7
#READS IN 9 PHOTOS AND REMOVES PESKY TOURIST, DISPLAYING A NEW CANVAS OF THE SCULPTURE.

#from pprint import pprint #PRETTY PRINT FOR PRETTY ARRAY
#HOW WIDE TAKES IN A PICTURE AND RETURNS AN INTEGER (WIDTH)
def howWide(photoYouChoose):
  width = getWidth(photoYouChoose)
  return width
   
#HOW HIGH TAKES IN A PICTURE AND RETURNS AN INTEGER (HEIGHT)
def howHigh(photoYouChoose):
  height = getHeight(photoYouChoose)
  return height
  
#SORTS LIST AND RETURNS MIDDLE ELEMENT
def medianOdd(myList):
  listLength = len(myList)
  sortedValues = sorted(myList)
  middleIndex = ((listLength+1)/2) - 1
  return sortedValues[middleIndex]

#ACCEPTS THREE RBG AND CREATES NEW COLOR
def makeNewColor(ohRed, ohGreen, ohBlue):
  newColor = makeColor(ohRed, ohGreen, ohBlue)
  return newColor

#CREATE AN ARRAY OF NINE PICTURES
pictures = []
folder = "/home/copypasta/CST205/MedianImageFiltering/Project1Images/Project1Images/"

pic1 = makePicture(folder + "1.png")
pictures.append(pic1)
pic2 = makePicture(folder + "2.png")
pictures.append(pic2)
pic3 = makePicture(folder + "3.png")
pictures.append(pic3)
pic4 = makePicture(folder + "4.png")
pictures.append(pic4)
pic5 = makePicture(folder + "5.png")
pictures.append(pic5)
pic6 = makePicture(folder + "6.png")
pictures.append(pic6)
pic7 = makePicture(folder + "7.png")
pictures.append(pic7)
pic8 = makePicture(folder + "8.png")
pictures.append(pic8)
pic9 = makePicture(folder + "9.png")
pictures.append(pic9)

#STORE OFFICIAL HEIGHT AND WIDTH.
officialWidth = howWide(pic1) #495
officialHeight = howHigh(pic1) #557

#LIST OF RGB TO STORE 
rojoPixList = []
verdePixList = []
azulPixList = []

#THIS IS THE FINAL CANVAS (CURRENTLY BLANK, WHITE)
finalPhoto = makeEmptyPicture(officialWidth, officialHeight)

#FOR LOOP THROUGH EACH WIDTH, HEIGHT (x,y) PIXEL
for x in range (0, officialWidth):
  for y in range (0, officialHeight):
    #FOR LOOP FOR EACH NINE PHOTOS
    for index in range(0,9):
      #GRAB A SINGLE PIXEL IN A PHOTO
      pixel = getPixel(pictures[index],x,y)
      
      #GET THE RGB VALUES OF THAT SINGLE PIXEL
      rojo = getRed(pixel)
      verde = getGreen(pixel)
      azul = getBlue(pixel)
      		
      #APPEND RGB TO RESPECTIVE LISTS
      rojoPixList.append(rojo)
      verdePixList.append(verde)
      azulPixList.append(azul)
      
      #SORTING INT VALUES FROM SMALLEST TO GREATEST 
      sorted(rojoPixList)
      sorted(verdePixList)
      sorted(azulPixList)
    #END NINE PHOTO FOR LOOP
    #NOW THAT LISTS ARE SORTED, FIND MEDIAN, GOOD PIXEL. OUTLIERS WILL BE THE BAD PIXELS.
    rePix = medianOdd(rojoPixList)
    grPix= medianOdd(verdePixList)
    blPix = medianOdd(azulPixList)
      
    #FINAL COLOR COMBINES ALL THE MEDIAN RGB VALUES.
    finalColor = makeNewColor(rePix, grPix, blPix)
      
    #FINAL PIXEL IS THE CURRENT PIXEL THAT NEEDS THE FINAL COLOR
    finalPixel = getPixel(finalPhoto,x,y)
  
    #DRAW YOUR MASTERPIECE.
    setColor(finalPixel, finalColor)

    #EMPTY OR RESET LISTS; NEED ROOM FOR NEXT PIXEL'S BAGGAGE, SO MOVE OUT!
    rojoPixList[:] = []
    verdePixList[:] = []
    azulPixList[:] = []
  #END Y LOOP
#END X LOOP

#PIECE OF CAKE.
show(finalPhoto)
  
  
  
  
