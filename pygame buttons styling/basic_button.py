import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))

red_button = pygame.Surface((50, 50)) 
red_button.fill((255, 0, 0))


red_button2 = pygame.Surface((50, 50))
red_button2.fill((255, 0, 0))
red_button3 = pygame.Surface((50, 50))
red_button3.fill((255, 0, 0))

window.blit(red_button, (200, 200)) 
pygame.display.update()

window.blit(red_button2, (400, 200)) 
window.blit(red_button3, (600, 200))
pygame.display.update()

start_img = pygame.image.load('start.webp')
start_button = pygame.Surface(start_img.get_rect().size)
start_button.blit(start_img, (0, 0))

class Button():
    def __init__(self, color, x,y,width,height, text='click_me'):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

start_button = Button((255, 0, 0), 200, 200, 50, 50, 'Start')
start_button.draw(window)

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if red_button.get_rect().collidepoint(pos):
                print("Button clicked!")

font = pygame.font.Font(None, 35)
text = font.render('Click Me!', True, (255, 255, 255))                
red_button.blit(text, (5, 5))
window.blit(red_button, (200, 200)) 
pygame.display.update()

hovered = False
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if red_button.get_rect().collidepoint(pos):
                hovered = True
            else:
                hovered = False
    if hovered:
        red_button.fill((200, 0, 0))
    else:
        red_button.fill((255, 0, 0))
    red_button.blit(text, (5, 5))
    window.blit(red_button, (200, 200)) 
    pygame.display.update()


pygame.quit()