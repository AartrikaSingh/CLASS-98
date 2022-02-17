def countnumberofwords():
    filename=input("enter the file name:")
    numberofwords=0
    file=open(filename,"r")
    for line in file:
        word=line.split()
        numberofwords=numberofwords+len(word)
    print("Number Of Words:",numberofwords)
countnumberofwords()        
