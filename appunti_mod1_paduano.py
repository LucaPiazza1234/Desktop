#    ___         _                   
#  / __|___ ___| |__ ___            
# | (_ / -_) -_) / /(_-<            
#  \___\___\___|_\_\/__/            
#   /_\  __ __ _ __| |___ _ __ _  _ 
#  / _ \/ _/ _` / _` / -_) '  \ || |
# /_/ \_\__\__,_\__,_\___|_|_|_\_, |
#                              |__/

# +---------------------+
# |  LINGUAGGIO PYTHON  |
# +---------------------+

# Cos'è Python?
'''
Linguaggio di programmazione
- interpretato
- interattivo
- orientato agli oggetti
Incorpora al proprio interno:
- moduli
- eccezioni
- tipizzazione dinamica
- tipi di dato di alto livello
- classi
- sintassi chiara

Inoltre è
- estensibile in C e C++ (e Java, eccetera)
- usabile come linguaggio di configurazione
- portabile
'''


# Interattività
14 + 10
9 * 9


# Hello World
print("Hello World!")


# Variabili
messaggio = "Hello World!"
print(messaggio)

numero = 281
print(numero)

numero_decimale = 21.78
print(numero_decimale)


# I nomi delle variabili cominciano con lettere o underscore e sono case sensitive


# Il cancelletto è un commento
# Qualsiasi cosa scritta in un commento non verrà eseguita


# Ancora sulle variabili
city = "Como"
print(city)

city = "Roma"
print(city)

print(numero + numero_decimale)
print(10 + numero_decimale)

nome = "Aldo"
cognome = "Serra"

print(nome + cognome)
print(nome + " " + cognome)


# Cancellare una variabile
del city
print(city)


# Funzione 'type'
# visualizza il tipo dell'oggetto passato come parametro
type(5)


type("ciao")

type(numero)

type(numero_decimale)

type(messaggio)

type(nome)

type = 5 # <--- ?
# si risolve con 'del type'


# Funzione 'help'
# visualizza la descrizione e le funzionalità dell'oggetto passato come parametro
help(print) # (da terminale premere 'q' per uscire dall'help)


# Nuove funzioni?
import math
math.sqrt(100)
math.pow(5, 3)


# Impostare una working directory
import os
os.getcwd()

os.chdir("a/")
os.getcwd()


# Versione di Python
import sys
print(sys.version)


# Liste
# Un elenco ordinato di elementi eterogenei
elenco = [15, 7, 19, 75]
print(elenco)

varie = [19, "hello", elenco]
print(varie)

# Aggiungere elementi
varie.append(124.75)
print(varie)

import math
varie.append(math)
print(varie)


# Il punto, '.', separa un oggetto da un suo attributo o da un suo metodo


# Accedere agli elementi
elenco[0]

elenco[1]

varie[1]

elenco[9]

elenco[-1]


# Funzione 'len'
# Ci permette di scoprire la lunghezza di una lista
len(elenco)

len(varie)


# Simbolo ':'
elenco[0:2]

elenco[1:3]

elenco[1:]

elenco[:2]

elenco[:]


# L'ultimo comando può servire per duplicare una lista:
elenco_copia = elenco[:]


# Slicing
lista = ["P", "Y", "T", "H", "O", "N", "!"]
'''
 0   1   2   3   4   5   6   7
 |   |   |   |   |   |   |   |
 | P | Y | T | H | O | N | ! |
 |   |   |   |   |   |   |   |
-7  -6  -5  -4  -3  -2  -1   0
'''

# Assegnare elementi
lista_copia = lista[:]
lista_copia[0:2] = [13, "abc"]

# Inserire elementi
lista_copia[1:1] = [1, 2, 3]

# Cancellare elementi
lista_copia[1:3] = []

# Es. cancellare gli ultimi due elementi
lista_copia[-2:] = []

# Metodo 'insert'
elenco.insert(3, "nuovo")
elenco.insert(42, "fondo")  # <- attenzione

# Metodo 'extend'
aggiunta = ["x", "y", "z"]
elenco.extend(aggiunta)

# Metodo 'remove'
elenco.remove(75)
elenco.remove("nuovo")

# Metodo 'pop'
# Estrae l'ultimo elemento (e lo rimuove dalla lista)
elenco.pop()
elenco.pop()

# Metodo 'count'
elenco.count(7)

# Metodo 'index'
elenco.index(7)

elenco.index("ciao")

# Metodo 'reverse'
elenco.reverse()

# Metodo 'sort'
numeri = [1, 7, 54, 3, 21, 500, 12, 4, 8]
numeri.sort()

elenco.sort()

lista.sort()

# Operatore 'in'
21 in numeri

987 in numeri

# Lista vuota
lista_vuota = []
lista_vuota = list()


# Stringhe
stringa = "0123456789"

