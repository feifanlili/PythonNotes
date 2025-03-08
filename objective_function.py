import numpy as np
import matplotlib.pyplot as plt

class ObjectiveFunction():
     def __init__(self, xBound:list, yBound:list, objective_function_id, dimension = 2):
        self.dimension = dimension
        self.xBound = xBound
        self.yBound = yBound
        self.objective_function_id = objective_function_id

     def f(self, x, y): # define objective function
        if self.objective_function_id==1:
            result = x ** 2.0 + y ** 2.0
        elif self.objective_function_id==2:
            result = np.sin(x) ** 2.0 + np.sin(y) ** 2.0 + 0.005 * (x ** 2.0 + y ** 2.0)
        elif self.objective_function_id==3:
            result = 50.0 * abs(x + y) + x ** 2.0
        elif self.objective_function_id==4:
            result = x ** 2.0 + 50.0 * y ** 2.0
        elif self.objective_function_id==5: # Ackley function
            X = np.asarray([x, y])
            a = 20.0
            b = 0.2
            c = 2 * np.pi
            s = (
        -a * np.exp(-b * np.sqrt(1.0 / 2 * np.sum(np.square(X), 0)))
        - np.exp(1.0 / 2 * np.sum(np.cos(c * X), 0))
        + a
        + np.exp(1)
    )
            result = s

        elif self.objective_function_id==6: # Levy function
            wx = (x + 3.0) / 4.0
            wy = (y + 3.0) / 4.0
            s = np.sin(np.pi * wx) ** 2 + (wy - 1) * (wy - 1) * (
        1 + np.sin(2 * np.pi * wy) ** 2
    )
            s += (wx - 1) * (wx - 1) * (1 + 10 * np.sin(np.pi * wx) ** 2)
            result = s
        else:
            result = 0
            print("Not valid function id!")

        return result
     
     def visualization(self,delta=0.5,showPlot=True):
         # generate sample data
        x = np.arange(self.xBound[0],self.xBound[1],delta)
        y = np.arange(self.yBound[0],self.yBound[1],delta)
        print(x)
        print(y)
        X,Y = np.meshgrid(x,y)
        Z = self.f(X, Y)
        print(Z)

        fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2)
        ax1 = fig.add_subplot(1, 2, 1, projection="3d")
        ax2 = fig.add_subplot(1, 2, 2)
        ax1.plot_surface(X, Y, Z, cmap="coolwarm")
        ax2.contour(X, Y, Z, cmap="coolwarm")
        if showPlot:
            plt.show()
