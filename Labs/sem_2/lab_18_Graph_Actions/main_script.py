import pygame as pg

clock = pg.time.Clock()

bg = pg.image.load('bg.jpg')
char = pg.image.load('standing.png')

WIN_WIDTH = 800
WIN_HEIGHT = 475

class player(object):
    walkRight = [
        pg.image.load('R1.png'), 
        pg.image.load('R2.png'), 
        pg.image.load('R3.png'), 
        pg.image.load('R4.png'), 
        pg.image.load('R5.png'), 
        pg.image.load('R6.png'), 
        pg.image.load('R7.png'), 
        pg.image.load('R8.png'), 
        pg.image.load('R9.png')
    ]
    walkLeft = [
        pg.image.load('L1.png'), 
        pg.image.load('L2.png'), 
        pg.image.load('L3.png'), 
        pg.image.load('L4.png'), 
        pg.image.load('L5.png'), 
        pg.image.load('L6.png'),
        pg.image.load('L7.png'), 
        pg.image.load('L8.png'), 
        pg.image.load('L9.png')
    ]

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))

class enemy(object):
    walkRight = [
        pg.image.load('R1E.png'), 
        pg.image.load('R2E.png'), 
        pg.image.load('R3E.png'), 
        pg.image.load('R4E.png'), 
        pg.image.load('R5E.png'), 
        pg.image.load('R6E.png'), 
        pg.image.load('R7E.png'), 
        pg.image.load('R8E.png'), 
        pg.image.load('R9E.png'), 
        pg.image.load('R10E.png'), 
        pg.image.load('R11E.png')
    ]
    walkLeft = [
        pg.image.load('L1E.png'), 
        pg.image.load('L2E.png'), 
        pg.image.load('L3E.png'), 
        pg.image.load('L4E.png'), 
        pg.image.load('L5E.png'), 
        pg.image.load('L6E.png'), 
        pg.image.load('L7E.png'), 
        pg.image.load('L8E.png'), 
        pg.image.load('L9E.png'), 
        pg.image.load('L10E.png'), 
        pg.image.load('L11E.png')
    ]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

class circle(object):
    ORANGE = (255, 150, 100)

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self, win):
        self.move()
        pg.draw.circle(win, self.ORANGE, (self.x, self.y), self.r) 
            
    def move(self):
        if self.x >= WIN_WIDTH + self.r:
            self.x = 0 - self.r
        else:
            self.x += 2

def main():
    pg.init()
    win = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pg.display.set_caption("Lab 5")

    def redrawGameWindow():
        win.blit(bg, (0,0))
        man1.draw(win)
        man2.draw(win)
        goblin.draw(win)

        sun.draw(win)

        pg.display.update()
    
    man1 = player(200, 410, 64, 64)
    man2 = player(600, 410, 64, 64)
    goblin = enemy(100, 410, 64, 64, 700)

    sun = circle(-30, WIN_HEIGHT//3, 30)

    while True:
        clock.tick(27)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and man1.x > man1.vel:
            man1.x -= man1.vel
            man1.left = True
            man1.right = False
        elif keys[pg.K_RIGHT] and man1.x < WIN_WIDTH - man1.width - man1.vel:
            man1.x += man1.vel
            man1.right = True
            man1.left = False
        else:
            man1.right = False
            man1.left = False
            man1.walkCount = 0

        if keys[pg.K_a] and man2.x > man2.vel:
            man2.x -= man2.vel
            man2.left = True
            man2.right = False
        elif keys[pg.K_d] and man2.x < WIN_WIDTH - man2.width - man2.vel:
            man2.x += man2.vel
            man2.right = True
            man2.left = False
        else:
            man2.right = False
            man2.left = False
            man2.walkCount = 0
            
        if not(man1.isJump):
            if keys[pg.K_UP]:
                man1.isJump = True
                man1.right = False
                man1.left = False
                man1.walkCount = 0
        else:
            if man1.jumpCount >= -10:
                neg = 1
                if man1.jumpCount < 0:
                    neg = -1
                man1.y -= (man1.jumpCount ** 2) * 0.5 * neg
                man1.jumpCount -= 1
            else:
                man1.isJump = False
                man1.jumpCount = 10
        
        if not(man2.isJump):
            if keys[pg.K_w]:
                man2.isJump = True
                man2.right = False
                man2.left = False
                man2.walkCount = 0
        else:
            if man2.jumpCount >= -10:
                neg = 1
                if man2.jumpCount < 0:
                    neg = -1
                man2.y -= (man2.jumpCount ** 2) * 0.5 * neg
                man2.jumpCount -= 1
            else:
                man2.isJump = False
                man2.jumpCount = 10

        redrawGameWindow()

if __name__ == "__main__":
    main()