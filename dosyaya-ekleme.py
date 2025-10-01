#   open(dosyaAdi, dosyaErisimModu)
#   dosyaErisimModu => dosyayı hangi amaçla açtığımızı belirtir

#   "r": (Read) okuma. Dosya konumda yoksa hata verir.
#   "w": (Write) yazma modu
#       **Dosyayı konumda oluşturur.
#       ** Dosya içeriğini siler ve yeniden ekleme yapar
#   "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
#   "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.
with open("dosya.txt","r+",encoding="utf-8") as file:
    #file.seek(20)
    file.read()
    file.write("yeni satır\n")