from Task4HW import create_dictionary
from Task4HW import polynomial

if __name__ == "__main__":
    my_dict = create_dictionary()
    print(my_dict)

    new_equation=polynomial(my_dict)
    print(new_equation)