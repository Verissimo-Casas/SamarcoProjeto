
f = lambda x,y,z: (x-i/z for i in range(int((y-x)/z)))

print(list(f(1,10,0.5)))