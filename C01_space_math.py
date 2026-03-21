# Space Math Module

def calculate_fuel(distance):
    # Calculate fuel needed for the journey
    # Formula: fuel = distance * 500
    # TODO: Implement the function
    fuel = distance * 500
    return fuel

def time_to_destination(distance, speed):
    # Calculate time to reach the destination
    # Formula: time = distance / speed
    # TODO: Implement the function
    time = distance / speed
    return time

def gravity_force(mass1, mass2, distance):
    # Calculate the gravitational force between two objects
    # Formula: force = (G * mass1 * mass2) / (distance ** 2)
    # Where G is the gravitational constant (G = 6.67430e-11)
    # TODO: Implement the function
    G = 6.67430e-11
    force = (G * mass1 * mass2) / (distance ** 2)
    return force