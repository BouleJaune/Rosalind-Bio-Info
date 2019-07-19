def id_string(string):
    return string[1:]

def GC_content(string):
    g = string.count("G")
    c = string.count("C")
    m = len(string)
    return (g+c)/m*100    


with open("test.txt","r") as f:
    content = ""   
    id = ""
    GC_max = 0
    GC = 0 
    k=0
    while True:    
        line = f.readline()
        line=line.replace("\n","")
        if len(line)==0:
            GC = GC_content(content) 
            if GC_max < GC:
                GC_max = GC
                id_max = id
            break
        if line[0]==">":
            if k>0:
                GC = GC_content(content) 
            if GC_max < GC:
                GC_max = GC
                id_max = id
            id = id_string(line)   
            content = ""
        else:
            content = content+line
            k+=1

print(id_max,GC_max)

