#direkte definition der euklidschen metrik: a**2 entspricht a-quadrat, a**(1/2) entspricht Quadratwurzel(a)
def dist_euclid(v1, v2):
    z = sum( (x1-x2)**2 for x1, x2 in zip(v1, v2))
    return z ** 0.5

#direkte definition der manhattan metrik:
def dist_manhattan(v1, v2):
    return sum( abs(x1-x2) for x1, x2 in zip(v1, v2))

#auch eine metrik
def dist_hm(v1, v2):
    return sum( 0 if x1==x2 else 1 for x1, x2 in zip(v1, v2) )

#todo: definiere funktion für Minkowski-Distanz
def dist_mink( p, v1, v2 ):
    return sum( abs(x1-x2)**p for x1, x2 in zip(v1, v2) )**(1/p)

#todo: definiere funktion für Euklidsche_Distanz und Manhattan-Distanz (Zurückführung auf Minkowski)
def dist_eucl( v1, v2 ):
    return dist_mink( 2, v1, v2 )

#todo
def dist_man( v1, v2 ):
    return dist_mink( 1, v1, v2 )

x1 = [1,1]
x2 = [3,3]
d1 = dist_euclid( x1, x2 )
d2 = dist_manhattan( x1, x2 )
d3 = dist_hm(x1, [1,3])
print( d1, d2, d3 )
dist_eucl(v1, v2)
dist_man(v1, v2)
