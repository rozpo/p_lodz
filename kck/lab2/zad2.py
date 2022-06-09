from pathlib import Path
from PIL import Image, ImageOps
import os
path = Path('./index.html')
imglist = []

for file in os.listdir('.'):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        imglist.append(file)

if path.exists():
    os.remove('./index.html')
file = open('index.html','w')
stringfile = '<html>\n\t<head><title>wakacje2014</title></head>\n\t<body><h1>wakacje2014</h1>\n'

for i in range(len(imglist)):
    img = Image.open(imglist[i]).rotate(180).convert('L')
    img2 = ImageOps.fit(img, (128,128), Image.ANTIALIAS)
    img2.save('ico' + imglist[i])
    stringfile += '\t\t<a href="' + imglist[i] + '"><img src="ico' + imglist[i]+ '"></a>\n'
stringfile += '\t</body>\n</html>'
file.write(stringfile)