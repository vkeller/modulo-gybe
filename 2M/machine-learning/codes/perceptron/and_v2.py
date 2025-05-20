# Inputs for the AND function
# Each tuple represents (input1, input2, expected_output)
data = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
]

# Weights initialization
weight1 = 0.0  # weight for input1
weight2 = 0.0  # weight for input2
bias = 0.0     # bias

# Learning rate
learning_rate = 0.1

# Training the perceptron for a number of epochs
epochs = 10
for epoch in range(epochs):
    print(f'Epoch {epoch + 1}/{epochs}')
    for x1, x2, expected in data:
        # Calculate the weighted sum
        weighted_sum = x1 * weight1 + x2 * weight2 + bias

        # Activation function (Step function)
        output = 1 if weighted_sum >= 0 else 0

        # Calculate the error
        error = expected - output

        # Update weights and bias
        weight1 += learning_rate * error * x1
        weight2 += learning_rate * error * x2
        bias += learning_rate * error

        # Debug output
        print(f'Input: ({x1}, {x2}) - Expected: {expected}, '
              f'Output: {output}, Error: {error}, '
              f'Weights: ({weight1:.4f}, {weight2:.4f}), Bias: {bias:.4f}')

# Final weights and bias
print(f'Final Weights: ({weight1:.4f}, {weight2:.4f}), Final Bias: {bias:.4f}')

# Testing the learned perceptron
for x1, x2, expected in data:
    # Calculate the weighted sum again
    weighted_sum = x1 * weight1 + x2 * weight2 + bias
    output = 1 if weighted_sum >= 0 else 0
    print(f'Testing Input: ({x1}, {x2}) - Predicted Output: {output}, Expected: {expected}')