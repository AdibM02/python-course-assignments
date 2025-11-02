def get_user_input():
    """
    Get the base and height values from user input.
    
    Returns:
        tuple: A tuple containing the base and height values as floats
    """
    while True:
        try:
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            if base <= 0 or height <= 0:
                print("Please enter positive numbers for base and height.")
                continue
            return base, height
        except ValueError:
            print("Please enter valid numbers for base and height.")

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.
    
    Args:
        base (float): The length of the triangle's base
        height (float): The height of the triangle
    
    Returns:
        float: The area of the triangle
    """
    area = 0.5 * base * height
    return area

# Main program
if __name__ == "__main__":
    # Get input from user
    base, height = get_user_input()
    
    # Calculate and display the area
    area = calculate_triangle_area(base, height)
    print(f"\nThe area of the triangle with base {base} and height {height} is: {area}")
