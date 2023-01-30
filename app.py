from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

def creer_bande(taille, nb_pieces):
    t = [0]*taille
    deb = 1
    fin = taille - nb_pieces
    for _ in range(nb_pieces):
        i = randint(deb, fin)
        t[i] = 1
        deb = i+1
        fin = fin + 1
    return t

def est_valide(bande, saisie):
    try:
        index = int(saisie)
    except:
        return False
    saisie = int(saisie)
    if not bande[saisie]==1:
        if 0<=saisie<len(bande):
           return True
        else:
            return False
    else:
        return False
        
def jouer(bande, saisie):
    if est_valide(bande, saisie):
        saisie = int(saisie)
        for i in range(len(bande)):
            if i==saisie:
               bande[i]=1
               fin = i
               break
        for i in range(fin+1, len(bande)):
            if bande[i]==1:
                bande[i]=0
                break
                
def partie_finie(bande):
    return bande[:bande.count(1)]==[1]*bande.count(1)

def choix_dispo(tab):
    pos = []
    for i in range(len(tab)):
        if tab[i] == 0:
            if 1 in tab[i+1:]:
                pos.append(i)
    return pos

@app.route('/', methods=['GET', 'POST'])
def index():
    global bande
    if request.method == 'POST':
        saisie = request.form['saisie']
        jouer(bande, saisie)
    if partie_finie(bande):
        bande = creer_bande(10, 3)
    return render_template('index.html', bande=bande, choix=choix_dispo(bande))

if __name__ == '__main__':
    bande = creer_bande(10, 3)
    app.run(debug=True)