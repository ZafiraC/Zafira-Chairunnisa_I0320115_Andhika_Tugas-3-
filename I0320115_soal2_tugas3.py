#Membuat Dictionary
dict = {'Nama': 'Zafira Chairunnisa',
        'Hobi': ['Menonton drakor', 'Memasak', 'Olahraga'],
        'Sosmed': [
            'Instagram: zafiraaa.ch',
            'Twitter: woilahapeni',
            'Facebook: Zafira Chairunnisa'],
        'Lagu Favorit': ['Billie Eilish - my future', 'Niki - lose', 'Baekhyun - UN Village'],
        'Makanan Favorit': ['Tahu Kupat', 'Bakso', 'Pizza']}
print(dict)

#mengubah salah satu hobi
dict['Hobi'][1] = ('Travelling')

#mengubah salah satu sosmed
dict['Sosmed'] = [
        'Instagram: zafiraaa.ch'
        'Twitter: woilahapeni'
        'LinkedIn: Zafira Chairunnisa']

#menghapus 2 makanan favorit
del dict['Makanan Favorit'][1:3]

#menambah 1 hobi
dict['Hobi'].append('Menggambar')
print(dict)