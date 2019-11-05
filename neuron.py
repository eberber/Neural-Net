import numpy as np
#reference: https://medium.com/@thomascountz/19-line-line-by-line-python-perceptron-b6f113b161f3
# https://towardsdatascience.com/what-the-hell-is-perceptron-626217814f53
class perceptron():
#######################################     GLOBAL  VAR   ############################################
    fileName = "nn_debug.txt"
    RGBList = []
    labelsList = []
    weightedSum = 0.0
    activation = 0 
#######################################    FUNCTIONS  ############################################
    def __init__(self, no_of_inputs, epochs=30, learning_rate=0.01):
        self.epochs = epochs
        self.learning_rate = learning_rate
        #init will be zero, but changes as we adjust in activation function 
        self.weights = np.zeros(no_of_inputs)

#splits input into RGB and label list
    def readFile(self):
        tempRGB = []  
        with open(self.fileName) as f:
            for i in f.readlines():
                for j in i.split():
                    if j.isdigit(): #int in string
                        tempRGB.append(int(j))
                    else: #found label
                        self.labelsList.append(j.strip('\n'))
                self.RGBList.append(tempRGB)
                tempRGB = []
        print(self.RGBList)
        print(self.labelsList)

# input * weight, then sums results
    def calcWeightedSum(self, color):
        for rgbValue in range(len(color)):
            self.weightedSum += color[rgbValue] * self.weights[rgbValue]
            print(self.weightedSum)                

#sets activation to 1 or 0    
    def prediction(self):
        if self.weightedSum > 0:
            self.activation = 1
        else:
            self.activation = 0            
#run for x epochs
    def runEpochs(self):
        self.readFile()
        #need to run for # of epochs and each RGB group
        for _ in range(self.epochs):
            for color, label in zip(self.RGBList, self.labelsList):
                self.calcWeightedSum(color)
                self.prediction()
                #modify weights
                self.weights += self.learning_rate * (1 - self.activation) #* color

#######################################     MAIN   ############################################
def main():
    neuron = perceptron(3) #takes RGB, so 3 
    neuron.runEpochs()

if __name__ == "__main__":
    main()