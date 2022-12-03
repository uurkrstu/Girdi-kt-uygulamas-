print("Hesaplama Uygulaması (Girdi ve Çıktılar (Net Kar Hesaplama)")

print("""
	İşlemler;
	1. Bakiye Sorgulama
	2. Girdiler
	3. Çıktılar
	Programdan çıkış için 'çıkış' yazınız.
	""")

bakiye = 0

while True:
	işlem = input("İşlemi Giriniz. ")

	if (işlem == "çıkış"):
		print("Uygulamadan çıkış yapılıyor...")
		print("Bizi kullandığınız için teşekkür ederiz.")
		break
	elif (işlem == "1"):
		print("Bakiyeniz şuanda {} türk lirasıdır.".format(bakiye))
	elif (işlem == "2"):
		girdi = int(input("Girdi tutarını ekleyiniz. "))
		bakiye += girdi

	elif  (işlem == "3"):
		çıktı = int(input("Çıktı tutarını giriniz. "))
		bakiye -= çıktı

	else:
		print("Lütfen geçerli bir işlem giriniz. ")