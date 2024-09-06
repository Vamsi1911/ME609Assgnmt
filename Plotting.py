import numpy as np
import matplotlib.pyplot as plt
import os

# Define your functions and their results
functions = {
    "First": {
        "func": lambda x: (2 * x - 5) ** 4 - (x**2 - 1) ** 3,
        "bounds": [(-10, 0)],
        "results": [
            {"start": -6.71513, "bounding": [-5.45513, -6.73513], "secant": -5.77507},
            {"start": -9.78514, "bounding": [-4.68514, -9.80514], "secant": -5.77507},
            {"start": -7.23708, "bounding": [-5.97708, -4.69708], "secant": -5.77507},
            {"start": -8.6895, "bounding": [-6.1495, -3.5895], "secant": -5.77507},
            {"start": -8.57103, "bounding": [-6.03103, -3.47103], "secant": -5.77507},
            {"start": -2.66238, "bounding": [-5.20238, -7.76238], "secant": -5.77507},
            {"start": -9.33161, "bounding": [-4.23161, -9.35161], "secant": -5.77507},
            {"start": -9.23069, "bounding": [-6.69069, -4.13069], "secant": -5.77507},
            {"start": -5.12918, "bounding": [-5.74918, -6.38918], "secant": -5.77507},
            {"start": -8.94316, "bounding": [-6.40316, -3.84316], "secant": -5.77507},
        ],
    },
    "Second": {
        "func": lambda x: 8 + x**3 - 2 * x - 2 * np.exp(x),
        "bounds": [(-2, 1)],
        "results": [
            {
                "start": -0.158718,
                "bounding": [-0.778718, -1.41872],
                "secant": -0.960151,
            },
            {"start": -1.16939, "bounding": [-1.02939, -0.869395], "secant": -0.960149},
            {
                "start": -0.884252,
                "bounding": [-0.944252, -1.02425],
                "secant": -0.960154,
            },
            {"start": -1.48404, "bounding": [-0.864042, -1.50404], "secant": -0.960146},
            {
                "start": -0.535937,
                "bounding": [-0.835937, -1.15594],
                "secant": -0.960149,
            },
            {"start": 0.248293, "bounding": [-1.01171, 0.268293], "secant": -0.960151},
            {"start": -1.88596, "bounding": [-1.26596, -0.625956], "secant": -0.960145},
            {"start": 0.670251, "bounding": [-0.589749, -1.86975], "secant": -0.960144},
            {"start": -1.18009, "bounding": [-0.880089, -1.20009], "secant": -0.96015},
            {
                "start": -0.318165,
                "bounding": [-0.938165, -1.57816],
                "secant": -0.960151,
            },
        ],
    },
    "Third": {
        "func": lambda x: 4 * x * np.sin(x),
        "bounds": [(0.5, 3.14)],
        "results": [
            {"start": 2.9232, "bounding": [2.3032, 1.6632], "secant": 2.02876},
            {"start": 2.42091, "bounding": [2.12091, 1.80091], "secant": 2.02876},
            {"start": 1.32068, "bounding": [1.94068, 2.58068], "secant": 2.02875},
            {"start": 1.20642, "bounding": [1.82642, 2.46642], "secant": 2.02876},
            {"start": 0.980227, "bounding": [2.24023, 0.960227], "secant": 2.02875},
            {"start": 0.882627, "bounding": [2.14263, 0.862627], "secant": 2.02876},
            {"start": 3.06551, "bounding": [1.80551, 3.08551], "secant": 2.02875},
            {"start": 2.72462, "bounding": [2.10462, 1.46462], "secant": 2.02876},
            {"start": 1.2905, "bounding": [1.9105, 2.5505], "secant": 2.02876},
            {"start": 2.73846, "bounding": [2.11846, 1.47846], "secant": 2.02876},
        ],
    },
    "Fourth": {
        "func": lambda x: 2 * (x - 3) ** 2 + np.exp(0.5 * x**2),
        "bounds": [(-2, 3)],
        "results": [
            {"start": 0.303083, "bounding": [1.56308, 2.84308], "secant": 1.59071},
            {"start": 1.48848, "bounding": [1.62848, 1.46848], "secant": 1.59072},
            {"start": 1.93436, "bounding": [1.63436, 1.31436], "secant": 1.59072},
            {"start": 1.75763, "bounding": [1.61763, 1.45763], "secant": 1.59072},
            {"start": 2.30676, "bounding": [1.68676, 1.04676], "secant": 1.59072},
            {"start": 2.27176, "bounding": [1.65176, 1.01176], "secant": 1.59072},
            {"start": -1.25123, "bounding": [1.28877, 3], "secant": 1.59071},
            {"start": 2.20207, "bounding": [1.58207, 2.22207], "secant": 1.59071},
            {"start": -1.63336, "bounding": [0.90664, 3], "secant": 1.59071},
            {"start": 2.58217, "bounding": [1.32217, 2.60217], "secant": 1.59071},
        ],
    },
    "Fifth": {
        "func": lambda x: x**2 - 10 * np.exp(0.1 * x),
        "bounds": [(-6, 6)],
        "results": [
            {"start": 3.00055, "bounding": [0.460554, 3.02055], "secant": 0.52706},
            {"start": 3.6867, "bounding": [1.1467, -1.4133], "secant": 0.527054},
            {
                "start": -0.0431851,
                "bounding": [0.576815, -0.0631851],
                "secant": 0.52706,
            },
            {"start": 4.55029, "bounding": [-0.549709, 4.57029], "secant": 0.527099},
            {"start": -4.13212, "bounding": [0.967882, -4.15212], "secant": 0.527054},
            {"start": 1.38724, "bounding": [0.767237, 0.127237], "secant": 0.52706},
            {"start": -2.24209, "bounding": [0.297914, 2.85791], "secant": 0.527061},
            {"start": 3.31136, "bounding": [0.771356, -1.78864], "secant": 0.527059},
            {"start": 1.27814, "bounding": [0.658144, 0.0181436], "secant": 0.52706},
            {"start": 1.67081, "bounding": [0.410811, 1.69081], "secant": 0.52706},
        ],
    },
    "Sixth": {
        "func": lambda x: x**3 - 2 * x + 1,
        "bounds": [(-2, 2)],
        "results": [
            {"start": -1.94707, "bounding": [-2.46707, -1.42707], "secant": -1.52707},
            {
                "start": -0.368493,
                "bounding": [-1.56849, -0.338493],
                "secant": -0.509993,
            },
            {"start": -1.02829, "bounding": [-1.43829, -0.858293], "secant": -1.15829},
            {"start": 0.182569, "bounding": [-0.318431, -0.258569], "secant": -0.30957},
            {"start": -0.84562, "bounding": [-1.34562, -0.72562], "secant": -1.07562},
            {"start": 1.23712, "bounding": [0.73712, 1.65712], "secant": 1.45712},
            {"start": 1.17312, "bounding": [0.67312, 1.59312], "secant": 1.41712},
            {"start": -0.89412, "bounding": [-1.39412, -0.79412], "secant": -1.09412},
            {"start": -1.02912, "bounding": [-1.32912, -0.72912], "secant": -1.07912},
            {"start": -1.07812, "bounding": [-1.37812, -0.77812], "secant": -1.12712},
        ],
    },
}

