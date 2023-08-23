class Calculator:

    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(("add", x, y, result))
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.append(("subtract", x, y, result))
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.append(("multiply", x, y, result))
        return result

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        result = x / y
        self.history.append(("divide", x, y, result))
        return result

    def print_history(self):
        for operation, x, y, result in self.history:
            print(f"{operation}({x}, {y}) = {result}")

class Menu:

    def __init__(self):
        self.options = {
            "1": "Add",
            "2": "Subtract",
            "3": "Multiply".
            "4": "Divide"
        }

    def print_menu(self):
        for key, option in self.options.items():
            print(f"{key}. {option}")

    def get_input(self):
        choice = input("Enter choice: ")
        x = float(input("Enter x: ")) 
        y = float(input("Enter y: "))
        return choice, x, y

def main():
  menu = Menu()
  calculator = Calculator()

  while True:
      menu.print_menu()
      choice, x, y = menu.get_input()
      
      if choice == '1':
          result = calculator.add(x, y)
      # And so on
      
      print(result)
      
      if choice == 'q':
        print("Goodbye")
        break  
  calculator.print_history()

if __name__ == "__main__":
  main()