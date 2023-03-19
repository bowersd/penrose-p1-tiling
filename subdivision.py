import math

#p1 tiling uses 4 tiles: pentagons, pentagrams (5 pointed star), rhombuses, and boats (roughly a 5 pointed star with 2 points lopped off)
#these have 5, 10, 4, 7 vertices, respectively, so that is how we will identify them
            #pentagon = 2 108x36x36 triangles + 1 36x72x72 triangle, 
            #so break the 108 triangles into a pentagon thus composed flanked by a pair of 36 (joins to make rhombus) and 108 triangles
            #break the 36 triangle into a pentagon thus composed, plus 3 36s (finishing pentagons), 2 108s (finishing pentagons), and a 36 (joins to make a rhombus)

phi = (1 + math.sqrt(5))/2

def subdivide(depth, *shapes):
    h = []
    if depth < 1: return h
    for s in shapes:
        nu = []
        if len(s) == 4:
            pass #rhombus -> 1 pentagon (and join with neighboring pentagons to make 1 boat and 1 pentagram)
        if len(s) == 5:
            pass #pentagon -> 6 pentagons (and join with neighboring pentagons to make 5 rhombuses) 
        if len(s) == 7:
            pass #boat -> 3 pentagons (and join with neighboring pentagons to make 3 boats on tips and a pentagram on base)
        if len(s) == 10:
            pass #pentagram -> 5 pentagons, 1 pentagram (and join with neighboring pentagons to make 5 boats on tips)
        h = nu
    subdivide(depth-1, *h)
