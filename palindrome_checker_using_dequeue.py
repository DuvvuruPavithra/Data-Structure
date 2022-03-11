class Deque(object):
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isempty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek_front(self):
        return self.items[0]

    def peek_rear(self):
        return self.items[-1]


def main(data):
    deque = Deque()
    for character in data:
        deque.add_rear(character)
    while deque.size() >= 2:
        front_item = deque.remove_front()
        rear_item = deque.remove_rear()

        if rear_item != front_item:
           print("It is not a palindrome")
           break
        else:
           print("It is  a palindrome")
           break

if __name__ == "__main__":
    string = input("Enter string to be checked:")
    main(string)