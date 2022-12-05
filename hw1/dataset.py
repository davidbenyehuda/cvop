import os
import numpy as np
import cv2
import pandas as pd
LABELS=[""]
VIDEO_PATH="hw1/videos/"
DATASET_PATH="hw1/HW1_dataset/"

def get_images_names(name):
    """
    return a list of all the flie names in a given name (train or valid or test) 
    """
    with open(DATASET_PATH+name+".txt", "r") as f: #get classes
        text=f.readlines()
        return[t[:-5] for t in text ]
    return []

def get_file_labels(filename):
    """
    return a list of all the image objects: [label_index, xcenter, ycenter, w, h] in a given file 
    """
    with open("{0}bboxes_labels/{1}.txt".format(DATASET_PATH,filename), "r") as f: #get classes
        text=f.readlines()
        return[[int(v) if len(v)==1 else np.double(v) for v in t[:-2].split() ] for t in text ]#get rid of \n
    return []
    
    
def create_df(filename,with_image_names=False):
    """
    return a pandas df with ["ImgName","image","boxes"] from train or valid or test with image boxes and img values 
    where ImgName is the name of the image and is optional 
    """
    #df=pd.DataFrame(columns =['image',"objects"])

    data=[]
    names=get_images_names(filename)
    for name in names:
        im=cv2.imread("{0}images/{1}.jpg".format(DATASET_PATH,name))
        pred=get_file_labels(name)
        data.append([im,pred])
    df=pd.DataFrame(data,columns =['image',"boxes"])
    if with_image_names:
        df["ImgName"]=names
    return df

        
        
        
    
def create_labels():
    with open(DATASET_PATH+"classes.names", "r") as f: #get classes
        text=f.readlines()
        LABELS+=[t[:-2] for t in text ]#get rid of \n

def main():
    df=create_df("train")
    print(x)
if __name__ == "__main__":
    main()