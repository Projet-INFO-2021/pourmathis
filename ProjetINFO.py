##importations
import random
import sqlite3
from math import *
##BDD

conn = sqlite3.connect('INFO')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Identifiants(
  NomDeCompte VARCHAR(45) NOT NULL,
  MotDePasse VARCHAR(45) NOT NULL,
  Personne_idPersonne INT NOT NULL,
  Connexion INT NULL,
  PRIMARY KEY (NomDeCompte, MotDePasse)
)
""")
 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Chapitre(
  NomChapitre VARCHAR(45) NULL,
  Module_CodeModule INT NOT NULL,
  CodeChapitre INT NOT NULL,
  PRIMARY KEY (Module_CodeModule, CodeChapitre)
)
""")

 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Personne (
  idPersonne INT NOT NULL,
  Nom TEXT NULL,
  Prenom TEXT NULL,
  DateDeNaissance DATE NULL,
  Annee VARCHAR(45) NULL,
  Filliaire VARCHAR(45) NULL,
  Personne_Statut VARCHAR(45) NULL,
  PRIMARY KEY (idPersonne))
  """)



cursor.execute("""
CREATE TABLE IF NOT EXISTS Statut (
  Statut INT NOT NULL,
  PRIMARY KEY (Statut))
  """)

 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Etat (
  Etat INT NOT NULL,
  NomEtat VARCHAR(45) NULL,
  PRIMARY KEY (Etat))
  """)

 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Module (
  NomModule VARCHAR(45) NULL,
  CodeModule INT NOT NULL,
  PRIMARY KEY (CodeModule))
  """)

 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Activite (
  NomActivite VARCHAR(45) NULL,
  CodeActivite INT NOT NULL,
  Chapitre_Module_CodeModule INT NOT NULL,
  Chapitre_CodeChapitre INT NOT NULL,
  PRIMARY KEY (Chapitre_Module_CodeModule, Chapitre_CodeChapitre, CodeActivite))
  """)

 

cursor.execute("""
CREATE TABLE IF NOT EXISTS SousActivite (
  NomSousActivite VARCHAR(45) NULL,
  CodeSousActivite INT NOT NULL,
  Activite_CodeActivite INT NOT NULL,
  Activite_Chapitre_Module_CodeModule INT NOT NULL,
  Activite_Chapitre_CodeChapitre INT NOT NULL,
  PRIMARY KEY (Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre, Activite_CodeActivite, CodeSousActivite))
""")

 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Ressource (
  NomdeDocument VARCHAR(45) NULL,
  SousActivite_CodeSousActivite INT NOT NULL,
  SousActivite_Activite_CodeActivite INT NOT NULL,
  SousActivite_Activite_Chapitre_Module_CodeModule INT NOT NULL,
  SousActivite_Activite_Chapitre_CodeChapitre INT NOT NULL,
  CodeRessource INT NOT NULL,
  PRIMARY KEY (SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, SousActivite_Activite_CodeActivite, SousActivite_CodeSousActivite, CodeRessource))
  """)

 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Module_has_Personne (
  Module_CodeModule INT NOT NULL,
  Personne_idPersonne INT NOT NULL,
  PRIMARY KEY (Module_CodeModule, Personne_idPersonne))
  """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Rendu (
  idRendu INT NOT NULL,
  NomRendu VARCHAR(45) NULL,
  Personne_idPersonne INT NOT NULL,
  SousActivite_Activite_Chapitre_Module_CodeModule INT NOT NULL,
  SousActivite_Activite_Chapitre_CodeChapitre INT NOT NULL,
  SousActivite_Activite_CodeActivite INT NOT NULL,
  SousActivite_CodeSousActivite INT NOT NULL,
  PRIMARY KEY (Personne_idPersonne, idRendu, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, SousActivite_Activite_CodeActivite, SousActivite_CodeSousActivite))
  """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Avancement (
  Personne_idPersonne INT NOT NULL,
  Etat_Etat INT NULL,
  Ressource_SousActivite_Activite_Chapitre_Module_CodeModule INT NOT NULL,
  Ressource_SousActivite_Activite_Chapitre_CodeChapitre INT NOT NULL,
  Ressource_SousActivite_Activite_CodeActivite INT NOT NULL,
  Ressource_SousActivite_CodeSousActivite INT NOT NULL,
  Ressource_CodeRessource INT NOT NULL,
  PRIMARY KEY (Personne_idPersonne, Etat_Etat, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource))
  """)



