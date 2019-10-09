# A simple Crossy Road game

import pygame

Screen_Title = "Crossy RPG"
Screen_Width = 800
Screen_Height = 800
White_Colour = (255, 255, 255)
Black_Colour = (0, 0, 0)

clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("comicsans", 75)



class Game:

    Tick_Rate = 60
    
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        
        self.game_window = pygame.display.set_mode((width, height))
        self.game_window.fill(White_Colour)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))
                                            
    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter("player.png", 375, 700, 50, 50)
        enemy_0 = EnemyCharacter("enemy.png", 20, 600, 50, 50)
        enemy_0.Speed *= level_speed

        enemy_1 = EnemyCharacter("enemy.png", self.width - 40, 450, 50, 50)
        enemy_1.Speed *= level_speed

        enemy_2 = EnemyCharacter("enemy.png", 20, 300, 50, 50)
        enemy_2.Speed *= level_speed

        treasure = GameObject("treasure.png", 375, 50, 50, 50)

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                         direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                        print(event)

            self.game_window.fill(White_Colour)
            self.game_window.blit(self.image, (0,0))

            treasure.draw(self.game_window)

            player_character.move(direction, self.height)
            player_character.draw(self.game_window)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_window)

            if level_speed >1:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_window)
            if level_speed >3:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_window)
                
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render("You Lose :(", True, Black_Colour)
                self.game_window.blit(text, (250, 350))
                pygame.display.update()
                clock.tick(1)
                break
            if player_character.detect_collision(enemy_1):
                is_game_over = True
                did_win = False
                text = font.render("You Lose :(", True, Black_Colour)
                self.game_window.blit(text, (250, 350))
                pygame.display.update()
                clock.tick(1)
                break
            if player_character.detect_collision(enemy_2):
                is_game_over = True
                did_win = False
                text = font.render("You Lose :(", True, Black_Colour)
                self.game_window.blit(text, (250, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render("You Won!", True, Black_Colour)
                self.game_window.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break
                          
            pygame.display.update()
            clock.tick(self.Tick_Rate)    

        if did_win:
            self.run_game_loop(level_speed + 0.5)
        else:
            return

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image,(self.x_pos, self.y_pos))

class PlayerCharacter(GameObject):

    Speed = 10

    def __init__self(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.Speed
        elif direction < 0:
            self.y_pos += self.Speed

        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 60

    def detect_collision(self, other_body):
        if self.y_pos >= other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height <= other_body.y_pos:
            return False

        if self.x_pos >= other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width <= other_body.x_pos:
            return False

        return True            

class EnemyCharacter(GameObject):

    Speed = 7

    def __init__self(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        
    def move(self, max_width):
        if self.x_pos <= 10:
            self.Speed = abs(self.Speed)
        elif self.x_pos >= max_width - 60:
            self.Speed = -abs(self.Speed)
        self.x_pos += self.Speed    
        
pygame.init()

new_game = Game("background.png", Screen_Title, Screen_Width, Screen_Height)
new_game.run_game_loop(1)

pygame.quit()
quit()



    # game_window.blit(player_image, (375, 375))
        
    # displaying a rectangle on the window (x, y, width, height)
    # pygame.draw.rect(game_window, Black_Colour,[350, 350, 100, 100])

    # displaying a circle on the window (x, y, radius)
    # pygame.draw.circle(game_window, Black_Colour, (400, 300), 50)
