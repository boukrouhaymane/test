#! /usr/bin/python

def f(x: int) -> int:
    '''return double of an integer'''
    return 2*x

def say_hello(name: str):
    print(f'Hello {name}!')

if __name__ == '__main__':
    print(f(0))
