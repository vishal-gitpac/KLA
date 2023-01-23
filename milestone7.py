# code to read text file
# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
from shapely.geometry import Polygon
import math

def convert(list):
    return tuple(list)

def polygonArea(vertices, n):
 
    # Initialize area
    area = 0.0
 
    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0,n):
        area += (vertices[j][0] + vertices[i][0]) * (vertices[j][1] - vertices[i][1])
        j = i   # j is previous vertex to i
     
 
    # Return absolute value
    return int(abs(area / 2.0))    

def check_polygon_identity(vertices1, vertices2):
    #print(type(vertices1))
    poly1 = Polygon(vertices1)
    poly2 = Polygon(vertices2)
    #print(line1.equals(line2))
    lengths1 = []
    lengths2 = []
    for i in range(len(vertices1)):
        lengths1.append(
            math.dist(
                vertices1[i % (len(vertices1))], vertices1[(i + 1) % (len(vertices1))]
            )
        )
    for i in range(len(vertices2)):
        lengths2.append(
            math.dist(
                vertices2[i % (len(vertices2))], vertices2[(i + 1) % (len(vertices2))]
            )
        )
    # print(lengths1[0])
    # print(lengths2[0])
    check = True
    if len(lengths1)!=len(lengths2):
        return False
        
    lengths1.sort() 
    lengths2.sort()
    if(lengths1==lengths2):
        return True
    else:
        for i in range(len(lengths1)):
            if(lengths2[i]%lengths1[i]!=0 and lengths1[i]%lengths2[i]!=0):
                check=False
        return False        
    for i in range(len(lengths1)):
        if lengths1[i] != lengths2[i]:
            check = False
    if check == False:
        return False
    xor=1    
    for i in range(len(lengths1)):
        xor^=(int(lengths1[i])^int(lengths2[i]))
    if xor==0:
        return True    
    if(polygonArea(vertices1,len(vertices1))==polygonArea(vertices2,len(vertices2))):
        return True
    return poly1.equals(poly2)

vertices_POI=[]
with open("D:\KLA\main\Milestone_Input\Milestone 7\POI.txt") as f:
    lines = f.readlines()
    start = False
    poly_cnt = 1
    for line in lines:
        if line == lines[8]:
            if poly_cnt < 3:
                start = True
        if start:
            # print(line)
            if line[:2] == "xy":
                no_of_vertices = int(line[4:5])
                # print(no_of_vertices)
                vertices = []
                """for vertice_num in range(no_of_vertices): 
                    ver1_st=vertice_num*9+7
                    ver2_st=vertice_num*9+13
                    if(line[ver1_st]=='-'):
                        vertices.append((-int(line[ver1_st+1:ver1_st+5]),int(line[ver2_st+1:ver2_st+5])))
                    elif(line[ver2_st]=='-'):    
                        vertices.append((int(line[ver1_st+1:ver1_st+5]),-int(line[ver2_st:ver2_st+4])))
                    else:
                        vertices.append((int(line[ver1_st:ver1_st+4]),int(line[ver2_st:ver2_st+4])))"""
                digit = True
                number = ""
                neg = False
                count = 1
                vertice = []
                vertices = []
                first_num = True
                for st in line:
                    if st == "-":
                        neg = True
                    if st.isdigit():
                        number += st
                        if first_num:

                            number = ""
                            first_num = False
                    else:
                        if neg and number != "":
                            # print(int(number))
                            if count < 3:
                                vertice.append(-int(number))
                                count += 1
                            else:
                                vertices.append(convert(vertice))
                                # print(vertices)
                                count = 1
                                vertice = []
                                vertice.append(-int(number))
                                count+=1
                            neg = False    
                        elif number != "":
                            # print(int(number))
                            if count < 3:
                                vertice.append(int(number))
                                count += 1
                            else:
                                vertices.append(convert(vertice))
                                # print(vertices)
                                count = 1
                                vertice = []
                                vertice.append(int(number))
                                count += 1
                        number = ""
                        digit = False
                vertices_POI.append(vertices)                
                poly_cnt += 1
                start = False
vertices_POI1 = vertices_POI[0]
vertices_POI2= vertices_POI[1]
print(vertices_POI1)
print(vertices_POI2)
with open("output7.txt", "w") as f:
    f.write("header 600\n")
    f.write("bgnlib 1/19/2023 19:25:24 1/19/2023 19:25:24\n")
    f.write("libname egdslib\n")
    f.write("units 0.0001 1e-10\n")
    f.write("\n")
    f.write("bgnstr 1/19/2023 19:25:24 1/19/2023 19:25:24\n")
    f.write("strname top\n\n")
with open("D:\KLA\main\Milestone_Input\Milestone 7\Source.txt") as f:
    lines = f.readlines()
    start = False
    poly_cnt = 1
    for line in lines:
        if line == lines[8]:
            start = True
        if start:
            # print(line)
            if line[:2] == "xy":
                no_of_vertices = int(line[4:5])
                # print(no_of_vertices)
                vertices = []
                """for vertice_num in range(no_of_vertices): 
                    ver1_st=vertice_num*9+7
                    ver2_st=vertice_num*9+13
                    if(line[ver1_st]=='-'):
                        vertices.append((-int(line[ver1_st+1:ver1_st+5]),int(line[ver2_st+1:ver2_st+5])))
                    elif(line[ver2_st]=='-'):    
                        vertices.append((int(line[ver1_st+1:ver1_st+5]),-int(line[ver2_st:ver2_st+4])))
                    else:
                        vertices.append((int(line[ver1_st:ver1_st+4]),int(line[ver2_st:ver2_st+4])))"""
                digit = True
                number = ""
                neg = False
                count = 1
                vertice = []
                vertices = []
                first_num = True
                for st in line:
                    if st == "-":
                        neg = True
                    if st.isdigit():
                        number += st
                        if first_num:

                            number = ""
                            first_num = False
                    else:
                        if neg and number != "":
                            # print(int(number))
                            if count < 3:
                                vertice.append(-int(number))
                                count += 1
                            else:
                                vertices.append(convert(vertice))
                                # print(vertices)
                                count = 1
                                vertice = []
                                vertice.append(-int(number))
                                count+=1
                            neg = False    
                        elif number != "":
                            # print(int(number))
                            if count < 3:
                                vertice.append(int(number))
                                count += 1
                            else:
                                vertices.append(convert(vertice))
                                # print(vertices)
                                count = 1
                                vertice = []
                                vertice.append(int(number))
                                count += 1
                        number = ""
                        digit = False
                
                if(check_polygon_identity(vertices_POI1, vertices)):
                    print(vertices)
                    with open("output7.txt", "a") as f:
                        f.write("boundary\nlayer 1\ndatatype 0\n")
                        f.write("xy "+str(no_of_vertices)+" ")
                        for vrs in vertices:
                            for vr in vrs:
                                f.write(str(vr)+" ")
                        for vr in vertices[0]:
                            f.write(str(vr)+" ")
                        f.write("\nendel\n")    
                if(check_polygon_identity(vertices_POI2, vertices)):
                    with open("output7.txt", "a") as f:
                        f.write("boundary\nlayer 1\ndatatype 0\n")
                        f.write("xy "+str(no_of_vertices)+" ")
                        for vrs in vertices:
                            for vr in vrs:
                                f.write(str(vr)+" ")
                        for vr in vertices[0]:
                            f.write(str(vr)+" ")
                        f.write("\nendel\n")         
                poly_cnt += 1
                start = False
