# This is the Question 

# memory limit per test256 megabytes
# A 10×10 target is made out of five "rings" as shown. Each ring has a different point value: the outermost ring — 1 point, the next ring — 2 points, ..., the center ring — 5 points.
# Vlad fired several arrows at the target. Help him determine how many points he got.

# Input
# The input consists of multiple test cases. The first line of the input contains a single integer t(1≤𝑡≤1000) — the number of test cases.
# Each test case consists of 10 lines, each containing 10 characters. Each character in the grid is either 𝚇(representing an arrow) or .(representing no arrow).

# Output
# For each test case, output a single integer — the total number of points of the arrows.

# Example
  
# Input 
# 4
# X.........
# ..........
# .......X..
# .....X....
# ......X...
# ..........
# .........X
# ..X.......
# ..........
# .........X
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ....X.....
# ..........
# ..........
# ..........
# ..........
# ..........
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX
# XXXXXXXXXX

# Output
# 17
# 0
# 5
# 220


# This is the Code

def hi():
    l=[]
    count=0
    for i in range(10):    #input
        a=input()
        if i==0 or i==9: 
            for i in range(10):
                if a[i]=='X':
                    count+=1
        elif i==1 or i==8:
            for i in range(10):
                if a[i]=='X':
                    if (i==0 or i==9):
                        count+=1
                    else:
                        count+=2
        elif i==2 or i==7:
            for i in range(10):
                if a[i]=='X' :
                    if (i==0 or i==9):
                        count+=1
                    elif (i==1 or i==8):
                        count+=2
                    else:
                        count+=3
        elif i==3 or i==6:
            for i in range(10):
                if a[i]=='X' :
                    if (i==0 or i==9):
                        count+=1
                    elif (i==1 or i==8):
                        count+=2
                    elif i==2 or i==7:
                        count+=3 
                    else:
                        count+=4
        elif i==4 or i==5:
            for i in range(10):
                if a[i]=='X' :
                    if (i==0 or i==9):
                        count+=1
                    elif (i==1 or i==8):
                        count+=2
                    elif i==2 or i==7:
                        count+=3 
                    elif i==3 or i==6:
                        count+=4
                    else:
                        count+=5
    print(count)
for i in range(int(input())):
    hi()
