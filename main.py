import pygame
x=pygame.init()


#colors
white = (255,255,255)
red = (255,0,0)
black=(0,0,0)

#creating window    
gamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("MY First Game")

#game specific variable
exit_game = False
game_over = False

#creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")
                
    Game_window.fill(white)
   pygame.display.update()


pygame.quit()
quit()
