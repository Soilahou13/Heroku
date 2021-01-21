from app import app
from flask import render_template,request
import sqlite3
import json,random,string


def motdepasse():
    """Générer une chaîne aléatoire de longueur fixe"""
    str = string.ascii_lowercase
    return ''.join(random.choice(str) for i in range(8))

def createdb():
    conn = sqlite3.connect ('base.db')
    print ("base de donnéées ouverte avec succès")
    conn.execute("CREATE TABLE IF NOT EXISTS Patient(Numero_utilisateur INTEGER, Mot_de_passe TEXT, Nom TEXT, Prenom TEXT, Age INTEGER, Adresse TEXT, Hematies INTEGER, Hemoglobine INTEGER, Hematocrite INTEGER, VGM INTEGER, CCMH INTEGER, TCMH INTEGER,RDW INTEGER,Polynucleaires_neutrophiles INTEGER,Polynucleaires_eosinophiles INTEGER,Polynucleaires_basophiles INTEGER,Lymphocytes INTEGER, Monocytes INTEGER)")
    print ("Table créée avec succès")
    conn.close()

def adduser(Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes):
    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        cur.execute(" INSERT INTO Patient (Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" , (Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes))
        con.commit()
    con.close()

def Utilisateur1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Numero_utilisateur from Patient ;")
    a = cursor.fetchall()
    Utilisateur=""
    for i in a:
        Utilisateur = "".join(map(str, i))

    return Utilisateur


def Mdp1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Mot_de_passe from Patient ;")
    a = cursor.fetchall()
    Mdp=''
    for i in a:
        Mdp = "".join(map(str, i))
    return Mdp

def Nom1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Nom from Patient ;")
    a = cursor.fetchall()
    Nom=''
    for i in a:
        Nom = "".join(map(str, i))
    return Nom

def Prenom1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Prenom from Patient ;")
    a = cursor.fetchall()
    Prenom=''
    for i in a:
        Prenom = "".join(map(str, i))
    return Prenom

def Age1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Age from Patient ;")
    a = cursor.fetchall()
    Age=''
    for i in a:
        Age = "".join(map(str, i))
    return Age

def Adresse1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Adresse from Patient ;")
    a = cursor.fetchall()
    Adresse=''
    for i in a:
        Adresse = "".join(map(str, i))
    return Adresse

def Hematies1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Hematies from Patient ;")
    a = cursor.fetchall()
    Hematies=''
    for i in a:
        Hematies = "".join(map(str, i))
    return Hematies

def Hemoglobine1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Hemoglobine from Patient ;")
    a = cursor.fetchall()
    Hemoglobine=''
    for i in a:
        Hemoglobine = "".join(map(str, i))
    return Hemoglobine

def Hematocrite1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Hematocrite from Patient ;")
    a = cursor.fetchall()
    Hematocrite=''
    for i in a:
        Hematocrite = "".join(map(str, i))
    return Hematocrite

def VGM1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT VGM from Patient ;")
    a = cursor.fetchall()
    VGM=''
    for i in a:
        VGM = "".join(map(str, i))
    return VGM

def CCMH1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT CCMH from Patient ;")
    a = cursor.fetchall()
    CCMH=''
    for i in a:
        CCMH = "".join(map(str, i))
    return CCMH

def TCMH1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT TCMH from Patient ;")
    a = cursor.fetchall()
    TCMH=''
    for i in a:
        TCMH = "".join(map(str, i))
    return TCMH

def RDW1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT RDW from Patient ;")
    a = cursor.fetchall()
    RDW=''
    for i in a:
        RDW = "".join(map(str, i))
    return RDW

def Polynucleaires_neutrophiles1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Polynucleaires_neutrophiles from Patient ;")
    a = cursor.fetchall()
    Polynucleaires_neutrophiles=''
    for i in a:
        Polynucleaires_neutrophiles = "".join(map(str, i))
    return Polynucleaires_neutrophiles

def Polynucleaires_eosinophiles1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Polynucleaires_eosinophiles from Patient ;")
    a = cursor.fetchall()
    Polynucleaires_eosinophiles=''
    for i in a:
        Polynucleaires_eosinophiles = "".join(map(str, i))
    return Polynucleaires_eosinophiles

