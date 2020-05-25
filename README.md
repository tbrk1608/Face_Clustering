## Face Clustering:

This is a simple Python script which uses the images from /dataset directory and generates the output feature vector is 128-d (i.e., a list of 128 real-valued numbers) that is used to quantify the face then group the similar faces together.

Here the /dataset directory contains images (20 each) of 5 Indian Cricketers: Dravid, Ganguly, MS Dhoni, Sachin Tendulkar and Virat Kohli.

1. face_cluster.py : Detects similar faces from given directoy and show them together
2. face_cluster_encodes_colab.pkl : pickle file containing the encodings of images in /dataset

**Sample output:**

![Unknown](https://github.com/tbrk1608/Face_Clustering/blob/master/unknown.png?raw=true)
![First](https://github.com/tbrk1608/Face_Clustering/blob/master/first.png?raw=true)
![Second](https://github.com/tbrk1608/Face_Clustering/blob/master/second.png?raw=true)
![Third](https://github.com/tbrk1608/Face_Clustering/blob/master/third.png?raw=true)
![Fourth](https://github.com/tbrk1608/Face_Clustering/blob/master/fourth.png?raw=true)
![Fifth](https://github.com/tbrk1608/Face_Clustering/blob/master/fifth.png?raw=true)

*(/dataset Images source: Google Images)*

*Thanks to Adrian Rosebrock from https://www.pyimagesearch.com/*

*Link : https://www.pyimagesearch.com/2018/07/09/face-clustering-with-python/*
