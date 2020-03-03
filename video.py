import imageio
from os import listdir
from PIL import Image, ImageOps


images = []
video = []


for filename in sorted(listdir('images/eps'))[:121]:
	img = Image.open('images/eps/' + filename)
	img = ImageOps.invert(img)
	img.save('images/png/' + filename.replace('eps', 'png'), 'png') 
	images.append(imageio.imread('images/png/' + filename.replace('eps', 'png')))
video = images[::-1] + images


images = []


for filename in sorted(listdir('images/deconstruct')):
	img = Image.open('images/deconstruct/' + filename)
	img = ImageOps.invert(img)
	img.save('images/deconstruct_png/' + filename.replace('eps', 'png'), 'png') 
	images.append(imageio.imread('images/deconstruct_png/' + filename.replace('eps', 'png')))
video = images + video + images[::-1]
#imageio.mimsave('sierpinski_deconstruct.gif', images[1:-1] + images[::-1])


#imageio.mimsave('sierpinski_short.gif', images[1:-1] + images[::-1])
imageio.mimsave('sierpinski_morph.gif', video)
