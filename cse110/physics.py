import math
# Ask for mass
m = float(input("Mass (in kg): "))

# Gravity Earth
g_e = 9.8

# Gravity Jupiter
g_j= 24

# g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))

# Ask for time
t = float(input("Time (in seconds): "))

# Ask for density of the fluid 
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))

# Ask for cross sectional area
A = float(input("Cross sectional area (in m^2): "))

# Ask for drag constant
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()

# Compute c
c = (1 / 2) * p * A * C
print(f"The inner value of c is: {c:.3f}")

v_t = math.sqrt(m*g_e/c) * (1 - math.exp(-math.sqrt(m*g_e*c)/m*t))
print(f"The velocity after {t} seconds on Earth is: {v_t:.3f} m/s ")

v_t = math.sqrt(m*g_j/c) * (1 - math.exp(-math.sqrt(m*g_j*c)/m*t))
print(f"The velocity after {t} seconds on Jupiter is: {v_t:.3f} m/s ")