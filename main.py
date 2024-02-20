def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()        # stored frankenstein text
        words = file_contents.split()   # frankenstein text split into words
        words_count = len(words)        # word count
        print(words_count)

        count_char(file_contents)




def count_char(file_contents):
    lowered_file_contents = file_contents.lower()
    letter_count = {}
    for i in lowered_file_contents:
        if i.isalpha():
            if i not in letter_count:
                letter_count[i] = 1
            else:
                letter_count[i] += 1
    
    print(letter_count)
    


main()