stringa[:5]  # I primi 5 caratteri

stringa[-5:]  # Gli ultimi 5 caratteri

stringa[1:-1]  # Tutti i caratteri tranne primo e ultimo

# Slicing a tre parametri
stringa[0:8:2]

stringa[::2]  # Ogni 2

stringa[1::2]  # Ogni 2 a partire dal secondo

# Immutabili
stringa[2] = "c"
stringa_modificata = stringa[:2] + "c" + stringa[3:]

stringa1 = "Pizza con patatine"  # Usando doppi apici

stringa2 = 'Pizza "speciale"'  # Usando apici singoli

stringa3 = "Pizze:\n - bianche\n - rosse"

print(stringa3)

stringa4 = """
Scrivere stringhe
su più righe
con apici: 'pizza'
e doppi apici: "calzone"!
"""

stringa6 = "pizza"

stringa6 * 5

# Metodo 'find'
stringa1.find("p")

# Metodi uppercase e lowercase
stringa1.lower()
stringa1.upper()
stringa1.title()
stringa1.capitalize()
stringa1.swapcase()

# Metodo 'strip'
# Rimuove gli spazi all'inizio e alla fine di una stringa
stringa7 = "  kebab   "
stringa7.strip()

# Metodo 'replace'
stringa1.replace("patatine", "funghi")

# Metodi 'split' e 'join'
stringa1.split(" ")

stringa1.split("a")

# Esempio: e-mail
stringa8 = "abc@ccc.ddd.com"

componenti_mail = stringa8.split("@")

print(componenti_mail)

provider = componenti_mail[1].split(".")

print(provider[-1])

divisore = "/"
data_num = ["27", "10", "1977"]
divisore.join(data_num)

stringa6.join(data_num)

# Funzione 'list'
list("abcd")

list("PYTHON!")

# Operatore 'in'
"z" in stringa6

# Usare metodi sulla stringa
", ".join(data_num)

"Pizza e kebab".split(" ")

# Metodo 'format'
utente1 = "Sabrina"

"L'utente {} si è appena collegato.".format(utente1)

utente2 = "Michele"

"L'utente {} si è appena collegato.".format(utente2)

# Se vogliamo usarne più di uno:
"Gli utenti {0} e {1} si sono appena collegati.".format(utente1, utente2)

"Gli utenti {0} e {1} si sono appena collegati. L'utente {0} ha privilegi da amministratore.".format(utente1, utente2)



# Tuple
# Sono sequenze ordinate di oggetti eterogenei (similmente alle liste) ma immutabili (diversamente dalle liste e similmente alle stringhe)

tupla = (1, 2, 3, 4, 5)

# Slicing
tupla[:3]

tupla[-1]

# Immutabilità
tupla[2] = "abc"

# Metodo 'count'
fibonacci = (1, 1, 2, 3, 5, 8, 13, 21)

fibonacci.count(8)

fibonacci.count(1)

fibonacci.count(100)

# Metodo 'index'
fibonacci.index(13)

# Operatore 'in'
5 in fibonacci

9 in fibonacci

# Tupla con un solo elemento
singolo = (1, )


# Insiemi (Set)
# Sono un tipo di dati per gestire gruppi di elementi non ordinati e senza duplicati
insieme = {"pizza", "kebab", "hamburger", "kebab"}

print(insieme)

insieme[0]  # Errore

lettere = set("hello")

# Operatore unione
piccoli = {"topo", "lucertola"}
grandi = {"elefante", "balena"}
grandi | piccoli

bianchi = {"ermellino", "topo"}
piccoli | bianchi

# Operatore differenza
piccoli - bianchi

# Operatore intersezione
piccoli & bianchi

# Operatore differenza simmetrica (xor)
piccoli ^ bianchi


# Dizionari
# Un dizionario è un array associativo, ovvero un insieme di oggetti ognuno dei quali associato ad una chiave
rubrica = dict()  # oppure rubrica = {}
rubrica["Sergio"] = "333-111222333"
rubrica["Simona"] = "345-999944444"
print(rubrica)

rubrica["Sergio"]

rubrica["Davide"] = "321-000222444"

# Elencare le chiavi di un dizionario (metodo 'keys')
rubrica.keys()

# Operatore 'in'
"Ada" in rubrica

"Sergio" in rubrica

# Cancellare
del rubrica["Sergio"]

# Possiamo assegnare ad un elemento di un dizionario qualsiasi oggetto Python (anche funzioni e classi).
# Dobbiamo usare come chiave qualsiasi oggetto immutabile (stringa, intero, tupla)

# Metodo 'get'
# Permette di estrarre un valore di default se la chiave specificata non è presente
magazzino = {"t-shirt": 10, 
             "cappotti": 8,
             "sciarpe": 7}

magazzino["sciarpe"]

