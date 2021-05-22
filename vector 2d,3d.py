
class C2dVec:
    
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i +{self.jcap}j"


class C3dVec(C2dVec):

    def __init__(self,i, j, k):
        self.icap=i
        self.jcap=j
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"    


v2d=C2dVec(4,5)
v3d=C3dVec(2, 3, 7)

print(v2d)
print(v3d)

