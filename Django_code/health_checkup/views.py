from django.shortcuts import render, redirect
from .models import Detail
from datetime import datetime
import base64, six
from django.contrib.auth.models import User, auth

# def encrypt(key, source, encode=True):
#     key = SHA256.new(key.encode('utf8')).digest()  # use SHA-256 over our key to get a proper-sized AES key
#     IV = Random.new().read(AES.block_size)  # generate IV
#     encryptor = AES.new(key, AES.MODE_CBC, IV)
#     padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
#     source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
#     data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
#     return base64.b64encode(data).decode("latin-1") if encode else data


def encrypt(string, key):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    encoded_string = encoded_string.encode('latin') if six.PY3 else encoded_string
    encoded_string =  base64.urlsafe_b64encode(encoded_string).rstrip(b'=')
    return encoded_string.decode('utf8')

def decrypt(string, key):
    string = bytes(string,'utf8')
    string = base64.urlsafe_b64decode(string + b'===')
    string = string.decode('latin') if six.PY3 else string
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


# def decrypt(key, source, decode=True):
#     if decode:
#         source = base64.b64decode(source.encode("latin-1"))
#     key = SHA256.new(key.encode('utf8')).digest()  # use SHA-256 over our key to get a proper-sized AES key
#     print(source)
#     IV = source[:AES.block_size]  # extract the IV from the beginning
#     print(IV)
#     decryptor = AES.new(key, AES.MODE_CBC, IV)
#     data = decryptor.decrypt(source[AES.block_size:])  # decrypt)
#     padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
#     if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
#         raise ValueError("Invalid padding...")
#     return data[:-padding]  # remove the padding

# key = Fernet.generate_key()
# fernet = Fernet(key)
# Create your views here.
def health_checkup(request):
	# print(request.POST)
	# age = request.POST.get('age')
	# bp = request.POST.get('bp')
	# gen = request.POST.get('gen')
	# sug = request.POST.get('sug')
	# temp = request.POST.get('temp')
	# dia = diabetes(age,sug)
	# print(dia)

	return render(request, 'home.html', {'name':request.session['user']})

def view(request):
	# e = encrypt('sasi', '1234')
	# print(e)
	# d = decrypt(e, '1234')
	# print(d)
	# print(2,encrypt(request.session['user'],request.session['pass']))
	# print(request.session['pass'],request.session['user'])
	user=encrypt(request.session['user'],request.session['pass'])
	# print(user)
	# print(request.session['user'])
	# print(request.session['pass'])
	history = Detail.objects.filter(user=encrypt(request.session['user'],request.session['pass']))
	print("\n\nHistory")

	for a in history:
		a.wei=decrypt(a.wei,request.session['pass'])[:2]
		a.hei=decrypt(a.hei,request.session['pass'])[:4]
		a.age=decrypt(a.age,request.session['pass'])[:2]
		a.bp=decrypt(a.bp,request.session['pass'])[:3]
		a.gen=decrypt(a.gen,request.session['pass'])[:1]
		a.sug=decrypt(a.sug,request.session['pass'])[:3]
		a.tem =decrypt(a.tem,request.session['pass'])[:2]
		a.hae = decrypt(a.hae,request.session['pass'])[:2]
		a.bmi = decrypt(a.bmi,request.session['pass'])[:3]
		a.dia = decrypt(a.dia,request.session['pass'])[:4]+"%"
		a.typ = decrypt(a.typ,request.session['pass'])[:4]+"%"
		a.hea = decrypt(a.hea,request.session['pass'])[:4]+"%"
		a.ane = decrypt(a.ane,request.session['pass'])[:4]+"%"
		a.den = decrypt(a.den,request.session['pass'])[:4]+"%"

		print(a.dia,a.typ,a.hea,a.ane,a.den)
	# user=request.session['user']
	# print(user)
	# history = Detail.objects.filter(user=request.session['user'])
	return render(request,'view.html',{'data':history})

