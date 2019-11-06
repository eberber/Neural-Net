# Neural-Net
 To gain experience with implementing an artificial neural network and with the design choices that accompany using one.

# Requirements
 Ran using Python 3.7.3
 Learned weights are stored in weights.txt
 Best learned weights are in bestWeight.txt
 To run a test set through (without updating weights) and evaluate the correctness of the output firing, set epoch = 1
 Given a training and test set with only one example (for example, only red), network can learn to always fire that neuron and never fire any of the others. Set epoch to 100 then 500 and notice the rise in accuracy using nn_debug.txt

# Parameters
 The filename containing the training data.
    Can be modified under "GLOBAL VAR"
 The initial learning rate.
    Can be modified in perceptron constructor.
 The number of epochs.
    Can be modified in perceptron constructor.
 Whether to load in the initial weights for the neural network from a file or initialize them randomly
    Since its a perceptron, uses a constant 0 that changes as the program runs