magazzino["calze"]

magazzino.get("calze", 0)

magazzino.get("sciarpe", 0)


# Metodo 'setdefault'
# Estrae un valore di defaulte E lo aggiunge al dizionario
magazzino.setdefault("calze", 0)

magazzino.setdefault("sciarpe", 0)


# Estrarre gli elementi di un dizionario (metodo 'values')
magazzino.values()

sum(magazzino.values())

# Metodo 'items'
# Estrae un oggetto che contiene le coppie chiave-valore sotto forma di tuple
magazzino.items()

magazzino.update({"t-shirt": 4,
                  "calze": 9})



# Numeri
2 ** 10

# Non c'è limite alle dimensioni di un numero intero (almeno finché la memoria del calcolatore regge)
2 ** 10000

32.7854 / 9.738

# Numeri esadecimali, ottali, binari
0xff
0o77
0b110

# Numeri immaginari
num = 2.4 - 6.7j
num.real
num.imag

# Notazione scientifica
3e2
7e10


# Valori booleani
True
False


# Valore nullo
None

variabile = None


# Conversioni
una_tupla = ("x", "y", "z")
una_lista = [18, 19, 20]
una_stringa = "1997"
un_intero = 42
un_decimale = 3.1416

tuple(una_lista)

list(una_tupla)

int(una_stringa)

str(un_intero)

float(un_intero)

int(un_decimale)  # troncamento



# Commenti su più righe: ''' commento '''
'''
Questo è un commento su più righe.
Non ho bisogno di aggiungere ogni volta il cancelletto all'inizio.
'''




# +-------------+
# |  OPERATORI  |
# +-------------+

# Operatori:
'''
Addizione: +
Sottrazione: -
Divisione: /
Moltiplicazione: *
Modulo: %
Elevazione a potenza: **
Divisione con troncamento: //
'''
10 / 6

10 // 6

7 % 3

# Operatori di comparazione:
'''
<
>
==
>=
<=
!=
is
is not
in
not in
'''
5 < 7

8 == 9

"ciao" == "ciao"

200 <= 200

"c" in "ciao"

"c" not in "ciao"

var = None

var is None

# Operatori bitwise:
'''
and
or
xor
not
'''
5<2 and 10>=7

5>2 and 10>=7

eta = 20

eta > 17 and eta < 19

eta >= 17 and eta <= 19

17 < eta < 19

eta >= 17 or eta <= 19

5<2 or 10>=7

not 21==21

not eta == 18

eta = 90
not (eta >= 17 and eta <= 19)

eta = 18
not eta >= 17 and eta <= 19

# Operatori di assegnazione:
'''
=
+=
-=
/=
*=
%=
**=
//=
'''
num = 5

num = num + 1

num = 5

num += 1

num *= 10

prezzo = 100
nuovo_prezzo = prezzo * 0.8
prezzo *= 0.8
prezzo == nuovo_prezzo

num **= 2




# +---------------+
# |  LA SINTASSI  |
# +---------------+
'''
Istruzioni condizionali e loop:
- if
- elif
- else
- for
- while
- continue e break
'''


# IF
'''
if condizione:
	esegui azione/i
'''
x = 5
y = 7
if x < y:
	print("x è minore di y")

eta = 17
if 17 <= eta <= 19:
    print("idoneo per il torneo")

# Attenzione all'indentazione!
# Se la sbagliamo il codice non funziona

'''
if condizione:
	esegui azione
else:
	esegui altra azione
'''
x = 5
y = 7
if x < y:
	print("x è minore di y")
else:
	print("x è maggiore o uguale ad y")

eta = 16
if 17 <= eta <= 19:
    print("idoneo per il torneo")
else:
    print("non idoneo")

'''
if condizione:
	esegui azione
elif altra condizione:
	esegui altra azione
else:
	esegui ancora altra azione
'''
temperatura = 27
if temperatura < 20:
	print("freddino")
elif temperatura > 30:
	print("caldino")
else:
	print("ottimale")

temperatura = 27
if temperatura < 20:
    print("freddino")
elif temperatura > 30:
    print("caldino")
elif 20 < temperatura < 30:
    print("ottimale")


# FOR
# Esegui una o più operazioni per un determinato numero di volte
'''
for elemento in iterabile:
	esegui azione/i su elemento
'''
insieme = (1, 4, 6, 7, 2, 8)
for numero in insieme:
	print(numero)

parola = "Python"
for lettera in parola:
	print(lettera + "!")

for numero in range(4):
	print(numero)

range(4)

list(range(4))

# Con 'range' possiamo specificare inizio, fine, e passo
list(range(3, 10))

list(range(2, 10, 2))

list(range(5, 0, -1))

for chiave, valore in rubrica.items():
	print(chiave, valore)


