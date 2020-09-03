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
spaceship.set_kind(SpriteKind.player)

#Configure player controls 
controller.move_sprite(spaceship, 200,200)

#Make Enemys
rock = sprites.create(img("""
    . . . . . . . . . c c 8 . . . .
    . . . . . . 8 c c c f 8 c c . .
    . . . c c 8 8 f c a f f f c c .
    . . c c c f f f c a a f f c c c
    8 c c c f f f f c c a a c 8 c c
    c c c b f f f 8 a c c a a a c c
    c a a b b 8 a b c c c c c c c c
    a f c a a b b a c c c c c f f c
    a 8 f c a a c c a c a c f f f c
    c a 8 a a c c c c a a f f f 8 a
    . a c a a c f f a a b 8 f f c a
    . . c c b a f f f a b b c c 6 c
    . . . c b b a f f 6 6 a b 6 c .
    . . . c c b b b 6 6 a c c c c .
    . . . . c c a b b c c c . . . .
    . . . . . c c c c c c . . . . .
"""))
rock.set_position(100,60)
rock.set_velocity(-100, 0)
rock.set_kind(SpriteKind.enemy)

#Bop Enemys
def on_button_event_a_pressed():
    bop = sprites.create_projectile_from_sprite(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . 2 .
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    . . . . . . . . . . . . . . 2 .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    """), spaceship, 50, 50)
controller.player1.on_button_event(ControllerButton.A, ControllerButtonEvent.PRESSED, on_button_event_a_pressed)

#destroy
def on_rock_blasted(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire,10)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_rock_blasted)
#take life
def on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap)