class expression :
  def __init__(self):


    def choose_operator() :
      print("Choose an operator to continue")
      print('+')
      print('-')
      print('x')
      print('/')
      choice = input()

      num1 = int(input("Enter a number"))
      num2 = int(input("Enter another number"))
       
      if choice not in ['+', '-', 'x', '/'] :
        print("Invalid Choice")

      else :
        choice = str(choice)

      if choice == '+' :
        print(num1 + num2)

obj = expression