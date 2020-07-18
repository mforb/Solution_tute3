#
#   contigcheck.py
#
#   A program to check if two simple polygons (i.e. each consisting of just three unique
#   coordinates to make a triangle) are connected via a shared boundary
#   (i.e. topological contiguity)
#   Uses variables and user input.
#   *Further demonstrates use of the if...elif...else statement*
#
#   Author: Tony Moore
#
#   Date: July 2014
#   Updated for Python 3: July 2018
#

# First we'll use the input statement to enter the coordinates of our two polygons.

poly1pt1x = input("Please enter the x-coordinate of the first point of the first polygon: ")
poly1pt1y = input("Please enter the y-coordinate of the first point of the first polygon: ")
poly1pt2x = input("Please enter the x-coordinate of the second point of the first polygon: ")
poly1pt2y = input("Please enter the y-coordinate of the second point of the first polygon: ")
poly1pt3x = input("Please enter the x-coordinate of the third point of the first polygon: ")
poly1pt3y = input("Please enter the y-coordinate of the third point of the first polygon: ")
poly2pt1x = input("Please enter the x-coordinate of the first point of the second polygon: ")
poly2pt1y = input("Please enter the y-coordinate of the first point of the second polygon: ")
poly2pt2x = input("Please enter the x-coordinate of the second point of the second polygon: ")
poly2pt2y = input("Please enter the y-coordinate of the second point of the second polygon: ")
poly2pt3x = input("Please enter the x-coordinate of the third point of the second polygon: ")
poly2pt3y = input("Please enter the y-coordinate of the third point of the second polygon: ")

# This is the conditional statement which will assess contiguity of your two polygons.

if (poly1pt1x == poly2pt1x and poly1pt1y == poly2pt1y and poly1pt2x == poly2pt2x and poly1pt2y == poly2pt2y)or \
(poly1pt1x == poly2pt2x and poly1pt1y == poly2pt2y and poly1pt2x == poly2pt1x and poly1pt2y == poly2pt1y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt1x + ", " + poly1pt1y + ") and (" +
          poly1pt2x + ", " + poly1pt2y + ")")
elif (poly1pt1x == poly2pt2x and poly1pt1y == poly2pt2y and poly1pt2x == poly2pt3x and poly1pt2y == poly2pt3y)or \
(poly1pt1x == poly2pt3x and poly1pt1y == poly2pt3y and poly1pt2x == poly2pt2x and poly1pt2y == poly2pt2y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt1x + ", " + poly1pt1y + ") and (" +
          poly1pt2x + ", " + poly1pt2y + ")")
elif (poly1pt1x == poly2pt3x and poly1pt1y == poly2pt3y and poly1pt2x == poly2pt1x and poly1pt2y == poly2pt1y)or \
(poly1pt1x == poly2pt1x and poly1pt1y == poly2pt1y and poly1pt2x == poly2pt3x and poly1pt2y == poly2pt3y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt1x + ", " + poly1pt1y + ") and (" +
          poly1pt2x + ", " + poly1pt2y + ")")
elif (poly1pt2x == poly2pt1x and poly1pt2y == poly2pt1y and poly1pt3x == poly2pt2x and poly1pt3y == poly2pt2y)or \
(poly1pt2x == poly2pt2x and poly1pt2y == poly2pt2y and poly1pt3x == poly2pt1x and poly1pt3y == poly2pt1y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt2x + ", " + poly1pt2y + ") and (" +
          poly1pt3x + ", " + poly1pt3y + ")")
elif (poly1pt2x == poly2pt2x and poly1pt2y == poly2pt2y and poly1pt3x == poly2pt3x and poly1pt3y == poly2pt3y)or \
(poly1pt2x == poly2pt3x and poly1pt2y == poly2pt3y and poly1pt3x == poly2pt2x and poly1pt3y == poly2pt2y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt2x + ", " + poly1pt2y + ") and (" +
          poly1pt3x + ", " + poly1pt3y + ")")
elif (poly1pt2x == poly2pt3x and poly1pt2y == poly2pt3y and poly1pt3x == poly2pt1x and poly1pt3y == poly2pt1y)or \
(poly1pt2x == poly2pt1x and poly1pt2y == poly2pt1y and poly1pt3x == poly2pt3x and poly1pt3y == poly2pt3y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt2x + ", " + poly1pt2y + ") and (" +
          poly1pt3x + ", " + poly1pt3y + ")")
elif (poly1pt3x == poly2pt1x and poly1pt3y == poly2pt1y and poly1pt1x == poly2pt2x and poly1pt1y == poly2pt2y)or \
(poly1pt3x == poly2pt2x and poly1pt3y == poly2pt2y and poly1pt1x == poly2pt1x and poly1pt1y == poly2pt1y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt3x + ", " + poly1pt3y + ") and (" +
          poly1pt1x + ", " + poly1pt1y + ")")
elif (poly1pt3x == poly2pt2x and poly1pt3y == poly2pt2y and poly1pt1x == poly2pt3x and poly1pt1y == poly2pt3y)or \
(poly1pt3x == poly2pt3x and poly1pt3y == poly2pt3y and poly1pt1x == poly2pt2x and poly1pt1y == poly2pt2y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt3x + ", " + poly1pt3y + ") and (" +
          poly1pt1x + ", " + poly1pt1y + ")")
elif (poly1pt3x == poly2pt3x and poly1pt3y == poly2pt3y and poly1pt1x == poly2pt1x and poly1pt1y == poly2pt1y)or \
(poly1pt3x == poly2pt1x and poly1pt3y == poly2pt1y and poly1pt1x == poly2pt3x and poly1pt1y == poly2pt3y):
    print("The two polygons are contiguous along the line that connects (" +
          poly1pt3x + ", " + poly1pt3y + ") and (" +
          poly1pt1x + ", " + poly1pt1y + ")")
else:
    print("The polygons are not contiguous")

# Note the use of the 'and' to combine the results of four matches
# It means that both elements in two consecutive x-y coordinate pairs (i.e. a simple line) have to match
# with another similar set in the other polygon (in either direction, hence the use of 'or')

# Of course this only covers the minute percentage of polygons that are triangles (and look at all the code!!)
# For the kinds of polygons (i.e. real world shapes) that we usually encounter in GIS, we'll need loops
# to ease such repetitive tasks...

# ...and that's what we're covering in the next tutorial

