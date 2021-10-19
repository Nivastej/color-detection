






#Taking an image from the user:
#We will be using argparse library to create an argument parser.
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
#Reading image with opencv
Img = cv2.imread(img_path)
#Teaching the Colors:
#import colors.csv file to our program using read_csv method. Since the csv file we 
#downloaded  doesn’t  have  column  names,  I  will  be  defining  them  in  the  program. 
#This process is known as data manipulation.

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

The pandas library is very useful when we need to perform various operations on 
data files like CSV. pd.read_csv() reads the CSV file and loads it into the pandas 
Data Frame.

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)



#Mouse Click Function:
#A callback function which will be called when a mouse event happens.

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

#Calculating the RGB values of the double-clicked location:
#It will calculate the rgb values of the pixel which we double click. The function 
#parameters have the event name, (x,y) coordinates of the mouse position, etc. In 
#the function, we check if the event is double-clicked then we calculate and set the 
#r,g,b values along with x,y positions of the mouse.

def draw_function(event, x,y,flags,param):            
if event == cv2.EVENT_LBUTTONDBLCLK:        
global b,g,r,xpos,ypos, clicked        
clicked = True        
xpos = x        
ypos = y        
b,g,r = img[y,x]        
b = int(b)        
g = int(g)        
r = int(r)






#Calculate distance to get color name
#We have the r,g and b values.
#To get the color name, we calculate a distance(d) which tells us how close we are 
#to color and choose the one having minimum distance.

Distance =
d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)

#Display image on the window:
#Finally, when a mouse-click happens, it will update the color name and RGB values on 
#the screen. By using cv2.imshow(), we draw the image on the window. When the 
#user double clicks the window, we draw a rectangle and get the color name to 
#draw text on the window using cv2.rectangle and cv2.putText() functions.


#SOURCE CODE:

import cv2
import pandas as pd
num=int(input("1:temple\n2:F\n3:cmr\n"))
img_path  =r'C:/Users/ginugaripavan/OneDrive/Desktop/hindu-
temple-gopuram,2618304.jpg'
17



img = cv2.imread(img_path)

# declaring global variables (are used later on)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# function to calculate minimum distance from all colors and get 
the most matching color
def get_color_name(R, G, B):    
minimum = 10000    
for i in range(len(csv)):        
d  =  abs(R  - int(csv.loc[i,  "R"]))  +  abs(G  - int(csv.loc[i, 
"G"])) + abs(B - int(csv.loc[i, "B"]))        
if d <= minimum:            
minimum = d            
cname = csv.loc[i, "color_name"]
18



    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):    
if event == cv2.EVENT_LBUTTONDBLCLK:        
global b, g, r, x_pos, y_pos, clicked        
clicked = True        
x_pos = x        
y_pos = y       
b, g, r = img[y, x]        
b = int(b)        
g = int(g)        
r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
