# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Reina")
define k = Character("Kuma")

# defaults 

default preferences.text_cps = 40


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show reina default

    # These display lines of dialogue.

    r "CODING MECHANICS"

    r "voice bleeps, texting mechanic, point and click, auto highlight?"

    r "hihihihihiih"



    # This ends the game.

    return
