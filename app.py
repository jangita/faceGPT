import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation


def draw_face():
    fig, ax = plt.subplots()

    # Draw the face
    face = patches.Circle((0.5, 0.5), 0.4, color="yellow", fill=True)
    ax.add_patch(face)

    # Draw the left eye
    left_eye = patches.Circle((0.35, 0.65), 0.08, color="white", fill=True)
    ax.add_patch(left_eye)
    left_pupil = patches.Circle((0.35, 0.65), 0.04, color="black", fill=True)
    ax.add_patch(left_pupil)

    # Draw the right eye
    right_eye = patches.Circle((0.65, 0.65), 0.08, color="white", fill=True)
    ax.add_patch(right_eye)
    right_pupil = patches.Circle((0.65, 0.65), 0.04, color="black", fill=True)
    ax.add_patch(right_pupil)

    # Draw the mouth
    mouth = patches.Arc(
        (0.5, 0.5), 0.2, 0.1, angle=0, theta1=0, theta2=180, color="black"
    )
    ax.add_patch(mouth)

    # Set equal aspect ratio, remove axes
    ax.set_aspect("equal", adjustable="box")
    plt.axis("off")

    # Animation function
    def animate(frame):
        if frame % 10 < 5:
            # Eyes open
            left_pupil.set_radius(0.04)
            right_pupil.set_radius(0.04)
        else:
            # Eyes closed (simulate blink by setting pupil radius to 0)
            left_pupil.set_radius(0)
            right_pupil.set_radius(0)
        return (
            left_pupil,
            right_pupil,
        )

    # Create the animation
    anim = FuncAnimation(fig, animate, frames=20, interval=200, blit=True)

    # Display the animation
    plt.show()


# Call the function to draw the face
draw_face()
