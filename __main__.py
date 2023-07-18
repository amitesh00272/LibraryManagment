####### Library

class Library:
    def __int__(self):
        self.List = [
            'Django',
            'Python IDE',
            'Java',
            'Computer Application',
            'Encyclopedia',
            'Science World',
            'Software Engineer',
            'English'
        ]

        self.BorrowBookList = (
            'Django',
            'Python IDE',
            'Java',
            'Computer Application',
            'Encyclopedia',
            'Science World',
            'Software Engineer',
            'English'
        )

    def mainCode(self):
        print('Welcome in the library!!!!')
        print('>This the library that is made using python language.')

        while True:
            print('\nChoose any one:')
            print('1.Borrow')
            print('2.List Of Book')
            print('3.Returning Book')
            print('4.Quit')

            YourChoice = int(input('\n🍑🍑Enter your choice🎀🎀: '))

            def ReturnBook():
                ReturnBook = input('\nஜ۩۞۩ஜ Which Book You Want To Return ஜ۩۞۩ஜ ')
                if ReturnBook in self.BorrowBookList:
                    self.List.append(ReturnBook)

            def Borrow():
                BorrowBook = input('\nஜ۩۞۩ஜ Which Book You Want To Borrow ஜ۩۞۩ஜ ')
                if BorrowBook in self.BorrowBookList:
                    TellMe = int(input('🍑🍑For How Many Days You Take This Book💖💖 '))

                    if TellMe <= 201:
                        print(f'OK!! You Can Take {BorrowBook} Book')
                        self.List.remove(f"{BorrowBook}")


                    else:
                        print('Sorry!! Your take this book for only 20 days.')


            def ListOfBook():
                print('»»------(¯`This is the some list of book that are available in library´¯)------»»')
                BookList = self.List
                for i in BookList:
                    print(i)

            if YourChoice == 1:
                Borrow()

            elif YourChoice == 2:
                ListOfBook()

            elif YourChoice == 3:
                ReturnBook()

            elif YourChoice == 4:
                quit()

            else:
                print('Error: This option is not present in Library.')
                print('Try Again!!')


if __name__ == '__main__':
    ### Class Call ###
    SoftwareEngineer = Library()
    SoftwareEngineer.__int__()

    SoftwareEngineer.mainCode()



