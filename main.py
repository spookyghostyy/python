#Setup the game
info.set_score(0)
info.set_life(3)

#Setup the player 
spaceship = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . a a . . . . . . .
    . . . . a a a a a a a . . . . .
    . . . . a a a a a a a a a a a .
    . . . . a a a a a a a a . . . .
    . . . a a a a . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
spaceship.set_position(10, 60)
spaceship.set_flag(SpriteFlag.STAY_IN_SCREEN, True )

#Configure player controls 
controller.move_sprite(spaceship, 200,200)

#Make Enemys

#Bop Enemys
