import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_floor_plan(save_path="coworking_space_floor_plan.png"):
    # Define room dimensions
    width, height = 30, 32  # in feet
    seat_size = 3  # Each seat occupies 3x3 ft
    path_width = 4  # Path width in feet
    door_width = 4  # Door width in feet
    door_position = 8  # Door positioned 8 feet from the left
    seat_spacing_x = 1  # Horizontal spacing between chairs
    seat_spacing_y = 2  # Vertical spacing between chairs

    # Compute available area for seating
    x_offset = seat_size + seat_spacing_x
    y_offset = seat_size + seat_spacing_y
    num_seats_x = (width - path_width) // x_offset  # Ensuring path is excluded
    num_seats_y = height // y_offset  # Number of seats per column with spacing

    # Calculate starting position to center the seats
    start_x = (width - (num_seats_x * x_offset)) / 2
    start_y = (height - (num_seats_y * y_offset)) / 2

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the outer walls
    ax.add_patch(patches.Rectangle((0, 0), width, height, fill=None, edgecolor='black', linewidth=2, label="Room Boundary"))
    
    # Add doors
    ax.add_patch(patches.Rectangle((door_position, height - 0.5), door_width, 0.5, fill=True, color='brown', label="Top Door (4 ft)"))
    ax.add_patch(patches.Rectangle((door_position, 0), door_width, 0.5, fill=True, color='brown', label="Bottom Door (4 ft)"))
    
    # Draw path
    ax.add_patch(patches.Rectangle((door_position + door_width/2 - path_width/2, 0), path_width, height, fill=True, color='gray', alpha=0.3, label="Path (4 ft)"))
    
    # Place seats ensuring no overlap with the path
    chair_count = 1
    for i in range(num_seats_x):
        for j in range(num_seats_y):
            seat_x, seat_y = start_x + i * x_offset, start_y + j * y_offset
            # Ensure seats do not overlap with the path
            if not (door_position - seat_size < seat_x < door_position + path_width):
                ax.add_patch(patches.Rectangle((seat_x, seat_y), seat_size, seat_size, fill=True, color='blue', alpha=0.6, label="Chair" if chair_count == 1 else ""))
                ax.text(seat_x + seat_size/2, seat_y + seat_size/2, str(chair_count), fontsize=8, ha='center', va='center', color='white')
                chair_count += 1
    
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
    plt.title("Co-Working Space Floor Plan with Optimized Seating")
    plt.legend()
    
    # Save the image
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    print(f"Floor plan saved at: {save_path}")

# Run the function
create_floor_plan()
