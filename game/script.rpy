# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg cty = "images/cty.png"
image logo text = Text("This is a text displayable.", size=30)
image bg blck = "images/bg blck.png"
image prologue = "images/prologue.jpg"

define slowdissolve = Dissolve(1.0)
define sh = Character("", window_background=None)
define mc = Character("[name]")
define sr = Character("Sarah", color="#008cff")

screen gender():
    vbox:
        xalign 0.5 ypos 0.2
        text "Gendermu?"
 
screen Nama():
    vbox:
        xalign 0.5 ypos 0.2
        text "Namamu?"
 
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

screen bab1_l():
    vbox:
        xalign 0.5 ypos 0.3
        text "{size=+50}BAB 1"

screen prologue_text():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}P r o l o g u e"

screen part_1():
    vbox:
        xalign 0.5 ypos 0.3
        text "{size=+50}PART 1"

screen jdl_prt1_l():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}Masa Perkenalan"
# Deklarasikan karakter yang digunakan di game.

label start:
    show prologue
    show screen gender
    menu:
        xalign 0.5 ypos 0.3
        
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
        show bg blck
        show screen bab1_l
        with dissolve

        pause 1.0

        show screen prologue_text
        with dissolve

        sh " "
         
        hide bg blck
        hide screen bab1_l
        hide screen prologue_text
        #show bg cty
        mc "{cps=25}Jadi inikah kota tujuanku?{/cps}"
        mc "{cps=25}Sepertinya ini kota yang sama seperti dulu"
        mc "{cps=25}Kota yang damai dan tenang{/cps}"
        mc "{cps=15}Menarik...{/cps}"

    #show bg blck
    #with dissole    
    show screen find_home1
    with dissolve
    sh ""
    hide screen find_home1

    show screen find_home2
    with dissolve
    sh ""
    hide screen find_home2

    show screen find_home3
    with dissolve
    sh ""
    hide screen find_home3

    #show my room l
    with dissolve
    mc "{cps=25}Akhirnya aku menemukan tempat tinggal{/cps}"

    #show my room l plafond
    #with pushdown
    #with vpunch
    mc "{cps=25}aku akan menepati janjiku untuk bersekolah disana{/cps}"
    mc "{cps=25}apakah kau masih mengingatku{/cps}"
    " " "{cps=10}{i}{color=#008cff}{size=+20}SARAH{/color}{/size}{size=+20}!{/i}{/cps}{/size}"

    show bg blck
    show screen part_1
    with dissolve

    pause 1.0

    show screen jdl_prt1_l
    with dissolve

    " " " "   
    hide bg blck
    hide screen part_1
    hide screen jdl_prt1_l
    
    #show bg schl
    #with dissolve
    mc "Jadi ini sekolahnya?"
    mc "Berapa lama aku pergi sehingga sekolah ini terlihat berbeda"
    mc "Terakhir kali aku di kota ini waktu aku masih kecil"
    mc "Banyak sekali yang berbeda termasuk sekolah ini"
    mc "Aku belum pernah masuk ke dalamnya sih waktu aku masih kecil"
    mc "Siapa peduli"
    mc "Aku akan menepati janjiku"
    #show bg side_schl


    return
