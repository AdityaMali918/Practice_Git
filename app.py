import functools

def add(*a):
   print(type(a))
   sum_number = sum(a)
   print(f'Sum: {sum_number}')

def multiply(*b):
   ans = functools.reduce(lambda x,y: x*y ,b)
   print(f'Multiply: {ans}')

if __name__ == "__main__":
   add(1,2,3)   
