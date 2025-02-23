def posterize(image, rgb):
    
	white = (255, 255, 255)
 
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(r, g, b) = image.getPixel(x, y)
			average = (r + g + b) // 3
		
  
			if average < 128:
				image.setPixel(x, y, rgb)
			else:
				image.setPixel(x, y, white)
