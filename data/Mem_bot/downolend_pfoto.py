import httplib2
import csv

csv_path = 'хуемесная все изображения.csv'
mem = [[],[],[]]
ol_size = 0
download_max = 50
with open(csv_path, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        mem[0].append(row[0])
        mem[1].append(row[1])
        mem[2].append(row[3])
#print(mem)

def download (url, mem_name,ol_size):
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    out = open('pfoto/' + mem_name, 'wb')
    mem_size = float(out.raw._blksize) / 1000000
    #round(mem_size,)
    ol_size = float(ol_size) + float(mem_size)
    out.write(content)
    out.close()
    return ol_size

def mem_name1 (i):
    a = mem[2][i] + ' ' + mem[0][i] + '.jpg'
    return a

for i in range(len(mem[0])) or ol_size<download_max:
    mem_name = mem_name1(i)
    ol_size = download (mem[1][i],mem_name,ol_size)
    print(i)
    print(ol_size)
