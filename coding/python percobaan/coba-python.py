print ("halo")

#variabel

nama = "rafi nurul fauzan"
alamat = "jatinegara"

#gabungan

print(nama + alamat)

print ('''hallo oi oi
       
       saya rafi''')

print (f"hallo {nama}")

print ("hallo " + nama)

#if,else

ayam_kuning = "tidur"
ayam_merah = "makan"

if ayam_kuning == "tidur":
    print("buku cerita")
else:
    print("ajak bermain")

if ayam_merah == "tidur":
    print("buku cerita")
else:
    print("ajak bermain")

#input

input("nama anda: ")

#input_jawaban saja

nama_user = input("nama anda: ")

print(nama_user)

#input_jawaban_dan_text

nama_user = input("nama anda: ")

print(f"hallo {nama_user} salam kenal")

#contohbikinsoal


print('''cicak disungai bermain air 
ketika dia dirumah ayah tanya dari mana si cicak
si cicak menjawab dari sekolah
sicicak termasuk melakukan prilaku??
a.tidur b.makan c.berbohong''')

jawaban_user = input("jawaban yang benar antara a/b/c adalah: ")

if jawaban_user == "c":
    print("SELAMAT KAMU BENAR")
else:
    print("JAWABAN MU SALAH")