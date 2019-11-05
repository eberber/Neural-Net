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
    total = 0
#######################################    FUNCTIONS  ############################################
    def __init__(self, no_of_inputs, targetColor, epochs=100, learning_rate=0.1):
        self.epochs = epochs
        self.learning_rate = learning_rate
        #init will be zero, but changes as we adjust in activation function 
        self.weights = np.zeros(no_of_inputs)
        self.targetColor = targetColor
        self.correct = 0 #init to 0
        self.numCorrect = 0

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
                self.RGBList.append(np.array(tempRGB))
                tempRGB = []

# input * weight, then sums results
    def calcWeightedSum(self, color):
        for rgbValue in range(len(color)):
            self.weightedSum += color[rgbValue] * self.weights[rgbValue]

#sets activation to 1 or 0    
    def prediction(self):
        if self.weightedSum > 0:
            self.activation = 1
        else:
            self.activation = 0            

#states what perceptron thought was the right value
    def identifyColor(self, label):
        if self.targetColor == label and self.activation == 1: #color matched and we got a yes
            self.correct = 1
            self.numCorrect += 1
        elif self.targetColor == label and self.activation == 0:
            self.correct = 1
        elif self.targetColor != label and self.activation == 1: #color did not match but we got a yes
            self.correct = 0
        elif self.targetColor != label and self.activation == 0:
            self.correct = 0
            self.numCorrect += 1

#run for x epochs
    def trainNeuron(self):
        self.readFile()
        #need to run for # of epochs and each RGB group
        for _ in range(self.epochs):
            for color, label in zip(self.RGBList, self.labelsList):
                self.calcWeightedSum(color)
                self.prediction()
                self.identifyColor(label)
                self.weights += self.learning_rate * (self.correct - self.activation) * color
                self.total += 1

#######################################     MAIN   ############################################
def main():
    neronList = []
    colorList = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Brown', 'Pink', 'Gray']
    total = 0
    correct = 0
    #init 9 perceptrons of each color with 3 inputs each representing RGB
    for color in colorList:
        neuron = perceptron(3, color)
        neuron.trainNeuron()
        total += neuron.total
        correct += neuron.numCorrect
        neronList.append(neuron)
    print("TOTAL CORRECT", correct)
    print("TOTAL    ", total)
    print("TOTAL ACCURACY: ", round((correct/total) * 100, 2), "%")

if __name__ == "__main__":
    main()