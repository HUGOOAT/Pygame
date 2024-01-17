import pygame
import os
import pytmx
import pyscroll

pygame.init()

# Paramètres du jeu
FPS = 60
WIDTH, HEIGHT = 1600, 900

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

DialogueDebut = False

# Fonction pour afficher les boutons
def afficher_boutons(game):
    print("affichage screen1")
    # Charger l'image du personnage
    personnage_image = pygame.image.load(os.path.join("assets", "Indiana-Salle1-dialoguesortie.png"))
    personnage_rect = personnage_image.get_rect()

    # Charger l'image du bouton
    bouton_image1 = pygame.image.load(os.path.join("assets", "Rester.png"))
    bouton_image2 = pygame.image.load(os.path.join("assets", "Partir.png"))
    # Redimensionner le bouton à une taille plus petite
    nouvelle_taille = (bouton_image1.get_width() // 1.5, bouton_image1.get_height() // 1.5)
    bouton_image1 = pygame.transform.scale(bouton_image1, nouvelle_taille)
    bouton_image2 = pygame.transform.scale(bouton_image2, nouvelle_taille)
    bouton1_rect = bouton_image1.get_rect()
    bouton2_rect = bouton_image2.get_rect()

    # Positions initiales des boutons
    bouton1_x = 140
    bouton2_x = 440
    bouton_y = HEIGHT - bouton1_rect.height - 120

    running = True
    clock = pygame.time.Clock()

    bouton_en_surbrillance = 1  # 1 pour le bouton1, 2 pour le bouton2

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if bouton_en_surbrillance == 1:
                        # Si le bouton "rester" est en surbrillance, reprendre le jeu
                        game.reprendre_jeu()
                        running = False
                    elif bouton_en_surbrillance == 2:
                        print("Le bouton Partir a été activé !")  # Ajoutez ici votre code d'activation
                        running = False
                        game.trigger_journaliste_event()

                elif event.key == pygame.K_q:
                    bouton_en_surbrillance = 1
                elif event.key == pygame.K_d:
                    bouton_en_surbrillance = 2

        # Mise à jour du jeu

        # Affichage du jeu
        game.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du personnage
        game.screen.blit(personnage_image,
                         ((WIDTH - personnage_rect.width) // 2, (HEIGHT - personnage_rect.height) // 2))

        # Affichage du bouton1 en surbrillance
        if bouton_en_surbrillance == 1:
            rectangle_surbrillance1 = pygame.Rect(bouton1_x - 2, bouton_y - 2, bouton1_rect.width + 4,
                                                  bouton1_rect.height + 4)
            pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance1, 2)

        # Affichage du bouton2 en surbrillance
        elif bouton_en_surbrillance == 2:

            rectangle_surbrillance2 = pygame.Rect(bouton2_x - 2, bouton_y - 2, bouton2_rect.width + 4,
                                                  bouton2_rect.height + 4)
            pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance2, 2)

        # Affichage des boutons
        game.screen.blit(bouton_image1, (bouton1_x, bouton_y))
        game.screen.blit(bouton_image2, (bouton2_x, bouton_y))

        pygame.display.flip()

        clock.tick(60)  # Limiter la boucle à 60 images par seconde

    # pygame.quit()
def afficher_boutons2(game):
    print("afficher screen 2")
    # Charger l'image du personnage
    personnage_image = pygame.image.load(os.path.join("assets", "Journaliste-Sortie.png"))
    personnage_rect = personnage_image.get_rect()

    # Charger l'image du bouton
    bouton_image1 = pygame.image.load(os.path.join("assets", "Continuer.png"))

    bouton1_rect = bouton_image1.get_rect()

    bouton1_x = 185

    bouton_y = HEIGHT - bouton1_rect.height - 75

    running = True
    clock = pygame.time.Clock()

    bouton_en_surbrillance = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and bouton_en_surbrillance:
                    game.trigger_gameover_sortie()

        # Coordonnées du rectangle de surbrillance en fonction du bouton

        # Affichage du jeu
        game.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du personnage
        game.screen.blit(personnage_image,
                        ((WIDTH - personnage_rect.width) // 2, (HEIGHT - personnage_rect.height) // 2))

        # Affichage des boutons
        game.screen.blit(bouton_image1, (bouton1_x, bouton_y))

        rectangle_surbrillance = pygame.Rect(bouton1_x - 2, bouton_y - 2, bouton1_rect.width + 4, bouton1_rect.height + 4)
        pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance, 2)

        pygame.display.flip()

        clock.tick(60)  # Limiter la boucle à 60 images par seconde

def afficher_gameover(game):
    # Charger l'image du game over
    gameover_image = pygame.image.load(os.path.join("assets", "Game-OvertParti.png"))
    gameover_rect = gameover_image.get_rect()

# Charger l'image du bouton
    bouton_image1 = pygame.image.load(os.path.join("assets", "Continuer.png"))

    bouton1_rect = bouton_image1.get_rect()

    bouton1_x = 185

    bouton_y = HEIGHT - bouton1_rect.height - 75

    running = True
    clock = pygame.time.Clock()

    bouton_en_surbrillance = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and bouton_en_surbrillance:
                    pygame.quit()

        # Coordonnées du rectangle de surbrillance en fonction du bouton

        # Affichage du jeu
        game.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du personnage
        game.screen.blit(gameover_image,
                        ((WIDTH - gameover_rect.width) // 2, (HEIGHT - gameover_rect.height) // 2))

        # Affichage des boutons
        game.screen.blit(bouton_image1, (bouton1_x, bouton_y))

        rectangle_surbrillance = pygame.Rect(bouton1_x - 2, bouton_y - 2, bouton1_rect.width + 4, bouton1_rect.height + 4)
        pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance, 2)

        pygame.display.flip()

        clock.tick(60)  # Limiter la boucle à 60 images par seconde

def afficher_gameover_esiee(game):
    # Charger l'image du game over
    gameover_image = pygame.image.load(os.path.join("assets", "Game-OverEsiee.png"))
    gameover_rect = gameover_image.get_rect()

# Charger l'image du bouton
    bouton_image1 = pygame.image.load(os.path.join("assets", "Continuer.png"))

    bouton1_rect = bouton_image1.get_rect()

    bouton1_x = 185

    bouton_y = HEIGHT - bouton1_rect.height - 75

    running = True
    clock = pygame.time.Clock()

    bouton_en_surbrillance = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and bouton_en_surbrillance:
                    pygame.quit()

        # Coordonnées du rectangle de surbrillance en fonction du bouton

        # Affichage du jeu
        game.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du personnage
        game.screen.blit(gameover_image,
                        ((WIDTH - gameover_rect.width) // 2, (HEIGHT - gameover_rect.height) // 2))

        # Affichage des boutons
        game.screen.blit(bouton_image1, (bouton1_x, bouton_y))

        rectangle_surbrillance = pygame.Rect(bouton1_x - 2, bouton_y - 2, bouton1_rect.width + 4, bouton1_rect.height + 4)
        pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance, 2)

        pygame.display.flip()

        clock.tick(60)  # Limiter la boucle à 60 images par seconde

def afficher_dialogue_debut(game):
    dialogue_image = pygame.image.load(os.path.join("assets", "Indiana-Salle1-arrivée.png"))
    dialogue_rect = dialogue_image.get_rect()

    # Charger l'image du bouton
    bouton_image1 = pygame.image.load(os.path.join("assets", "Continuer.png"))

    bouton1_rect = bouton_image1.get_rect()

    bouton1_x = 185

    bouton_y = HEIGHT - bouton1_rect.height - 75

    running = True
    clock = pygame.time.Clock()

    bouton_en_surbrillance = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and bouton_en_surbrillance:
                    running = False

        # Coordonnées du rectangle de surbrillance en fonction du bouton

        # Affichage du jeu
        game.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du personnage
        game.screen.blit(dialogue_image,
                         ((WIDTH - dialogue_rect.width) // 2, (HEIGHT - dialogue_rect.height) // 2))

        # Affichage des boutons
        game.screen.blit(bouton_image1, (bouton1_x, bouton_y))

        rectangle_surbrillance = pygame.Rect(bouton1_x - 2, bouton_y - 2, bouton1_rect.width + 4,
                                             bouton1_rect.height + 4)
        pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance, 2)

        pygame.display.flip()

        clock.tick(60)  # Limiter la boucle à 60 images par seconde

def afficher_enigme_bibliotheque(game):
    print("affichage enigme biblio")
    # Charger l'image du personnage
    personnage_image = pygame.image.load(os.path.join("assets", "Indiana-Bibliothèque.png"))
    personnage_rect = personnage_image.get_rect()

    # Charger l'image du bouton
    bouton_images = [pygame.image.load(os.path.join("assets", "1995.png")), pygame.image.load(os.path.join("assets", "1988.png")), pygame.image.load(os.path.join("assets", "2005.png")), pygame.image.load(os.path.join("assets", "2003.png"))]
    # Redimensionner les boutons à une taille plus petite
    nouvelle_taille = (bouton_images[0].get_width() // 2.2, bouton_images[0].get_height() // 2.2)
    bouton_images = [pygame.transform.scale(img, nouvelle_taille) for img in bouton_images]

    # Rectangles des boutons
    bouton_rects = [img.get_rect() for img in bouton_images]

    # Positions initiales des boutons
    boutons_x = [150, 450, 150, 450]
    boutons_y = [HEIGHT - bouton_rects[0].height - 150, HEIGHT - bouton_rects[1].height - 150,
                 HEIGHT - bouton_rects[2].height - 70, HEIGHT - bouton_rects[3].height - 70]

    running = True
    clock = pygame.time.Clock()

    bouton_en_surbrillance = 0  # 0 pour aucun bouton, 1-4 pour les boutons respectifs

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if bouton_en_surbrillance == 1:
                        game.trigger_gameover_esiee()
                    elif bouton_en_surbrillance == 2:
                        running = False
                        game.trigger_choix_1988()
                    elif bouton_en_surbrillance == 3:
                        game.trigger_gameover_esiee()
                    elif bouton_en_surbrillance == 4:
                        game.trigger_gameover_esiee()

                elif event.key == pygame.K_z:
                    bouton_en_surbrillance = 1
                elif event.key == pygame.K_s:
                    bouton_en_surbrillance = 2
                elif event.key == pygame.K_q:
                    bouton_en_surbrillance = 3
                elif event.key == pygame.K_d:
                    bouton_en_surbrillance = 4

        # Mise à jour du jeu

        # Affichage du jeu
        game.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du personnage
        game.screen.blit(personnage_image,
                         ((WIDTH - personnage_rect.width) // 2, (HEIGHT - personnage_rect.height) // 2))

        # Affichage des boutons en surbrillance
        for i in range(1, 5):
            if bouton_en_surbrillance == i:
                rectangle_surbrillance = pygame.Rect(boutons_x[i - 1] - 2, boutons_y[i - 1] - 2,
                                                     bouton_rects[i - 1].width + 4, bouton_rects[i - 1].height + 4)
                pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance, 2)

        # Affichage des boutons
        for i in range(4):
            game.screen.blit(bouton_images[i], (boutons_x[i], boutons_y[i]))

        pygame.display.flip()

        clock.tick(60)  # Limiter la boucle à 60 images par seconde

def afficher_choix_1988(game):
    dialogue_image = pygame.image.load(os.path.join("assets", "Indiana-Bibliothèque-bon.png"))
    dialogue_rect = dialogue_image.get_rect()

    # Charger l'image du bouton
    bouton_image1 = pygame.image.load(os.path.join("assets", "Continuer.png"))

    bouton1_rect = bouton_image1.get_rect()

    bouton1_x = 185

    bouton_y = HEIGHT - bouton1_rect.height - 75

    running = True
    clock = pygame.time.Clock()

    bouton_en_surbrillance = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and bouton_en_surbrillance:
                    running = False

        # Coordonnées du rectangle de surbrillance en fonction du bouton

        # Affichage du jeu
        game.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du personnage
        game.screen.blit(dialogue_image,
                         ((WIDTH - dialogue_rect.width) // 2, (HEIGHT - dialogue_rect.height) // 2))

        # Affichage des boutons
        game.screen.blit(bouton_image1, (bouton1_x, bouton_y))

        rectangle_surbrillance = pygame.Rect(bouton1_x - 2, bouton_y - 2, bouton1_rect.width + 4,
                                             bouton1_rect.height + 4)
        pygame.draw.rect(game.screen, (255, 255, 255), rectangle_surbrillance, 2)

        pygame.display.flip()

        clock.tick(60)  # Limiter la boucle à 60 images par seconde
class Game:
    def __init__(self):
        # Création de la fenêtre du jeu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hugoat")

        # Charger la carte Tiled
        tmx_data = pytmx.util_pygame.load_pygame(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "python-map.tmx"))
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        map_layer.zoom = 3

        # Chargement des éléments du jeu
        self.player = Player()
        self.player.rect.topleft = (250, 400)  # Position initiale du joueur

        # Charger les bordures depuis la carte Tiled
        self.borders = Borders(tmx_data)

        # Charger les événements de sortie depuis la carte Tiled
        self.sortie_events = SortieEvents(tmx_data)

        # Ajouter les bordures au groupe de calques
        self.group.add(self.borders)

        # Ajouter le joueur au groupe de calques
        self.group.add(self.player)

        # Variable pour la gestion de la pause
        self.paused = False

        # Ajout d'une variable pour savoir si l'événement de sortie a été déclenché
        self.sortie_event_triggered = False

    def run(self):
        clock = pygame.time.Clock()
        running = True

        game.trigger_dialogue_debut()

        while running:
            dt = clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.paused:
                # Mise à jour des sprites

                self.player.update(dt)
                # Mise à jour du groupe de calque
                self.group.update(dt)
                # Détection de collision avec l'événement de sortie
                self.check_sortie_event_collision()

                # Définir la position de la caméra pour suivre le joueur
                self.group.center(self.player.rect.center)

                # Afficher le groupe
                self.group.draw(self.screen)

            elif self.paused:
                # Afficher le menu pause
                self.draw_pause_menu()

            pygame.display.flip()

        pygame.quit()

    def check_sortie_event_collision(self):
        # Vérifier la collision avec l'événement de sortie
        if not self.sortie_event_triggered:
            sortie_event_collisions = pygame.sprite.spritecollide(self.player, self.sortie_events, False)
            if sortie_event_collisions:
                # Déclencher l'événement de sortie
                self.trigger_sortie_event()

    def trigger_sortie_event(self):
        # Mettez ici le code que vous voulez exécuter lorsque l'événement de sortie est déclenché
        # Par exemple, afficher la fenêtre avec les boutons
        print("Événement de sortie déclenché !")
        self.sortie_event_triggered = True  # Pour éviter de redéclencher l'événement à chaque itération
        # Appeler la fonction pour afficher les boutons
        afficher_boutons(self)

    def trigger_journaliste_event(self):
        afficher_boutons2(self)

    def trigger_gameover_sortie(self):
        afficher_gameover(self)

    def trigger_gameover_esiee(self):
        afficher_gameover_esiee(self)
    def reprendre_jeu(self):
        self.paused = False

    def trigger_dialogue_debut(self):
        afficher_dialogue_debut(self)

    def trigger_enigme_bibliotheque(self):
        afficher_enigme_bibliotheque(self)

    def trigger_choix_1988(self):
        afficher_choix_1988(self)

# Ajout de la classe SortieEvents pour gérer les événements de sortie
class SortieEvents(pygame.sprite.Group):
    def __init__(self, tmx_data):
        super().__init__()
        # Ajout des événements de sortie depuis la carte Tiled
        self.load_from_tmx_data(tmx_data)

    def load_from_tmx_data(self, tmx_data):
        for obj in tmx_data.objects:
            if obj.type == "event_sortie":
                sortie_event = SortieEvent(obj.x, obj.y, obj.width, obj.height)
                self.add(sortie_event)


class SortieEvent(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Chargement des images du joueur depuis le dossier "assets"
        self.image_down = pygame.image.load(os.path.join("assets", "bas.png"))
        self.image_up = pygame.image.load(os.path.join("assets", "haut.png"))
        self.image_left = pygame.image.load(os.path.join("assets", "gauche.png"))
        self.image_right = pygame.image.load(os.path.join("assets", "droite.png"))

        # Ajustez la taille du joueur selon vos besoins
        nouvelle_largeur, nouvelle_hauteur = 25, 25
        self.image_down = pygame.transform.scale(self.image_down, (nouvelle_largeur, nouvelle_hauteur))
        self.image_up = pygame.transform.scale(self.image_up, (nouvelle_largeur, nouvelle_hauteur))
        self.image_left = pygame.transform.scale(self.image_left, (nouvelle_largeur, nouvelle_hauteur))
        self.image_right = pygame.transform.scale(self.image_right, (nouvelle_largeur, nouvelle_hauteur))

        self.image = self.image_down  # Image par défaut
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 70  # Ajustez la vitesse du joueur selon vos besoins

    def update(self, dt):
        # Mettez à jour la position et l'image du joueur en fonction de la direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and not self.check_collision(0, -self.speed * dt):
            self.rect.y -= self.speed * dt
            self.image = self.image_up
        if keys[pygame.K_s] and not self.check_collision(0, self.speed * dt):
            self.rect.y += self.speed * dt
            self.image = self.image_down
        if keys[pygame.K_q] and not self.check_collision(-self.speed * dt, 0):
            self.rect.x -= self.speed * dt
            self.image = self.image_left
        if keys[pygame.K_d] and not self.check_collision(self.speed * dt, 0):
            self.rect.x += self.speed * dt
            self.image = self.image_right

    def check_collision(self, dx, dy):
        # Vérifie s'il y a une collision avec les bordures
        new_rect = self.rect.copy()
        new_rect.x += dx
        new_rect.y += dy

        return any(border.rect.colliderect(new_rect) for border in game.borders)


class Borders(pygame.sprite.Group):
    def __init__(self, tmx_data):
        super().__init__()
        # Ajout des bordures depuis la carte Tiled
        self.load_from_tmx_data(tmx_data)

    def load_from_tmx_data(self, tmx_data):
        for obj in tmx_data.objects:
            if obj.type == "colision":
                border = Border(obj.x, obj.y, obj.width, obj.height)
                self.add(border)


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)  # Surface transparente
        self.rect = self.image.get_rect(topleft=(x, y))


# Création de l'instance du jeu
game = Game()
# Lancement du jeu
game.run()
