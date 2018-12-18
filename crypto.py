import unicodedata, re

def to_int(s):
	return ord(s) - 65

def to_chr(i):
	return chr(i + 65)

def crypt(text, key):
	v = [to_int(k) for k in key]
	l= list(text)
	n1 = len(v)
	n2 = len(l)
	i = 0
	for k in range(n2):
		l[k] = to_chr((to_int(l[k]) + v[i]) % 26)
		i = i + 1
		i = i % n1
	return "".join(l)

def decrypt(text, key):
	v = [to_int(k) for k in key]
	l= list(text)
	n1 = len(v)
	n2 = len(l)
	i = 0
	for k in range(n2):
		l[k] = to_chr((to_int(l[k]) - v[i]) % 26)
		i = i + 1
		i = i % n1
	return "".join(l)

def pgcd(a, b):
	r = a % b
	while(r != 0):
		a = b
		b = r
		r = a % b
	return b
		
def pgcdlist(l):
	d = l[0]
	n = len(l)
	for i in range(1, n):
		d = pgcd(d, l[i])
	return d

def convert_upper(s):
	s = unicode(s, 'utf-8')
	s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
	s = s.upper()
	autre = re.compile('[^A-Z]')
	s = autre.sub('', s)
	return s

f = open("text.txt", 'r')
text = f.read()
n = len(text)
f.seek(n/2.0)
text = f.read(999)
f.close()


text = convert_upper(text)
textcrypt = crypt(text, "vim")

def occu(s):
	d = {}
	n = len(s)
	for i in range(n - 2):
		occu = "".join([s[i], s[i + 1], s[i + 2]])
		for k in range(i + 3, n - 2):
			test = "".join([s[k], s[k + 1], s[k + 2]])
			if occu == test:
				if not(occu in d):
					d[occu] = {i, k}
				else:
					d[occu].add(k)
	return d
			
