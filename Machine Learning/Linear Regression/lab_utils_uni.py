import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Plot intuition (cost vs parameter)
# -------------------------------------------------
def plt_intuition(x, y, w_range=(-2, 2)):
    w_values = np.linspace(w_range[0], w_range[1], 50)
    costs = []

    for w in w_values:
        cost = np.mean((w*x - y)**2) / 2
        costs.append(cost)

    plt.plot(w_values, costs)
    plt.xlabel("w")
    plt.ylabel("Cost")
    plt.title("Cost vs Parameter w")
    plt.show()


# -------------------------------------------------
# Stationary cost plot
# -------------------------------------------------
def plt_stationary(x, y):
    w_values = np.linspace(-2, 2, 100)
    costs = []

    for w in w_values:
        cost = np.mean((w*x - y)**2) / 2
        costs.append(cost)

    plt.figure()
    plt.plot(w_values, costs)
    plt.title("Stationary Cost Function")
    plt.xlabel("w")
    plt.ylabel("Cost")
    plt.show()


# -------------------------------------------------
# Interactive click update (simplified)
# -------------------------------------------------
def plt_update_onclick(x, y):
    fig, ax = plt.subplots()

    ax.scatter(x, y)

    line, = ax.plot([], [], color="red")

    def onclick(event):
        w = event.xdata
        if w is None:
            return
        y_pred = w * x
        line.set_data(x, y_pred)
        fig.canvas.draw()

    fig.canvas.mpl_connect("button_press_event", onclick)
    plt.title("Click on graph to change slope")
    plt.show()


# -------------------------------------------------
# Soup bowl cost surface (3D visualization)
# -------------------------------------------------
def soup_bowl():
    from mpl_toolkits.mplot3d import Axes3D

    w = np.linspace(-2, 2, 50)
    b = np.linspace(-2, 2, 50)
    W, B = np.meshgrid(w, b)

    J = W**2 + B**2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(W, B, J, cmap='viridis')

    ax.set_xlabel("w")
    ax.set_ylabel("b")
    ax.set_zlabel("Cost")

    plt.title("Cost Function Surface (Soup Bowl)")
    plt.show()