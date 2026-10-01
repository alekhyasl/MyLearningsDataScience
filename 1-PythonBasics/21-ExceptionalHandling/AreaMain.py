# Main is the entry point of execution in other programming languages like java

# In python also we can define entry point using __main__

def calculate_triangle_area(base,height):
    print("value of __name__: ",__name__)
    return (base*height)/2

if __name__ == "__main__":
    print("Area : ",calculate_triangle_area(3,4))