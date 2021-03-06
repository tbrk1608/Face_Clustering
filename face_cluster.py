# -*- coding: utf-8 -*-
"""Face_cluster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PaffmNcufG5PUgOaU0L66cpNHmn-30jn

# Face Clustering
"""

# imports
from imutils import paths
import face_recognition
import pickle
import cv2
import os
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from imutils import build_montages
import numpy as np
from google.colab.patches import cv2_imshow # Since cv2.imshow is not supported on Google collab, we neet to do this import

imgs = list(paths.list_images("/content/drive/My Drive/facerecog/dataset"))
encodes_list = []
for img in imgs:
    image = cv2.imread(img)
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    locs = face_recognition.face_locations(rgb_img,model='cnn')
    encodings = face_recognition.face_encodings(rgb_img, locs)
    print(img.split(os.path.sep)[-1]+" ::: "+str(len(encodings))+ ' Face(s) found')
    d = [{"img_path": img, "loc": loc, "encoding": e} for (loc, e) in zip(locs, encodings)]
    encodes_list.extend(d)
    
# saving to pickle
outfile = "/content/drive/My Drive/facerecog/face_cluster_encodes_colab.pkl"
os.makedirs(os.path.dirname(outfile), exist_ok=True)
with open(outfile, 'wb') as f:
    pickle.dump(encodes_list, f)

pkl_path = "/content/drive/My Drive/facerecog/face_cluster_encodes_colab.pkl"
encodes_list = pickle.loads(open(pkl_path, "rb").read())
encodings = [d["encoding"] for d in encodes_list]
db_clt = DBSCAN(metric="euclidean", n_jobs=-1)
db_clt.fit(encodings)

unique_faces = np.unique(db_clt.labels_)
print("Unique Faces: ",len(unique_faces))
print("Known Faces:",len(np.where(unique_faces > -1)[0]))

for k,u_face in enumerate(unique_faces):
    if u_face == -1:
      k = "Unknown"
    print("Detected #{} Faces".format(k))
    matched_ids = np.where(db_clt.labels_ == u_face)[0]
    # [print(encodes_list[i]['img_path'].split(os.path.sep)[-1]) for i in matched_ids]
    print('\n')
    fig = plt.figure(figsize=(12,8))

    for n,i in enumerate(matched_ids):
        image = cv2.imread(encodes_list[i]["img_path"])
        (t,r,b,l) = encodes_list[i]["loc"]
        face = image[t:b,l:r]
        a = fig.add_subplot(3, np.ceil(len(matched_ids)/float(3)), n + 1)
        plt.axis('off')
        plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
    plt.show()

