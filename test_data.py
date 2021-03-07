import matplotlib.pyplot as plt
from my_lib import DataProcessing

if __name__ == "__main__":
    d = DataProcessing()
    print(type(d))

    d.df["rating-number"].hist(bins=10)
    plt.show()