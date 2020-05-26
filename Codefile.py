#This is a code file to print fibonacci series.
def fibonacci(n):
    a = 0
    b= 1
    series_list = [a, b]
    while len(series_list) <= n:
          i = a+b
          series_list.append(i)
          a = b
          b = i
    return series_list
fibonacci(6)    



