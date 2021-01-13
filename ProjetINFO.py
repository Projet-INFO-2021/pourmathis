##importations
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
  Etat_Etat INT NOT NULL,
  Ressource_SousActivite_Activite_Chapitre_Module_CodeModule INT NOT NULL,
  Ressource_SousActivite_Activite_Chapitre_CodeChapitre INT NOT NULL,
  Ressource_SousActivite_Activite_CodeActivite INT NOT NULL,
  Ressource_SousActivite_CodeSousActivite INT NOT NULL,
  Ressource_CodeRessource INT NOT NULL,
  PRIMARY KEY (Personne_idPersonne, Etat_Etat, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivite_Activite_CodeActivite, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource))
  """)

cursor.execute("""
DROP TABLE Commentaires""")

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
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES (64186, '123456', 1, 0);""")
cursor.execute("""
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES (64098, '335489', 2, 0);""")
cursor.execute("""
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES (64125, '951753', 3, 0);""")
cursor.execute("""
INSERT INTO Identifiants (NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES (00112, '147369', 4, 0);""")


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
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (1, 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (1, 1, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (1, 2, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 1, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 1, 1, 1, 1, 3);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 2, 1, 1, 1, 1);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 2, 1, 1, 1, 2);""")
cursor.execute("""
INSERT INTO Token_has_Ressource (Token_idToken, Ressource_SousActivite_Activite_Chapitre_Module_CodeModule, Ressource_SousActivite_Activite_Chapitre_CodeChapitre, Ressource_SousActivité_Activité_CodeActivité, Ressource_SousActivite_CodeSousActivite, Ressource_CodeRessource) VALUES (2, 3, 2, 1, 1, 1);""")

#cursor.execute("""""")





cursor.execute("""
INSERT INTO Identifiants(Personne_idPersonne, NomDeCompte, MotDePasse) VALUES(?, ?, ?)""", (31041, 'carolilou', "Beignet"))
cursor.execute("""SELECT Personne_idPersonne,MotDePasse  FROM Identifiants""")
user1 = cursor.fetchone()
print(user1)

def identification(id, motdepasse):
    cursor.execute("SELECT * FROM Identifiants WHERE Personne_idPersonne = " + str(id))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "identifiant ou mot de passe incorrect"
    elif resultat[0][1]==str(motdepasse) :
        cursor.execute("""UPDATE Identifiants SET Connexion = ? WHERE Personne_idPersonne = ?""", (1,id,))
        return 'Bonjour' , resultat[0][0]
    return "identifiant ou mot de passe incorrect"


def ajouter_Module(NomModule,CodeModule):
    cursor.execute("""INSERT INTO Module(NomModule, CodeModule) VALUES(?, ?)""", (NomModule, CodeModule))

def ajouter_Chapitre(NomChapitre,CodeModule,CodeChapitre):
    cursor.execute("""INSERT INTO Module(NomChapitre, CodeModule, CodeChapitre) VALUES(?, ?)""", (NomChapitre, CodeModule,CodeChapitre))

def ajouter_Activite(NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre):
    cursor.execute("""INSERT INTO Module(NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre) VALUES(?, ?)""", (NomActivite, CodeActivite, Chapitre_Module_CodeModule, Chapitre_CodeChapitre))

def ajouter_SousActivite(NomSousActivite,CodeSousActivite,Activite_CodeActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre):
    cursor.execute("""INSERT INTO Module(NomSousActivite, CodeSousActivite, Activite_CodeActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre) VALUES(?, ?)""", 
    (NomSousActivite, CodeSousActivite,Activite_CodeActivite, Activite_Chapitre_Module_CodeModule, Activite_Chapitre_CodeChapitre))


def ajouter_Ressource(NomdeDocument,SousActivite_CodeSousActivite,SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource):
    cursor.execute("""INSERT INTO Module(NomdeDocument, SousActivite_CodeSousActivite, SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource) VALUES(?, ?)""", 
    (NomdeDocument, SousActivite_CodeSousActivite,SousActivite_Activite_CodeActivite, SousActivite_Activite_Chapitre_Module_CodeModule, SousActivite_Activite_Chapitre_CodeChapitre, CodeRessource))

def ajouter_eleve(id, nom, prenom, datedenaissance, annee, filiaire, statut, motdepasse, nomdecompte):
    cursor.execute("""INSERT INTO  Identifiants(NomDeCompte, MotDePasse, Personne_idPersonne, Connexion) VALUES(?,?,?,?)""",(nomdecompte,motdepasse, id, 0))
    cursor.execute("""INSERT INTO Personne(idPersonne, Nom, Prenom, DateDeNaissance, Annee, Filliaire, Personne_Statut) VALUES(?,?,?,?,?,?,?)""",(id, nom, prenom, datedenaissance, annee, filiaire, statut))

def afficher_connectes():
    cursor.execute("""SELECT NomDeCompte FROM Identifiants WHERE Connexion =1""")


ajouter_eleve(5, 'bous', 'cha', '28102000', 3, 'csi', 'eleve', 'mdp', 'jeo')
ajouter_eleve(6, 'lilou', 'caro', '28072001','', '', 'prof', 'crce', 'carolane')

cursor.execute("""SELECT idPersonne, Nom, Prenom, DateDeNaissance, Annee, Filliaire, Personne_Statut FROM Personne""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2} - {3} - {4} - {5} - {6}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

