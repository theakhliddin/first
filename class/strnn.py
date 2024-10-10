def wordsearch(file):
    f = open(file, "r")
    read = f.read()
    f.close()
    word = input("Enter the word to be searched: ")
    detector = 0
    words = read.split()
    for i in words:
        if i == word:
            print("Words was found: ", i)
            detector = 1
        if detector == 0:
            print("Word was not found")
def main():
    file = input("Enter file name: ")
    wordsearch(file)