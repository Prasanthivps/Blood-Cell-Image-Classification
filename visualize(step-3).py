#!/bin/python
"""generate labeled img like example.jpg"""

import xml.etree.ElementTree as ET
import cv2
filename=""

    
def ytd():
   
    from tkinter.filedialog import askopenfilename
    global filename
    filename= askopenfilename()
    myname=filename
    

from tkinter import *
import tkinter as tk
root=tk.Tk()
root.geometry('1000x1000')
w=tk.Label(root,text="Combining Convolutional Neural Network With Recursive Neural Network for Blood  Cell Image Classification",fg = "red",font = "Helvetica 19 bold italic")
w.pack()
btn=Button(root, text='import image',bd='5',command=root.destroy)
btn.pack(side='top')
btn.pack()
btn.config(command=ytd)
root.mainloop()
colan='"'
myname=colan+filename+colan
print(myname)

image = cv2.imread("C:/Users/PRASANTHI/Desktop/term project/BCCD_Dataset-master/BCCD/JPEGImages/BloodImage_00014.jpg")
#image=cv2.imread(myname)


tree = ET.parse("C:/Users/PRASANTHI/Desktop/term project/BCCD_Dataset-master/BCCD/Annotations/BloodImage_00014.xml")
for elem in tree.iter():
	if 'object' in elem.tag or 'part' in elem.tag:
		for attr in list(elem):
			if 'name' in attr.tag:
				name = attr.text
			if 'bndbox' in attr.tag:
				for dim in list(attr):
					if 'xmin' in dim.tag:
						xmin = int(round(float(dim.text)))
					if 'ymin' in dim.tag:
						ymin = int(round(float(dim.text)))
					if 'xmax' in dim.tag:
						xmax = int(round(float(dim.text)))
					if 'ymax' in dim.tag:
						ymax = int(round(float(dim.text)))
				if name[0] == "R":
					cv2.rectangle(image, (xmin, ymin),
								(xmax, ymax), (0, 255, 0), 1)
					cv2.putText(image, name, (xmin + 10, ymin + 15),cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * image.shape[0], (0, 255, 0), 1)
				if name[0] == "W":
					cv2.rectangle(image, (xmin, ymin),
								(xmax, ymax), (0, 0, 255), 1)
					cv2.putText(image, name, (xmin + 10, ymin + 15),
							cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * image.shape[0], (0, 0, 255), 1)
				if name[0] == "P":
					cv2.rectangle(image, (xmin, ymin),
								(xmax, ymax), (255, 0, 0), 1)
					cv2.putText(image, name, (xmin + 10, ymin + 15),
							cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * image.shape[0], (255, 0, 0), 1)

cv2.imshow("test", image)
cv2.imwrite("test.jpg", image)
cv2.waitKey()
