'''
description :
Vous jouez un astronaute qui essaye d'empêcher son vaisseau d'exploser alors qu'il traverse un champ d'astéroïdes.
Eteignez les flammes qui ravagent votre vaisseau pour vous en sortir !


Documentation : 
Z / ↑ : monter
S / ↓ : descendre
Q / ⟵ : aller à gauche
D / ⟶ : aller à droite
P : quitter le jeu

Vous devez atteindre un score de 20 pour gagner la partie.
Si vous arrivez à 10 au nombres de flammes vous avez perdu.

D'autres musiques et bruitages sont disponible dans les fichiers du jeu mais n'ont pas été utilisé par manque de temps.

Univers sélectionné : 1

Module pyxel uniquement
'''

import pyxel

class App():
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023", fps=30, quit_key=pyxel.KEY_P)
        pyxel.load("1.pyxres")#chargement du fichier ressource
        self.pos_x = 60 #position joueur
        self.pos_y = 40#position joueur
        self.perso_x = 8 #choix de l'image du personnage
        self.perso_y = 0 #choix de l'image du personnage
        self.recta = 200 #position rectangle victoire
        ##position flamme : 
        #x = 32 
        self.pos1_x = 500 
        self.pos2_x = 500 
        self.pos3_x = 500
        self.pos1_y = 57
        self.pos2_y = 81
        self.pos3_y = 104
        #x = 88
        self.pos4_x = 500
        self.pos5_x = 500
        self.pos6_x = 500
        self.pos4_y = 104
        self.pos5_y = 89
        self.pos6_y = 57
        self.aaa = "  "
        self.aab = "  "
        self.abb = "  "
        self.bbb = "  "
        self.couleur_recta = 1#couleur rectangle
        self.timer = ((pyxel.frame_count // 30) )
        self.danger = 0 #variable de fin du jeu en cas de perte
        self.score = 0 #score = nb de flammes éteinte
        self.nb_music = 4 #numéro de la musique
        pyxel.playm(self.nb_music, 0, True)#musique
        #pyxel.playm(self.nb_music, 0, True)#musique
        pyxel.run(self.update, self.draw)
    
    def update(self):
        pyxel.cls(0) #actualisation de l'écran
        if (pyxel.frame_count // 30) < 12 :
            self.recta = 0 #mise en place du rectangle de victoire
            self.couleur_recta = 2
            self.aab = "Bienvenue dans mon vaisseau"
            self.abb = "a vous d'éteindre les flammes"
            self.bbb = f"Lancement dans : {15 - (pyxel.frame_count // 30)}"
        else : 
            self.aab = "  "
            self.abb = "  "
            self.bbb = "  "
            self.recta = 200 #position rectangle 
        if pyxel.frame_count >= 6000 or self.score >= 20 : #temps et de score pour la victoire
            self.couleur_recta = 5
            self.recta = 0 #mise en place du rectangle de victoire
            self.aaa = "Victoire !!"
        if pyxel.frame_count // 30 > 15 :
            if pyxel.frame_count % 30 == 0 :
                self.On_Fire()
        if self.danger >= 3 :
            pass
            #self.nb_music = 5
            #pyxel.playm(self.nb_music, 0)#musique
            #pyxel.music(5)
            #self.music = pyxel.playm(5, 0, True)
        if self.danger >= 5 and self.aaa != "Victoire !!":
            self.couleur_recta = 4
            self.recta = 0 #mise en place du rectangle de défaite
            self.aaa = "Perdu !!"
            #self.nb_music = 5
            #pyxel.music(5)
            #self.music = pyxel.playm(5, 0, True)
        self.update_player()
        self.Un_Fire()

    def Un_Fire(self):  #flamme : extinction
        if ((self.pos_x <= 37) and (self.pos_x >= 27) and (self.pos_y >= 52) and (self.pos_y <= 62)) :
            if self.pos1_x == 32 : 
                self.pos1_x = 500
                self.danger -= 1
                self.score += 1
        elif ((self.pos_x <= 37) and (self.pos_x >= 27) and (self.pos_y >= 76) and (self.pos_y <= 86)) :
            if self.pos2_x == 32 :
                self.pos2_x = 500
                self.danger -= 1
                self.score += 1
        elif ((self.pos_x <= 37) and (self.pos_x >= 27) and (self.pos_y >= 99) and (self.pos_y <= 109)) :
            if self.pos3_x == 32 :
                self.pos3_x = 500
                self.danger -= 1
                self.score += 1
        elif ((self.pos_x <= 93) and (self.pos_x >= 83) and (self.pos_y >= 99) and (self.pos_y <= 109)) :
            if self.pos4_x == 88 :
                self.pos4_x = 500
                self.danger -= 1
                self.score += 1
        elif ((self.pos_x <= 93) and (self.pos_x >= 83) and (self.pos_y >= 84) and (self.pos_y <= 94)) :
            if self.pos5_x == 88 :
                self.pos5_x = 500
                self.danger -= 1
                self.score += 1
        elif ((self.pos_x <= 93) and (self.pos_x >= 83) and (self.pos_y >= 52) and (self.pos_y <= 62)) :
            if self.pos6_x == 88 :
                self.pos6_x = 500
                self.danger -= 1
                self.score += 1
        
    def update_player(self) :
        if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_UP):
            if not ((self.pos_x >= 48) and (self.pos_x <= 72) and (self.pos_y == 24)) :
                if not ((self.pos_x >= 32) and (self.pos_x <= 47) and (self.pos_y == 56)) :
                    if not ((self.pos_x >=73) and (self.pos_x <= 88) and (self.pos_y == 56)) :
                        if not ((self.pos_x >= 41) and (self.pos_x <= 79) and (self.pos_y == 96)) : #carré milieu bord sud
                            self.pos_y -= 1
                            if self.perso_x == 8 :
                                    self.perso_x = 16
                            elif self.perso_x == 16 :
                                self.perso_x = 24
                            else :
                                self.perso_x = 8
        elif pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_LEFT):
            if not ((self.pos_x == 32) and (self.pos_y >= 56) and (self.pos_y <= 104)) :
                if not ((self.pos_x == 80) and (self.pos_y >= 57) and (self.pos_y <= 95)) : 
                    if not ((self.pos_x == 48) and (self.pos_y >= 24) and (self.pos_y <= 55)) : 
                        self.pos_x -= 1
                        self.perso_y = 8
                        if self.perso_x == 8 :
                            self.perso_x = 16
                        else :
                            self.perso_x = 8
        elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            if not ((self.pos_x >= 32) and (self.pos_x <= 88) and (self.pos_y == 104)) :
                if not ((self.pos_x >= 41) and (self.pos_x <= 79) and (self.pos_y == 56)) : 
                    self.pos_y += 1
                    if self.perso_x == 8 :
                        self.perso_x = 16
                    elif self.perso_x == 16 :
                        self.perso_x = 24
                    else :
                        self.perso_x = 8
        elif pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            if not ((self.pos_x == 88) and (self.pos_y >= 56) and (self.pos_y <= 104)) :
                if not ((self.pos_x == 40) and (self.pos_y >= 57) and (self.pos_y <= 95)) :
                    if not ((self.pos_x == 72) and (self.pos_y >= 24) and (self.pos_y <= 55)) :  
                        self.pos_x += 1
                        self.perso_y = 0
                        if self.perso_x == 8 :
                            self.perso_x = 16
                        else :
                            self.perso_x = 8

    def On_Fire(self): #apparition des flammes
        self.aleatoire = pyxel.rndi(1, 6)
        if self.aleatoire == 1 : 
            if self.pos1_x != 32 : 
                self.pos1_x = 32
                self.danger += 1
        elif self.aleatoire == 2 : 
            if self.pos2_x != 32 : 
                self.pos2_x = 32
                self.danger += 1
        elif self.aleatoire == 3 :
            if self.pos3_x != 32 :  
                self.pos3_x = 32
                self.danger += 1
        elif self.aleatoire == 4 :
            if self.pos4_x != 88 :  
                self.pos4_x = 88
                self.danger += 1
        elif self.aleatoire == 5 : 
            if self.pos5_x != 88 : 
                self.pos5_x = 88
                self.danger += 1
        elif self.aleatoire == 6 : 
            if self.pos6_x != 88 : 
                self.pos6_x = 88
                self.danger += 1
    
    def draw(self):
        pyxel.bltm(0, 0, 3, 0, 0, 128, 128)
        pyxel.blt(self.pos_x, self.pos_y, 0, self.perso_x, self.perso_y, 8, 8, 0) #personnage
        #pyxel.blt(10, 10, 0, 16, 16, 8, 8) #machinne
        pyxel.blt(self.pos1_x, self.pos1_y, 0, 0, 16, 8, 8, 0) #fire 1
        pyxel.blt(self.pos2_x, self.pos2_y, 0, 0, 16, 8, 8, 0) #fire 2
        pyxel.blt(self.pos3_x, self.pos3_y, 0, 0, 16, 8, 8, 0) #fire 3
        pyxel.blt(self.pos4_x, self.pos4_y, 0, 0, 16, 8, 8, 0) #fire 4
        pyxel.blt(self.pos5_x, self.pos5_y, 0, 0, 16, 8, 8, 0) #fire 5
        pyxel.blt(self.pos6_x, self.pos6_y, 0, 0, 16, 8, 8, 0) #fire 6
        pyxel.blt(56, 72, 0, 0, 32, 16, 16, 0) #fusée
        pyxel.text(0,122, F"Temps:{pyxel.frame_count // 30}", 7) #texte timer
        pyxel.text(0, 0, F"Flammes: {self.danger}", 7) #nb de flammes
        pyxel.text(0, 6, F"Score: {self.score}", 7) #score
        pyxel.rect(self.recta, self.recta, 128, 128, self.couleur_recta) #rectangle victoire
        pyxel.text(50, 60, self.aaa, 7) #texte de victoire/defaite
        pyxel.text(10, 50, self.aab, 7) #texte de victoire/defaite
        pyxel.text(10, 60, self.abb, 7) #texte de victoire/defaite
        pyxel.text(20, 80, self.bbb, 7) #texte de victoire/defaite
        pyxel.text(84, 1, "P : Quitter", 7) #score

App()

'''
maj du 4/6/2023 : 
- ajout des fleches du clavier 
- ajout d'une page d'accueil
- ajout d'un score
- ajout du temps 
- ajout du texte "p : quitter"
- ajout des mouvement du perso
- modif des couleurs en fonction de la perte ou de la victoire
- modif de la victoire : il faut que score = 20

'''