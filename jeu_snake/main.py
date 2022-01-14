import random
import sys

import pygame


class Jeu:
    # Contient toutes les variables ainsi que fonction pour déroulement du Jeu

    def __init__(self):
        self.ecran = pygame.display.set_mode((900, 600))

        pygame.display.set_caption('Jeu snake')
        self.jeu_encours = True

        # Creer variables position et direction
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 30

        # Creer position pomme

        self.pomme_position_x = random.randrange(0, 900, 30)
        self.pomme_position_y = random.randrange(0, 600, 30)
        self.pomme = 30

        # Creer liste position ensemble corp serpent
        self.positions_serpent = []

        # Creer variable taille serpent
        self.taille_serpent = 1

        self.clock = pygame.time.Clock()

    def fonction_principale(self):
        # Permet de gérer les évènements, ainsi que d'aficher certains composants du jeu

        while self.jeu_encours:
            for evenement in pygame.event.get():

                # Evenement fermer fenêtre
                if evenement.type == pygame.QUIT:
                    sys.exit()

                # Evenement bouger serpent
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction_x = 30
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -30
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = 30

                    if evenement.key == pygame.K_UP:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = -30

            # Faire bouger le serpent lorsqu'il atteint les limites du jeu

            if self.serpent_position_x < 0 or self.serpent_position_x > 900 \
                    or self.serpent_position_y < 0 or self.serpent_position_y > 600:
                sys.exit()

            # Serpent mange la pomme
            if self.pomme_position_x == self.serpent_position_x and self.pomme_position_y == self.serpent_position_y:
                self.pomme_position_x = random.randrange(0, 900, 30)
                self.pomme_position_y = random.randrange(0, 600, 30)
                self.taille_serpent += 1

            # Faire bouger le serpent
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y

            # Stocker position tete serpent
            tete_serpent = [self.serpent_position_x, self.serpent_position_y]

            # Ajouter tete dans positions serpent
            self.positions_serpent.append(tete_serpent)

            # Jumeler position serpent et taille serpent
            if len(self.positions_serpent) > self.taille_serpent:
                self.positions_serpent.pop(0)

            self.ecran.fill((0, 0, 0))

            # Serpent se mort la queue
            for partie_du_serpent in self.positions_serpent[:-1]:
                if tete_serpent == partie_du_serpent:
                    sys.exit()

            # Afficher serpent
            pygame.draw.rect(self.ecran, (0, 255, 0),
                             (self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))

            # Afficher reste serpent
            for p11artie_du_serpent in self.positions_serpent:
                pygame.draw.rect(self.ecran, (0, 255, 0),
                                 (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

            # Afficher pomme
            pygame.draw.rect(self.ecran, (255, 0, 0),
                             (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

            # Afficher les limites
            self.creer_limite()

            self.clock.tick(10)
            # Rafraichir écran
            pygame.display.flip()

    # Creer limite map

    def creer_limite(self):

        pygame.draw.rect(self.ecran, (255, 0, 0), (0, 0, 900, 600), 1)


if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
