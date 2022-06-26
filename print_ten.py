def print_ten(word):
    counter = []
    for i in range(1,11):
        counter.append(f'{i} {word}')  
    return " ".join(counter)

print(print_ten("123"))