insieme = (1, 4, 6, 7, 2, 8)
for numero in insieme:
    print("Numero originale:", numero)
    doppio = numero * 2
    print("Numero raddoppiato:", doppio)
print("Ho finito.")


insieme = (1, 4, 6, 7, 2, 8)
for numero in insieme:
    doppio = numero * 2
    print("Il doppio di {0} è uguale a {1}.\n".format(numero, doppio))
print("Ho finito.")


prezzi = (20, 40, 50, 60, 190, 30)
prezzi_scontati = []
for prezzo in prezzi:
    print("Prezzo originale: {}".format(prezzo))
    prezzi_scontati.append(prezzo * 0.8)
    print("Prezzo scontato: {}".format(prezzo * 0.8))
    print("\n")
print("Finito.")


prezzi = (20, 40, 50, 60, 190, 30)
prezzi_scontati = []
sconto = 0.9
for prezzo in prezzi:
    print("Prezzo originale: {}".format(prezzo))
    prezzi_scontati.append(prezzo * sconto)
    print("Prezzo scontato: {}".format(prezzi_scontati[-1]))
    print("")
print("Finito.")



prezzi = (20, 40, 50, 60, 190, 30)
prezzi_scontati = []
sconto = 0.8  # questa in realtà è la porzione da pagare
sconto_stampa = round((1-sconto)*100)
for prezzo in prezzi:
    print("Prezzo originale: {}".format(prezzo))
    prezzi_scontati.append(prezzo * sconto)
    print("Prezzo scontato ({}%): {}".format(sconto_stampa, prezzi_scontati[-1]))
    print("")
print("Finito.")


prezzi = (20, 40, 50, 60, 190, 30)
sconto1 = 37  # %
sconto2 = 10
prezzi_scontati = []
for prezzo in prezzi:
    print("Prezzo originale: {}".format(prezzo))
    if prezzo > 55:
        print("Sto usando uno sconto del {}%".format(sconto2))
        prezzi_scontati.append(prezzo * (100 - sconto2) / 100)
    else:
        print("Sto usando uno sconto del {}%".format(sconto1))
        prezzi_scontati.append(prezzo * (100 - sconto1) / 100) 
    print("Prezzo scontato: {}".format(prezzi_scontati[-1]))
    print("")
print("Finito.")


# Istruzione 'enumerate'
# Per contare gli elementi di una sequenza mentre vengono iterati
libri = ["enciclopedia", "atlante", "dizionario"]
for libro in libri:
	print(libro)

for contatore, libro in enumerate(libri):
	print(contatore, libro)

# Funzione 'zip'
# Per iterare su più di una lista
alunni = ["Lucio", "Silvio", "Michela", "Natalia"]
corsi = ["ingegneria", "medicina", "cinema", "giurisprudenza"]
anni = [19, 22, 25, 21]
for alunno, corso, eta in zip(alunni, corsi, anni):
	print(alunno, "frequenta", corso, "e ha", eta, "anni.\n")


for num in range(10000):
	if num in [1000, 2000, 3000, 4000, 5000]:
		print("Sei alla riga no.", num)

for num in range(10000):
	if num in list(range(1000, 10000, 1000)):
		print("Sei alla riga no.", num)

for num in range(10000):
	if num % 1000 == 0:
		print("Sei alla riga no.", num)


# WHILE
# Esegue una o più operazioni finché è soddisfatta una condizione
'''
while condizione:
	esegui azione
'''
x = 1
while x < 5:
	print(x)
	x += 1

# errore?
x = 7
while x > 5:
	print(x)
	x = x + 1

# Istruzione 'continue'
lista1 = [4, 5, 7, 8, 12, "abc", 15, 21, 45]
print("Ora stamperò solo i numeri:")
for item in lista1:
	if item == "abc":
		continue
	else:
		print("-", item)

# Istruzione 'break'
lista1 = [4, 5, 7, 8, 12, "abc", 15, 21, 45]
print("Questa lista contiene solo numeri:")
for item in lista1:
	if item == "abc":
		print("Errore! Non ci sono solo numeri!")
		break
	else:
		print("-", item)

isinstance(5, int)

# Clausola 'else'
# In un ciclo 'for' viene eseguita alla fine del ciclo
'''
for elemento in lista:
	if elemento_ha_una_certa_caratteristica:
		print("trovato!")
		break
else:
	print("ho cercato dovunque, ma non c'era")
'''
lista = [1, 5, 7, 8, 10, 9, 14]
print("Cerco un numero divisibile per 3...")
for numero in lista:
	print("Controllo il", numero)
    if numero % 3 == 0:
        print("Trovato:", numero)
        break
else:
    print("\nNon ci sono numeri divisibili per 3")


# Istruzione 'pass'
# Serve quando non vogliamo far fare nulla ad un costrutto
x = 10
if x < 1:
	print("bene")
