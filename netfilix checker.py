import requests

def netflix_checker(api_token, telegram_id, dosya_yolu):
    try:
        with open(dosya_yolu, 'r') as dosya:
            for satir in dosya:
                kullanici = satir.strip()
                headers = {'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'}
                data = {"username": kullanici}
                response = requests.post("https://api.netflix.com/check", headers=headers, json=data)
                veri = response.json()
                if veri['status'] == 'SUCCESS':
                    print(f"{kullanici} NETFLİX BAŞARİLİ GİRİŞ ")
                elif veri['status'] == 'ERROR':
                    print(f"{kullanici}  Netflix başarisiz giriş ")
                
                # Telegram'a bilgi gönder
                requests.post(f"https://api.telegram.org/bot{telegram_id}/sendMessage", data={'chat_id': telegram_id, 'text': f"{kullanici} hesabı kontrol edildi: {veri['status']}"})
    except FileNotFoundError:
        print("Dosya bulunamadı!")
print("                TELEGRAM @MTNOWERPRX")
print("            _____________________________________                                    -_-    NETFLİX CHECKER")
           


api_token = input("TOKEN GİR : ")
telegram_id = input("İD GİR KANKA ")
dosya_yolu = input("DOSYA YOLU GİR KANKA: ")
netflix_checker(api_token, telegram_id, dosya_yolu)