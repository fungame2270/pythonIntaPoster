def getKey(filename):
    with open(filename,'r') as f:
        key = f.readline()
    
    f.close()
    return key