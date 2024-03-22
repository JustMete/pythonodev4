fibonacci = [1, 1]  

while len(fibonacci) < 20: 
    next_fib = fibonacci[-1] + fibonacci[-2]  
    fibonacci.append(next_fib)  

print(fibonacci)