def Polynucleaires_basophiles1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Polynucleaires_basophiles from Patient ;")
    a = cursor.fetchall()
    Polynucleaires_basophiles=''
    for i in a:
        Polynucleaires_basophiles = "".join(map(str, i))
    return Polynucleaires_basophiles

def Lymphocytes1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Lymphocytes from Patient ;")
    a = cursor.fetchall()
    Lymphocytes=''
    for i in a:
        Lymphocytes = "".join(map(str, i))
    return Lymphocytes

def Monocytes1():
    con = sqlite3.connect('base.db')
    cursor = con.cursor()
    cursor.execute("SELECT Monocytes from Patient ;")
    a = cursor.fetchall()
    Monocytes=''
    for i in a:
        Monocytes = "".join(map(str, i))
    return Monocytes


def remplissage(data):
    for i in data:
        Numero_utilisateur = data['Numero_utilisateur']
        Adresse = data['Adresse']
        Mot_de_passe = data['Mot_de_passe']
        Nom = data['Nom']
        Prenom = data['Prenom']
        Age = data['Age']
        Hematies = data['Hematies']
        Hemoglobine = data['Hemoglobine']
        Hematocrite = data['Hematocrite']
        VGM = data['VGM']
        CCMH = data['CCMH']
        TCMH = data['TCMH']
        RDW = data['RDW']
        Polynucleaires_neutrophiles = data['Polynucleaires_neutrophiles']
        Polynucleaires_eosinophiles = data['Polynucleaires_neutrophiles']
        Polynucleaires_basophiles = data['Polynucleaires_basophiles']
        Lymphocytes = data['Lymphocytes']
        Monocytes = data['Monocytes']
    adduser(Numero_utilisateur,Mot_de_passe, Nom , Prenom, Age, Adresse, Hematies, Hemoglobine, Hematocrite, VGM, CCMH , TCMH, RDW , Polynucleaires_neutrophiles,Polynucleaires_eosinophiles,Polynucleaires_basophiles,Lymphocytes,Monocytes)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personnell')
def espace_perso():
    return render_template('espace_personnel.html')

@app.route("/Resultats")

def resultats():
    Hematies = Hematies1()
    Hemoglobine = Hemoglobine1()
    Hematocrite = Hematocrite1()
    VGM = VGM1()
    CCMH = CCMH1()
    TCMH = TCMH1()
    RDW = RDW1()
    Polynucleaires_neutrophiles = Polynucleaires_neutrophiles1()
    Polynucleaires_basophiles = Polynucleaires_basophiles1()
    Polynucleaires_eosinophiles = Polynucleaires_eosinophiles1()
    Lymphocytes = Lymphocytes1()
    Monocytes = Monocytes1()
    return render_template('resultats.html', Hematies = str(Hematies), Hemoglobine = str(Hemoglobine), Hematocrite = str(Hematocrite), VGM = str(VGM), CCMH = str(CCMH), TCMH = str(TCMH), RDW = str(RDW), Polynucleaires_neutrophiles = str(Polynucleaires_neutrophiles),Polynucleaires_eosinophiles = str(Polynucleaires_eosinophiles),Polynucleaires_basophiles = str(Polynucleaires_basophiles),Lymphocytes = str(Lymphocytes),Monocytes = str(Monocytes))
    
@app.route("/Resultats",methods=['POST'])