cursor.execute("""
CREATE TABLE IF NOT EXISTS Commentaires (
  idCommentaires INT NOT NULL,
  CommentaireTexte LONGTEXT NULL,
  Ressource_SousActivite_Activite_Chapitre_Module_CodeModule INT NOT NULL,
  Ressource_SousActivite_Activite_Chapitre_CodeChapitre INT NOT NULL,
  Ressource_SousActivite_Activite_CodeActivite INT NOT NULL,
  Ressource_SousActivite_CodeSousActivite INT NOT NULL,
  Ressource_CodeRessource INT NOT NULL,
  Personne_idPersonne INT NOT NULL,
  PRIMARY KEY (idCommentaires, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource, Personne_idPersonne))
  """) 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Token (
  idToken INT NOT NULL,
  TokenName VARCHAR(45) NULL,
  PRIMARY KEY (idToken))
  """)


cursor.execute("""
CREATE TABLE IF NOT EXISTS Token_has_Personne (
  Token_idToken INT NOT NULL,
  Personne_idPersonne INT NOT NULL,
  PRIMARY KEY (Token_idToken, Personne_idPersonne))
  """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS TokenModule (
  Token_Code INT NOT NULL,
  Module_CodeModule INT NOT NULL,
  PRIMARY KEY (Token_Code))
  """)


cursor.execute("""
CREATE TABLE IF NOT EXISTS Token_has_Ressource (
  Token_idToken INT NOT NULL,
  Ressource_SousActivite_Activite_Chapitre_Module_CodeModule INT NOT NULL,
  Ressource_SousActivite_Activite_Chapitre_CodeChapitre INT NOT NULL,
  Ressource_SousActivite_Activite_CodeActivite INT NOT NULL,
  Ressource_SousActivite_CodeSousActivite INT NOT NULL,
  Ressource_CodeRessource INT NOT NULL,
  PRIMARY KEY (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource))
  """)




cursor.execute("""
INSERT INTO Ressource (NomDeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES ('bip', 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Ressource (NomDeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES ('bap', 1, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Ressource (NomDeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES ('boop', 1, 1, 1, 1, 3);""")
cursor.execute("""
INSERT INTO Ressource (NomDeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES ('pif', 2, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Ressource (NomDeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES ('paf', 2, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Ressource (NomDeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES ('pouf', 3, 2, 1, 1, 1);""")

cursor.execute("""
INSERT INTO SousActivite (NomSousActivite, CodeSousActivite, Activite_CodeActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre) VALUES ('poteau', 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO SousActivite (NomSousActivite, CodeSousActivite, Activite_CodeActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre) VALUES ('piquet', 2, 1, 1, 1);""")
cursor.execute("""
INSERT INTO SousActivite (NomSousActivite, CodeSousActivite, Activite_CodeActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre) VALUES ('torche', 1, 2, 1, 1);""")

cursor.execute("""
INSERT INTO Activite (NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre) VALUES ('lampadaire', 1, 1, 1);""")
cursor.execute("""
INSERT INTO Activite (NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre) VALUES ('ampoule', 2, 1, 1);""")
cursor.execute("""
INSERT INTO Activite (NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre) VALUES ('led', 3, 1, 1);""")
cursor.execute("""
INSERT INTO Activite (NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre) VALUES ('Briquet', 1, 1, 2);""")

