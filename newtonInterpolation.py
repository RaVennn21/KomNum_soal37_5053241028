class NewtonInterpolation:
    def __init__(self, x, fx):
        self.x = x
        self.fx = fx
        self.n = len(x);
        self.divided_diff = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.divided_diff[i][0] = fx[i];

    def Calculate(self, target_x):
        self.__FirstOrde()
        self.__SecondOrde()
        self.__ThirdOrde()

        x0 = self.x[0]
        x1 = self.x[1]
        x2 = self.x[2]

        b0 = self.divided_diff[0][0]
        b1 = self.divided_diff[0][1]
        b2 = self.divided_diff[0][2]
        b3 = self.divided_diff[0][3]

        result = b0
        result += b1 * (target_x - x0)
        result += b2 * (target_x - x0) * (target_x - x1)
        result += b3 * (target_x - x0) * (target_x - x1) * (target_x - x2)

        return round(result, 2)

    def __FirstOrde(self):
        for i in range(self.n - 1):
            self.divided_diff[i][1] = (self.divided_diff[i + 1][0] - self.divided_diff[i][0]) / (self.x[i + 1] - self.x[i])

    def __SecondOrde(self):
        for i in range(self.n - 2):
            self.divided_diff[i][2] = (self.divided_diff[i + 1][1] - self.divided_diff[i][1]) / (self.x[i + 2] - self.x[i])

    def __ThirdOrde(self):
        for i in range(self.n - 3):
            self.divided_diff[i][3] = (self.divided_diff[i + 1][2] - self.divided_diff[i][2]) / (self.x[i + 3] - self.x[i])

x = [8, 10, 12, 14]
fx = [660, 1326, 2280, 3570]
target = 11

newtonInterpolation = NewtonInterpolation(x, fx)
result = newtonInterpolation.Calculate(target);

print(f"{result: .2f}");