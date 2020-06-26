from PIL import Image

def Cropping(image, base="w", length=None, size=None):
	"""
	이미지를 잘라내기
	:param base: "w" or "h" or "n". w면 width는 고정이고, 상하만 선택한 길이만 제외하고 잘라냄.
	"""

	im = Image.open(image)
	print(im.size)
	
	if base=="w":

		if im.size[1] >= length:
			cropIm = im.crop((0,(im.size[1]-length)/2,im.size[0],im.size[1]-(im.size[1]-length)/2))
			cropIm.save(image[:-4]+"_cropped.png")
		else:
			print(im.size)

	elif base == "h":

		if im.size[0] >= length:
			cropIm = im.crop(((im.size[0]-length)/2,0,im.size[0]-(im.size[0]-length)/2, im.size[1]))

			cropIm.save(image[:-4]+"_cropped.png")
		else:
			print(im.size)

	elif base== "n":
		cropIm = im.crop(size)
		cropIm.save(image[:-4]+"_cropped.png")

	else:

		print("Please set up cropping rule")
		raise AttributeError





def Resizing(image, width=None, height=None, ratio=True, basewidth = None, baseheight=None):


	im = Image.open(p)
	print("Image Size : ", im.size)

	if ratio == True:
		if (basewidth != None)&(baseheight==None):

			wpercent = basewidth/float(im.size[0])
			hsize = int(float(im.size[1])*float(wpercent))
			im2 = im.resize((basewidth, hsize))
			im2.save(image[:-4]+"_resized.png")
		
		elif (basewidth == None)&(baseheight!=None):

			hpercent = baseheight/float(im.size[1])
			wsize = int(float(im.size[0])*float(hpercent))
			im2 = im.resize((wsize, baseheight))
			im2.save(image[:-4]+"_resized.png")
		
		else:
			print("Please set up basewidth or baseheight")
			raise AttributeError

	else:
		im2 = im.resize((width, height))
		im2.save(image[:-4]+"_resized.png")





if __name__ == '__main__':
	path = "D://4.기획/2. 홈페이지개비/홈페이지 디자인/20. Resin 시장가격 예측"


	filename = input("Enter the name of file: ")

	p = path+"/"+filename


	try:

		Resizing(p, basewidth=600, baseheight=None)
		Cropping(p[:-4]+"_resized.png", base="w", length=450)


	except UnboundLocalError:


		Resizing(p, basewidth=None, baseheight=450)
		Cropping(p[:-4]+"_resized.png", base="h", length=600)
