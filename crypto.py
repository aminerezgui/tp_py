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
		
def pgcd_list(l):
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
text = f.read(5000)
'''n = len(text)
f.seek(n/2.0)
text = f.read(999)'''

f.close()


text = convert_upper(text)
textcrypte = crypt(text, "LINUX")


def occu(s, to):
	d = {}
	n = len(s)
	for i in range(n - (to - 1)):
            occu = s[i : i + to]
            if not(occu in d):
		for k in range(i + to, n - (to - 1)):
                    test = s[k : k + to]
		    if occu == test:
			    if not(occu in d):
				    d[occu] = [i, k]
			    else:
				    d[occu] = d[occu] + [k]
	return d

def list_dist(d):
    L = []
    for o in d:
        l = d[o]
        n = len(l)
        for i in range(n - 1):
            L = L + [abs(l[i] - l[i + 1])]
    return L

def tc(textcrypte):
    to = 4
    tc = pgcd_list(list_dist(occu(textcrypte, to)))
    while(tc < 3):
        to = to + 1
        tc = pgcd_list(list_dist(occu(textcrypte, to)))
    return tc


def lpf(l):
    x = [chr(i) for i in range(65, 65 + 26)]
    d = dict((i, 0) for i in x)
    for i in l:
        d[i] = d[i] + 1
    c = d["A"]
    g = "A"
    for i in d:
        if d[i] > c:
            c = d[i]
            g = i
    return g



def cle(s, tc):
    cle = '' 
    n = len(s)
    for k in range(tc):
        l = []
        for i in range(n):
            if i % tc == k:
                l = l + [s[i]]
        cle = cle + to_chr((to_int(lpf(l)) - to_int("E"))% 26)
    return cle