cursor.execute("""
INSERT INTO Chapitre (NomChapitre, Module_CodeModule, CodeChapitre) VALUES ('banane', 1, 1);""")
cursor.execute("""
INSERT INTO Chapitre (NomChapitre, Module_CodeModule, CodeChapitre) VALUES ('lait', 1, 2);""")
cursor.execute("""
INSERT INTO Chapitre (NomChapitre, Module_CodeModule, CodeChapitre) VALUES ('tartine', 2, 1);""")
cursor.execute("""
INSERT INTO Chapitre (NomChapitre, Module_CodeModule, CodeChapitre) VALUES ('soupe', 3, 1);""")

cursor.execute("""
INSERT INTO Module (NomModule, CodeModule) VALUES ('chocolat', 1);""")
cursor.execute("""
INSERT INTO Module (NomModule, CodeModule) VALUES ('nutella', 2);""")
cursor.execute("""
INSERT INTO Module (NomModule, CodeModule) VALUES ('champi', 3);""")


cursor.execute("""
INSERT INTO Module_has_Personne (Module_CodeModule, Personne_idPersonne) VALUES (1, 1);""")
cursor.execute("""
INSERT INTO Module_has_Personne (Module_CodeModule, Personne_idPersonne) VALUES (1, 2);""")
cursor.execute("""
INSERT INTO Module_has_Personne (Module_CodeModule, Personne_idPersonne) VALUES (1, 3);""")
cursor.execute("""
INSERT INTO Module_has_Personne (Module_CodeModule, Personne_idPersonne) VALUES (2, 2);""")
cursor.execute("""
INSERT INTO Module_has_Personne (Module_CodeModule, Personne_idPersonne) VALUES (2, 3);""")
cursor.execute("""
INSERT INTO Module_has_Personne (Module_CodeModule, Personne_idPersonne) VALUES (3, 1);""")
cursor.execute("""
INSERT INTO Module_has_Personne (Module_CodeModule, Personne_idPersonne) VALUES (3, 3);""")

cursor.execute("""
INSERT INTO Personne (idPersonne, Nom, Prenom, DateDeNaissance, Annee, Filliaire, Personne_Statut) VALUES (1, 'Tinel', 'Nicolas', NULL, '3', '1', 'eleve');""")
cursor.execute("""
INSERT INTO Personne (idPersonne, Nom, Prenom, DateDeNaissance, Annee, Filliaire, Personne_Statut) VALUES (2, 'Boussemart', 'Charles', NULL, '3', '1', 'eleve');""")
cursor.execute("""
INSERT INTO Personne (idPersonne, Nom, Prenom, DateDeNaissance, Annee, Filliaire, Personne_Statut) VALUES (3, 'Serlooten', 'Come', NULL, '3', '1', 'eleve');""")
cursor.execute("""
INSERT INTO Personne (idPersonne, Nom, Prenom, DateDeNaissance, Annee, Filliaire, Personne_Statut) VALUES (4, 'Dumont', 'P-E', NULL, '', NULL, 'prof');""")

cursor.execute("""
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES ('64186', '123456', 1, 0);""")
cursor.execute("""
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES ('64098', '335489', 2, 0);""")
cursor.execute("""
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES ('64125', '951753', 3, 0);""")
cursor.execute("""
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES ('00112', '147369', 4, 0);""")


cursor.execute("""
INSERT INTO Statut (Statut) VALUES ('prof');""")
cursor.execute("""
INSERT INTO Statut (Statut) VALUES ('eleve');
""")

cursor.execute("""
INSERT INTO Avancement (Personne_idPersonne, Etat_Etat, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (1, 1, 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Avancement (Personne_idPersonne, Etat_Etat, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 0, 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Avancement (Personne_idPersonne, Etat_Etat, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (3, 0, 1, 1, 1, 1, 1);""")

cursor.execute("""
INSERT INTO Etat (Etat, NomEtat) VALUES (0, 'Non Lu');""")
cursor.execute("""
INSERT INTO Etat (Etat, NomEtat) VALUES (1, 'Lu');""")

