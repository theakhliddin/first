stringMsg = "GCIS"
print(len((stringMsg)))

def rangeFtn(rangeAmount):
    length = len(rangeAmount)
    for i in range(length):
        print(rangeAmount[i])
        
def main():
    rangeFtn(range(0,11))
    rangeFtn(range(10, -1, -1))
    
if  __name__ == "__main__":
    main()