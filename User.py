# your improved User class goes here

user_list = []
class User:
    
    message_board = []
    
    def __init__(self, name, email_address, drivers_license_number):
        self.name = name
        self.email = email_address
        self.license = drivers_license_number
        self.my_posts = []
        
    def __str__(self):
        return f'{self.name}, {self.email}, {self.license}'
    
    def post(self, message):
        self.my_posts.append(message)
        User.message_board.append({self.name: message})
        # print(User.message_board)
        pass
    
    def delete_my_last_post(self):
        for post in range(len(User.message_board), 0, -1):
            index = post-1
            if self.name in User.message_board[index]:
                del User.message_board[index]
                break
    
    def see_all_posts():
        return User.message_board
            
Alice = User('Alice', 'email@address.com', '111-222-3333')
Dale = User('Dale', 'Dale123@email.com', '111-555-1234')
Sarah = User('Sarah', 'SarahAgain@email.com', '555-123-4444')

Alice.post("Alice is posting")
Dale.post("Dale made a post")
Sarah.post("Sarah can post too!")
Dale.post("Dale talks too much")

print(User.message_board)
Dale.delete_my_last_post()
print(User.message_board)