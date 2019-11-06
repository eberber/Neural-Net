import numpy as np

class perceptron():
#######################################     GLOBAL  VAR   ############################################
    fileName = "nn_debug.txt"
    weightedSum = 0.0
    activation = 0 
#######################################    FUNCTIONS  ############################################
    def __init__(self, no_of_inputs, targetColor, epochs=500, learning_rate=0.3):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.labelsList = [] #label color
        self.RGBList = [] #color as rgb value
        self.weights = np.zeros(no_of_inputs) #init will be CONSTANT zero, but changes as we adjust in activation function 
        self.targetColor = targetColor #neurons color
        self.correct = 0 #correct value to be used in activation function
        self.firedCorrectly = 0 #how many values we guess correctly
        self.falsePositive = 0 #fired when it should not have
        self.falseNegative = 0 #fired when it should have
        self.multiFire = 0 #keep track of data that cause multiple neurons to fire
        self.zeroFire = 0  #keep track of data that cause zero neurons to fire
        self.myTotal = 0 #keep track of perceptrons total only, not overall

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
            self.correct = 1 #what the label actually is supposed to be, regardless of whether we thought it was right or wrong
            self.firedCorrectly += 1 #correctly guessed it was the color we are
            self.multiFire += 1
        elif self.targetColor == label and self.activation == 0:
            self.correct = 1
            self.falseNegative += 1 #fail to fire
            self.zeroFire += 1
        elif self.targetColor != label and self.activation == 1: #color did not match but we got a yes
            self.correct = 0
            self.falsePositive += 1 #fail to guess right
            self.multiFire +=1 
        elif self.targetColor != label and self.activation == 0:
            self.correct = 0
            self.firedCorrectly += 1 #corectly guessed it was not the color we are
            self.zeroFire += 1

    #stores weights
    def storeWeights(self):
        f = open("weights.txt", "w")
        f.write(str(self.weights))
        f.close

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
                self.myTotal += 1

#######################################     MAIN   ############################################
def main():
    neronList = []
    colorList = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'Brown', 'Pink', 'Gray']
    total = 0
    correct = 0
    multiFire = 0
    zeroFire = 0
    #init 9 perceptrons of each color with 3 inputs each representing RGB
    #each perceptron will do x num of epochs and data
    for color in colorList:
        neuron = perceptron(3, color)
        neuron.trainNeuron()
        total += neuron.myTotal
        correct += neuron.firedCorrectly
        multiFire += neuron.multiFire
        zeroFire += neuron.zeroFire
        neuron.storeWeights()
        print("PERCEPTRON: ", neuron.targetColor)
        print("PERCEPTRONS ACCURACY: ", round((neuron.firedCorrectly/neuron.myTotal) * 100,2), "%")
        if neuron.falsePositive != 0:
            print("FALSE POSITIVES: ", round((neuron.falsePositive/neuron.myTotal) * 100,2), "%")
        else:
            print("NO FALSE POSITIVES")
        if neuron.falseNegative != 0:
            print("FALSE NEGATIVES: ", round((neuron.falseNegative/neuron.myTotal)* 100,2), "%\n")
        else:
            print("NO FALSE NEGATIVES\n")
        neronList.append(neuron)
    print("PERCENT OF DATA CAUSING MULTIPLE NEURON FIRE", round((multiFire/total) * 100, 2), "%")
    print("PERCENT OF DATA CAUSING ZERO NEURON FIRE", round((zeroFire/total) * 100, 2), "%")
    print("TOTAL CORRECT", correct)
    print("TOTAL    ", total)
    print("PERFECTLY CLASSIFIED: ", round((correct/total) * 100, 2), "%")

if __name__ == "__main__":
    while 1:
        main()
        choice = input("Run again? Enter 'n' to stop: ")
        if choice == 'n':
            break