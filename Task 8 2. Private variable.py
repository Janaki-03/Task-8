class Circle:
    # Private class variable for pi
    _pi = 3.141

    def __init__(self, radius_list):
        self.radius_list = radius_list

    def display_radii(self):
        for radius in self.radius_list:
            print(f"Radius: {radius}")
    
    def calculate_area(self):
        areas = [self._pi * (r ** 2) for r in self.radius_list]
        return areas


# Create an instance of the Circle class with the provided list
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Display the radii from the list
circle_instance.display_radii()

# Calculate and display the areas of the circles
areas = circle_instance.calculate_area()
for i, area in enumerate(areas):
    print(f"Area of circle {i + 1}: {area:.2f}")