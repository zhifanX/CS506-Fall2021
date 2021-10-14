def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i]-y[i])

    return res


def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(set(x)) + len(set(y))) - intersection
    if union != 0:
        return  float(intersection)/union
    else:
        return 'undefined'

def cosine_sim(x, y):
    inner = 0
    lenx = 0
    leny = 0
    for i in range(len(x)):
        inner = inner + x[i]*y[i]
        lenx += x[i]**2
        leny += y[i]**2
    
    lenx = lenx ** (1/2)
    leny = leny ** (1/2)
    if (lenx * leny)==0:
        return 'undefined'
    return inner/(lenx * leny)
    

# Feel free to add more
