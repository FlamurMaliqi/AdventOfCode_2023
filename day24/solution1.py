from itertools import combinations

hail = [[int(i) for i in l.replace('@',',').split(',')]
                for l in open('input.txt')]

def check(pair):
    (x,y,_,dx,dy,_), (u,v,_,du,dv,_) = pair

    if dy*du == dv*dx: return False

    t1 = (dv*(x-u) - du*(y-v)) / (dy*du - dx*dv)
    t2 = (dy*(u-x) - dx*(v-y)) / (dv*dx - du*dy)

    return (t1 > 0 and 2e14 < x+t1*dx < 4e14
        and t2 > 0 and 2e14 < y+t1*dy < 4e14)

print(sum(map(check, combinations(hail, 2))))