import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0, 10, 1)
n = len(x)

# Linear points along x-axis
y = np.full_like(x, 5)
points = np.stack([x, y], axis=1)

# Plot all points as gray
dots = []
labels = []
for i, (cx, cy) in enumerate(points):
    dot, = ax.plot(cx, cy, 'o', color='lightgray')
    dots.append(dot)
    label = ax.text(cx, cy + 0.3, str(i+1), ha='center', va='bottom', color='gray')
    labels.append(label)

# For the path
path_line, = ax.plot([], [], color='skyblue', linewidth=2)

# Arrow annotation (initially invisible)
arrow = ax.annotate(
    '', xy=(0,0), xytext=(0,0.7),
    arrowprops=dict(facecolor='blue', shrink=0.05, width=2, headwidth=8),
    ha='center', va='bottom', fontsize=14, color='blue', annotation_clip=False
)
arrow.set_visible(False)

# Text box for sum of even numbers
sum_text = ax.text(0.98, 0.95, '', transform=ax.transAxes, ha='right', va='top', fontsize=14, color='blue',
                   bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=0.3'))

ax.set_aspect('auto')
ax.set_xlim(-1, 10)
ax.set_ylim(4, 7)
ax.set_title("Visualizing a For Loop (Step by Step)")

even_sum = [0]  # Use list for mutable integer in closure

def update(frame):
    # Reset all dots and labels to gray
    for dot, label in zip(dots, labels):
        dot.set_color('lightgray')
        label.set_color('gray')
    # Highlight current dot and label
    dots[frame].set_color('orange')
    labels[frame].set_color('black')
    # Draw path up to current frame
    if frame > 0:
        path_line.set_data(points[:frame+1,0], points[:frame+1,1])
    else:
        path_line.set_data([], [])
    ax.set_xlabel(f"Iteration: {frame + 1}")

    # Arrow and sum for even numbers
    if (frame + 1) % 2 == 0:
        dots[frame].set_color('blue')
        labels[frame].set_color('blue')
        # Show arrow above the current even number
        arrow.xy = (points[frame,0], points[frame,1]+0.3)
        arrow.set_position((points[frame,0], points[frame,1]+0.7))
        arrow.set_visible(True)
        # Update sum
        even_sum[0] += (frame + 1)
    else:
        arrow.set_visible(False)
    # Show sum of even numbers so far
    sum_text.set_text(f"Sum of even numbers: {even_sum[0]}")

ani = animation.FuncAnimation(fig, update, frames=n, repeat=False, interval=1000)
plt.show()
