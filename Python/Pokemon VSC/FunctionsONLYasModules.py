import math
def read_file(file_name):
    with open(file_name, 'r') as file:
        WordList = [line.strip() for line in file.readlines()]
    return WordList


def  calculate_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) # (x2-x1)**2 + (y2-y1) **2



#  p1= [x1, y1] and p2 = [x2, y2]