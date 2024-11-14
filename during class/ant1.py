def write_in_file(filePath):
    with open(filePath, 'a') as file:
        file.write("Hello, world!")
    

def main():
    filePath = "file2024.txt"
    write_in_file(filePath)
    
if  __name__ == "__main__":
    main()
