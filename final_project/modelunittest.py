import pygame
import model

bg_width = 480 # bg size
bg_height = 852


pygame.init()
# =========================Player test=========================
print('########## Testing Player Model ###########')
p = model.Player(bg_width, bg_height) # set up player，starting coordinates
print('  Initial Top Coordinate',p.rect.midtop)
print(' ########## Move Up ###########')
for i in range(0, 5):  # get the coordinates in 5 times
    p.move_up()
    print('  Current Top Coordinate: ',p.rect.midtop)
print(' ########## Move Down ###########')
for i in range(0, 5):
    p.move_down()
    print('  Current Top Coordinate: ',p.rect.midtop)
print(' ########## Move Left ###########')
for i in range(0, 5):
    p.move_left()
    print('  Current Top Coordinate: ',p.rect.midtop)
print(' ########## Move Right ###########')
for i in range(0, 5):
    p.move_right()
    print('  Current Top Coordinate: ',p.rect.midtop)
print(' ########## Input (1000,1000) ###########')  # input the coordinates out of range
p = model.Player(1000, 1000)
p.move_up()
print('  Current Top Coordinate: ',p.rect.midtop)
print(' ########## Object Reset ###########')  # reset object
p.reset()
print('  Current Top Coordinate: ', p.rect.midtop)
print()  # empty line

# =========================small enemy test=========================
print("########## Testing SmallPlane Model ##########")
s = model.SmallPlane(bg_width, bg_height)
print('  Initial Top Coordinate: ', s.rect.midtop)
print(" ########## Move ##########")
for i in range(0, 5):
    s.move()
    print('  Current Top Coordinate: ',s.rect.midtop)
print(' ########## Input (1000,1000) ###########')
s = model.SmallPlane(1000, 1000)
s.move()
print('  Current Top Coordinate: ',s.rect.midtop)
print(" ########## Object Reset ##########")
s.reset()
print('  Current Top Coordinate: ',s.rect.midtop)
print()

# =========================bullet test=========================
print("########## Testing Bullet Model ###########")
b =model.Bullet(p.rect.midtop)
print('  Initial Top Coordinate',b.rect.midtop)
print(" ########## Move ##########")
for i in range(0, 5):
    b.move()
    print('  Current Top Coordinate: ',b.rect.midtop)
print(' ########## Input (1000,1000) ###########')
p = model.Player(1000, 1000)
print('  Current Top Coordinate: ',b.rect.midtop)
input ("Please Enter:")  