def patient_data(request):
	# print(request)
	wei = int(request.GET.get('wei'))
	hei = float(request.GET.get('hei'))
	hei = hei/100
	age = int(request.GET.get('age'))
	bp = int(request.GET.get('bp'))
	gen = request.GET.get('gen')
	sug = int(request.GET.get('sug'))
	temp = int(request.GET.get('temp'))
	blo = int(request.GET.get('blo'))
	# print(age,sug)
	dia = diabetes(age,sug)*100
	bmi = wei/(hei*hei)
	obe=2
	if(bmi<18):
		obe=0
	if(bmi>25):
		obe=1
	bmi = "{:.2f}".format(bmi)
	
	typ = typhoid(age,temp,bp)*100
	ane = anemia(blo,gen)*100
	htk = heartatk(age,blo,wei)*100
	den = dengue(blo,temp)*100
	# Detail.objects.create(user=encrypt(request.session['user'],request.session['pass']),time=datetime.now(),age=age,gen=gen,wei=wei,hei=hei,bp=bp,sug=sug,tem=temp,hae=blo,bmi=bmi,dia=dia,typ=typ,hea=htk,ane=ane,den=den)
	Detail.objects.create(user=encrypt(request.session['user'],request.session['pass']),time=datetime.now(),age=encrypt(request.session['pass'],str(age)),gen=encrypt(request.session['pass'],str(gen)),wei=encrypt(request.session['pass'],str(wei)),hei=encrypt(request.session['pass'],str(hei)),bp=encrypt(request.session['pass'],str(bp)),sug=encrypt(request.session['pass'],str(sug)),tem=encrypt(request.session['pass'],str(temp)),hae=encrypt(request.session['pass'],str(blo)),bmi=encrypt(request.session['pass'],str(bmi)),dia=encrypt(request.session['pass'],str(dia)),typ=encrypt(request.session['pass'],str(typ)),hea=encrypt(request.session['pass'],str(htk)),ane=encrypt(request.session['pass'],str(ane)),den=encrypt(request.session['pass'],str(den)))
	context = {'dia': dia , 'bmi':bmi, 'typ':typ, 'ane':ane, 'htk':htk, 'den':den, 'obe':obe}
	return render(request, 'dia.html', context)
	# if(dia==1):
	# 	context = {'dia': 100}
	# 	return render(request, 'dia.html', context)
	# else:
	# 	context = {'dia': 0}
	# 	return render(request, 'dia.html', context)


# def tuber(age,bp,gen,sug):
	


def diabetes(age,sug):
	if(age>30 and sug>140):
		return 0.9
	if(age>30 and sug>135):
		return 0.7	
	if(age<30 and sug>160):
		return 0.45
	if(age<30 and sug>140):
		return 0.3
	return 0

def typhoid(age,temp,bp):
	if(temp>40 and bp>140):
		return 0.8
	if(temp>40 and bp>130):
		return 0.6
	if(temp>37 and bp>120):
		return 0.2
	return 0

def anemia(blo,gen):
	if(blo<6 and (gen=='M' or gen=='m')):
		return 0.9
	if(blo<9 and (gen=='M' or gen=='m')):
		return 0.5
	if(blo<11 and (gen=='M' or gen=='m')):
		return 0.2
	if(blo<4 and (gen=='F' or gen=='f')):
		return 0.9
	if(blo<7 and (gen=='F' or gen=='f')):
		return 0.6
	if(blo<9 and (gen=='F' or gen=='f')):
		return 0.3
	return 0

def heartatk(age,blo,wei):
	if(age>50 and wei>100 and bp>150):
		return 0.6
	if(age>30 and wei>80 and bp>135):
		return 0.3
	return 0

def dengue(blo,temp):
	if(blo<4 and temp>40):
		return 0.9
	if(blo<7 and temp>38):
		return 0.6
	if(blo<10 and temp>37):
		return 0.3
	return 0

def logout(request):
	auth.logout(request)
	return redirect('login')