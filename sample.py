import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_floor_plan(save_path="coworking_space_floor_plan.png"):
    # Define room dimensions
    width, height = 30, 32  # in feet

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the outer walls
    ax.add_patch(patches.Rectangle((0, 0), width, height, fill=None, edgecolor='black', linewidth=2, label="Room Boundary"))

    # Formatting
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Co-Working Space Floor Plan")
    plt.legend()
    
    # Save the image
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    print(f"Floor plan saved at: {save_path}")

# Run the function
create_floor_plan()