if x == 10:
	# da completare
	pass


# Esercizio
'''
Dato un numero intero n, scrivere un programma che genera un dizionario che contiene come chiave i, e come valore i*i, in maniera tale che i sia compreso tra 1 ed n (entrambi inclusi).
Alla fine il programma deve stampare il dizionario.
Supponiamo che l'input dato al programma sia:
n = 7
'''



# +-----------------+
# |  COMPREHENSION  |
# +-----------------+

# List comprehension
'''
Un costrutto sintattico che permette di costruire nuove liste a partire da altre liste preesistenti
'''
numeri = [1, 3, 4, 8, 9, 10, 16, 20, 31]
doppi = [num*2 for num in numeri]
print(doppi)

pari = [num for num in numeri if num%2 == 0]
print(pari)

prezzi_scontati = [num*0.8 for num in numeri]
print(prezzi_scontati)

# Set comprehension
'''
Simile alla list comprehension, ma il risultato finale non ha duplicati
'''
resti = {num % 8 for num in numeri}
print(resti)

# Dictionary comprehension
prezzi = {"uova": 12, "broccoli": 8, "mele": 5}
nuovi_prezzi = {articolo: prezzi[articolo]*2 for articolo in prezzi.keys()}

nuovi_prezzi = {articolo: prezzo*2 for articolo, prezzo in prezzi.items()}


# IMPORT
'''
Serve per importare librerie che contengono funzioni aggiuntive che ci possono essere utili
'''
import math
math.sqrt(144)

math.degrees(math.pi/2)

from math import factorial
factorial(12)

from math import sqrt, degrees, pi
sqrt(144)
degrees(pi/2)

import math as mt

from math import factorial as fct

fct(12)

# Numpy
import numpy as np

my_list = [1, 2, 3]
array = np.array(my_list)
type(array)

np.arange(0, 11, 2)

np.zeros(5)

np.zeros((3, 4))

np.ones((3, 4))

np.linspace(0, 11, 10)

np.linspace(0, 11, 11)

np.linspace(0, 11, 100)

# Random
np.random.randint(0, 10) # minimo incluso, massimo escluso

np.random.randint(0, 1000)

np.random.randint(0, 1000, (3, 4))

np.random.seed(42)
np.random.randint(0, 100, 10)

np.random.seed(42)
array = np.random.randint(0, 100, 10)
array.max()
array.mean()
array.argmax()
array.reshape(2, 5)

mat = np.arange(0, 100).reshape(10, 10)

mat[0, 1]

mat[4, 3]

mat[:, 0]

mat[5, :]

mat[:3, :3]

mat.shape

len(mat)  # <- attenzione

mat.size

mat.transpose()

# Differenza tra liste e array?
# Masking!
array / 3

my_list / 3

array > 80

my_filter = array > 80

array[my_filter]

array[array > 50]

mat > 50

my_filter = mat > 50

mat[my_filter]

mat[mat > 50]

new_mat = np.array([ [1, 2], [3, 4], [5, 6] ])


# +-------------+
# |  ECCEZIONI  |
# +-------------+

# Le eccezioni sono eventi scatenati da errori di varia natura
'''
Errori:
- sintattici
- semantici
- logici

Eccezioni
- handled
- unhandled

Gestione delle eccezioni
- try
- except
- raise
'''

1 / 0


a = 1
b = 0
print("Inizio del programma")
print("Divisione:", a/b)
print("Somma:", a+b)
print("Fine del programma")


a = 1
b = 0
print("Inizio del programma")
try:
	print("Divisione:", a/b)
except ZeroDivisionError:
	print("Divisione per zero!")
print("Somma:", a+b)
print("Fine del programma")


try:
	d = dict(arg)
except TypeError:
	print("Il parametro non si può convertire in dict")
except NameError:
	print("Il parametro non esiste")
except:
	print("Errore generico")


raise ValueError("Errore")


37 + "abc"


# Clausole 'else' e 'finally'
numeratore = 10
denominatore = 0
try:
	quoziente = numeratore / denominatore
except ZeroDivisionError:
	print("Il denominatore è nullo")
else:
	print("Quoziente uguale a", quoziente)
finally:
	print("Fine del programma")

# Funzione 'exc_info'
'''
Serve per sapere che tipo di eccezione è accaduta
'''
from sys import exc_info
numeratore = 10
denominatore = 0
try:
	quoziente = numeratore / denominatore
except Exception:
	print("Errore")
	print(exc_info())
else:
	print("Quoziente uguale a", quoziente)
finally:
	print("Fine del programma")


'''
Esempi di eccezioni:
- TypeError
- ValueError
- AttributeError
- IOError
- IndexError
- KeyboardInterrupt
- NameError
- StopIteration
- ZeroDivisionError
- ...
'''



