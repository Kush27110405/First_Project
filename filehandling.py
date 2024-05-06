#Open a file in read mode

#with open("c:/Users/Dell/Desktop/File handling/data.txt",'r') as file1:
    #read the file content
    #data = file1.read()
    #print(data)


#file1 = open("c:/Users/Dell/Desktop/File handling/data.txt",'w')
#data = "This is a file"
#file1.write(data)

#FileDescriptorLeakage:-
#file_descriptors = []
#for x in range(100000):
#    file_descriptors.append(open("c:/Users/Dell/Desktop/File handling/data.txt",'w'))

class FileManager():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

with FileManager("c:/Users/Dell/Desktop/File handling/data.txt",'w') as f:
    f.write("test")

print(f.closed)