import pandas as pd

pts = list()

# Input four co-ordinates
print("Enter x1,y1 and x2,y2:")
while(len(pts) != 4):
    pts = input().split()
    if len(pts) != 4:
        print("Enter 4 points : x1 y1 x2 y2")
        print("Ex. 0 0 5 5")

x1,y1 = int(pts[0]),int(pts[1])
x2,y2 = int(pts[2]),int(pts[3])

soln_table = {"i" : [],
              "setpixel" : [],
              "x" : [],
              "y" : []
              }

if abs(x2-x1) >= abs(y2-y1):
    length = abs(x2-x1)
else:
    length = abs(y2-y1)

del_x = (x2-x1)/length
del_y = (y2-y1)/length

x = x1 + 0.5
y = y1 + 0.5

pixels_x,pixels_y = list(),list()

i = 1 
while i <= length:
    pixels_x.append(x)
    pixels_y.append(y)
    soln_table["i"].append(i)
    soln_table["setpixel"].append((int(x),int(y)))
    x += del_x
    y += del_y
    if i == length:
        pixels_x.append(x)
        pixels_y.append(y)
    i += 1

soln_table["x"] = pixels_x
soln_table["y"] = pixels_y

for i in range(0,length*2+1):
    if i%2 == 0:
        soln_table["i"].insert(i,"")
        soln_table["setpixel"].insert(i, "")
    else:
        soln_table["x"].insert(i,"")
        soln_table["y"].insert(i, "")

framed_soln_table = pd.DataFrame(soln_table)
print(framed_soln_table)
