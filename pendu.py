import pygame 

pygame.init()
import pygame
import random
import sys

pygame.init()

largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")

blanc = (255, 255, 255)
noir = (0, 0, 0)

with open('mots.txt', 'r') as fichier : 
    lignes = fichier.readlines()

mots = [mot.strip() for mot in lignes]
mot_a_deviner = random.choice(mots).upper()

mot_actuel = ["_" if lettre.isalpha() else lettre for lettre in mot_a_deviner]
lettres_utilisees = set()
lettre = None
essais_max = 6
essais_restants = essais_max

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()


while True:
    fenetre.fill(blanc)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if pygame.K_a <= event.key <= pygame.K_z:
                lettre = chr(event.key).upper()
                if lettre not in lettres_utilisees:
                    lettres_utilisees.add(lettre)
                    if lettre not in mot_a_deviner:
                        essais_restants -= 1


    if "_" not in mot_actuel:
        texte_gagne = font.render("Félicitations, vous avez gagné !", True, noir)
        fenetre.blit(texte_gagne, (largeur // 2 - 200, hauteur // 2 - 50))

    elif essais_restants == 0 :
        texte_perdu = font.render(f"Désolé, vous avez perdu. Le mot était {mot_a_deviner}", True, noir)
        fenetre.blit(texte_perdu, (largeur // 2 - 200, hauteur // 2 - 50))
    
    else:
        texte_mot = font.render(" ".join(mot_actuel), True, noir)
        fenetre.blit(texte_mot, (largeur // 2 - 50, hauteur // 2 - 50))

        texte_lettres = font.render("Lettres utilisées: " + ", ".join(lettres_utilisees), True, noir)
        fenetre.blit(texte_lettres, (largeur // 2 - 150, hauteur // 2 + 50))

        pygame.draw.line(fenetre, noir, (largeur // 2 - 50, hauteur // 2 + 100), (largeur // 2 - 50, hauteur // 2 + 200), 5)
        pygame.draw.circle(fenetre, noir, (largeur // 2 - 50, hauteur // 2 + 230), 30, 5)

        if essais_restants < essais_max:
            pygame.draw.line(fenetre, noir, (largeur // 2 - 50, hauteur // 2 + 150), (largeur // 2 - 100, hauteur // 2 + 100), 5)
            pygame.draw.line(fenetre, noir, (largeur // 2 - 50, hauteur // 2 + 150), (largeur // 2, hauteur // 2 + 100), 5)

    pygame.display.flip()
    clock.tick(60)

    if essais_restants == 0:
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
    
    for i, lettre_mot in enumerate(mot_a_deviner):
        if lettre_mot == lettre:
            mot_actuel[i] = lettre
    
    essais_restants = min(essais_restants, essais_max)
