import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_floor_plan(save_path="coworking_space_floor_plan.png"):
    # Define room dimensions
    width, height = 30, 32  # in feet

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the outer walls
    ax.add_patch(patches.Rectangle((0, 0), width, height, fill=None, edgecolor='black', linewidth=2, label="Room Boundary"))
    
    # Add doors
    door_width = 4  # Door width in feet
    door_position = 8  # Door positioned 8 feet from the left
    
    # Top door at 8 feet from left
    ax.add_patch(patches.Rectangle((door_position, height - 0.5), door_width, 0.5, fill=True, color='brown', label="Top Door (4 ft)"))
    
    # Bottom door also at 8 feet from left
    ax.add_patch(patches.Rectangle((door_position, 0), door_width, 0.5, fill=True, color='brown', label="Bottom Door (4 ft)"))
    
    # Draw path (4 feet wide)
    path_width = 4
    ax.add_patch(patches.Rectangle((door_position + door_width/2 - path_width/2, 0), path_width, height, fill=True, color='gray', alpha=0.3, label="Path (4 ft)"))
    
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
    plt.title("Co-Working Space Floor Plan with Doors, Path, and Dimensions")
    plt.legend()
    
    # Save the image
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    print(f"Floor plan saved at: {save_path}")

# Run the function
create_floor_plan()
