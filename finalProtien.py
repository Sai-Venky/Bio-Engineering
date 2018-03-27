Store_all = []
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np;
with open("1qm3.pdb") as protein:
    for lines in protein:
        if "ATOM   " in lines:
            lines = lines.split()
            #'ATOM', '1', 'N', 'LEU', 'A', '125', '4.329', '-12.012', '2.376', '1.00', '0.00', 'N'
            Store_all.append(map(float, lines[6:9]))
x=[];
y=[];
z=[];
'''
Store_all=np.array(Store_all)
print np.shape(Store_all)
Store_all=Store_all.reshape((len(Store_all),1))
'''
x=[item[0] for item in Store_all];
y=[item[1] for item in Store_all];
z=[item[2] for item in Store_all];
#print x;
#print y
#print z;
fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z,"o");
ax.axis("on")

plt.show()