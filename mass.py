import math
print("all formulas used from surface area and volume chapter maths class 10 21-22 batch")
name=input("enter your name: ")
while True:
  bhai="-commands-""\n Curved Suface Area of cylinder= csacy \n Total surface area of cylinder= tsacy \n Volume of cylinder= volcy \n \n Curved Suface Area of a cone= csaco \n Total Suface Area of cone= tsaco \n Volume of cone= volco \n \n Lateral surface area of cuboid= lsacu \n Total suface area of cuboid= tsacu \n Volume of cuboid= volcu \n \n Lateral surface area of the cube= lsacb \n Total surface area of the cube= tsacb \n Volume of the cube= volcb \n \n Area of the sphere= aresph \n Volume of the sphere= volsph \n \n Curved surface area of the hemisphere= lsahem \n Total surface area of the hemisphere= tsahem \n Volume of the hemisphere= volhem"
  print()
  print(bhai)
  dib= input("\n enter command: ")
  if dib=="csacy":
      h= float(input("enter cylinder height(in cm: "))
      r= float(input("enter cylinder radius(in cm: "))
      π=22/7
      print("The curved surface area of the cylinder will be", float(2*π*r*h), "sq.cm")
  if dib=="tsacy":
      h= float(input("enter cylinder height(in cm)= "))
      r= float(input("enter cylinder radius(in cm)=  "))
      π=22/7
      print("The total surface area of the cylinder will be", float(2*π*r*(r+h)), "sq.cm")
  if dib=="volcy":
      h=float(input("enter cylinder height(in cm)= "))
      r=float(input("enter cylinder radius(in cm)= "))
      π=22/7
      print("The volume of the cylinder will be", float(π*r*r*h), "cube.cm")
  if dib=="csaco":
      r= float(input("enter cone radius(in cm)="))
      sl=float(input("enter cone slant height(in cm)= "))
      π=22/7
      print("The curved surface area of the cone will be", float(π*r*sl), "sq.cm")
  if dib=="tsaco":
      r= float(input("enter cone radius(in cm)= "))
      sl=float(input("enter cone slant height(in cm)= "))
      π=22/7
      print("The total surface area of the cone will be", float(π*r*(r+sl)), "sq.cm")
  if dib=="volco":
      h=float(input("enter cone height(in cm)= "))
      r= float(input("enter cone radius(in cm)= "))
      π=22/7
      print("The volume of the cone will be", float(1/3*π*r*r*h), "cube.cm")
  if dib=="lsacu":
      l=float(input("enter cuboid length(in cm)= "))
      h=float(input("enter cuboid height(in cm)= "))
      b=float(input("enter cuboid breadth(in cm)= "))
      print("The lateral surface area of the cuboid will be", float(2*h*(l+b)), "sq.cm")
  if dib=="tsacu":
      l=float(input("enter cuboid length(in cm)= "))
      h=float(input("enter cuboid height(in cm)= "))
      b=float(input("enter cuboid breadth(in cm)="))
      print("The total surface area of the cuboid will be", float(2*(l*b+b*h+h*l)), "sq.cm")
  if dib=="volcu":
      l=float(input("enter cuboid length(in cm)= "))
      h=float(input("enter cuboid height(in cm)= "))
      b=float(input("enter cuboid breadth(in cm)= "))
      print("The volume of the cuboid will be", float(l*b*h), "cube.cm")
  if dib=="lsacb":
      l=float(input("enter cube side length(in cm)= "))
      print("The lateral surface area of the cube will be", float(4*l*l), "sq.cm")
  if dib=="tsacb":
      l=float(input("enter cube side length(in cm)= "))
      print("The total surface area of the cube will be", float(6*l*l), "sq.cm")
  if dib=="volcb":
      l=float(input("enter cube side length(in cm)= "))
      print("The volume of the cube will be", float(l*l*l), "cube.cm")
  if dib=="aresph":
      r=float(input("enter sphere radius(in cm)= "))
      π=22/7
      print("The area of the sphere will be", float(4*π*r*r), "sq.cm")
  if dib=="volsph":
      r=float(input("enter sphere radius(in cm)= "))
      π=22/7
      print("The volume the sphere will be", float(4/3*π*r*r*r), "cube.cm")
  if dib=="lsahem":
      r=float(input("enter hemisphere radius(in cm)= "))
      π=22/7
      print("The lateral surface area of the hemisphere will be", float(2*π*r*r), "sq.cm")
  if dib=="tsahem":
      r=float(input("enter hemisphere radius(in cm)= "))
      π=22/7
      print("The total surface area of the hemisphere will be", float(3*π*r*r), "sq.cm")
  if dib=="volhem":
      r=float(input("enter hemisphere radius(in cm)="))
      π=22/7
      print("The volume of the hemisphere will be", float(2/3*π*r*r*r), "cube.cm")
  while True:
    dy=input("\nDo you want to continue? [yes/no] : ")
    if dy=="no":
      break
    elif dy=="yes":
      break
    else:
      print("invalid command! try again")
  if dy=="no":
    break
print("\n Thank you", name, "\n Powered by chou")
