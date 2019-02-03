import numpy
from matplotlib import pyplot as plt
if __name__ == '__main__':
    x = [1, 2, 3]
    plt.ion() # turn on interactive mode, non-blocking `show`
    for loop in range(0,3):
        y = numpy.dot(x, loop)
        plt.figure()   # create a new figure
        plt.plot(x,y)  # plot the figure
        plt.show()     # show the figure, non-blocking
        x = input("Press [enter] to continue.") # wait for input from the user
        plt.close()    # close the figure to show the next one.