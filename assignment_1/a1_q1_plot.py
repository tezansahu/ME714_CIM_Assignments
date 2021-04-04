import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define the coordinates for the triangles
tr1 = np.array([[0,3], [0,0], [3,0]])       # Original
tr2 = np.array([[0,-6], [0,-3], [3,-3]])    # Translation -> Rotation
tr3 = np.array([[3,-3], [3,0], [6,0]])      # Rotation -> Translation

# Plot the triangles
p1 = Polygon(tr1, closed=False, color="r")
p2 = Polygon(tr2, closed=False, color="g")
p3 = Polygon(tr3, closed=False, color="b")
ax = plt.gca()
ax.add_patch(p1)
p1.set(label="Original Triangle")
ax.add_patch(p2)    
p2.set(label="Translation then Rotation")                                                                                                
ax.add_patch(p3)
p3.set(label="Rotation then Translation")
ax.legend()
ax.set_xlim(-1, 7)
ax.set_ylim(-7, 4)
plt.yticks(np.arange(-7,5))
ax.set_aspect('equal')
plt.grid(linestyle="--")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()