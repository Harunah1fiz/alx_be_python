
def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operations on two numbers based on the specified operation.
    
    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
    
    Returns:
    int or float: The result of the arithmetic operation.
    
    Raises:
    ValueError: If an unsupported operation is provided.
    ZeroDivisionError: If division by zero is attempted.
    """
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Unsupported operation. Use 'add', 'subtract', 'multiply', or 'divide'.")
