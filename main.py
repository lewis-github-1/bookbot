def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()        # stored frankenstein text
        words = file_contents.split()   # frankenstein text split into words
        words_count = len(words)        # word count
        
        letter_counts = count_char(file_contents)
        agg = aggregate(letter_counts)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words_count} words found in the document")
        for item in agg:
            print(f"The {item['name']} character was found {item['num']} times")
        print("--- End report ---")


def count_char(file_contents):
    lowered_file_contents = file_contents.lower()
    letter_count = {}
    for i in lowered_file_contents:
        if i.isalpha():
            if i not in letter_count:
                letter_count[i] = 1
            else:
                letter_count[i] += 1
    return letter_count
    
def aggregate(letter_counts):    
    dict_list = []
    for key, value in letter_counts.items():
        dict_list.append({"name": key, "num": value})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]



main()


