class Queue():
    def __init__(self):
        self.cards = []

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def push(self, card):
        self.cards.append(card)
        

    #REMOVE PASS AND COMPLETE THE FUNCTION
    def pop(self):
        del self.cards[0]
    
        
        

if __name__ == '__main__':
    #REMOVE PASS AND YOUR CODE GOES HERE
    deck = Queue()
    deck.push(3)
    deck.push(4)
    deck.push(5)
    deck.pop()
    print(deck.cards)