def affichage():
    createdb()
    nom = request.form.get("nom")
    fichier = nom+'.json'
    try:
        with open(fichier):pass
    except IOError:
        return 'Erreur! vérifiez le nom'
    f = open(fichier)
    data = json.load(f)
    f.close()
    remplissage(data)
    Utilisateur = Utilisateur1()

    Nom = Nom1()
    Prenom = Prenom1()
    Adresse = Adresse1()
    Mdp = Mdp1()
    Age = Age1()
    Hematies = Hematies1()
    Hemoglobine = Hemoglobine1()
    Hematocrite = Hematocrite1()
    VGM = VGM1()
    CCMH = CCMH1()
    TCMH = TCMH1()
    RDW = RDW1()
    Polynucleaires_neutrophiles = Polynucleaires_neutrophiles1()
    Polynucleaires_basophiles = Polynucleaires_basophiles1()
    Polynucleaires_eosinophiles = Polynucleaires_eosinophiles1()
    Lymphocytes = Lymphocytes1()
    Monocytes = Monocytes1()
    login=request.form.get("utilisateur")
    Mdp2=request.form.get("motdepasse")
    if login == Utilisateur and Mdp2 == Mdp and nom == Nom:
        return render_template('resultats.html',Utilisateur = str(Utilisateur),Mdp = str(Mdp) ,Nom = str(Nom),Prenom = str(Prenom),Age = str(Age), Adresse = str(Adresse), Hematies = str(Hematies), Hemoglobine = str(Hemoglobine), Hematocrite = str(Hematocrite), VGM = str(VGM), CCMH = str(CCMH), TCMH = str(TCMH), RDW = str(RDW), Polynucleaires_neutrophiles = str(Polynucleaires_neutrophiles),Polynucleaires_eosinophiles = str(Polynucleaires_eosinophiles),Polynucleaires_basophiles = str(Polynucleaires_basophiles),Lymphocytes = str(Lymphocytes),Monocytes = str(Monocytes))
        return 'Bonsoir, non'
    
    

@app.route('/informations')
def informations():
    Nom = Nom1()
    Prenom = Prenom1()
    Adresse = Adresse1()
    Age = Age1()
    return render_template('informations.html',Nom = str(Nom),Prenom = str(Prenom),Age = str(Age), Adresse = str(Adresse))

@app.route('/Personnel')
def personnel():
    return render_template('espace_personnel.html')


@app.route("/confirmation",methods=['POST'])
    

def recup_json():    
    Numero_utilisateur = random.randint(100000,999999)
    Adresse = request.form.get('Adresse')
    Mot_de_passe = motdepasse()
    Nom = request.form.get('Nom')
    Prenom = request.form.get('Prenom')
    Age = request.form.get('Age')
    Hematies = round(random.uniform(3.0, 7.0),2)
    Hemoglobine = round(random.uniform(10.0, 16.0),2)
    Hematocrite = round(random.uniform(32.0, 45.0),2)
    VGM = round(random.uniform(70.0, 100.0),2)
    CCMH = round(random.uniform(25.0, 38.0),2)
    TCMH = round(random.uniform(22.0, 35),2)
    RDW = round(random.uniform(9.0,17.0),2)
    Polynucleaires_neutrophiles = round(random.uniform(1.5, 8),2)
    Polynucleaires_eosinophiles = round(random.uniform(0.04, 0.66),2)
    Polynucleaires_basophiles = round(random.uniform(0.1, 0.09),2)
    Lymphocytes = round(random.uniform(1.3, 4),2)
    Monocytes = round(random.uniform(0.15, 0.9),2)

        

    data = {
        "Numero_utilisateur":Numero_utilisateur,
        "Mot_de_passe":Mot_de_passe,
        "Nom":Nom,
        "Prenom":Prenom,
        "Age":Age,
        "Adresse":Adresse,
        "Hematies":Hematies,
        "Hemoglobine":Hemoglobine,
        "Hematocrite":Hematocrite,
        "VGM":VGM,
        "CCMH":CCMH,
        "TCMH":TCMH,
        "RDW":RDW,
        "Polynucleaires_neutrophiles":Polynucleaires_neutrophiles,
        "Polynucleaires_eosinophiles":Polynucleaires_eosinophiles,
        "Polynucleaires_basophiles":Polynucleaires_basophiles,
        "Lymphocytes":Lymphocytes,
        "Monocytes":Monocytes,
        }
    with open(Nom+".json", "w") as f_write:
        json.dump(data, f_write, indent=1)

    return ('<h4>Veuillez communiquer ces données au patient </h4>'+'<h4> Numéro Utilisateur:'+str(Numero_utilisateur)+"</h4>"+"<h4>Mot de passe : "+str(Mot_de_passe)+"</h4>")

@app.route('/modification',methods=['POST'])
def modification():
    nom = Nom1()
    Newadd = request.form.get('Adresse')

    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE Patient SET Adresse = "+"'"+Newadd+"'"+"WHERE Nom = "+"'"+nom+"'"+" ;")
        con.commit()
    con.close()
    return (Newadd,nom)