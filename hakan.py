# Fill in this file with the code from parsing JSON exercise
#Buralar değerlenir
import json #otomatik doldurmada büyük harf çıkıyor. büyük harf hata veriyor
dosya = open("hakan.json", "r")
json_dosya = json.load(dosya)
print(json_dosya["karsilama"])
print("Ad:",json_dosya["Ad"])
print("Soyad:",json_dosya["Soyad"])
print("e-mail:",json_dosya["e-mail"])
print(json_dosya["ugurlama"])
