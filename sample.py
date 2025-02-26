import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_floor_plan(save_path="coworking_space_floor_plan.png"):
    # Define room dimensions
    width, height = 30, 32  # in feet
    seat_size = 3  # Each seat occupies 3x3 ft
    path_width = 4  # Path width in feet
    door_width = 4  # Door width in feet
    door_position = 8  # Door positioned 8 feet from the left

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the outer walls
    ax.add_patch(patches.Rectangle((0, 0), width, height, fill=None, edgecolor='black', linewidth=2, label="Room Boundary"))
    
    # Add doors
    ax.add_patch(patches.Rectangle((door_position, height - 0.5), door_width, 0.5, fill=True, color='brown', label="Top Door (4 ft)"))
    ax.add_patch(patches.Rectangle((door_position, 0), door_width, 0.5, fill=True, color='brown', label="Bottom Door (4 ft)"))
    
    # Draw path
    ax.add_patch(patches.Rectangle((door_position + door_width/2 - path_width/2, 0), path_width, height, fill=True, color='gray', alpha=0.3, label="Path (4 ft)"))
    
    # Place seats avoiding the path
    num_seats_x = width // seat_size  # Number of seats per row
    num_seats_y = height // seat_size  # Number of seats per column
    for i in range(num_seats_x):
        for j in range(num_seats_y):
            seat_x, seat_y = i * seat_size, j * seat_size
            # Skip seats that overlap with the path
            if not (door_position <= seat_x <= door_position + path_width - seat_size):
                ax.add_patch(patches.Rectangle((seat_x, seat_y), seat_size, seat_size, fill=True, color='blue', alpha=0.6))
    
    # Add dimensions
    ax.text(15, height + 1, "30 ft", fontsize=10, ha='center')
    ax.text(-1, 16, "32 ft", fontsize=10, va='center', rotation=90)
    ax.text(door_position + door_width/2, height - 1, "4 ft", fontsize=8, ha='center')
    ax.text(door_position + door_width/2, -1, "4 ft", fontsize=8, ha='center')
    ax.text(10, height/2, "Path 4 ft", fontsize=8, ha='center')
    
    # Formatting
    plt.xlim(0, width)
    plt.ylim(0, height + 2)
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Co-Working Space Floor Plan with Doors, Path, and Maximum Seating")
    plt.legend()
    
    # Save the image
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    print(f"Floor plan saved at: {save_path}")

# Run the function
create_floor_plan()
