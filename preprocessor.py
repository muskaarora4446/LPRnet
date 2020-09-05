'''
created:31-08-2020
Author:https://github.com/bernard0047
'''
import os
import shutil
import pandas as pd
import numpy as np
import cv2 as cv
from PIL import Image
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='parameters for dataset preprocessing')
    parser.add_argument('--input_dir', default="./Input/", help='Input path (contains imgfolder and label csv)')
    parser.add_argument('--output_dir', default="./images/", help='a folder containing train and test folders will be created here') #don't pass for easy training
    args = parser.parse_args()
    return args

def modify(root,label,ext):
    if os.path.exists(os.path.join(root,label+ext)):
        label = modify(root,label+'_',ext)
    return label

def preprocess():
    args = get_parser()
    idr = os.path.expanduser(args.input_dir)
    odr = os.path.expanduser(args.output_dir)
    if os.path.exists(odr):
        print("Error: Path exists")
        return
    else:
        os.mkdir(odr)
    #print(input_dir,output_dir)
    imgfolder,dfpath = None, None
    for item in os.listdir(idr):
        if os.path.isdir(os.path.join(idr,item)):
            imgfolder = os.path.join(idr,item)
        else:
            dfpath = os.path.join(idr,item)
    if dfpath[-3:]!="csv":
        df = pd.read_excel(dfpath)
    else:
        df = pd.read_csv(dfpath,encoding = "ISO-8859-1")
    df = df.astype(str)
    allFileNames = os.listdir(imgfolder)
    np.random.shuffle(allFileNames)
    train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                            [int(len(allFileNames)*0.9)])
    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Testing: ', len(test_FileNames))
    train_FileNames = [imgfolder+'/'+ name for name in train_FileNames.tolist()]
    test_FileNames = [imgfolder+'/' + name for name in test_FileNames.tolist()]
    os.makedirs(odr +'/train')
    os.makedirs(odr +'/test')
    for name in train_FileNames:
        shutil.copy(name, odr+"/train")
    for name in test_FileNames:
        shutil.copy(name, odr+"/test")
    count=0
    for dirs in os.listdir(odr):
        for img in os.listdir(os.path.join(odr+dirs)):
            ipath = os.path.join(odr,dirs,img)
            #img,_ = os.path.splitext(img) #uncomment this line if your dataset has imgname without label, if so, modify to accomodate imgname of type(int)
            _,ext = os.path.splitext(ipath)
            label = df[df.iloc[:,0]==img].iloc[0,1]
            label = ''.join(e for e in label if e.isalnum())
            tpath = os.path.join(odr,dirs,modify(os.path.join(odr+dirs),label,ext)+ext)
            if img not in df.iloc[:,0].tolist() or len(label)<4:
                count+=1
                print(f"Label not found Error: Discarding image:{img}")
                os.remove(ipath)
                continue

            os.rename(ipath,tpath)
    print(f"Discarded {count} images in total.")
            

if __name__ == "__main__":
    preprocess()