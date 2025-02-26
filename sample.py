import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define room dimensions
width, height = 30, 32  # in feet

fig, ax = plt.subplots(figsize=(10, 10))

# Draw the outer walls
ax.add_patch(patches.Rectangle((0, 0), width, height, fill=None, edgecolor='black', linewidth=2))

# Workstations (Example: 4 rows of 7 desks)
for row in range(4):
    for col in range(7):
        ax.add_patch(patches.Rectangle((2 + col * 3, 2 + row * 4), 3, 3, fill=True, color='lightgrey'))

# Private Cabins
ax.add_patch(patches.Rectangle((22, 2), 6, 6, fill=True, color='lightblue', label="Private Cabin"))
ax.add_patch(patches.Rectangle((22, 10), 6, 6, fill=True, color='lightblue'))

# Meeting Room
ax.add_patch(patches.Rectangle((2, 20), 8, 8, fill=True, color='orange', label="Meeting Room"))

# Storage & Printer Area
ax.add_patch(patches.Rectangle((12, 20), 6, 6, fill=True, color='purple', label="Storage & Print"))

# Labels
ax.text(24, 5, "Cabin 1", fontsize=10, color="white", ha="center")
ax.text(24, 13, "Cabin 2", fontsize=10, color="white", ha="center")
ax.text(6, 24, "Meeting Room", fontsize=10, color="white", ha="center")
ax.text(15, 23, "Storage", fontsize=10, color="white", ha="center")

# Formatting
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
ax.legend()
plt.title("Co-Working Space Floor Plan")
plt.show()
