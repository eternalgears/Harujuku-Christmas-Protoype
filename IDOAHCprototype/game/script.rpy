# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Reina", image = "reina")
define k = Character("Kuma")

# nvl characters
define r_nvl = Character("Reina", kind = nvl, image = "reina")
define k_nvl = Character("Kuma", kind = nvl)

# defaults 

default preferences.text_cps = 40
define config.nvl_list_length = None


# The game starts here.

label start:

    scene bg room

    show reina default


    r "CODING MECHANICS"

    r "voice bleeps, texting mechanic, point and click, auto highlight?"

    r "hihihihihiih"

    show reina happy:
        ease 0.5 xalign 0.7 
    
    nvl_narrator "text tex ttext kuma"
    k_nvl "hi"
    r_nvl "hi"
    r_nvl happy "hiiiii"

    # This ends the game.

    return
