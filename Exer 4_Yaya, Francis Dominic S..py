file_text = open("DNA.txt").read()
file_text
len(file_text)

n=0
for char in file_text:
    if char=='C' or char=='G':
        n = n + 1
print (n/18.0)*100
