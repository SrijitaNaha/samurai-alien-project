import pgzrun
import random

WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

samurai = Actor("samurai")
samurai.pos = (200,200)

alien = Actor("alien")
alien.pos = (100,100)

def draw():
    screen.blit("background",(0,0))
    samurai.draw()
    alien.draw()
    screen.draw.text("Score: " + str(score), color="purple", topleft=(10,10))
    
    if game_over:
        screen.fill("red")
        screen.draw.text("Hey!! Your time is up. your final score is: "+str(score), topleft=(10,10),fontsize=40,color="white")
        
def place_alien():
    alien.x = random.randint(50,550)
    alien.y = random.randint(50,450)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.a:
        samurai.x -= 5
    if keyboard.d:
        samurai.x += 5
    if keyboard.w:
        samurai.y -= 5
    if keyboard.s:
        samurai.y += 5
    
    alien_collected = samurai.colliderect(alien)
    if alien_collected:
        score += 5
        place_alien()

clock.schedule(time_up,60.0)
pgzrun.go()