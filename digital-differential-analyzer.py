pt1 = list()
pt2 = list()

print("Enter x1,y1 and x2,y2:")

for i in range(0,4):
    if i < 2:
        pt1.append(int(input()))
    else:
        pt2.append(int(input()))

x1,y1 = pt1[0],pt1[1]
x2,y2 = pt2[0],pt2[1]

#print("(x1,y1) = (" + str(x1) + "," + str(y1) + ")")
#print("(x2,y2) = (" + str(x2) + "," + str(y2) + ")")

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
    i += 1

soln_table["x"] = pixels_x
soln_table["y"] = pixels_y

print(soln_table)

