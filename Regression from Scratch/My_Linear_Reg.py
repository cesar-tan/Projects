class MyLinRegression:
    def __init__(self, learning_rate = 0.01):
        self.w = 0
        self.b = 0
        self.learning_rate = learning_rate
    
    # Make predictions
    def predict(self, x):
        return self.w * x + self.b
    
    # Calculate the cost
    def cost(self, x, y):
        m = x.shape[0]

        total_cost = 0

        for i in range(m):
            pred = self.predict(x[i])
            total_cost += (y[i] - pred)**2
        
        return total_cost / (2 * m)
    
    # Calculate the gradient
    def compute_gradient(self, x, y):
        
        m = x.shape[0]
        total_w = 0
        total_b = 0

        for i in range(m):
            error = self.predict(x[i]) - y[i]
            total_w += error * x[i]
            total_b += error
        
        return total_w / m, total_b / m
    
    # Function for gradient descent to find values for w and b. Basically like sklearn fit() function.
    def gradient_descent(self, x, y, iterations = 10000, tol = 1e-6):
        in_cost = float('inf')

        for i in range(iterations):
            dj_dw, dj_db = self.compute_gradient(x, y)
            self.w = self.w - (self.learning_rate * dj_dw)
            self.b = self.b - (self.learning_rate * dj_db)
            next_cost = self.cost(x, y)
        
            if abs(in_cost - next_cost) < tol:
                break
            in_cost = next_cost
        return self.w.item(), self.b.item()
