import json
from pprint import pprint

with open('annotations.json') as f:
    x = f.read()
    data = json.loads(x)


for p in [data['imgs']]:
    for q in [p.items()]:
        print ("images"),(q[2][0])
        imglen = int(len(q)) # finds list length of 'imgs' list
        print ("imglen"),(imglen)
        for v in range(imglen):
            for r in [q[v]]: # image name iterator
                #print ("images"),(r[0])

                for s in [r[1]]:
                    #print("***********"), ("Path: "),(s['path'])
                    print ("***********"),("Image name: ") ,(s['id'])
                    for t in [s['objects']]:
                        objlen=int(len(t))
                        #print (objlen)
                        for i in range(objlen):
                            for u in [t[i]]:

                                '''print ("***********"), ("Category: "),(u['category'])
                                print ("Xmin: "),(u["bbox"]['xmin'])
                                print ("Ymin: "),(u["bbox"]['ymin'])
                                print ("Xmax: "),(u["bbox"]['xmax'])
                                print ("Ymax: "),(u["bbox"]['ymax'])'''
