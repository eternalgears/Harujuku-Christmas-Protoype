# The script of the game goes in this file.

# voice bleeps

init python:
    def reina_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/reina.wav", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def kuma_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/kuma.wav", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Reina", image = "reina", cb_name="reina", callback = CallbackList(reina_sound, name_callback))
define k = Character("Kuma", cb_name="kuma", callback = CallbackList(kuma_sound, name_callback))

# nvl characters
define r_nvl = Character("Reina", kind = nvl, image = "reina")
define k_nvl = Character("Kuma", kind = nvl)

layeredimage reina1:
    #at sprite_highlight('reina')
    group emotion:
        attribute neutral default:
            "reina_neutral"
        attribute happy:
            "reina_happy"

layeredimage kuma1:
    #at sprite_highlight('kuma')
    group emotion:
        attribute neutral default:
            "kuma_neutral"
        attribute happy:
            "kuma_happy"

image reina = LayeredImageProxy("reina1", transform=sprite_highlight("r"))
image kuma = LayeredImageProxy("kuma1", transform=sprite_highlight("k"))

# defaults 

default preferences.text_cps = 40
define config.nvl_list_length = None

# The game starts here.

label start:

    scene bg room

    show reina neutral:
        ease 0.5 xalign 0.9

    show kuma neutral:
        ease 0.5 xalign 0.1

    r "CODING MECHANICS"

    r "voice bleeps, texting mechanic, point and click, auto highlight?"
    
    r "hihihihihiih"

    k "hiiiiii"

    r "ajsdfhkjahjskdfhkja"

    show reina happy:
        ease 0.5 xalign 0.7 
    
    nvl_narrator "text tex ttext kuma"
    k_nvl "hi"
    r_nvl "hi"
    r_nvl neutral "hiiiii"
    k_nvl "hiiiii"

    show reina happy:
        ease 0.5 xalign 0.5 

    # This ends the game.

    return
