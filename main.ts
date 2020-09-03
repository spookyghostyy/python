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
// Configure player controls 
controller.moveSprite(spaceship, 200, 200)
