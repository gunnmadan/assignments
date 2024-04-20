def build_dictionary(word_list): 
    word_frequency = {}
    for word in word_list: 
        word = word.lower()
        if word in word_frequency: 
            word_frequency[word] += 1
        else: 
            word_frequency[word] = 1
    return word_frequency

def main():
    text = input()
    word_list = text.split()
    print("\nWord List:")
    print(word_list)

    word_frequency = build_dictionary(word_list)

    print("\nBag of Words: ")
    for word, freq in sorted(word_frequency.items()):
        print(f'{word} - {freq}')

if __name__ == '__main__':
    main()        

