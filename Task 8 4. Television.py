class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  # You can set the initial price here
        self.inches = 0  # You can set the initial inches here
        self.volume = 50
        self.is_on = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 178  # Default viewing angle
        self.backlight = "LED"  # Default backlight type

    def display_details(self):
        return f"{self.brand} LED TV - {self.inches} inches, {self.screen_thickness} mm thick, {self.energy_usage} kWh, {self.lifespan} years lifespan, {self.refresh_rate} Hz refresh rate"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 160  # Default viewing angle
        self.backlight = "Plasma"  # Default backlight type

    def display_details(self):
        return f"{self.brand} Plasma TV - {self.inches} inches, {self.screen_thickness} mm thick, {self.energy_usage} kWh, {self.lifespan} years lifespan, {self.refresh_rate} Hz refresh rate"


# Example usage
led_tv = LedTV("Sony", 10, 150, 5, 120)
led_tv.inches = 55
led_tv.price = 1000
led_tv.set_channel(8)
led_tv.increase_volume()

plasma_tv = PlasmaTV("LG", 15, 200, 6, 60)
plasma_tv.inches = 50
plasma_tv.price = 800
plasma_tv.reset_tv()

print(led_tv.status())
print(plasma_tv.status())

print(led_tv.display_details())
print(plasma_tv.display_details())