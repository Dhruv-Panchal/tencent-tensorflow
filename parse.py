import json
from pprint import pprint
from PIL import Image
import os

with open('annotations.json') as f:
    x = f.read()
    data = json.loads(x)

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)

count = 0

for p in [data['imgs']]:
    for q in [p.items()]:
        imglen = int(len(q))
        for v in range(imglen):
            for r in [q[v]]: # image name iterator
                for s in [r[1]]:
                    print ("***********"),("Image Path: ") ,(s['path'])
                    for t in [s['objects']]:
                        objlen=int(len(t))
                        for i in range(objlen):
                            for u in [t[i]]:
                                filename = 'cropped1/'+u['category']
                                if not os.path.exists(filename):
                                    os.makedirs(filename)
                                crop(s['path'], (u["bbox"]['xmin'], u["bbox"]\
                                ['ymin'],u["bbox"]['xmax'],u["bbox"]['ymax']),\
                                 'cropped1/'+u['category']+'/'+str(s['id'])+'.jpg')
