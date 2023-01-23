# code to read text file
# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
from shapely.geometry import Polygon


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
    if(polygonArea(vertices1,len(vertices1))==polygonArea(vertices2,len(vertices2))):
        return True
    return poly1.equals(poly2)

with open("D:\KLA\main\Milestone_Input\Milestone 3\POI.txt") as f:
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
                poly_cnt += 1
                start = False
vertices_POI = vertices
with open("output3.txt", "w") as f:
    f.write("header 600\n")
    f.write("bgnlib 1/19/2023 19:25:24 1/19/2023 19:25:24\n")
    f.write("libname egdslib\n")
    f.write("units 0.0001 1e-10\n")
    f.write("\n")
    f.write("bgnstr 1/19/2023 19:25:24 1/19/2023 19:25:24\n")
    f.write("strname top\n\n")
with open("D:\KLA\main\Milestone_Input\Milestone 3\Source.txt") as f:
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
                
                if(check_polygon_identity(vertices_POI, vertices)):
                    print(vertices)
                    with open("output3.txt", "a") as f:
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
