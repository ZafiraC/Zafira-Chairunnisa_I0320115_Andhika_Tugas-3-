#List nama teman
teman = ['Tsania', 'Salma', 'Yuku', 'Yola', 'Sekar', 'Zaneta', 'Maurich', 'Titus','Alvin', 'Riri']

#print indeks ke 4,6,7
print("teman[4]: ", teman[4])
print("teman[6:8]: ", teman[6:8])

#remove teman 3,5,9
teman.remove('Yola')
teman.remove('Zaneta')
teman.remove('Riri')

#insert teman 3,5,9
teman.insert(3,'Rio')
teman.insert(5,'Aji')
teman.insert(9,'Rara')
print(teman)

#menambahkan 2 teman
teman.extend(['Gea', 'Tazkiya'])
print(teman)

#melakukan perulangan pada list teman
x = 0
for y in range (0,12):
    print(teman[x])
    x = x + 1

#menampilkan panjang list
print(len(teman))
