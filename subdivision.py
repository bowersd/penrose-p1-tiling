import math

#p1 tiling uses 4 tiles: pentagons, pentagrams (5 pointed star), rhombuses, and boats (roughly a 5 pointed star with 2 points lopped off)
#these have 5, 10, 4, 7 vertices, respectively, so that is how we will identify them
            #pentagon = 2 108x36x36 triangles + 1 36x72x72 triangle, 
            #so break the 108 triangles into a pentagon thus composed flanked by a pair of 36 (joins to make rhombus) and 108 triangles
            #break the 36 triangle into a pentagon thus composed, plus 3 36s (finishing pentagons), 2 108s (finishing pentagons), and a 36 (joins to make a rhombus)
            #boats and pentagrams can be treated similarly, since they are pentagons with 36 triangles jutting off the edges. 
            #rhombuses are even simpler, base to base 36 triangles -> though directionality of embedded pentagon is something I am unsure about

phi = (1 + math.sqrt(5))/2

def subdivide(depth, *triangles):
    #triangles are tuples with 3 coordinates and an id for what larger tile they belong to and whether they are 108 (1) or 36 (0) triangles: 1 = pentagon, 2 = boat, 3 = pentagram, 0 = rhomb/excised triangle from pentagon
    if depth < 1: return triangles
    for t in triangles:
        nu = []
        if len(t) == 2:
            pass #rhombus (2 triangles with apex 36) -> 1 pentagon (and join with neighboring pentagons to make 1 boat and 1 pentagram)
        if t[0] == 1 and t[1]:
            d = t[2] + (t[3]-t[2])/phi #marks on the hypotenuse
            e = t[3] + (t[2]-t[3])/phi #marks on the hypotenuse
            #need marks f,g,h,i on the legs
            nu.extend([(1,1,t[2],d,f), (0,0,d,f,g), (1,1,d,e,g),(1,0,g,e,t[4]), (1,1,e,h,t[4]), (0,0,e,h,i), (1,1,t[3],e,i)])
            #pentagon (2 108 triangles and 1 apex 36)-> 6 pentagons (and join with neighboring pentagons to make 5 rhombuses) 
        if len(t) == 6:
            pass #boat (3 36 triangles and 2 108 triangles plus a 36-> 3 pentagons (and join with neighboring pentagons to make 3 boats on tips and a pentagram on base)
        if len(t) == 8:
            pass #pentagram (5 36 triangles and 2 108 triangles plus a 36)-> 5 pentagons, 1 pentagram (and join with neighboring pentagons to make 5 boats on tips)
    subdivide(depth-1, *nu)
