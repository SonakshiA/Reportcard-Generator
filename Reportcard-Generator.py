#%%
import cv2
import csv
import os
from PIL import Image
 
img=cv2.imread('template.jpg',1) #result template
img_resized=cv2.resize(img,(550,750)) #making image smaller

font=cv2.FONT_HERSHEY_SIMPLEX
fontSize=0.5
fontColor=(0,0,0) #Black

#Student data is saved in a csv file
with open('Grades.csv',encoding='utf-8-sig')as file:
   csv_rows = csv.reader(file)
   for row in csv_rows:
    img=cv2.imread('template.jpg',1)
    img_resized=cv2.resize(img,(550,750)) #making image smaller
    cv2.putText(img_resized,row[0],(110,160),font,fontSize,fontColor)
    cv2.putText(img_resized,row[1],(110,190),font,fontSize,fontColor)
    cv2.putText(img_resized,row[2],(450,300),font,fontSize,fontColor)
    cv2.putText(img_resized,row[3],(450,330),font,fontSize,fontColor)
    cv2.putText(img_resized,row[4],(450,360),font,fontSize,fontColor)
    cv2.putText(img_resized,row[5],(450,390),font,fontSize,fontColor)
    cv2.putText(img_resized,row[6],(450,455),font,fontSize,fontColor)
    cv2.putText(img_resized,row[7],(450,485),font,fontSize,fontColor)
    cv2.putText(img_resized,row[8],(450,515),font,fontSize,fontColor)
    cv2.putText(img_resized,row[9],(450,550),font,fontSize,fontColor)
    cv2.putText(img_resized,row[10],(280,670),font,fontSize,fontColor)
    cv2.imshow('result',img_resized)
    filename=(row[0].split())[0]+'.jpg' #filename should be the first name of the student
    cv2.imwrite(filename, img_resized) #saving the image
    result=Image.open(filename)
    pdfName=(row[0].split())[0]+'.pdf'
    result.save(r'C:\Users\ar_so\Results\{}'.format(pdfName))
    os.remove(filename) #removes the jpg file to avoid crowding
    cv2.waitKey(0)
#%%