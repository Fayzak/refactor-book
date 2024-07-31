class MathOperations:
    @staticmethod
    def calculate_square(x):
        return x * x
    
    def calculate_square_instance(self, x):
        return MathOperations.calculate_square(x)

class AreaCalculator:
    def __init__(self, math_operations):
        self.math_operations = math_operations

    def calculate_area(self, side_length):
        return self.math_operations.calculate_square_instance(side_length)

# Пример использования
math_operations = MathOperations()
area_calculator = AreaCalculator(math_operations)
area = area_calculator.calculate_area(5)
print(area)
