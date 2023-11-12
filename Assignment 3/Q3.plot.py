import matplotlib.pyplot as plt
import numpy as np

FIGURE_NUMBER_START_WITH = 1

sleep_quality = {
    "name": "Sleep Quality",
    "data": {
        "Poor": np.array([[0, 1], [2, 1], [4, 0]]),
        "Fair": np.array([[2, 0], [4, 1], [6, 0]]),
        "Good": np.array([[4, 0], [6, 1], [8, 0]]),
        "Excellent": np.array([[6, 0], [8, 1], [10, 1]])
    }
}

leisure_time = {
    "name": "Leisure Time",
    "data": {
        "Minimal": np.array([[0, 1], [3, 1], [6, 1], [9, 0]]),
        "Moderate": np.array([[6, 0], [9, 1], [12, 1], [15, 0]]),
        "Adequate": np.array([[12, 0], [15, 1], [18, 1], [21, 0]]),
        "Plenty": np.array([[18, 0], [21, 1], [24, 1]])
    }
}

stress_level = {
    "name": "Stress Level",
    "data": {
        "Calm": np.array([[0, 1], [3, 1], [6, 0]]),
        "Moderate": np.array([[3, 0], [6, 1], [9, 0]]),
        "Intense": np.array([[6, 0], [9, 1], [12, 0]]),
        "Extreme": np.array([[9, 0], [12, 1], [15, 1]])
    }
}

for index, variable in enumerate((sleep_quality, leisure_time, stress_level)):
    name = variable["name"]
    data = variable["data"]
    figure_number = FIGURE_NUMBER_START_WITH + index

    x_lower_bound = min(min(array[:, 0]) for array in data.values())
    x_upper_bound = max(max(array[:, 0]) for array in data.values())
    y_lower_bound = min(min(array[:, 1]) for array in data.values())
    y_upper_bound = max(max(array[:, 1]) for array in data.values())

    plt.figure(figure_number, figsize=(15, 4))
    plt.xlim(x_lower_bound, x_upper_bound)
    plt.ylim(y_lower_bound, y_upper_bound + 0.2)
    plt.xlabel(name)
    plt.ylabel("Value")

    for key, value in data.items():
        plt.plot(value[:, 0], value[:, 1], label=key)

    plt.legend()

    plt.grid(True)
    plt.savefig(f"Figure.3.{figure_number}.svg")
