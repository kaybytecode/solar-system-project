class Moon:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Planet:
    def __init__(self, name, mass, distance_from_sun, planet_type):
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type
        self.moons = []

    def add_moon(self, moon):
        self.moons.append(moon)

    def moon_count(self):
        return len(self.moons)

    def get_moons(self):
        if len(self.moons) == 0:
            return "None"

        moon_names = []
        for moon in self.moons:
            moon_names.append(moon.name)

        return ", ".join(moon_names)

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Mass: {self.mass}\n"
            f"Distance from the Sun: {self.distance_from_sun}\n"
            f"Type: {self.planet_type}\n"
            f"Moons: {self.get_moons()}"
        )


class SolarSystem:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def find_planet(self, name):
        for planet in self.planets:
            if planet.name.lower() == name.lower():
                return planet
        return None

    def planet_exists(self, name):
        return self.find_planet(name) is not None


def create_solar_system():
    solar_system = SolarSystem()

    mercury = Planet("Mercury", "3.30 x 10^23 kg", "57.9 million km", "Terrestrial planet")
    venus = Planet("Venus", "4.87 x 10^24 kg", "108.2 million km", "Terrestrial planet")
    earth = Planet("Earth", "5.97 x 10^24 kg", "149.6 million km", "Terrestrial planet")
    mars = Planet("Mars", "6.42 x 10^23 kg", "227.9 million km", "Terrestrial planet")
    jupiter = Planet("Jupiter", "1.90 x 10^27 kg", "778.3 million km", "Gas giant")
    saturn = Planet("Saturn", "5.68 x 10^26 kg", "1.43 billion km", "Gas giant")
    uranus = Planet("Uranus", "8.68 x 10^25 kg", "2.87 billion km", "Ice giant")
    neptune = Planet("Neptune", "1.02 x 10^26 kg", "4.50 billion km", "Ice giant")

    earth.add_moon(Moon("Moon"))

    mars.add_moon(Moon("Phobos"))
    mars.add_moon(Moon("Deimos"))

    jupiter.add_moon(Moon("Io"))
    jupiter.add_moon(Moon("Europa"))
    jupiter.add_moon(Moon("Ganymede"))
    jupiter.add_moon(Moon("Callisto"))

    saturn.add_moon(Moon("Titan"))
    saturn.add_moon(Moon("Enceladus"))
    saturn.add_moon(Moon("Rhea"))
    saturn.add_moon(Moon("Iapetus"))

    uranus.add_moon(Moon("Titania"))
    uranus.add_moon(Moon("Oberon"))
    uranus.add_moon(Moon("Miranda"))

    neptune.add_moon(Moon("Triton"))
    neptune.add_moon(Moon("Nereid"))

    solar_system.add_planet(mercury)
    solar_system.add_planet(venus)
    solar_system.add_planet(earth)
    solar_system.add_planet(mars)
    solar_system.add_planet(jupiter)
    solar_system.add_planet(saturn)
    solar_system.add_planet(uranus)
    solar_system.add_planet(neptune)

    return solar_system


def get_planet_name():
    name = input("Enter planet name: ").strip()

    while name == "":
        print("Planet name cannot be empty.")
        name = input("Enter planet name: ").strip()

    return name


def display_menu():
    print("Solar System Menu")
    print("1. Tell me everything about a planet")
    print("2. How massive is a planet?")
    print("3. Check if a planet is in the list")
    print("4. How many moons does a planet have?")
    print("5. Exit")


def main():
    solar_system = create_solar_system()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = get_planet_name()
            planet = solar_system.find_planet(name)

            if planet:
                print(planet)
            else:
                print("Planet not found.")

        elif choice == "2":
            name = get_planet_name()
            planet = solar_system.find_planet(name)

            if planet:
                print(f"{planet.name} has a mass of {planet.mass}.")
            else:
                print("Planet not found.")

        elif choice == "3":
            name = get_planet_name()

            if solar_system.planet_exists(name):
                print(f"{name} is in the list of planets.")
            else:
                print(f"{name} is not in the list of planets.")

        elif choice == "4":
            name = get_planet_name()
            planet = solar_system.find_planet(name)

            if planet:
                print(f"{planet.name} has {planet.moon_count()} moon(s) listed in this program.")
            else:
                print("Planet not found.")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 5.")

        print()


if __name__ == "__main__":
    main()

# References
#
# Lutz, M. (2013). Learning Python (5th ed.). O’Reilly Media.
# Used for general Python structure, classes, and methods.
#
# Downey, A. B. (2015). Think Python (2nd ed.). O’Reilly Media.
# https://greenteapress.com/thinkpython2/
# Used for understanding functions, loops, and program structure.
#
# Sommerville, I. (2016). Software engineering (10th ed.). Pearson.
# Used for object-oriented design and structuring classes.
#
# National Aeronautics and Space Administration (NASA). (n.d.).
# Solar System Exploration. https://solarsystem.nasa.gov
# Used for planetary data (mass, distance, moons).
#
# Wikipedia contributors. (n.d.). Solar System.
# https://en.wikipedia.org/wiki/Solar_System
# Used for supporting planetary information.
#
# Wikipedia contributors. (n.d.). List of natural satellites.
# https://en.wikipedia.org/wiki/List_of_natural_satellites
# Used for moon data.