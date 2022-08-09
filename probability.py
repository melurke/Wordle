word_list = []
word_list_complete = []
word_file = open("data/word_lists/word_list.txt")
word_file_complete = open("data/word_lists/word_list_complete.txt")

for word in word_file:
    word_list.append(word.strip())
for word in word_file_complete:
    word_list_complete.append(word.strip())

num_of_words = len(word_list)
num_of_words_complete = len(word_list_complete)

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

letters = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

for word in word_list:
    if "a" in word:
        a += 1
    if "b" in word:
        b += 1
    if "c" in word:
        c += 1
    if "d" in word:
        d += 1
    if "e" in word:
        e += 1
    if "f" in word:
        f += 1
    if "g" in word:
        g += 1
    if "h" in word:
        h += 1
    if "i" in word:
        i += 1
    if "j" in word:
        j += 1
    if "k" in word:
        k += 1
    if "l" in word:
        l += 1
    if "m" in word:
        m += 1
    if "n" in word:
        n += 1
    if "o" in word:
        o += 1
    if "p" in word:
        p += 1
    if "q" in word:
        q += 1
    if "r" in word:
        r += 1
    if "s" in word:
        s += 1
    if "t" in word:
        t += 1
    if "u" in word:
        u += 1
    if "v" in word:
        v += 1
    if "w" in word:
        w += 1
    if "x" in word:
        x += 1
    if "y" in word:
        y += 1
    if "z" in word:
        z += 1

print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('e:', e)
print('f:', f)
print('g:', g)
print('h:', h)
print('i:', i)
print('j:', j)
print('k:', k)
print('l:', l)
print('m:', m)
print('n:', n)
print('o:', o)
print('p:', p)
print('q:', q)
print('r:', r)
print('s:', s)
print('t:', t)
print('u:', u)
print('v:', v)
print('w:', w)
print('x:', x)
print('y:', y)
print('z:', z)

letters = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
letter = []

for i in letters:
    i = i/num_of_words
    letter.append(i)

letters.sort(), letters.reverse()

print(letter)
