import numpy as np
from scipy.optimize import brentq

# # # Task 6

class Circle:
    def __init__(self, x,y, radius):
            self.radius = radius
            self.x = x
            self.y = y

    def area(self):
        return np.pi * pow(self.radius,2)


def distance_centres (x1, y1, x2, y2, z1=0, z2=0):
    return pow(pow(x2-x1, 2)+ pow(y2-y1, 2) +pow(z2-z1,2), 0.5)

def circles_intersection_area(dist, r1, r2):

    if dist <= np.abs(r2-r1):
        
        return np.pi * min(r1, r2)**2
    elif dist >= r2 + r1:
        
        return 0
    else:
        r1_square, r2_square, dist_square = r1**2, r2**2, dist**2 
        alpha = np.arccos((dist_square + r1_square - r2_square) / (2*dist*r1)) 
        beta = np.arccos((dist_square - r1_square + r2_square) / (2*dist*r2))
        return  r1_square * alpha + r2_square * beta - 0.5 * (r1_square * np.sin(2*alpha) + r2_square * np.sin(2*beta))

def intersection_area(circles):
    area = 0
    for i in range(len(circles) - 1):
        distance = distance_centres(circles[i].x, circles[i].y, circles[i+1].x, circles[i+1].y)
        area += circles_intersection_area(distance,circles[i].radius, circles[i+1].radius)
        return area

circles = []
number_of_circles = int(input("Enter number of circles: "))


for i in range(number_of_circles):
    print("Circle {}" .format(i+1))
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    radius = int(input("Enter radius: "))
    circles.append(Circle(x,y,radius))

print("Circle intersection area: {} " .format(round(intersection_area(circles),3)))



# Task 7
#creating sphere class
class Sphere(Circle):
    def __init__(self, x,y,z,radius):
        super().__init__(x,y,radius)
        self.z = z

    def volume(self):
        return np.pi *( 4 / 3 ) * pow(self.radius, 3)

def spheres_intesection_volume(distance, radius1,radius2):
    if distance <= np.abs(radius2 - radius1):
        return np.pi * (4/3) * pow(min(radius1,radius2),3)
    elif distance >= radius1 +radius2:
        return 0
    else:
        return (np.pi * pow((radius2 +radius1-distance),2)* (pow(distance,2) +(2 * distance*radius2-3* pow(radius2,2)+2*distance*radius1-3*pow(radius1,2)) + 6* radius2*radius1)) / (12*distance)

def intersection_volume(spheres):
    volume = 0
    for i in range(len(spheres)-1):
        distance = distance_centres(spheres[i].x,spheres[i].y,spheres[i+1].x,spheres[i+1].y,spheres[i].z,spheres[i+1].z)
        volume += spheres_intesection_volume(distance, spheres[i].radius,spheres[i+1].radius)
    return volume

spheres = []
number_of_spheres = int(input("Enter number of spheres: "))

for i in range(number_of_spheres):
    print("Spheres {}" .format(i+1))
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    radius = int(input("Enter radius: "))
    spheres.append(Sphere(x,y,z,radius))

print("Sphere intersection area: {} " .format(round(intersection_volume(spheres), 3)))