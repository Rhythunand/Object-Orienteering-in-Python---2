class library :
  def __init__(self,list,name):
    self.list = list
    self.name = name
    self.lendDict = {}

    def displayBooks(self) :
      print("We have following Books in our library : {self.name}")
      for book in self.list :
        print(book)

    def lendBook(self,user,book) :
      if book not in self.lendDict.keys() :
        self.lendDict.update({book:user})
        print("Lender book database has been updated now you can take the book")

      else :
        print(f"Boom is already being used by {self.lendDict[book]}")
    
    def addBook(self,book) :
      self.list.append(book)
      print("Book has been added to your book list")
    
    def returnBook(self,book) :
      self.lendDict.pop(book)
  
if __name__ == '__main__' :
  books = library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ basics', 'Algorithms ny CLRS'], "Lets Upskill")


  while True :

    print("Welcome to {books.name} library. Enter your choice to continue")
    print('1. Display Book')
    print('2. Lend a book')
    print("3. Add a book")
    print('4. Return a book')
    user_choice = input()
    if user_choice not in ['1', '2', '3', '4'] :
      print("Please enter a valid choice")
      continue

    else :
      user_choice = int(user_choice)

    if user_choice == 1 : 
      books.displayBooks()
    
    elif user_choice == 2 : 
      print("Enter the name of the book you want to lend")
      user = input("Enter your name")
      books.lendBook(user, book)

    elif user_choice == 3 :
      book =  input("Enter the nam")