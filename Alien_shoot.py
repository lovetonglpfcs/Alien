import pgzrun,time

WIDTH = 800
HEIGHT = 600
alien1 = Actor('alien')
alien2 = Actor('alien')
alien3 = Actor('alien')
alien2.y = HEIGHT/2
alien3.bottom = HEIGHT
def draw():
    screen.fill((210,100,100))
    alien1.draw()
    alien2.draw()
    alien3.draw()
    
def update():
    alien1.left += 2
    alien2.left += 6
    alien3.left += 10
    if alien1.left > WIDTH:
        alien1.right = 0
    if alien2.left > WIDTH:
        alien2.right = 0
    if alien3.left > WIDTH:
        alien3.right = 0

def on_mouse_down(pos,button):
    if button == mouse.LEFT and alien1.collidepoint(pos):
        set_alien1_hurt()
    if button == mouse.LEFT and alien2.collidepoint(pos):
        set_alien2_hurt()
    if button == mouse.LEFT and alien3.collidepoint(pos):
        set_alien3_hurt()
    



def set_alien1_hurt():
    alien1.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule(set_alien1NM,1.0)
def set_alien2_hurt():
    alien2.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule(set_alien2NM,1.0)
def set_alien3_hurt():
    alien3.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule(set_alien3NM,1.0)

def set_alien1NM():
    alien1.image = 'alien'
def set_alien2NM():
    alien2.image = 'alien'
def set_alien3NM():
    alien3.image = 'alien'
    
pgzrun.go()
    
