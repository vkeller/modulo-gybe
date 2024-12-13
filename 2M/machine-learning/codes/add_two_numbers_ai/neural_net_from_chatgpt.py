import streamlit as st
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Function to generate the dataset
def generate_data(n_samples=100):
    x = np.random.uniform(1, 10, size=(n_samples, 2))
    y = np.sum(x, axis=1, keepdims=True)
    return x, y

# Function to initialize weights for visualization
def initialize_weights(input_dim, hidden_dim, output_dim):
    weights_input_hidden = np.random.uniform(-1, 1, (input_dim, hidden_dim))
    weights_hidden_output = np.random.uniform(-1, 1, (hidden_dim, output_dim))
    return weights_input_hidden, weights_hidden_output

def plot_neural_network(weights_input_hidden, weights_hidden_output):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Define neuron positions
    num_input = weights_input_hidden.shape[0]
    num_hidden = weights_input_hidden.shape[1]
    num_output = weights_hidden_output.shape[1]

    input_neurons = [(-1, 0.8 - i * 0.4) for i in range(num_input)]  # Dynamically adjust input neurons
    hidden_neurons = [(0, 0.6 - i * 0.4) for i in range(num_hidden)]  # Dynamically adjust hidden neurons
    output_neuron = [(1, 0.4)]  # Single output neuron

    # Draw input neurons
    for i, (x, y) in enumerate(input_neurons):
        ax.add_patch(plt.Circle((x, y), 0.05, color='blue', ec='black', lw=1.5))
        ax.text(x - 0.1, y, f"In {i+1}", fontsize=10, ha='right', va='center')

    # Draw hidden neurons
    for i, (x, y) in enumerate(hidden_neurons):
        ax.add_patch(plt.Circle((x, y), 0.05, color='green', ec='black', lw=1.5))
        ax.text(x, y + 0.1, f"Hid {i+1}", fontsize=10, ha='center', va='bottom')

    # Draw output neuron
    for i, (x, y) in enumerate(output_neuron):
        ax.add_patch(plt.Circle((x, y), 0.05, color='red', ec='black', lw=1.5))
        ax.text(x + 0.1, y, "Out", fontsize=10, ha='left', va='center')

    # Draw connections with color and annotations close to source neurons
    # Input to hidden
    for i, (x1, y1) in enumerate(input_neurons):
        for j, (x2, y2) in enumerate(hidden_neurons):
            weight = weights_input_hidden[i, j]
            color = cm.coolwarm((weight + 1) / 2)  # Normalize weight for color scale
            ax.plot([x1, x2], [y1, y2], color=color, lw=2)
            # Annotate close to the source neuron
            text_x, text_y = x1 + (x2 - x1) * 0.2, y1 + (y2 - y1) * 0.2
            ax.text(text_x, text_y, f"{weight:.2f}", fontsize=8, color='black', ha='center', va='center')

    # Hidden to output
    for i, (x1, y1) in enumerate(hidden_neurons):
        for j, (x2, y2) in enumerate(output_neuron):
            weight = weights_hidden_output[i, j]
            color = cm.coolwarm((weight + 1) / 2)  # Normalize weight for color scale
            ax.plot([x1, x2], [y1, y2], color=color, lw=2)
            # Annotate close to the source neuron
            text_x, text_y = x1 + (x2 - x1) * 0.2, y1 + (y2 - y1) * 0.2
            ax.text(text_x, text_y, f"{weight:.2f}", fontsize=8, color='black', ha='center', va='center')

    # Formatting
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 1)
    ax.axis('off')
    ax.set_title("Neural Network Structure with Weights")

    st.pyplot(fig)


# Initialize weights
st.session_state.weights_input_hidden, st.session_state.weights_hidden_output = initialize_weights(2, 2, 1)


# Neural network model
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(3, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_absolute_error')
    return model

# Streamlit UI
st.title("Neural Networks Demonstration: Learning to Add Two Numbers")

# User inputs
epochs = st.number_input("Number of epochs:", min_value=1, max_value=1000, value=50)
train_button = st.button("Train Neural Network")
reset_button = st.button("Reset Training Data and Weights")

# Global variables
if "data" not in st.session_state:
    st.session_state.data = generate_data()
if "model" not in st.session_state or reset_button:
    st.session_state.model = create_model()
    st.session_state.data = generate_data()
    st.session_state.epoch = 0
    st.session_state.history = {"mae": [], "predictions": []}
    st.session_state.weights_input_hidden, st.session_state.weights_hidden_output = initialize_weights(2, 2, 1)

# Epoch counter placeholder
epoch_counter = st.empty()

# Graph placeholders
col1, col2 = st.columns(2)
mae_plot_placeholder = col1.empty()
pred_vs_actual_plot_placeholder = col2.empty()

# Weight visualization placeholder
weight_visualization_placeholder = st.empty()

# Training and visualization
if train_button:
    x_train, y_train = st.session_state.data
    for epoch in range(epochs):
        # Train for one epoch
        history = st.session_state.model.fit(x_train, y_train, epochs=1, verbose=0)
        st.session_state.history["mae"].append(history.history["loss"][0])
        predictions = st.session_state.model.predict(x_train).flatten()
        st.session_state.history["predictions"] = predictions
        st.session_state.epoch += 1

        # Update weights
        st.session_state.weights_input_hidden = st.session_state.model.layers[0].get_weights()[0]
        st.session_state.weights_hidden_output = st.session_state.model.layers[1].get_weights()[0]

        # Update epoch counter
        epoch_counter.subheader(f"Epoch Counter: {st.session_state.epoch}")

        # Update MAE plot
        with mae_plot_placeholder:
            fig, ax = plt.subplots(figsize=(4, 3))
            ax.plot(st.session_state.history["mae"])
            ax.set_title("Mean Absolute Error (MAE) over epochs")
            ax.set_xlabel("Epochs")
            ax.set_ylabel("MAE")
            st.pyplot(fig)

        # Update Predicted vs Actual plot
        with pred_vs_actual_plot_placeholder:
            fig, ax = plt.subplots(figsize=(4, 3))
            ax.scatter(y_train, predictions, color="red", label="Predictions")
            ax.plot([0, 20], [0, 20], color="blue", label="Ideal Fit")
            ax.set_title("Predicted vs Actual")
            ax.set_xlabel("Actual Values")
            ax.set_ylabel("Predicted Values")
            ax.legend()
            st.pyplot(fig)

        # Update neural network weights visualization
        with weight_visualization_placeholder:
            plot_neural_network(
                st.session_state.weights_input_hidden,
                st.session_state.weights_hidden_output
            )

# User input for predictions
st.subheader("Test Neural Network After Training")
input1 = st.number_input("Input 1:", min_value=1.0, max_value=10.0, value=5.0)
input2 = st.number_input("Input 2:", min_value=1.0, max_value=10.0, value=5.0)
if st.button("Calculate Result"):
    prediction = st.session_state.model.predict(np.array([[input1, input2]])).flatten()[0]
    st.write(f"The predicted sum of {input1} and {input2} is {prediction:.2f}")

# NN Explanation Section
st.subheader("NNs Explained")
st.write("""
Neural networks simulate how the human brain processes information. They consist of layers:
1. **Input Layer**: Takes the data (e.g., two numbers).
2. **Hidden Layer**: Processes the data using weights and activation functions.
3. **Output Layer**: Produces the result (e.g., sum of numbers).

The network adjusts its weights during training to minimize the error between predicted and actual results.
""") 