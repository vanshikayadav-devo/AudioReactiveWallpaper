import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# -----------------------------------
# Figure Setup
# -----------------------------------

fig = plt.figure(figsize=(16,9))
ax = plt.axes()

ax.set_facecolor("black")
fig.patch.set_facecolor("black")

plt.xlim(0,100)
plt.ylim(0,100)
plt.axis("off")


# -----------------------------------
# Background Stars
# -----------------------------------

num_stars = 500

x = np.random.uniform(0,100,num_stars)
y = np.random.uniform(0,100,num_stars)

# Initial sizes
sizes = np.random.uniform(1,4,num_stars)

# Each star has its own twinkling timing
phase = np.random.uniform(
                        0,
                        2*np.pi,
                        num_stars
                        )

stars = plt.scatter(
                    x,
                    y,
                    s=sizes,
                    color='white',
                    alpha=0.8
                    )


# -----------------------------------
# Glowing Core
# -----------------------------------

glows = []

for i in range(5):

    glow = plt.Circle(

                        (50,50),

                        10+i*2,

                        color="#BC13FE",

                        alpha=0.1

                    )

    ax.add_patch(glow)
    glows.append(glow)



core = plt.Circle(

                    (50,50),

                    10,

                    color="#BC13FE",

                    alpha=0.9

                )

ax.add_patch(core)



# -----------------------------------
# Spiral Galaxy
# -----------------------------------

theta = np.linspace(

                        0,

                        8*np.pi,

                        2000

                    )


radius = 0.8*theta


x1 = 50 + radius*np.cos(theta)
y1 = 50 + radius*np.sin(theta)


plt.scatter(

            x1,

            y1,

            s=3,

            color="#00FFFF",

            alpha=0.7

            )


# -----------------------------------
# Animation Function
# -----------------------------------

def update(frame):

    # Twinkling stars
    new_sizes = 2 + 2*np.sin(

                                frame/10 + phase

                            )


    stars.set_sizes(new_sizes)


    # Pulsating core
    pulse = 10 + 1*np.sin(frame/10)

    core.set_radius(pulse)


    for i, glow in enumerate(glows):

        glow.set_radius(

                            pulse + i*2

                        )


    return stars, core



# -----------------------------------
# Animation
# -----------------------------------

ani = FuncAnimation(

                        fig,

                        update,

                        frames=300,

                        interval=50,

                        blit=False

                    )


plt.show()
