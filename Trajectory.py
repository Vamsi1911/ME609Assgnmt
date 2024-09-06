import numpy as np
import matplotlib.pyplot as plt
import random

# Function to minimize/maximize
def func(x):
    return -(20 * np.sin(x) - 15 * x ** 2)

# Derivative of the function (for secant method)
def func_derivative(x):
    return -20 * np.cos(x) + 30 * x

# Bounding Phase Method
def bounding_phase(lb, ub, delta):
    x = random.uniform(lb, ub)  # Initial random point
    print(f"Random starting point: {x}")
    
    dx = delta
    x_lb = max(x - dx, lb)
    x_ub = min(x + dx, ub)
    f_x = func(x)
    f_x_lb = func(x_lb)
    f_x_ub = func(x_ub)
    k = 0

    while x_ub <= ub and x_lb >= lb:
        dx = abs(dx) if (f_x <= f_x_lb and f_x >= f_x_ub) else -abs(dx)

        k += 1
        x_new = x + (2 ** k) * dx
        if x_new > ub:
            x_new = ub
        if x_new < lb:
            x_new = lb

        if func(x_new) > f_x:
            return x, x_new

        x = x_new
        x_ub = min(x + abs(dx), ub)
        x_lb = max(x - abs(dx), lb)
        f_x = func(x)
        f_x_lb = func(x_lb)
        f_x_ub = func(x_ub)

    return x, x

# Secant Method
def secant_method(x1, x2, epsilon):
    iterations = []
    z = None
    while True:
        z = x2 - func_derivative(x2) / ((func_derivative(x2) - func_derivative(x1)) / (x2 - x1))
        iterations.append((x1, x2, z))

        if abs(func_derivative(z)) <= epsilon:
            break

        if func_derivative(z) < 0:
            x1 = z
        else:
            x2 = z
    
    return z, iterations

# Helper function to extend line till it intersects the x-axis
def extend_to_x_axis(x1, y1, x2, y2):
    if x1 == x2:  # Avoid division by zero
        return x1
    m = (y2 - y1) / (x2 - x1)  # Slope of the line
    c = y1 - m * x1  # y = mx + c
    return -c / m  # Intersection point with x-axis (y = 0)

# Plot function and method points
def plot_bounding_and_secant(lb, ub, delta, epsilon):
    x = np.linspace(lb-10, ub+10, 400)
    y = func(x)
    
    # Plot the function
    fig, ax = plt.subplots()
    ax.plot(x, y, label='f(x)', color='blue')
    
    # Perform bounding phase method
    x1, x2 = bounding_phase(lb, ub, delta)
    ax.scatter([x1, x2], [func(x1), func(x2)], color='red', marker='o', label='Bounding Phase Points')
    print(f"Bounding phase result: [{x1}, {x2}]")
    
    # Perform secant method
    result, iterations = secant_method(x1, x2, epsilon)

    # Plot secant method progress
    for i, (x1_i, x2_i, z_i) in enumerate(iterations):
        # Plot the secant line between x1 and x2
        ax.plot([x1_i, x2_i], [func(x1_i), func(x2_i)], 'ro--', label=f'Secant iteration {i+1}' if i == 0 else "")
        
        # Find the intersection of the secant line with the x-axis
        intersection = extend_to_x_axis(x1_i, func(x1_i), x2_i, func(x2_i))
        
        # Plot the intersection point on the x-axis
        ax.scatter([intersection], [0], color='green', marker='x', s=100, label=f'z_{i+1} on x-axis')
        
        # Draw a vertical line from the intersection to the curve
        ax.plot([intersection, intersection], [0, func(intersection)], 'g--')
        ax.scatter([intersection], [func(intersection)], color='black', marker='+', s=100)

    # Final point
    ax.scatter([result], [func(result)], color='purple', marker='*', s=150, label='Final Secant Result')

    # Improve readability by limiting the number of legends and avoiding overlap
    handles, labels = ax.get_legend_handles_labels()
    unique_labels = list(dict.fromkeys(labels))  # Remove duplicate labels
    ax.legend(handles[:len(unique_labels)], unique_labels)

    ax.set_title('Bounding Phase & Secant Method with Extended Lines')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    plt.show()

# Example usage
lb = -4  # Lower bound
ub = 4  # Upper bound
delta = 0.5  # Step size for bounding phase
epsilon = 1e-6  # Convergence threshold for secant method

plot_bounding_and_secant(lb, ub, delta, epsilon)
