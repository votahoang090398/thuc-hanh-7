k=open('D:/a,txt','r')
char,wc,lc=0,0,0
for line in k:
    for k in range(0,len(line)):
        char +=1
        if(line[k]==' '):
            wc+=1
        if(line[k]=='\n'):
            wc,lc=wc+1,lc+1
print("The no.of chars is %d\n The no.of word is %d\n The no.of line is $d"%(char,wc,lc))
           
