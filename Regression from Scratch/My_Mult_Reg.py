import numpy as np

class MyMultRegression:
    def __init__(self, learning_rate = 0.01):
        self.w = None
        self.b = 0
        self.learning_rate = learning_rate
    
    def set_coeffs(self, x):
        self.w = np.zeros(x.shape[1])

    def predict(self, x):
        return x.dot(self.w) + self.b
    
    def cost(self, x, y):
        m = x.shape[0]
        error = y - self.predict(x)
        total_cost = np.sum(error ** 2)
        return total_cost / (2 * m)
    
    def gradient(self, x, y):
        m, n = x.shape
        total_w = np.zeros(n)
        total_b = 0

        for i in range(m):
            error = self.predict(x[i]) - y[i]
            for j in range(n):
                total_w[j] += error * x[i, j]
            total_b += error
        
        return total_w / m, total_b / m
    
    def gradient_descent(self, x, y, iterations, tolerance):
        in_cost = float('inf')

        for i in range(iterations):
            dj_dw, dj_db = self.gradient(x, y)
            self.w = self.w - (self.learning_rate * dj_dw)
            self.b = self.b - (self.learning_rate * dj_db)
            next_cost = self.cost(x, y)

            if abs(in_cost - next_cost) < tolerance:
                break
            in_cost = next_cost
        return self.w.tolist(), self.b.item()