cursor.execute("""UPDATE Personne SET Nom = ? WHERE idPersonne = 2""", ('Christ',))
cursor.execute("""UPDATE Personne SET Prenom = ? WHERE idPersonne = 2""", ('Jesus',))
cursor.execute("""UPDATE Personne SET DateDeNaissance = ? WHERE idPersonne = 2""", ('00000000',))

id = 2
cursor.execute("""SELECT idPersonne, Nom, Prenom, DateDeNaissance FROM Personne WHERE idPersonne=?""", (id,))
response = cursor.fetchone()
print(response)


print("Entrer ID d'élève que vous voulez supprimer")
iD=input()

 

#print("Entrer son nom")
#Nom=input()

  
#cursor.execute("SELECT Personne_idPersonne FROM Identifiants WHERE Personne_idPersonne = "+ str(id))
#resultat = list(cursor)
#print(resultat)
def delete(table,tableid,id):
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
        return "Vous avez bien supprimé l'élève"

def estconnecte():
    cursor.execute("""SELECT NomDeCompte FROM Identifiants WHERE Connexion = 1""")
    reponse=list(cursor)
    for x in reponse:
        print('?',(x))


def EleveVersID (nom, prenom, annee):
    cursor.execute("SELECT idPersonne FROM Personne WHERE Nom = ? AND Prenom = ? AND Annee = ? ",(nom, prenom, annee))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "Informations Eleve incorrectes" 
    else :
         return resultat


def ModuleVersID (nom):
    cursor.execute("SELECT CodeModule FROM Module WHERE NomModule = ? ",(nom))  
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "Module Inexistant"
    else :
        return

def SupprimerELeveModule(idEleve,idMod):
    cursor.execute("SELECT Personne_idPersonne FROM Module_has_Personne WHERE Personne_idPersonne = ? AND Module_CodeModule = ?",(idEleve,idMod))
    resultat = list(cursor)
    if len(resultat) == 0 :
        return "Eleve deja absent du Module"
    else :
        cursor.execute("DELETE * FROM Module_has_Personne WHERE Personne_idPersonne = ? AND Module_CodeModule = ?",(idEleve,idMod))


def trouveNom(id):
    cursor.execute("SELECT Nom, Prenom FROM Personne WHERE idPersonne =?",(id))
    res=list(cursor)
    return res[0]

print(trouveNom(3))