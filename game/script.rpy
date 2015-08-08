﻿init:
    # Custom effects / transitions
    image snow = Snow("img/Snowflake.gif", maxparticles=200, wind=200)
    define shake = Shake((0, 0, 0, 0), 1.0, dist=5)

    #Main characters
    define c = Character(name="Carmilla")
    define l = Character(name="Laura")
    define p = Character(name="Perry")
    define laf = Character(name="LaFontaine")

    #Minor characters
    define leif = Character(name="Leif")
    define mayor = Character(name="The Mayor")
    

# The game starts here.
label start:  
    menu:
        "Run tests, or tiny demo?"
    
        "Tiny Demo":
            call dorm from _call_dorm
        "Tests":
            "Testing twitter handles"

            tw_laura "On the bright side, we have a {b}lot{/b} of bear spray."

            tw_laf "Maybe Perry's right with the whole \"don't use flames in every experiment, weirdo!\" Thing. #goodbyehair #wehadsomefuntimes{w=3.0}\nBut then again, fire. #forscience"

            tw_carmilla "Day 21. I was reduced to eating a badger three days ago. Euugh."

            "Testing mob sounds"

            play sound "sound/effect/angry_mob.mp3"

            "Testing snow"

            show snow
            $ renpy.pause(5.0)
            hide snow

            "Testing shake"

            "An earthquake!?!?" with shake

            "Testing test riddle battle with placeholder dialogue."

            call riddle_battle from _call_riddle_battle

    call credits from _call_credits

    return