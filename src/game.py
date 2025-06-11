import random
import time
from datetime import datetime
from sys import exit
import utils
import pygame

from button import Button
from clouds import Clouds
from entity import Entity
from map import Map
from menu import Menu
from projectile import Projectile
from trophy import Trophy
from score import Score


class Game:
    def __init__(self):
        """
        This function initializes the Game object.
        """
        pygame.init()

        self.screen = pygame.display.set_mode((960, 960))
        self.display = pygame.Surface((320, 240))
        self.clock = pygame.time.Clock()

        self.assets = {
            "background": utils.load_image("background.png"),
            "clouds": utils.load_images("clouds"),
            "player_idle_left": utils.load_mirrored_image("entities/player.png"),
            "player_idle_right": utils.load_image("entities/player.png"),
            "player_run_right": utils.load_images("entities/player/run"),
            "player_run_left": utils.load_mirrored_images("entities/player/run"),
            "grass": utils.load_images("tiles/grass"),
            "projectile" : utils.load_image("projectile.png"),
            "trophy": utils.load_image("trophy.png"),
            "play_button": utils.load_image("play_button.png"),
            "exit_button": utils.load_image("exit_button.png"),
            "score_button": utils.load_image("score_button.png"),
            "load_button": utils.load_image("load_button.png"),
            "back_button": utils.load_image("back_button.png"),
            "save_button": utils.load_image("save_button.png")
        }

        self.clouds = Clouds(self.assets["clouds"], count=16)

        self.player = Entity(96, 224, self.assets["player_idle_right"], self.assets["player_idle_right"].get_size())

        self.map = Map(self)
        self.map.load_from_dir("assets/levels")

        self.camera_y = 75

        self.movement = [0,0]

        self.frame_counter = 0

        self.projectiles = []

        self.trophy = Trophy(112, -1776 - 16, self.assets["trophy"], self.assets["trophy"].get_size())

        for i in range(200, -1760, -100):
            self.projectiles.append(Projectile(-5, i, self.assets["projectile"], (6, 4), 320, random.randrange(0, 4)))

        self.menu = Menu(self.assets["play_button"], self.assets["exit_button"],
                         self.assets["score_button"], self.assets["load_button"])

        self.in_menu = True
        self.game_running = False
        self.post_game = False
        self.running = True
        self.viewing_score = False
        self.pause = False

        self.elapsed_seconds = 0

    def run(self):
        """
        This function runs the programs loop and switches between different states and loops
        """
        global timer
        while self.running:
            if self.in_menu:
                self.main_menu_loop()
            if self.game_running:
                timer = self.game_loop()
            if self.post_game:
                self.post_game_loop(timer)
            if self.viewing_score:
                self.viewing_score_loop()

    def main_menu_loop(self):
        """
        This function runs the main menu loop and handles buttons
        """
        while self.in_menu:
            self.display.blit(self.assets["background"], (0, 0))
            self.menu.render(self.display)

            mouse_pos = pygame.mouse.get_pos()
            scaled_mouse_pos = (
            mouse_pos[0] * 320 // self.screen.get_width(), mouse_pos[1] * 240 // self.screen.get_height())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.menu.play_button.get_rect().collidepoint(scaled_mouse_pos):
                        self.game_running = True
                        self.in_menu = False
                    elif self.menu.score_button.get_rect().collidepoint(scaled_mouse_pos):
                        self.in_menu = False
                        self.viewing_score = True
                    elif self.menu.load_button.get_rect().collidepoint(scaled_mouse_pos):
                        loaded = self.load_game()
                        if loaded:
                            self.game_running = True
                            self.in_menu = False
                    elif self.menu.exit_button.get_rect().collidepoint(scaled_mouse_pos):
                        pygame.quit()
                        exit()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

    def game_loop(self):
        """
        This function runs the gameplay loop, handles input, movement, collision detection and game ending

        Returns:
            float: Time stamp when the game ended in order to get score
        """
        timer = time.time()
        while self.game_running:
            self.display.blit(self.assets["background"], (0, 0))

            self.camera_y += int((self.player.get_rect().centery - self.display.get_height() / 2 - self.camera_y) / 30)

            self.clouds.move()
            self.clouds.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = -1
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = 1
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and self.player.standing:
                        self.player.velocity_y = -5
                        self.player.standing = False
                    if event.key == pygame.K_ESCAPE:
                        self.pause = True
                        self.pause_loop(int(time.time() - timer))

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.movement[0] == -1:
                        self.movement[0] = 0
                        self.player.image = self.assets["player_idle_left"]
                        self.frame_counter = 0
                    if event.key == pygame.K_RIGHT and self.movement[0] == 1:
                        self.movement[0] = 0
                        self.player.image = self.assets["player_idle_right"]
                        self.frame_counter = 0

            if not self.game_running:
                break

            if self.movement[0] != 0 and self.player.standing:
                frames = self.assets["player_run_left"] if self.movement[0] < 0 else self.assets["player_run_right"]
                index = (self.frame_counter // 4) % len(frames)
                self.player.image = frames[index]
                self.player.running = True
            else:
                self.player.running = False

            self.trophy.render(self.display, self.camera_y)

            self.player.move(self.map, *self.movement)

            self.map.render(self.display, self.camera_y)

            self.player.render(self.display, self.camera_y)

            for projectile in self.projectiles:
                projectile.move()
                projectile.render(self.display, self.camera_y)
                if self.player.check_if_got_hit(projectile.get_rect()):
                    self.player.die()
                    self.camera_y = 75

            if self.player.get_rect().colliderect(self.trophy.get_rect()):
                self.post_game = True
                self.game_running = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            self.frame_counter += 1

        return timer

    def post_game_loop(self, timer_after):
        """
        This function handles the loop that displays the score of current game, 5 of the best scores and handles a button click that returns the player to main menu

        Args:
            timer_after (float): Time stamp when the game ended in order to get score
        """
        elapsed_seconds = int(time.time() - timer_after) + self.elapsed_seconds
        utils.append_score(Score(elapsed_seconds, datetime.now()))
        best_scores = sorted(utils.load_scores())[:5]

        font = pygame.font.SysFont("Arial", 10)
        while self.post_game:
            back_button = Button(320 // 2 - self.assets["back_button"].get_width() // 2, 200,
                                 self.assets["back_button"], self.assets["back_button"].get_size(), "back")
            self.display.blit(self.assets["background"], (0, 0))

            header = font.render(f"YOUR SCORE: {elapsed_seconds // 60:02}:{elapsed_seconds % 60:02}\nBEST SCORES:",
                                 False, (0, 0, 0))
            self.display.blit(header, (10, 10))

            for i, score in enumerate(best_scores):
                text = font.render(f"{i + 1}. {str(score)}", False, (0, 0, 0))
                self.display.blit(text, (10, 30 + i * 20))

            back_button.render(self.display)

            mouse_pos = pygame.mouse.get_pos()
            scaled_mouse_pos = (
            mouse_pos[0] * 320 // self.screen.get_width(), mouse_pos[1] * 240 // self.screen.get_height())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back_button.get_rect().collidepoint(scaled_mouse_pos):
                        self.post_game = False
                        self.in_menu = True
                        self.restart()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

    def viewing_score_loop(self):
        """
        This function handles the loop that displays 5 best scores and handles a button click that returns the user to main menu
        """
        while self.viewing_score:
            self.display.blit(self.assets["background"], (0, 0))

            font = pygame.font.SysFont("Arial", 10)
            header = font.render("BEST SCORES:", False, (0, 0, 0))
            self.display.blit(header, (10, 10))

            best_scores = sorted(utils.load_scores())[:5]
            for i, score in enumerate(best_scores):
                text = font.render(f"{i + 1}. {str(score)}", False, (0, 0, 0))
                self.display.blit(text, (10, 30 + i * 20))

            back_button = Button(
                320 // 2 - self.assets["back_button"].get_width() // 2, 200,
                self.assets["back_button"], self.assets["back_button"].get_size(), "back"
            )
            back_button.render(self.display)

            mouse_pos = pygame.mouse.get_pos()
            scaled_mouse_pos = (
                mouse_pos[0] * 320 // self.screen.get_width(), mouse_pos[1] * 240 // self.screen.get_height())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back_button.get_rect().collidepoint(scaled_mouse_pos):
                        self.viewing_score = False
                        self.in_menu = True

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

    def restart(self):
        """
        This function resets the game and player state for a new game
        """
        self.player.x = 128
        self.player.y = 225
        self.camera_y = 75
        self.movement = [0, 0]
        self.player.standing = True
        self.player.running = False
        self.player.image = self.assets["player_idle_right"]

    def pause_loop(self, elapsed_seconds):
        """
        This function handles the loop after pausing the game displays the buttons for un pausing the game and saving it and handles them

        Args:
            elapsed_seconds (int): The number of seconds that passed between start of the game and pausing it. Used for saving the game
        """
        while self.pause:
            self.display.blit(self.assets["background"], (0, 0))

            back_button = Button(
                320 // 2 - self.assets["back_button"].get_width() // 2, 120,
                self.assets["back_button"], self.assets["back_button"].get_size(), "back"
            )
            back_button.render(self.display)

            save_button = Button(
                320 // 2 - self.assets["save_button"].get_width() // 2, 80,
                self.assets["save_button"], self.assets["save_button"].get_size(), "save"
            )
            save_button.render(self.display)

            mouse_pos = pygame.mouse.get_pos()
            scaled_mouse_pos = (
                mouse_pos[0] * 320 // self.screen.get_width(), mouse_pos[1] * 240 // self.screen.get_height())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back_button.get_rect().collidepoint(scaled_mouse_pos):
                        self.pause = False
                    if save_button.get_rect().collidepoint(scaled_mouse_pos):
                        self.save_game(self.player.x, self.player.y, self.camera_y, elapsed_seconds)
                        self.game_running = False
                        self.pause = False
                        self.in_menu = True

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

    def save_game(self, player_x, player_y, camera_y, elapsed_seconds):
        """
        This function saves the current game state.

        Args:
             player_x (float): The x coordinate of the player
             player_y (float): The y coordinate of the player
             camera_y (float): The y coordinate of the camera
             elapsed_seconds (int): The number of seconds that passed between start of the game and saving the game
        """
        with open("assets/save.txt", "w") as f:
            f.write(str(player_x) + "\n")
            f.write(str(player_y)+ "\n")
            f.write(str(camera_y) + "\n")
            f.write(str(elapsed_seconds))

    def load_game(self):
        """
        This function loads the game state from a file

        Returns:
            bool: False if there is no game state to be loaded, True otherwise.
        """
        try:
            with open("assets/save.txt", "r") as f:
                lines = f.readlines()

            if len(lines) < 4:
                print("There is no saved game state")
                return False

            self.player.x = float(lines[0].strip())
            self.player.y = float(lines[1].strip())
            self.camera_y = float(lines[2].strip())
            self.elapsed_seconds = int(lines[3].strip())
            open("assets/save.txt", "w").close()
            return True
        except (FileNotFoundError, ValueError) as e:
            print("An error occurred while loading the save: " + e)



if __name__ == '__main__':
    Game().run()

