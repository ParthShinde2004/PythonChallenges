from matplotlib.pyplot import ylabel, plot, show, xlabel, title
import math
import numpy as np

print("1. Constant \n2. Linear \n3. Log \n4. Quadratic \n5. Exponential \n6. Factorial")

choice = input('What type of graph do you want to see? (Type number)')


def draw_graph(graph):
    if choice == '1':
        x = [2, 4, 6, 8, 10, 12]
        y = [2, 2, 2, 2, 2, 2]
        
        plot(x, y, 'b')
        xlabel('Input')
        ylabel('Steps')
        title('Constant Complexity')
        show()

    elif choice == '2':
        x = np.arange(0, 100)
        y = x

        plot(x, y, 'b')
        xlabel('Input')
        ylabel('Steps')
        title('Linear Complexity')
        show()
        
    elif choice == '3':
        x = np.arange(0, 100)
        y = np.log10(x)

        plot(x, y, 'b')
        xlabel('Input')
        ylabel('Steps')
        title('Logarithmic Complexity')
        show()

    elif choice == '4':
        x = np.arange(0, 100)
        y = x**2

        plot(x, y, 'b')
        xlabel('Input')
        ylabel('Steps')
        title('Quadratic Complexity')
        show()
        
    elif choice == '5':
        x = np.arange(0, 100)
        y = np.exp(x)

        plot(x, y, 'b')
        xlabel('Input')
        ylabel('Steps')
        title('Exponential Complexity')
        show()
        
    elif choice == '6':
        x = np.arange(0, 100)
        y = math.factorial(x)

        plot(x, y, 'b')
        xlabel('Input')
        ylabel('Steps')
        title('Factorial Complexity')
        show()
        
draw_graph(choice)