cursor.execute("""
INSERT INTO Commentaires (idCommentaires, CommentaireTexte, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource, Personne_idPersonne) VALUES (1, 'Cetait nul jaime pas', 1, 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Commentaires (idCommentaires, CommentaireTexte, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource, Personne_idPersonne) VALUES (2, '0 sur 20 pas content jarrive pas a lire', 1, 1, 1, 1, 1, 1);""")

cursor.execute("""
INSERT INTO Token (idToken, TokenName) VALUES (1, 'AccesRessource1');""")
cursor.execute("""
INSERT INTO Token (idToken, TokenName) VALUES (2, 'AccesRessource2');""")

cursor.execute("""
INSERT INTO Token_has_Personne (Token_idToken, Personne_idPersonne) VALUES (1, 1);""")
cursor.execute("""
INSERT INTO Token_has_Personne (Token_idToken, Personne_idPersonne) VALUES (1, 2);""")
cursor.execute("""
INSERT INTO Token_has_Personne (Token_idToken, Personne_idPersonne) VALUES (1, 3);""")
cursor.execute("""
INSERT INTO Token_has_Personne (Token_idToken, Personne_idPersonne) VALUES (2, 3);""")

cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (1, 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (1, 1, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (1, 2, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 1, 1, 1, 1, 3);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 2, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 2, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 3, 2, 1, 1, 1);""")



def Identification(nomdecompte, motdepasse):
    cursor.execute("SELECT Personne_Statut FROM Personne INNER JOIN Identifiants ON Identifiants.Personne_idPersonne = Personne.idPersonne WHERE NomDeCompte = " + str(nomdecompte) + " AND MotDePasse = " + str(motdepasse))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "identifiant ou mot de passe incorrect"
    else :
        cursor.execute("""UPDATE Identifiants SET Connexion = 1 WHERE NomDeCompte = ?""", (nomdecompte,))
        return (resultat[0][0])

def CreationToken(codemodule):
    rand = random.randint(100000, 999999)
    cursor.execute("""INSERT INTO TokenModule(Token_Code, Module_CodeModule) VALUES(?,?)""",(rand,codemodule))
    return rand


def AjouterModule(NomModule):
    cursor.execute("""SELECT MAX(CodeModule) FROM Module""")
    idList = list(cursor)
    id = idList[0][0] +1
    cursor.execute("""INSERT INTO Module(NomModule, CodeModule) VALUES(?, ?)""", (NomModule,id))
    CreationToken(id)
    
 

def AjouterChapitre(NomChapitre,CodeModule,CodeChapitre):
    cursor.execute("""INSERT INTO Chapitre(NomChapitre, Module_CodeModule, CodeChapitre) VALUES(?,?,?)""", (NomChapitre, CodeModule,CodeChapitre))



def AjouterActivite(NomActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre, CodeActivite):
    cursor.execute("""INSERT INTO Activite(NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre) VALUES(?, ?, ?,?)""", (NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre))

def AjouterSousActivite(NomSousActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre, Activite_CodeActivite, CodeSousActivite):
    cursor.execute("""INSERT INTO SousActivite(NomSousActivite, CodeSousActivite, Activite_CodeActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre) VALUES(?, ?, ?, ?, ?)""",(NomSousActivite,CodeSousActivite,Activite_CodeActivite,Activite_Chapitre_Module_CodeModule,Activite_Chapitre_CodeChapitre))

def AjouterRessource(NomdeDocument, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre,SousActivite_Activite_CodeActivite, SousActivite_CodeSousActivite, CodeRessource):
    cursor.execute("""INSERT INTO Ressource(NomdeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES(?, ?)""", 
    (NomdeDocument, SousActivite_CodeSousActivite,SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource))
    AjouterAvancement(SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, SousActivite_Activite_CodeActivite,  SousActivite_CodeSousActivite, CodeRessource)

def AjouterEleveEcole(nom, prenom, datedenaissance, annee, filiaire, statut, motdepasse, nomdecompte):
    cursor.execute("""SELECT MAX(idPersonne) FROM Personne""")
    idList = list(cursor)
    id = idList[0][0] +1
    cursor.execute("""INSERT INTO  Identifiants(NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES(?,?,?,?)""",(nomdecompte,motdepasse, id, 0))
    cursor.execute("""INSERT INTO Personne(idPersonne, Nom, Prenom, DateDeNaissance, Annee, Filliaire, Personne_Statut) VALUES(?,?,?,?,?,?,?)""",(id, nom, prenom, datedenaissance, annee, filiaire, statut))

def AfficherConnexion():
    cursor.execute("""SELECT NomDeCompte FROM Identifiants WHERE Connexion =1""")

def Delete(table,tableid,id):
    cursor.execute("""DELETE * FROM ? WHERE ? = ?""",(table,tableid,id))

 
def SuppressionEleveEcole(iD):
    cursor.execute("SELECT Personne_idPersonne FROM Identifiants WHERE Personne_idPersonne = " + str(id))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "identifiant incorrect"
    else :
        cursor.execute("DELETE * FROM Identifiants WHERE Personne_idPersonne = " + str(id))
        cursor.execute("DELETE * FROM Personne WHERE idPersonne = " + str(id))
        cursor.execute("DELETE * FROM Avancement WHERE Personne_idPersonne = " + str(id))
        cursor.execute("DELETE * FROM Token_has_Personne WHERE Personne_idPersonne = " + str(id))
        cursor.execute("DELETE * FROM Module_has_Personne WHERE Personne_idPersonne = " + str(id))
        cursor.execute("DELETE * FROM Commentaires WHERE Personne_idPersonne = " + str(id))
        cursor.execute("DELETE * FROM Rendu WHERE Personne_idPersonne = " + str(id))
        return "Vous avez bien supprime l'eleve"


def EstConnecte():
    cursor.execute("""SELECT NomDeCompte FROM Identifiants WHERE Connexion = 1""")
    reponse=list(cursor)
    for x in reponse:
        print('?',(x))


def EleveVersID (nom, prenom, annee):
    cursor.execute("""SELECT idPersonne FROM Personne WHERE Nom = ? AND Prenom = ? AND Annee = ? """,(nom, prenom, annee))
    resultat = cursor.fetchone()
    if len(resultat) == 0 :
        return "Informations Eleve incorrectes" 
    else :
         return resultat


def ModuleVersID(nom):
    cursor.execute("""SELECT CodeModule FROM Module WHERE NomModule = ?""" ,[nom])
    rows = str(cursor.fetchone())
    return rows[1]
    

def SupprimerELeveModule(idEleve,idMod):
    cursor.execute("""SELECT Personne_idPersonne FROM Module_has_Personne WHERE Personne_idPersonne = ? AND Module_CodeModule = ?""",(idEleve,idMod))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "Eleve deja absent du Module"
    else :
        cursor.execute("""DELETE * FROM Module_has_Personne WHERE Personne_idPersonne = ? AND Module_CodeModule = ?""",(idEleve,idMod))
        cursor.execute("""DELETE * FROM Avancement WHERE Personne_idPersonne = ? """,(idEleve,idMod))


def TrouveNom(ids):
    cursor.execute("SELECT Nom, Prenom FROM Personne WHERE idPersonne = " +str(ids))
    rows = str(cursor.fetchone())
    return rows
    
def AjouterEleveAModule(nom, prenom, annee, mdule) :
    IDEleve = EleveEleveVersID(nom, prenom, annee)
    cursor.execute("SELECT CodeModule FROM Module WHERE NomModule = " +str(mdule))
    rows = cursor.fetchone()
    cursor.execute("""INSERT INTO Module_has_Personne(Module_CodeModule, Personne_idPersonne) VALUES(?, ?)""", rows, IDEleve)
    AvancementNouveauModule(rows, IDEleve)


def DeconnexionParNom(nom, prenom, annee):
    id=EleveVersId(nom, prenom, annee)
    cursor.execute("""UPDATE Identifiants SET Connexion = ? WHERE Personne_idPersonne = ?""", (0,id,))

def DeconnexionParId(id):
    cursor.execute("""UPDATE Identifiants SET Connexion = ? WHERE Personne_idPersonne = ?""", (0,id,))

def AfficherModules(nom,prenom,annee) : #Affiche les modules d'un élève
    id=EleveVersId(nom, prenom, annee)
    cursor.execute("""SELECT Module_CodeModule FROM Module_has_Personne WHERE Personne_idPersonne = ?""", (id))
    reponse=list(cursor)
    for x in reponse:
        print('?',(x))

def AfficherChapitresModule(nommodule): 
    cursor.execute("""SELECT NomChapitre FROM Chapitre INNER JOIN Module ON Module.CodeModule=Chapitre.Module_CodeModule WHERE NomModule = ?""",(nommodule,))
    reponse=list(cursor)
    liste = [reponse[x][0] for x in range(len(reponse))]
    return liste
   # for x in reponse:
    #    print('?',(x))

def EtatLectureDocument(idpersonne,codemodule,codechapitre,codeactivite,codesousactivite,coderessource):
    cursor.execute("""UPDATE Avancement SET Etat_Etat=1 WHERE Personne_idPersonne=? Ressource_CodeRessource=? Ressource_SousActivite_CodeSousActivite=? Ressource_SousActivite_Activite_CodeActivite=? Ressource_SousActivite_Activite_Chapitre_CodeChapitre=? Ressource_SousActivite_Activite_Chapitre_Module_CodeModule=?""",(idpersonne,coderessource,codesousactivite,codeactivite,codechapitre,codemodule))

def AfficheEleveAccesRessource(codeModule, codeChapitre, codeActivite, codeSousActivite, codeRessource) :
    cursor.execute("""SELECT idPersonne FROM Personne INNER JOIN Module_has_Personne ON Personne.idPersonne = Module_has_Personne.idPersonne INNER JOIN Module ON Module_has_Personne.CodeModule = Module.CodeModule INNER JOIN Chapitre ON Module.CodeModule = Chapitre.Module_CodeModule INNER JOIN Activite ON Chapitre.CodeChapitre = Activite.Chapitre_CodeChapitre INNER JOIN SousActivite ON Activite.CodeActivite = SousActivite.Activite_CodeActivite INNER JOIN Ressource ON SousActivite.CodeSousActivite = Ressource.Activite_CodeActivite WHERE Module.CodeModule = ? AND Chapitre.CodeChapitre = ? AND Activite.CodeActivite = ? AND SousActivite.CodeSousActivite = ? AND Ressource.CodeRessource = ?""" ,(codeModule, codeChapitre, codeActivite, codeSousActivite, codeRessource))
    reponse = list(cursor)
    return reponse

def AfficherEleveDansModule (idModule) : #Montre les eleves présents dans un module donné
    cursor.execute("""SELECT Nom, Prenom FROM Personne INNER JOIN Module_has_Personne ON Personne.idPersonne = Module_has_Personne.idPersonne INNER JOIN Module ON Module_has_Personne.CodeModule = Module.CodeModule WHERE CodeModule = ?""" ,[idModule])
    reponse = list(cursor)
    return reponse

def AfficherActiviteChapitre(nomchapitre):
    cursor.execute("""SELECT NomActivite FROM Activite INNER JOIN Chapitre ON Activite.Chapitre_CodeChapitre=Chapitre.CodeChapitre WHERE NomChapitre = ?""" ,[nomchapitre])
    reponse=list(cursor)
    liste = [reponse[x][0] for x in range(len(reponse))]
    return liste
 
def SousActivitedActivite(nomactivite):
    cursor.execute("""SELECT NomSousacitivite FROM SousActivite INNER JOIN Activite ON Activite.CodeActivite = SousActivite.Acitvite_CodeActivite WHERE NomActivite = ?""" ,[nomactivite])
    reponse=list(cursor)
    for x in reponse:
        print('?',(x))

def AjouterAvancement(codeModule, codeChapitre, codeActivite, codeSousActivite, codeRessource):
    listidpersonne = AfficheEleveAccesRessource(codeModule, codeChapitre, codeActivite, codeSousActivite, codeRessource)
    for x in listidpersonne:
        cursor.execute("""INSERT INTO Avancement(Personne_idPersonne, Etat_Etat, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES(?,?,?,?,?,?,?) """,(x,0,codeModule, codeChapitre, codeActivite, codeSousActivite, codeRessource))

def AvancementNouveauModule(idModule, idPersonne) : #Apres ajout d'un élève à un module met l'avancement de ce module à 0 
    cursor.execute("""SELECT  Ressource.CodeRessource, Ressource.SousActivite_CodeSousActivite, Ressource.SousActivite_Activite_CodeActivite, Ressource.SousActivite_Activite_Chapitre_CodeChapitre, Ressource.SousActivite_Activite_Chapitre_Module_CodeModule  FROM Ressource INNER JOIN SousActivite ON Ressource.SousActivite_CodeSousActivite = SousActivite.CodeSousActivite INNER JOIN Activite ON SousActivite.Activite_CodeActivite = Activite.CodeActivite INNER JOIN Chapitre ON Activite.Chapitre_CodeChapitre = Chapitre.CodeChapitre INNER JOIN Module ON Chapitre.Module_CodeModule = Module.CodeModule WHERE Module.CodeModule = ?""",(idModule))   
    listidpersonne = list(cursor)
    for x in listidpersonne:
        row = cursor.fetchone()
        codeR = row[0]
        codeSA = row[1]
        codeA = row[2]
        codeC = row[3]
        cursor.execute("""INSERT INTO Avancement(Personne_idPersonne, Etat_Etat, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES(?,?,?,?,?,?,?) """,(idPersonne,0,idModule, codeC, codeA, codeSoA, codeR))


def AfficherRessourceSousActivite(nomsousactivite):
     cursor.execute("""SELECT NomdeDocument FROM SousActivite INNER JOIN Ressource ON SousActivite.CodeSousActivite = Ressource.SousAcitvite_CodeSousActivite WHERE NomSousActivite = ?""" ,[nomsousactivite])
     reponse=list(cursor)
     for x in reponse:
        print('?',(x))


def VerificationToken(CodeToken):
    reponse = cursor.execute("""SELECT Module_CodeModule FROM TokenModule WHERE Token_Code=?""",(CodeToken))
    if len(reponse) == 0 :
        return -1
    else :
        return reponse
  
AjouterActivite('manger',1,1,6)
print(AfficherActiviteChapitre('banane'))


#Fonctions à Créer
#
#Pour les élèves :
#   
#   Afficher Modules                                    fait 
#   Afficher Chapitres d'un Module                      fait 
#   Afficher Activités d'un Chapitre                    fait 
#   Afficher Sous Activités d'une Activité              fait 
#   Afficher Ressource d'une Sous Activité              fait
#   Afficher Eleves de ses Modules                      fait 
#   EstConnecté                                         fait
#   Connexion                                           fait
#   Deconnexion                                         fait
#   Avancement
#   Etat de Lecture d'un Document                       fait
#       (optionnel) Commentaire                     non fait
#       (optionnel) Rendu                           non fait
#       (optionnel) Afficher ressources Token       non fait

#Pour les Professeurs :
#
#   Ajouter Eleve à Ecole                               fait
#   Retirer Eleve à Ecole                               fait
#   Afficher Eleves de ses Modules (avec modules?)      fait 
#   Ajouter Eleve a Module                              fait
#   Retirer Eleve à Module                              fait 
#   Creer Module                                        fait
#   Creer Chapitre                                      fait
#   Creer Activité                                      fait
#   Creer Sous Activité                                 fait
#   Ajouter Ressource                                   fait
#   Afficher Eleve ayant acces Ressource                fait
#   Ajouter Avancement                                  fait 
#   Afficher Etat Lecture par Eleve par Doc         non fait
#       (optionnel) Lire Commentaires               non fait
#       (optionnel) Consulter Rendus                non fait
 
#   Ajouter Avancements pour nouvel eleve