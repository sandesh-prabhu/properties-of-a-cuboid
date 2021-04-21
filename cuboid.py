def prop(l,b,h):
    l=int(l)
    b=int(b)
    h=int(h)
    print("Shape: 3D")
    print("Faces: 6 Rectangular Faces")
    print("Edges: 12")
    print("Vertices: 8")
    LSA=2*h*(l+b)
    TSA=2*((l*b)+(b*h)+(h*l))
    V=l*b*h
    D=((l**2)+(b**2)+(h**2))**(1/2)
    P=4*(l+b+h)
    print("Lateral Surface Area(LSA):"+str(LSA))
    print("Total Surface Area(TSA):"+str(TSA))
    print("Volume(v):"+str(V))
    print("Diagonal(D):"+str(D))
    print("Perimeter(P):"+str(P))
while 1:
    l=input("Enter the length of the cuboid(in cm)(enter nothing to exit):")
    if l=="":
        break
    b=input("Enter the breadth of the cuboid(in cm):")
    h=input("Enter the height of the cuboid(in cm):")
    if l.isnumeric() and b.isnumeric() and h.isnumeric():
        prop(l,b,h)
        break
    else:
        print("Enter valid details")
