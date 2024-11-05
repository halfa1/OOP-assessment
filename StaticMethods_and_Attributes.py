class Calculator:
    count = 0
    @staticmethod
    def sum(x,y):
        #increment count after calling sum
        Calculator.count += 1
        return x+y

#demonstrating usage
sum1 = Calculator.sum(9,10)

print(f'sum is : {sum1}')
print(f'sum method called {Calculator.count} times')

sum2 = Calculator.sum(10,11)

print(f'sum is : {sum2}')
print(f'sum method called {Calculator.count} times')