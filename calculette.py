'''
Calculette pour les temps laudren



'''

# coding: utf-8
from tkinter import * #import pour l'interface graphique
from tkinter.messagebox import * #pour les fenetres de dialog



def Calcul (heure, minute):
	'''
	Fonction pour le calcul du temps en centième
	Argument : heure en base 60 et minute en base 60
'''
	#Ajouter contrôle des entry
	try : 
		minute = minute.get ()
		heure = heure.get ()
	except TclError :
		showerror("Erreur","Veuiller saisir un nombre\ndans les champs heure et minute")
		return 0

	if minute == 0:
		minuteCent = 0
		
	else :
		minuteCent = minute * 100 / 60
	
	if heure == 0:
		heureCent = 0
	else :
		heureCent = heure * 100
	
	temps = heureCent + minuteCent
	
	varResultat.set (temps /100)
	lblResultat.configure (textvariable = varResultat)
	return temps / 100
	
	
if __name__ == "__main__":

	#temps = calcul(0,90)
	#print (temps)
	
	
	#Création de la fenêtre :
	fenetre = Tk()
	fenetre.title("Calculette base 60 vers base 100")
	
	#Création des variables  entryBox
	varHeure = IntVar ()
	varMinute = IntVar ()
	varResultat = DoubleVar()
	
	
	#Création des entryBox
	entHeure = Entry (fenetre, textvariable = varHeure, justify = 'right', width = 2)
	entHeure.grid (column = 0, row = 0)
	entMinute = Entry (fenetre, textvariable = varMinute, justify = 'right', width = 2)
	entMinute.grid(column = 2, row = 0)
	#entResultat = Entry (fenetre, textvariable = varResultat)
	
	#Création des labels
	lblHeure = Label (fenetre, text = ' heure : ')
	lblHeure.grid(column = 1, row = 0)
	lblMinute = Label (fenetre, text = ' minutes')
	lblMinute.grid (column = 3, row = 0 )
	lblResultatText = Label (fenetre, text = 'Resultat : ')
	lblResultatText.grid(column = 1, row = 1)
	lblResultat = Label (fenetre, textvariable = varResultat)
	lblResultat.grid(column = 2, row = 1)
	
	
	
	#Création du bouton pour le calcul
	btnCalcul = Button (fenetre, text = "Calculer", command = lambda : Calcul (varHeure,varMinute) )
	btnCalcul.grid (column = 3, row = 1)
	
	fenetre.mainloop()
