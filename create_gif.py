import imageio.v3 as iio

codedexpython = ['gatto1.png', 'gatto2.png']
images = [ ]

for filename in codedexpython:
  images.append(iio.imread(filename))

iio.imwrite('gatto.gif', images, duration = 300, loop = 0)