# Create folders for each function
for func_name in functions:
    folder_path = f"{func_name}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Plot results for each function
    for i, result in enumerate(functions[func_name]["results"]):
        x = np.linspace(-10, 10, 400)
        func = functions[func_name]["func"]
        y = func(x)

        # Start and bounding values
        start = result["start"]
        bounding = result["bounding"]
        secant = result["secant"]

        # Create the plot
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label="Function curve", color="blue")

        # Shade the vertical region between bounding points
        plt.fill_betweenx(
            [min(y), max(y)],  # Y limits for shading
            bounding[0],  # X lower bound
            bounding[1],  # X upper bound
            color="yellow",
            alpha=0.3,
        )

        # Plot vertical dotted lines at the bounding points
        plt.axvline(
            x=bounding[0], color="blue", linestyle=":", label="Bounding left limit"
        )
        plt.axvline(
            x=bounding[1], color="blue", linestyle=":", label="Bounding right limit"
        )

        # Mark the starting point and bounding points
        plt.scatter(
            [start],
            [func(start)],
            color="red",
            marker="x",
            s=100,
            label="Starting point",
            zorder=5,
        )
        plt.scatter(
            bounding,
            [func(b) for b in bounding],
            color="green",
            label="Bounding points",
            zorder=5,
        )

        # Plot the secant result
        plt.axvline(
            x=secant, color="purple", linestyle="--", label="Secant result", zorder=3
        )

        # Set plot labels and title
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"{func_name} - Result {i+1}")
        plt.legend()
        plt.grid(True)

        # Save the plot
        plt.savefig(f"{func_name}/result_{i+1}.png")
        plt.close()
