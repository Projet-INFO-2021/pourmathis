# Liste des fonctions :

Fonction(Parametres)	=> Explication

Identification(nomdecompte,mdp)		=> Renvoie le statut d'une personne ou un messsage d'erreur
AjouterModule (nomModule) 	=>Creer un module avec un Id + un token
AjouterChapitre(nomChap,CodeMODULE,CodeChap)		=> Creer chap	
AjouterActivite	(nomAct,CodeMODULE,CodeChap,CodeAct)		=> Creer Activite
AjouterSousActivite(nomSousAct,CodeMODULE,CodeChap,CodeAct,CodeSousAct)		=> Creer SousActivite
AjouterRessource(nomRessource,CodeMODULE,CodeChap,CodeAct,CodeSousAct,CodeRessource)		=> Creer Ressource
SuppressionEleveEcole(idPersonne)		Supprime TOUTES les données de l'élève
EstConnecte()		=> Affiche toutes les personnes connectées
EleveVersID (nom,prenom)		=> Besoin d'explication ? Non
IDVersEleve		=> Same here
ModuleVersID		=> And here
SupprimerELeveModule(idEleve,idModule)		=> Supprime un élève d'un module 
AjouterEleveAModule(Nom,Prenom,Module)		=> Flemme 
DeconnexionParNom(nom,prenom)		=> 
DeconnexionParId(idPersonne)		=>
AfficherModules(nom, prenom) 		=> Affiche tous les modules de l'élève
AfficherChapitresModule(codeModule)	=> Affiche tous les chapitres d'un module
EtatLectureDocument(IdPersonne,CodeModule,CodeChapitre,CodeActivite,CodeSousActivite,CodeRessource)		=> Met le document en lu
AfficherAvancement(IdPersonne,CodeModule,CodeChapitre,CodeActivite,CodeSousActivite,CodeRessource)		=> Affiche si le doc est lu 
AfficherEleveAccesRessource(CodeModule,CodeChapitre,CodeActivite,CodeSousActivite,CodeRessource)		=> Affiche les élèves qui ont accès à cette ressource
AfficherEleveDansModule(IdModule)	=> Affiche les élèves qui ont accès au module
AfficherActivitesChapitre(CodeModule,CodeChap)		=> Affiche les activités d'un chapitre
AfficherSousActivitesActivite(CodeMod,CodeChap,CodeAct)		=> Affiche les sous activités d'une activité
AjouterAvancement(CodeModule,CodeChapitre,CodeActivite,CodeSousActivite,CodeRessource)		=> Créer un avancement pour une ressource (à 0 de base)
AfficherRessourceSousActivite(CodeModule,CodeChapitre,CodeActivite,CodeSousActivite)		=> Affiche les ressources d'une sous activité
AvancementNouveauModule(IdModule,IdPersonne)		=> Créer un avancement pour un module (à 0 de base)
CreationToken(CodeMODULE) 	=> Renvoie un nombre aléatoire qui est CodeToken
VerificationToken(CodeToken)		=> Verifie si CodeToken existe pour un module si oui renvoie son codeModule
ListeEleves()		=> Donne la liste de tous les élèves de la base
AjoutSelonToken(CodeToken,IdPersonne)	=>Personne ajoutée au module correspondant
TokenDuModule(IdModule)		=> Renvoie le token du module
AfficherModulesComplet =>PasUtile 
