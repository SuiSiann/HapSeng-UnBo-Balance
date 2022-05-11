import csv

with open(
        '名姓字表 - 字姓.csv') as tong:
        reader = csv.reader(tong)
        next(reader, None)
        senn = []
        for pit in reader:
            senn.append(pit[2])


with open(
        '名姓字表 - 人名.csv') as tong:
        reader = csv.reader(tong)
        next(reader, None)
        senn_dict = {}
        ngangan_w = []
        ngangan_p = []
        for pit in reader:
            if '(文)' in pit[1]:
                ngangan_w.append(pit[0])
            if '(白)' in pit[1] or '(不標)' in pit[1]:
                ngangan_p.append(pit[0])
        print(ngangan_w, ngangan_p)




print(senn[0], 'X', ngangan_w[0])
print(senn[1], ngangan_w[1], 'X')
print('X', ngangan_w[2])
print(ngangan_w[3], 'X')

print(senn[0+2], 'X', ngangan_w[0+4])
print(senn[0+3], ngangan_w[0+5], 'X')
print('X', ngangan_w[0+6])
print(ngangan_w[0+7], 'X')

print(senn[0+2], 'X', ngangan_w[0+4])
print(senn[1+2], ngangan_w[1+4], 'X')
print('X', ngangan_w[2+4])
print(ngangan_w[3+4], 'X')

print(senn[0+4], 'X', ngangan_w[0+8])
print(senn[0+5], ngangan_w[0+9], 'X')
print('X', ngangan_w[0+10])
print(ngangan_w[0+11], 'X')

print(senn[0+2+2], 'X', ngangan_w[0+4+4])
print(senn[1+2+2], ngangan_w[1+4+4], 'X')
print('X', ngangan_w[2+4+4])
print(ngangan_w[3+4+4], 'X')