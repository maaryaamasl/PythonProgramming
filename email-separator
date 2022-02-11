fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
count = 0
file = open(fname)
for line in file:
    words = line.split()
    if len(words)>1  and words[0].lower() == "from":
        print(words[1])
        count = count + 1
print("There were "+str(count)+" lines in the file with From as the first word")
        
        
    
