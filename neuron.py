import numpy as np
#reference: https://medium.com/@thomascountz/19-line-line-by-line-python-perceptron-b6f113b161f3
# https://towardsdatascience.com/what-the-hell-is-perceptron-626217814f53
class perceptron():
#######################################     GLOBAL  VAR   ############################################
    fileName = "nn_debug.txt"
#######################################################################################################
    def __init__(self, no_of_inputs, epochs=100, learning_rate=0.01):
        self.epochs = epochs
        self.learning_rate = learning_rate
        #init will be zero, but changes as we adjust in activation function 
        self.weights = np.zeros(no_of_inputs + 1)

    def readFile(self):
        self.fileName  
        input = []
        inputList = []      
        with open(self.fileName) as f:
            content = f.readlines()
        for i in content:
            input = i[:-1]
            inputList = inputList.append(input)
        print(inputList)

def main():
    neuron = perceptron(3)
    neuron.readFile()
if __name__ == "__main__":
    main()