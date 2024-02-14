import csv
ral=sorted('йцукенгшщзхъфываролджэячсмитьбюЮБЬТИМСЧЯЭЖДЛОРПАВЫФЙЦУКЕНГШЩЗХЪ')
eal=sorted('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
f=open('russian_artists.txt', 'w', encoding='utf8')
fa=open('foreign_artists.txt', 'w', encoding='utf8')
kr=0
ke=0
with open('songs.csv', encoding='utf8') as file:
    reader=csv.reader(file, delimiter=';')
    data=list(reader)[1:]
    for i in data:
        for z in range(len(i[1])):
            if i[1][z] in ral:
                f.write(i[1])
                f.write('\n')
                kr+=1
                break
        for z in range(len(i[1])):
            if i[1][z] in eal and i[1]!='unknown':
                fa.write(i[1])
                fa.write('\n')
                ke+=1
                break
print(f"Количество российских исполнителей: {kr}")
print(f"Количество иностранных исполнителей: {ke}")