# +------------+
# |  FUNZIONI  |
# +------------+

'''
- built-in
- librerie
- user defined

- sono pezzi di codice
- effettuano operazioni su variabili o oggetti
- ad un determinato input corrisponde un determinato output
'''

# alcune funzioni built in
dir()
help()
type()
print()

import math
# Funzione 'help'
# Visualizza l'aiuto di una funzione, un oggetto, una libreria
help(math)
# Funzione 'type'
# Visualizza il tipo di oggetto passato come parametro
type(math)
# Funzione 'dir'
# visualizza un elenco degli attributi e dei metodi dell'oggetto passato come parametro
dir(math)

lista = [1, 2, 3]
dir(lista)

help(print)


# creare le proprie funzioni
"""
# tre parti:
- nome
- parametri
- corpo

def scopo_funzione(parametri):
	'''
	qui scriviamo la documentazione
	'''
	risultato = operazioni_varie(parametri)
	return risultato
"""

def al_cubo(n):
	cubo = n ** 3
	return cubo

def al_cubo(n):
	return n ** 3

al_cubo(3)


def al_cubo(n):
	'''
	Questa funzione restituisce il cubo di un numero.
	'''
	return n ** 3

help(al_cubo)


def moltiplica_due_numeri(x, y):
	'''
	Questa funzione moltiplica tra
	loro i due valori in input.
	'''
	return(x * y)

moltiplica_due_numeri(10, 5)


# Restituire più valori
def mari_e_monti():
	return "mari", "monti"

mari_e_monti()

a, b = mari_e_monti()

print(a, b)


# Passaggio di parametri
def dividi(numeratore, denominatore):
	return numeratore / denominatore

dividi(155, 72)

dividi(500, 20)

dividi(20, 500)

dividi(numeratore=500, denominatore=20)

dividi(denominatore=20, numeratore=500)

# su Jupyter 
# Per vedere i possibili parametri: nomefunzione + tab
# Per vedere la definizione: nomefunzione + shift + tab


# Valori di default
def compra(cosa="uova", quantita=10):
	print("Vai a comprare", quantita, cosa)

compra()

compra(cosa="sottilette")



help(print)


print("a", "b", "c", sep="-", end="!")


# Esercizio:
'''
Scrivere una funzione che trova il minimo tra tre numeri e lo restituisce
'''


# Esempio
def sconta(prezzo, perc=20):
    return prezzo * ((100 - perc) / 100)

sconta(prezzo=100)

sconta(prezzo=100, perc=17)

prezzi = [10, 40, 50, 60, 70, 100]
prezzi_scontati = [sconta(prezzo) for prezzo in prezzi]
print(prezzi_scontati)


campionario = {"t-shirt": 50, "cappello": 70, "guanti": 100}
print(campionario)

campionario["cappello"]

campionario_scontato = {oggetto: sconta(prezzo, perc=40) for oggetto, presso in campionario.items()}
print(campionario_scontato)


# Funzioni predefinite
dir(__builtins__)

help(abs)

abs(-4)

'''
Funzioni matematiche predefinite:
- min
- max
- sum
- pow
- abs
'''


'''
Funzioni booleane predefinite:
- all
se tutti i parametri di ingresso sono veri restituisce 'True'
- any
se alcuni dei parametri di ingresso sono veri restituisce 'True'
'''
all([True, True, False])

any([True, True, False])

tupla = (5, 15, 25)
all([n>10 for n in tupla])

any([n>10 for n in tupla])


'''
Funzioni per iterazioni:
- map
- zip 
- filter
'''

for x in zip([1, 2, 3, 4, 5], ["a", "b", "c", "d", "e"]):
	print(x)

for x in zip(range(6), "hello"):
	print(x)


def somma(a, b, c):
	return a+b+c
for n in map(somma, [1, 2], [5, 6], [10, 20]):
	print(n)

list(map(sconta, prezzi))
sconti = [10, 20, 30, 40, 50]
list(map(sconta, prezzi, sconti))


def maggiore_di_50(n):
	return n > 50
valori = [10, 20, 30, 35, 70, 80, 110, 5, 3, 2]
for n in filter(maggiore_di_50, valori):
	print(n)


'''
Funzioni di ordinamento:
- sorted
'''
sorted(valori)


# L'operatore 'lambda'
# per semplificare la scrittura di funzioni semplici in una riga
def square(x):
	return(x**2)

square(5)

square2 = lambda x: x**2

list(map(square2, valori))

list(map(lambda x: x**2, valori))

for n in filter(lambda x: x>50, valori):
	print(n)




# +----------+
# |  CLASSI  |
# +----------+

# Definire una classe
class Cibo:
	pass

# Istanza di una classe -> oggetto
pasta = Cibo()

