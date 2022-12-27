from Task4HW import create_equation
from Task4HW import decode

if __name__ == "__main__":
    equation = create_equation()
    print(equation)
    new_equation=decode(equation)
    print(new_equation)
