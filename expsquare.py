import numpy as np
import matplotlib.pyplot as plt


def main():
    k = np.linspace(-3, 3, 20)
    g = np.sqrt(np.pi) * np.exp(-(np.square(k))/4)

    plt.figure()
    plt.plot(k, g)
    plt.xlabel('k')
    plt.ylabel('g(k)')

    plt.show()

if __name__ == '__main__':
    main()