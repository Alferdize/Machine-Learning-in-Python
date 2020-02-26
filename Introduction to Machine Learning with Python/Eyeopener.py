from pandas import read_csv
from matplotlib import pyplot as plt


def ploting(data, values):
    plt.figure()
    for i in range(values.shape[1]):
        plt.subplot(values.shape[1], 1, i+1)
        plt.plot(values[:, 1])
    plt.show()


if __name__ == "__main__":
    eye_data = read_csv("Eye_State.csv", header=None)
    values = eye_data.values
    ploting(eye_data, values)
