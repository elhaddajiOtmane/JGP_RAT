from PIL import Image
import os

def change_icon_color(icon_path, new_color, output_path):
    # Open the icon image
    with Image.open(icon_path) as icon:
        # Ensure there's an alpha channel
        icon = icon.convert("RGBA")
        
        # Load the pixel data
        data = icon.getdata()
        
        # Create a new data list
        new_data = []
        for item in data:
            # Change all non-transparent pixels to the new color while maintaining the alpha value
            if item[3] != 0:  # item[3] is the alpha value
                new_data.append(new_color + (item[3],))  # Maintain original alpha value
            else:
                new_data.append((0, 0, 0, 0))  # Keep pixels that were originally transparent

        # Update the icon's data
        icon.putdata(new_data)
        # Save the modified icon
        icon.save(output_path, 'PNG')

# Convert hex color #1fd902 to an RGB tuple
hex_color = "1fd902"
new_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2 ,4))

# Directory containing the icons
input_dir = 'D:/Downloads/jpgrats-main/jpgrats-main/assets/icons'
output_dir = 'D:/Downloads/jpgrats-main/jpgrats-main/assets/icons'
# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process all PNG images in the input directory
for icon_name in os.listdir(input_dir):
    if icon_name.endswith('.png'):
        input_path = os.path.join(input_dir, icon_name)
        output_path = os.path.join(output_dir, icon_name)
        change_icon_color(input_path, new_color, output_path)

print("All icons have been recolored.")
