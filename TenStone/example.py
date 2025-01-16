from tensor import Tensor 

# Generate training data
x = Tensor.linspace(-1, 1, 100).reshape(-1, 1)  # Input: column vector
y = x ** 2  # Target output

# Initialize weights and biases for a simple 2-layer network
W1 = Tensor.randn(1, 10, requires_grad=True)  # First layer weights
b1 = Tensor.zeros(10, requires_grad=True)  # First layer biases
W2 = Tensor.randn(10, 1, requires_grad=True)  # Second layer weights
b2 = Tensor.zeros(1, requires_grad=True)  # Second layer biases

# Training hyperparameters
learning_rate = 0.1
num_epochs = 1000

# Training loop
for epoch in range(num_epochs):
    # Forward pass
    z1 = x @ W1 + b1  # First layer linear transformation
    a1 = z1.tanh()  # Activation function
    z2 = a1 @ W2 + b2  # Second layer linear transformation
    y_pred = z2  # Output (no activation for regression)

    # Compute mean squared error loss
    loss = ((y_pred - y) ** 2).mean()

    # Backpropagation
    loss.backward()

    # Gradient descent: manually update weights and biases
    with Tensor.no_grad():
        W1 -= learning_rate * W1.grad
        b1 -= learning_rate * b1.grad
        W2 -= learning_rate * W2.grad
        b2 -= learning_rate * b2.grad

        # Clear the gradients
        W1.grad.zero_()
        b1.grad.zero_()
        W2.grad.zero_()
        b2.grad.zero_()

    # Print progress
    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# Test the trained model
x_test = torch.linspace(-1, 1, 10).reshape(-1, 1)
y_test_pred = (torch.tanh(x_test @ W1 + b1) @ W2 + b2).detach()
print("\nTest Results:")
print(f"Input: {x_test.squeeze().tolist()}")
print(f"Predicted Output: {y_test_pred.squeeze().tolist()}")

