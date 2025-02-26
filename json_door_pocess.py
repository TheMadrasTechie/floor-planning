import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_floor_plan_from_json(json_file, save_path="coworking_space_floor_plan_json.png"):
    # Load configuration from JSON file
    with open(json_file, "r") as file:
        config = json.load(file)
    
    width = config["room"]["width"]
    height = config["room"]["height"]
    doors = config["doors"]
    paths = config["paths"]
    seats = config["seats"]
    objects = config.get("objects", [])
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Draw the outer walls
    ax.add_patch(patches.Rectangle((0, 0), width, height, fill=None, edgecolor='black', linewidth=2, label="Room Boundary"))
    
    # Add doors
    for door in doors:
        ax.add_patch(patches.Rectangle((door["x"], door["y"]), door["width"], 0.5, fill=True, color='brown', label="Door"))
    
    # Draw paths
    for path in paths:
        ax.add_patch(patches.Rectangle((path["x"], path["y"]), path["width"], path["height"], fill=True, color='gray', alpha=0.3, label="Path"))
    
    # Place seats
    for index, seat in enumerate(seats, start=1):
        ax.add_patch(patches.Rectangle((seat["x"], seat["y"]), seat["width"], seat["height"], fill=True, color='blue', alpha=0.6, label="Chair" if index == 1 else ""))
        ax.text(seat["x"] + seat["width"]/2, seat["y"] + seat["height"]/2, str(index), fontsize=8, ha='center', va='center', color='white')
    
    # Add other objects
    for obj in objects:
        ax.add_patch(patches.Rectangle((obj["x"], obj["y"]), obj["width"], obj["height"], fill=True, color=obj["color"], alpha=0.6, label=obj["name"]))
    
    # Formatting
    plt.xlim(0, width)
    plt.ylim(0, height + 2)
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Co-Working Space Floor Plan from JSON")
    plt.legend()
    
    # Save the image
    plt.savefig(save_path, dpi=300)
    plt.show()
    
    print(f"Floor plan saved at: {save_path}")

# Example Usage
create_floor_plan_from_json("floor_plan.json")
