def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word

def main():
    sentence = "The quicksilver brown fox jumps over the lazy dog"
    longest_word = find_longest_word(sentence)
    print("The longest word is: " + longest_word)

if __name__ == "__main__":
    main()