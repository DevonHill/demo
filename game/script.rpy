# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg cty = "images/cty.png"
image logo text = Text("This is a text displayable.", size=30)
image bg blck = "images/bg blck.png"
image prologue = "images/prologue.jpg"

define slowdissolve = Dissolve(1.0)
define sh = Character("", window_background=None)
 
 
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
define mc = Character("[name]")

label start:
    show prologue
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
    menu:
        "ya":
            jump enter_p
        
        "tidak":
            jump name_p
    
#    STORY  P
    label enter_p:
        show bg blck
        show screen bab1_l
        with dissolve

        pause 1.0

        show screen prologue_text
        with dissolve

        pause 1.0
         
        hide bg blck
        hide screen bab1_l
        hide screen prologue_text

        # show bg cty bench
        mc "{cps=35}Ahh......{/cps}{cps=25} kota ini memang membosankan ya... {/cps}"
        mc "{cps=25}Mungkin Aku doang yang kerjaannya itu itu aja pas SMP dulu {/cps}"
        mc "{cps=25}Memang banyak sih yang coba deketin Aku dulu, tapi entah kenapa Aku ngerasa mereka itu bukan tipeku Tau.....{/cps}"
        "Teman disamping" "{cps=25}Kalo Aku bodo amat masalah percintaan sih, kamu aja yang mikirin banget. Masalahnya mau cari rangking dikelas mah aku, terus tinggal kuliah deh kalo dapat beasiswa {/cps}"
        "Teman disamping" "{cps=25}Menurut loh gimana? bukannya mikirin masa depan bagus tuh daripada mikirin cowo yang nggak jelas gitu? {/cps}"

    menu:
        "Bosan ya... emang bosan atuh, tapi yang namanya tanggung jawab hidup ya... tinggal dijalanin aja atuh. Kalo stress tinggal nyari cowo, kalo kerja ya berusaha.":
            jump kursi_umum1

        "Bagi gua sih... hidup itu dibawa nyantai aja nggak sih? jadi menurut aku sih, maunya ngabisin momen-momen bahagia aja sih di sma.":
            jump kursi_umum2
        
        "Bebas sih, masalahnya kita gabisa tau takdir juga tuh. takdir kita juga sudah ditentukan tuhan dari lahir sampai mati. ":
            jump kursi_umum3
        
    label kursi_umum1:
        # show bg cty bench
        mc "{cps=25}Kan ada juga tuh pepatah bilang kalo kerasnya usaha lo akan membuahkan hasil, tapi hanya waktu yang menawabnya. {/cps}"
        "Teman disamping" "{cps=25}Kata-kata hari ini dari teman kocak disebelah {/cps}{cps=25}"
        "Teman disamping" "{cps=35}AnJay...{/cps}"
        "Teman disamping" "{cps=25}Tapi ada benernya juga lu, gua jadi merasa lebih semangat dari kota bosan ini. {/cps}"
        "Teman disamping" "{cps=35}Makasih [name]{/cps}"


    label kursi_umum2:
        # show bg cty bench
        mc "{cps=25}Memang cowo kadang gajelas...... tapi kadang lucu juga ngeliatnya. Lagian kuliah gampang, bahkan ada aja yang tinggal ngasih duit lulus juga tuh{/cps}"
        "Teman disamping" "{cps=25}Ohh gitu ya... Btw mau nanya [name]{/cps}"
        mc "Apaan tuch?"
        "Teman disamping" "{cps=25}Tipe cowomu gimana?{/cps}"
        mc "Wahhh, kalo itu sih...."
    
    menu: 
        "dsakdjasda"
             jump tipe_cowo1

        "dsakdjasda"
             jump tipe_cowo2

        "dsakdjasda"
             jump tipe_cowo3

    label kursi_umum3:
        # show bg cty bench
        mc "{cps=25}Mau kemanapun juga kita tetap berjalan sesuai kehendak tuhan kok. Jadi ya... hidup slowing down aja sih, udah The Best LAH.... walau dikerjain orang juga, jadi pengalaman lumayan juga {/cps}"
        "Teman disamping" "{cps=25}Ohh gitu... Tapi [name], bukannya takdir bisa diubah kalo kita usaha? Kan kita belum coba juga tuh?{/cps}"
        mc "{cps=25}Ya.... tetap aja sih, kamu ngubah takdir itu termasuk dalam perubahan yang udah ditakdirkan tuhan juga sih, aku kutip dari salah satu filsuf{/cps}"
        "Teman disamping" "{cps=25}Siapa namanya tuh?{/cps}"
        mc "lupa"
        "Teman disamping" "{cps=25}Yaudah gapapa juga sih{/cps}"
        "Teman disamping" "{cps=25}Ohh iya nih{/cps}"
        "Teman disamping" "{cps=25}Aku lupa ada yang dikerjain dirumah, mungkin takdir juga gue lupa tuh{/cps}"
        mc "{cps=25}Ahahhahahha.. ok nih gapapa juga kok, lagi gabut juga gue{/cps}"
        "Teman disamping" "{cps=25}Yaudah gue cabut dulu yaa.... Dah{/cps}"
        mc "{cps=25}Ehh... Tunggu Bentar{/cps}"
        "Teman disamping" "{cps=25}Kenapa lagi ngab?{/cps}"

    menu: 
        "dsakdjasda"
             jump homeOr_go1

        "dsakdjasda"
             jump homeOr_go2
    



#    STORY  L


    label enter_l:
        show bg blck
        show screen bab1_l
        with dissolve

        pause 1.0

        show screen prologue_text
        with dissolve

        pause 1.0
         
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

    pause 1.0
    
    hide bg blck
    hide screen part_1
    hide screen jdl_prt1_l
    mc "hmmgdsygfuydgfuy"

    return
