class Circle:
    # Private class variable for pi
    _pi = 3.141

    def __init__(self, radius_list):
        self.radius_list = radius_list

    def display_radii(self):
        for radius in self.radius_list:
            print(f"Radius: {radius}")

    @classmethod
    def calculate_area(cls, radius):
        return cls._pi * (radius ** 2)

    @classmethod
    def calculate_perimeter(cls, radius):
        return 2 * cls._pi * radius


# Create an instance of the Circle class with the provided list
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

# Display the radii from the list
circle_instance.display_radii()

# Calculate and display the areas and perimeters of the circles
for radius in circle_instance.radius_list:
    area = Circle.calculate_area(radius)
    perimeter = Circle.calculate_perimeter(radius)
    print(f"Radius: {radius}, Area: {area:.2f}, Perimeter: {perimeter:.2f}")