# I metodi
class Cibo:
	'''
	Un esempio di classe per gestire i valori nutritivi dei cibi.
	'''
	def __init__(self, prot, carb, gras):
		self.proteine = prot
		self.carboidrati = carb
		self.grassi = gras

'''
- il metodo '__init__' è il costruttore della classe
- il primo parametro del costruttore è sempre 'self', ma non dobbiamo specificarlo quando creiamo una istanza
'''

pasta = Cibo(prot=13, carb=74, gras=1)

print(pasta.carboidrati)

pizza = Cibo(prot=10, carb=30, gras=12)

print(pizza.grassi)

print(pizza.proteine)

strange = Cibo(prot="abc", carb=-72, gras=[5, 6])  # <- funziona?


# Aggiungiamo controlli al costruttore sui dati di input
class Cibo:
	'''
	Un esempio di classe per gestire i valori nutritivi dei cibi.
	'''
	def __init__(self, prot, carb, gras):
		# CONTROLLO: i dati sono tutti numerici?
		if not all([ type(elem) in (int, float) for elem in (prot, carb, gras) ]):
			raise Exception("Inserire solo numeri interi o con la virgola.")
		# CONTROLLO: i dati sono tutti positivi?
		elif any([ prot<0, carb<0, gras<0 ]):
			raise Exception("I valori nutritivi non possono essere negativi.")
		# Se è tutto ok, crea l'istanza!
		else:
			self.proteine = prot
			self.carboidrati = carb
			self.grassi = gras

diet_coke = Cibo(prot=5, carb=5, gras=-100)  # <- errore

alien_food = Cibo(prot=6, carb="space", gras=9)  # <- errore


# Aggiungiamo un metodo alla classe
class Cibo:
	'''
	Un esempio di classe per gestire i valori nutritivi dei cibi.
	'''
	def __init__(self, prot, carb, gras):
		# CONTROLLO: i dati sono tutti numerici?
		if not all([ type(elem) in (int, float) for elem in (prot, carb, gras) ]):
			raise Exception("Inserire solo numeri interi o con la virgola.")
		# CONTROLLO: i dati sono tutti positivi?
		elif any([ prot<0, carb<0, gras<0 ]):
			raise Exception("I valori nutritivi non possono essere negativi.")
		# Se è tutto ok, crea l'istanza!
		else:
			self.proteine = prot
			self.carboidrati = carb
			self.grassi = gras

	def calcola_calorie(self):
		return self.proteine*4 + self.carboidrati*4 + self.grassi*9

pasta = Cibo(prot=13, carb=74, gras=1)

print(pasta.calcola_calorie())

pizza = Cibo(prot=10, carb=30, gras=12)

print(pizza.calcola_calorie())


# Oppure un nuovo metodo si può definire a parte:
def calcola_calorie(self):
	return self.proteine*4 + self.carboidrati*4 + self.grassi*9
# E poi lo si aggiunge alla classe con:
Cibo.calcola_calorie = calcola_calorie


'''
- un metodo è una funzione abbinata all'oggetto
- un attributo è un dato che lo caratterizza
- si parla di "incapsulamento"
---> per questo si parla di 'programmazione orientata agli oggetti'
'''


# Un altro esempio
class Gatto:
	def __init__(self, nome, colore, eta, razza):
		self.nome = nome
		self.colore = colore
		self.eta = eta
		self.razza = razza

gatto1 = Gatto("Sylvester", "Nero", 3, "Soriano")

gatto1

print(gatto1.nome)

print(gatto1.colore)

print(gatto1.razza)

# Metodi della classe
class Gatto:
	def __init__(self, nome, colore, eta, razza):
		self.nome = nome
		self.colore = colore
		self.eta = eta
		self.razza = razza

	def verso(self):
		print("meow")

	def fusa(self):
		print("purr")

gatto2 = Gatto("Gibson", "Pezzato", 6, "Balinese")

gatto2.verso()

gatto2.fusa()


# Ereditarietà
'''
- definire una classe a partire da una classe preesistente, che quindi ne "eredita" i metodi e gli attributi
- la classe "superiore" generalizza, mentre la classe "inferiore" specifica.
'''
class Verdura(Cibo):
	def __init__(self, prot, carb):
		self.grassi = 0
		self.proteine = prot
		self.carboidrati = carb

# Creiamo una istanza
melanzana = Verdura(prot=1.5, carb=2.5)

print(melanzane.calcola_calorie())

# Un'altra versione, più corretta
# In questo modo non perdiamo tutti i controlli e le logiche già implementati
class Verdura(Cibo):
	def __init__(self, prot, carb):
		super().__init__(prot=prot, carb=carb, gras=0)


