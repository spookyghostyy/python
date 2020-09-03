// Setup the game
info.setScore(0)
info.setLife(3)
// Setup the player 
let spaceship = sprites.create(img`
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
`)
spaceship.setPosition(10, 60)
spaceship.setFlag(SpriteFlag.StayInScreen, true)
spaceship.setKind(SpriteKind.Player)
// Configure player controls 
controller.moveSprite(spaceship, 200, 200)
// Make Enemys
let rock = sprites.create(img`
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
`)
rock.setPosition(100, 60)
rock.setVelocity(-100, 0)
rock.setKind(SpriteKind.Enemy)
// Bop Enemys
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_button_event_a_pressed() {
    let bop = sprites.createProjectileFromSprite(img`
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
    `, spaceship, 50, 50)
})
// destroy
sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function on_rock_blasted(sprite: Sprite, otherSprite: Sprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 10)
    info.changeScoreBy(1)
})
// take life
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
