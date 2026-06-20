import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(16,9))
ax=plt.axes()

plt.xlim(0,100)
plt.ylim(0,100)

ax.set_facecolor("black")
fig.patch.set_facecolor("black")

plt.axis("off")

x=np.random.uniform(0,100,500)
y=np.random.uniform(0,100,500)
plt.scatter(x,y,
            s=2,
            color="white",
            alpha=0.8)
for i in range(5):
    glow=plt.Circle((50,50),
               10+i*2,
               color="purple",
               alpha=0.1)
    ax.add_patch(glow)


circle = plt.Circle(

                        (50,50),

                        10,

                        color="#BC13FE",

                        alpha=0.8

                    )


ax.add_patch(circle)
x1=np.random.uniform(30,70,200)
y1=np.random.uniform(30,70,200)

plt.scatter(x1,y1,
            s=5,
            color="#00FFFF",
            alpha=0.7
            )

plt.savefig(
    "galaxy.png",
    dpi=300
)

plt.show()