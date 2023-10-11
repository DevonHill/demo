# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg cty = "images/cty.png"
image logo text = Text("This is a text displayable.", size=30)
 
screen find_home1():
    vbox:
        xalign 0.5 ypos 0.4
        text "Beberapa jam telah berlalu"
            

screen find_home2():
    vbox:
        xalign 0.5 ypos 0.4
        text "aku mengelilingi kota ini untuk menemukan tempat tinggal"

screen find_home3():
    vbox:
        xalign 0.5 ypos 0.4
        text "aku telah menemukan tempat tinggal yang murah dan nyaman"

# Deklarasikan karakter yang digunakan di game.
define mc = Character("[name]")

# Game dimulai disini.
label start:
    #show bg blck
    "Gendermu?"
    menu:
        "Laki-Laki":
            jump name_l
        
        "Perempuan":
            jump name_p
    

    label name_l:
    python:
        name = renpy.input("Nama Panggilanmu?")

        name = name.strip() or "L"
    "Apakah namamu [name]?"
    menu:
        "ya":
            jump enter_l
        
        "tidak":
            jump name_l

    label name_p:
    python:
        name = renpy.input("Nama Panggilanmu?")
        
        name = name.strip() or "P"
    "{cps=25}Apakah namamu [name]?{/cps}"
    
    
   
    label enter_l:
        #show bg cty
        mc "{cps=25}Jadi inikah kota tujuanku{/cps}"
        
        mc "{cps=15}Menarik...{/cps}"

    #show bg blck
    #with dissole    
    show screen find_home1
    with dissolve
    "" ""
    hide screen find_home1

    show screen find_home2
    with dissolve
    "" ""
    hide screen find_home2

    show screen find_home3
    with dissolve
    "" ""
    hide screen find_home3

    #show my room l
    with dissolve
    mc "{cps=25}Akhirnya aku menemukan tempat tinggal{/cps}"

    #show my room l plafond
    #with pushdown
    mc "{cps=25}aku akan menepati janjiku untuk bersekolah disana{/cps}"
    mc "{cps=25}apakah kau masih mengingatku{/cps}"
    "" "{cps=10}{i}{color=#a50000}SARAH!{/i}{/color}{/cps}"

    return
