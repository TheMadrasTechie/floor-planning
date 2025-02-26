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
    door_width = 3  # Door width in feet
    
    # Door on the left side, 8 feet from the left and extending to the bottom
    ax.add_patch(patches.Rectangle((8, 0), door_width, 0.5, fill=True, color='brown', label="Door"))
    
    # Bottom door centered
    ax.add_patch(patches.Rectangle((width/2 - door_width/2, 0), door_width, 0.5, fill=True, color='brown'))
    
    # Draw path for doors
    ax.plot([8 + door_width/2, width/2], [0, height/2], linestyle='dashed', color='gray', label="Path")
    ax.plot([width/2, width/2], [0, height/2], linestyle='dashed', color='gray')
    
    # Formatting
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Co-Working Space Floor Plan with Doors and Path")
    plt.legend()
    
    # Save the image
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    print(f"Floor plan saved at: {save_path}")

# Run the function
create_floor_plan()