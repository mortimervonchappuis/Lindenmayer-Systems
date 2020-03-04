import imageio
from os import listdir
from PIL import Image, ImageOps


images = []
video = []


def to_png(path):
	img = Image.open('images/eps/' + path)
	img = ImageOps.invert(img)
	img.save('images/png/' + path.replace('eps', 'png'), 'png') 
	images.append(imageio.imread('images/png/' + path.replace('eps', 'png')))



#for filename in sorted(listdir('images/eps'))[:121] if 'sierpinski' in filename:
#	img = Image.open('images/eps/' + filename)
#	img = ImageOps.invert(img)
#	img.save('images/png/' + filename.replace('eps', 'png'), 'png') 
#	images.append(imageio.imread('images/png/' + filename.replace('eps', 'png')))
#video = images[::-1]



for filename in sorted(listdir('images/deconstruct_png')):
	images.append(imageio.imread('images/deconstruct_png/' + filename))

video += images
images = []


for filename in list(filter(lambda x: 'sierpinski' in x,sorted(listdir('images/png'))))[:121]:
	images.append(imageio.imread('images/png/' + filename))

video += images[::-1]
images = []
#for filename in sorted(listdir('images/deconstruct')):
#	img = Image.open('images/deconstruct/' + filename)
#	img = ImageOps.invert(img)
#	img.save('images/deconstruct_png/' + filename.replace('eps', 'png'), 'png') 
#	images.append(imageio.imread('images/deconstruct_png/' + filename.replace('eps', 'png')))
#video += images[::-1]
#imageio.mimsave('sierpinski_deconstruct.gif', images[1:-1] + images[::-1])

for filename in sorted(filter(lambda x: 'hollunder' in x, listdir('images/png')), key=lambda x: int(x.replace('hollunder_', '').replace('.png', ''))):
	images.append(imageio.imread('images/png/' + filename))

video += images
images = []

for filename in sorted(filter(lambda x: 'levy' in x, listdir('images/png')), key=lambda x: int(x.replace('levy', '').replace('_', '').replace('.png', ''))):
	images.append(imageio.imread('images/png/' + filename))

video += images[::-1]
images = []

#imageio.mimsave('sierpinski_short.gif', images[1:-1] + images[::-1])
imageio.mimsave('morph.gif', video, fps=60)
