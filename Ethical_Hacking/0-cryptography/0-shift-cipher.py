print('\n---Shift/Caesar Cipher---')

alphabeth = 'abcdefghijklmnopqrstuvwxyz' # alphabeth plain text

string = input('Masukkan kata / kalimat: ') 
key = int(input('Masukkan nilai kunci: ')) # kunci pergeseran encrypt

result = ''

for i in range(len(string)):
    char = string[i] # memisahkan setiap huruf yang ada agar bisa dicari pada alphabeth di step selanjutnya  
    if char == ' ':
        continue
    loc_char = alphabeth.find(char) # mencari indeks huruf yang sama dari string pada alphabeth
    new_loc = loc_char + key # menambahkan indeks yang sudah ditemukan tadi dengan kunci encrypt nya
    if new_loc >= 26: # kondisi jikka key nya lebih dari jumlah alphabeth
        new_loc -= 26
    
    result += alphabeth[new_loc] 
    
print(f'Hasil enkripsi dari "{string}" : {result}') 
