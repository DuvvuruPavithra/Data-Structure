from linked_list import LinkedList


if __name__ == "__main__":
    link = LinkedList()
    with open("sample.txt", 'r') as file:
        data_file = file.read().split()
        print(data_file)
    data = "Welcome to python!"
    present = link.present_data(data)
    if present:
        link.remove(data)
    else:
        link.insert_end(data)
    string_ = link.to_string()
    with open("sample.txt", 'w') as file:
         file = open("sample.txt", 'w')
         file.write(string_)
