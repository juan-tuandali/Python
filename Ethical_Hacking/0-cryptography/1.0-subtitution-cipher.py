print('\n---Subtitution Cipher (kunci = huruf random) ---')

alphabeth = 'abcdefghijklmnopqrstuvwxyz' # alphabeth plain text

string = input('Masukkan kata / kalimat: ') 
key = (input('Masukkan kunci 26 huruf / sesuai dengan jumlah alphabeth (tidak boleh ada huruf yang sama!): ')) # kunci encrypt

result = ''

for i in range(len(alphabeth)):
    char1 = alphabeth[i]
    char2 = key[i]
    if 0 <= i < len(string):
        char = string[i] # memisahkan setiap huruf yang ada agar bisa dicari pada alphabeth di step selanjutnya 
        if char == ' ':
            continue
        loc_char = alphabeth.find(char) # mencari indeks huruf yang sama dari string pada alphabeth 
            
        result += key[loc_char] # panggil hasil dari key sesuai dengan lokasi karakter
    
print(f'Hasil enkripsi dari "{string}" : {result}')
