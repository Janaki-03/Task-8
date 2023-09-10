class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def display_radii(self):
        for radius in self.radius_list:
            print(f"Radius: {radius}")


# Create an instance of the Circle class with the provided list
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Display the radii from the list
circle_instance.display_radii()