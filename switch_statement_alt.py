
def some_function_for_case1():
    # code to execute for case1
    print("case1")

def some_function_for_case2():
    # code to execute for case2
    print("case2")

def some_function_for_case3():
    # code to execute for case3
    print("case3")

def some_function_for_default_case():
    # code to execute for all other cases
    print("Dafault case")

def some_function(argument):
    switcher = {
        'case1': lambda: some_function_for_case1(),
        'case2': lambda: some_function_for_case2(),
        'case3': lambda: some_function_for_case3()
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: some_function_for_default_case())
    # Execute the function
    return func()


print("Call switch statement")
some_function("case1")
