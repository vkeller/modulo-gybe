# Define the number of inputs and the learning rate
num_inputs = 2
learning_rate = 0.1

# Initialize weights and bias randomly
weights = [0.5, 0.5]
bias = 0.5

# Define the training data for addition
training_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
training_outputs = [0, 1, 1, 2]

# Train the perceptron
for epoch in range(1000):
    total_error = 0
    for i in range(len(training_inputs)):
        # Forward pass
        output = 0
        for j in range(num_inputs):
            output += training_inputs[i][j] * weights[j]
        output += bias
        
        # Calculate the error
        error = training_outputs[i] - output
        total_error += abs(error)
        
        # Backward pass (update weights and bias)
        for j in range(num_inputs):
            weights[j] += learning_rate * error * training_inputs[i][j]
        bias += learning_rate * error
    
    # Print the total error at each epoch
    #print(f'Epoch {epoch+1}, Total Error: {total_error}')
    
    # Stop training if the total error is minimal
    if total_error == 0:
        break

# Test the trained perceptron
print('\nTesting the Perceptron:')
#test_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
test_inputs = [[3, 5], [2, 5], [2, 6], [12, 14]]
for test_input in test_inputs:
    output = sum([test_input[i] * weights[i] for i in range(num_inputs)]) + bias
    print(f'Input: {test_input}, Output: {output}')
