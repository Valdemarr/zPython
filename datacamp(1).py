# helpdocs
# https://github.com/wblakecannon/DataCamp/tree/master/01-intro-to-python-for-data-science/4-numpy
# https://github.com/datacamp/courses-introduction-to-python/blob/master/chapter4.md
# CHAP 3, EX 7

# Create list areas
import numpy as np
import math
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# CHAP 3, EX 8
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

# CHAP 3, EX 10

# Definition of radius
r = 0.43

# Import the math package

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# CHAP 3, EX 11
# Definition of radius
r = 192500

# Import radians function of math package

# Travel distance of Moon over 12 degrees. Store in dist.
phi = math.radians(12)
dist = r*phi

# Print out dist
print("Distance: "+str(dist))

# CHAP 4, EX 2
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# CHAP 4, EX 3
# height is available as a regular list
height_in = [72, 69, 77, 73, 74, 72, 73, 70, 69, 68]
# Import numpy

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in*0.0254

# Print np_height_m
print(np_height_m)

# CHAP 4, EX 4
# height and weight are available as regular lists
weight_lb = [180, 172, 192, 222, 186, 189, 190, 192, 202, 224]
# Import numpy

# Create array from height_in with metric units: np_height_m

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)

# CHAP 4, EX 5
# height and weight are available as a regular lists

# Import numpy


# Calculate the BMI: bmi


# Create the light array
light = np.array(bmi < 25)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# CHAP 4, EX 6
print(np.array([True, 1, 2]) + np.array([3, 4, False]))
# somehow ==
print(np.array([4, 3, 0]) + np.array([0, 2, 2]))

# CHAP 4, EX 7

# height and weight are available as a regular lists

# Import numpy


# Store weight and height lists as numpy arrays

# Print out the weight at index 50, but cant befausen ot 50 samples
print(np_weight_kg[5])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_m[5:9])

# CHAP 4, EX 8
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-4-numpy?ex=9
