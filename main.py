class Queue():
    def __init__(self):
        self.cards = []

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def push(self, card):
        self.cards.append(card)
        

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def pop(self):
        if len(self.cards) == 0:
            return None
        else:
              return self.cards.pop(0)
        

if __name__ == '__main__':
    #REMOVE PASS AND YOUR CODE GOES HERE
        queue = Queue() 
queue.push("Card1")  
queue.push("Card2")
queue.push("Card3")
print("Popped:", queue.pop())  
print("Popped:", queue.pop())
print("Popped:", queue.pop())
print("Popped:", queue.pop())