# Aggiungiamo caratteristiche specifiche
class Verdura(Cibo):
	def __init__(self, prot, carb, etic):
		# Chiamiamo il costruttore della classe precedente
		# per gestire i dati della classe 'Cibo'
		super().__init__(prot=prot, carb=carb, gras=0)

		# Gestiamo i dati specifici della classe 'Verdura'
		if type(etic) != str:
			raise Exception("L'etichetta deve essere una stringa.")
		else:
			self.etichetta = etic

	def valuta_etichetta(self):
		if self.etichetta == "certificata":
			print("Ottima etichetta")
		else:
			print("Etichetta mediocre")

carota = Verdura(prot=1, carb=7, etic=9)  # <- errore

carota = Verdura(prot=1, carb=7, etic="certificata")

carota.carboidrati

carota.calcola_calorie()

carota.valuta_etichetta()


# Proprietà
'''
- per usare un metodo di una classe come se fosse un attributo
'''
Cibo.calorie = property(calcola_calorie)
melanzane.calorie
pasta.calorie


# Proprietà che definiscono attributi
class Verdura(Cibo):
	def __init__(self, proteine=0, carboidrati=0):
		self.grassi = 0
		self.proteine = proteine
		self.carboidrati = carboidrati
	def get_carboidrati(self):
		return self.carboidrati
	def set_carboidrati(self, nuovo_valore_carboidrati):
		self.carboidrati = nuovo_valore_carboidrati
	carboidrati = property(get_carboidrati, set_carboidrati)
	def get_proteine(self):
		return self.proteine
	def set_proteine(self, nuovo_valore_proteine):
		self.proteine = nuovo_valore_proteine
	proteine = property(get_proteine, set_proteine)
	def get_grassi(self):
		return self.grassi
	def set_grassi(self, nuovo_valore_grassi):
		if nuovo_valore_grassi > 0:
			raise Exception("Le verdure non hanno grassi")
	grassi = property(get_grassi, set_grassi)

carota = Verdura(1, 7)

carota.calorie

carote.carboidrati

carota.carboidrati = 20

carota.grassi

carota.grassi = 5


# Metodi privati
'''
- sono metodi che non possono essere richiamati dall'esterno della classe cui appartengono
- per convenzione ("naming convention") iniziano con '__' (ad esempio '__init__')
'''
class Archivio:
	def __apri_file__(self):
		print("un metodo privato")


# Metodi speciali
'''
- permettono di adattare i metodi "classici" di Python a delle nuove classi
- ad esempio: 'len', 'str'
'''

# Ridefiniamo il metodo '__len__'
class Video:
	def __init__(self, nome, durata):
		self.nome = nome
		self.durata = durata

	def __len__(self):
		return self.durata

vlog1 = Video(nome="Parlo di me", durata=12)

print(len(vlog1))

lista = [1, 2, 3]
dir(lista)  # <- Contiene metodi speciali (e privati)
dir(vlog1)  # <- I metodi speciali sono già presenti!
print(vlog1)
str(vlog1)  # <- Ma hanno dei funzionamenti di default


# Ridefiniamo il metodo '__str__'
class Video:
	def __init__(self, nome, durata):
		self.nome = nome
		self.durata = durata

	def __len__(self):
		return self.durata

	def __str__(self):
		return "Video dal titolo '{0}'".format(self.nome)

vlog2 = Video(nome="Vi mostro la mia stanza", durata=5)

print(str(vlog1))

print(str(vlog2))




# +------------------+
# |  INPUT E OUTPUT  |
# +------------------+

# Funzione 'print'
help(print)

for n in range(3):
	print("Il valore di 'n' è:", n)

for n in range(3):
	print("Il valore di 'n' è:", n, sep="")

for n in range(3):
	print("Il valore di 'n' è:", n, sep="", end=", ")


# File
'''
- Python mette a disposizione la classe 'open'
'''
myfile = open("prova.txt", "w")
'''
- con l'istruzione precedente un eventuale file dal nome 'prova.txt' (nella working directory) verrà cancellato
'''

'''
Parametri:
- w: write
- r: read
- a: append
'''
dir(myfile)

myfile.name

myfile.mode 

myfile.closed

myfile.write("Scrivo nel file.")

myfile.close()

myfile.closed

myfile = open("prova.txt", "r")

myfile.readline()

myfile.close()

altro_file = open("altra_prova.txt", "w")
altro_file.write("Cose varie.\n")
altro_file.write("Altre cose.\n")
altro_file.write("E del testo.")
altro_file.close()

altro_file = open("altra_prova.txt", "r")
for line in altro_file.readlines():
	print(line)
altro_file.close()


'''
Esercitazione su Spyder
'''
print("Inserisci dei numeri")
lista = []
for n in range(5):
    num = input()
    lista.append(num)
    
il_file = open("mia_lista.txt", "w")
for elemento in lista:
    il_file.write(elemento)
    il_file.write("\n")
il_file.close()

print("Ho scritto il file")