def stopping_distance(speed_kmh, reaction_time, braking_deceleration):
    speed_mps = speed_kmh / 3.6

    reaction_distance = speed_mps * reaction_time

    braking_distance = (speed_mps ** 2) / (2 * braking_deceleration)

    total_stopping_distance = reaction_distance + braking_distance
    return total_stopping_distance


speed_kmh = float(input("Enter speed in km/h: "))
reaction_time = float(input("Enter reaction time in seconds: "))
braking_deceleration = float(input("Enter braking deceleration in m/s²: "))

stopping_dist = stopping_distance(
    speed_kmh, reaction_time, braking_deceleration)
print(f"Total stopping distance: {stopping_dist:.2f} meters")
