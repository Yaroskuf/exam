import csv
with open('songs.csv', encoding='utf8') as file:
    reader=csv.reader(file, delimiter=';')
    data=list(reader)[1:]
    for j in data:
        #a='Jun Takahira'
        a=str(input())
        if a=='0': break
        else:
            for i in data:
                if i[1] in a:
                    print(f'У {i[1]} найдена песня: {i[2]}')
                    break