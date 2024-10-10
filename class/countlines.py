def count_lines_words_char(filePath):
    with open(filePath, "r") as f:
        lineCount = 0
        wordCount = 0
        charCount = 0
        
        for line in f:
            lineCount =  lineCount + 1
           
            StrippedWords = line.strip()
            words = StrippedWords.split()
            wordCount = wordCount + len(words)
            
            
            
            print("Line count", lineCount)
            print("Word count", wordCount)
            print("Characcters count", charCount)

    
    
    
    
def main():
    filePath = "first/class/any.txt"
    count_lines_words_char(filePath)
    
if  __name__ == "__main__":
    main()
