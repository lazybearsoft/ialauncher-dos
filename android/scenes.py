import os
import random
#import pygame as pg
#from pgmain import pg
import pgmain
#from pgmain import screen

import sys
import os
 
# setting path
#sys.path.append('C:\ialauncher')
sys.path.append('/storage/emulated/0/Download/ialauncher')
 
# importing
#from parentdirectory.geeks import games as gd

import games as gd


from ialauncher.gamelist import GameList
from ialauncher.engine import Scene
#from . import options
import options as options

ADVANCE = pgmain.pg.event.custom_type()


class Loading(Scene):
    counter = 0

    def __init__(self, slurp_mode=False):
        self.slurp_mode = slurp_mode
        self.games_dir = os.path.dirname(gd.__file__)
        self.todo = [
            os.path.join(self.games_dir, entry) for entry in os.listdir(self.games_dir)
            if os.path.exists(os.path.join(self.games_dir, entry, 'metadata.ini'))
        ]
        self.games = GameList()
        super().__init__()

    def get_events(self):
        return pgmain.pg.event.get()

    def handle(self, event):
        if event.type == pgmain.pg.KEYDOWN and event.key == pgmain.pg.K_ESCAPE:
            return self.done()

    def load_games(self, number_of_games):
        while self.todo and number_of_games:
            path = self.todo.pop()
            self.games.add(path)
            self.counter += 1
            number_of_games -= 1

    def download_game(self):
        path = self.todo.pop()
        self.games.add(path)
        Download(self.games.games[-1]).run(self.screen)
        self.counter += 1

    def done(self):
        self.games.sort(slideshow=options.slideshow)
        return Browse(self.games)

    def update(self, screen):
        if not self.todo:
            return self.done()
        if self.slurp_mode:
            self.download_game()
        else:
            self.load_games(10)
        screen.fill((0,0,0))
#        self.draw(screen, f'''
#Welcome to IA Launcher!
#Found games directory at: {self.games_dir}
#Loading games... {self.counter}
#''')


class Browse(Scene):
    def __init__(self, games):
        self.games = games
        if options.slideshow:
            pgmain.pg.time.set_timer(ADVANCE, options.slideshow * 1000)
        self.handlers = {
            pgmain.pg.K_RIGHT: self.games.next_game,
            pgmain.pg.K_LEFT: self.games.previous_game,
            pgmain.pg.K_DOWN: self.games.next_letter,
            pgmain.pg.K_UP: self.games.previous_letter,
            pgmain.pg.K_SPACE: self.games.random_game,
            pgmain.pg.K_q: self.games.exitIAL
        }
        super().__init__()

    def get_events(self):
        return [pgmain.pg.event.wait()]

    def handle(self, event):
        if event.type == ADVANCE:
            self.games.random_game()
        if event.type == pgmain.pg.KEYDOWN:
            if event.key == pgmain.pg.K_ESCAPE:
                return False
            handler = self.handlers.get(event.key)
            if handler:
                handler()
            if event.unicode:
                self.games.letter(event.unicode)
            if event.key == pgmain.pg.K_RETURN:
                game = self.games.get_current_game()
                if event.mod & pgmain.pg.KMOD_SHIFT:
                    game.reset()
                if not game.is_ready():
                    Download(game).run(self.screen)
                if game.is_ready():

                    # Start playing (spawns a new thread)
                    game.start(autorun=not event.mod & pgmain.pg.KMOD_ALT)

    def update(self, screen):
        image = self.games.get_image()
        rect = screen.get_rect()
        scaled_image = pgmain.pg.transform.scale(image, rect.size)
        screen.blit(scaled_image, rect)

 
class Download(Scene):
    def __init__(self, game):
        self.game = game
        super().__init__()

        # Start downloading (spawns a new thread)
        self.game.download()

    def handle(self, event):
        if event.type == pgmain.pg.KEYDOWN:
            if event.key == pgmain.pg.K_ESCAPE:
                return False

    def update(self, screen):
        if self.game.download_completed():
            return False
        screen.fill((0,0,0))
#        self.draw(screen, f'Downloading {self.game.urls[0]} ({self.game.get_size():.1f} MB)')
