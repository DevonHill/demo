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


#  SCREEN P

# Next job = 
# 1. Kerjain bagian tipe cowok
# 2. Kerjain bagian choice buat next story

screen gabut1():
    vbox:
        xalign 0.5 ypos 0.4
        text "Beberapa jam telah berlalu"

screen gabut2():
    vbox:
        xalign 0.5 ypos 0.4
        text "Aku sedang duduk di tepi kota sambil melihat pemandangan kota dan merenung"

screen gabut3():
    vbox:
        xalign 0.5 ypos 0.4
        text "Tiba-tiba ada seorang temanku yang datang menghampiri dan duduk disampingku"

#  SCREEN L

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

# SCREEN BAB DAN JUDUL

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


# START GAME


# Game dimulai disini.
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

        #show bg blck
        mc "{cps=35}Ahh......{/cps}{cps=25} kota ini memang membosankan ya... {/cps}"
        mc "{cps=25}Mungkin Aku doang yang kerjaannya itu itu aja pas SMP dulu {/cps}"
        mc "{cps=35}Monoton yaa....{/cps}"
        mc "{cps=35}Jadi ini rasanya kesepian yaa....{/cps}"

        #show bg blck
        #with dissole    
        show screen gabut1
        with dissolve
        sh ""
        hide screen gabut1

        show screen gabut2
        with dissolve
        sh ""
        hide screen gabut2

        show screen gabut3
        with dissolve
        sh ""
        hide screen gabut3

        #show my room l
        with dissolve
        
        "Teman disamping" "{cps=25}Apa kabar nih.. [name]? {/cps}"
        mc "{cps=25}Lumayan sih...{/cps}"
        mc "{cps=25}Rada bingung sama diri sendiri aja gue..{/cps}"
        "Teman disamping" "{cps=25}Oalah, ceritain dong{/cps}"
        "Teman disamping" "{cps=25}Spill dikit nggak ngaruh, hehe{/cps}"
        mc "{cps=25}Sebenarnya...{/cps}"
        mc "{cps=25}Memang banyak sih yang coba deketin Aku dulu, tapi entah kenapa Aku ngerasa mereka itu bukan tipeku Tau.....{/cps}"
        "Teman disamping" "{cps=25}Kalo Aku bodo amat masalah percintaan sih, kamu aja yang mikirin banget. Masalahnya mau cari rangking dikelas mah aku, terus tinggal kuliah deh kalo dapat beasiswa {/cps}"
        "Teman disamping" "{cps=25}Menurut loh gimana? bukannya mikirin masa depan bagus tuh daripada mikirin cowo yang nggak jelas gitu? {/cps}"

    menu:
        "Bosan ya... emang bosan atuh, tapi yang namanya tanggung jawab hidup ya... tinggal dijalanin aja. Kalo stress tinggal nyari cowo, kalo kerja ya tinggal usaha.":
            jump kursi_umum1

        "Bagi gua sih... hidup itu dibawa nyantai aja nggak sih? jadi menurut aku sih, maunya ngabisin momen-momen bahagia aja sih di sma.":
            jump kursi_umum2
        
        "Bebas sih, masalahnya kita gabisa tau takdir juga tuh. takdir kita juga sudah ditentukan tuhan dari lahir sampai mati. ":
            jump kursi_umum3
        
    label kursi_umum1:
        # show bg cty bench
        mc "{cps=25}Kan ada juga tuh pepatah bilang kalo kerasnya usaha lo akan membuahkan hasil, tapi hanya waktu yang menjawabnya. {/cps}"
        "Teman disamping" "{cps=25}Kata-kata hari ini dari teman kocak si [name] {/cps}{cps=25}"
        "Teman disamping" "{cps=35}AnJay...{/cps}"
        "Teman disamping" "{cps=25}Tapi ada benernya juga lu, gua jadi merasa lebih semangat dari kota bosan ini. {/cps}"
        "Teman disamping" "{cps=25}Tapi juga gue penasaran satu hal deh...{/cps}"
        "Teman disamping" "{cps=25}Ehh dua deh...{/cps}"
        "Teman disamping" "{cps=25}Sebenarnya...{/cps}"
        "Teman disamping" "{cps=25}Aku masih bingung gimana cara dapetin beasiswa, terus..... aku juga gatau mau milih jurusan kuliah apa nanti pas sudah lulus SMA nih [name]{/cps}"
        mc "{cps=15}Gini-gini{/cps}"
        mc "{cps=30}Sebenarnya nyari beasiswa itu sih penting, tapi hal yang lebih penting lagi masih ada{/cps}"
        "Teman disamping" "{cps=25}Apa lagi sih [name], bikin penasaran aja..?{/cps}"
        mc "{cps=25}Nah, sebenarnya lu punya pilihan dalam hidup ini. {/cps}"
        mc "{cps=30}Tapi...{/cps}"
        mc "{cps=30}Semua pilihan yang kamu pilih pas lulus SMA nanti sebenarnya semuanya tergantung keadaan/kondisi kamu kek gimana gitu loh.{/cps}"
        mc "{cps=30}Jadi, pada akhirnya kita perlu ngeliat juga gimana kondisi keluarga kita, contohnya keuangan mereka. Syukur-syukur dapet beasiswa, kalo nggak gimana?{/cps}"
        "Teman disamping" "{cps=25}Iya juga yaa, terus?{/cps}"
        mc "{cps=30}Kalo pengen milih jurusan kuliah itu sebenarnya panjang lebar gue jelasinnya, tapi biar singkat gini aja nih...{/cps}"
        mc "{cps=30}Dimana passion dan posisi lo, disitu tempat kuliah lo{/cps}"
        mc "{cps=30}Sama satu lagi nih. kamu juga perlu liat bakatmu itu dimana{/cps}"
        mc "{cps=30}Udah, gitu simpelnya{/cps}"
        "Teman disamping" "{cps=25}Nah, jujurly aku pengen kuliah kedokteran sih, terus orang tua gue sebenarnya support sih, tapi gue liatnya mereka kayaknya nggak sanggup deh biayain semester gua{/cps}"
        "Teman disamping" "{cps=25}Modal buruh bisa apa coba?{/cps}"
        mc "{cps=25}Itu namanya lu gabisa bersyukur apa? Padahal orang tua lu udah usaha, kalo lu keberatan ya... lu ikut usaha juga gitu.{/cps}"
        mc "{cps=30}Dengan cara ikut nyari duit, kalo nggak, bisa lo bantu lah mereka minimal.{/cps}"
        "Teman disamping" "{cps=30}Hmmm.... iya juga sih [name]{/cps}"
        mc "{cps=20}Nah itu aja sih, sebenarnya masih panjang juga kalo mau gue jelasin sih. Setidaknya lo udah tau gambarannya gimana lah.....{/cps}"
        "Teman disamping" "{cps=25}Iya-iya gapapa, aku minta maaf kalo ngerepotin yaa....{/cps}"
        mc "{cps=20}Ohh ok deng{/cps}"
        "Teman disamping" "{cps=35}Makasih ya...{/cps}"
        mc "{cps=30}Sama-sama{/cps}"
        mc "{cps=30}By the way, kamu lagi gabut juga nggak?{/cps}"
        "Teman disamping" "{cps=35}Nggak juga..... emang kenapa?{/cps}"

    menu:
        "Mau ngerjain PR Matematika bareng nggak? ":
            jump kerumahMcBareng
        
        "Kita bicara sama Orang Tua kamu yuk, biar mereka ngertiin kamu ":
            jump kerumahTemenBareng
        
        "Aku mau pulang nih, ada yang gue kerjain dirumah ":
            jump pulangSendiri_sendiri
        



    label kursi_umum2:
        # show bg cty bench
        mc "{cps=25}Memang cowo kadang gajelas...... tapi kadang lucu juga ngeliatnya. Lagian kuliah gampang, bahkan ada aja yang tinggal ngasih duit lulus juga tuh{/cps}"
        "Teman disamping" "{cps=25}Ohh gitu ya... Btw mau nanya [name]{/cps}"
        mc "Apaan tuch?"
        "Teman disamping" "{cps=25}Tipe cowomu gimana?{/cps}"
        mc "Wahhh, kalo itu sih...."

    menu: 
        "dsakdjasda":
            jump tipe_cowo1

        "dsakdjasda":
            jump tipe_cowo2

        "dsakdjasda":
            jump tipe_cowo3

    label kursi_umum3:
        # show bg cty bench
        mc "{cps=25}Mau kemanapun juga kita tetap berjalan sesuai kehendak tuhan kok. Jadi ya... hidup slowing down aja sih, udah The Best LAH.... walau dikerjain orang juga, jadi pengalaman lumayan juga {/cps}"
        "Teman disamping" "{cps=25}Ohh gitu... Tapi [name], bukannya takdir bisa diubah kalo kita usaha? Kan kita belum coba juga tuh?{/cps}"
        mc "{cps=25}Ya.... tetap aja sih, kamu ngubah takdir itu termasuk dalam perubahan yang udah ditakdirkan tuhan juga sih, aku kutip dari salah satu filsuf{/cps}"
        "Teman disamping" "{cps=25}Siapa namanya tuh?{/cps}"
        mc "Aduh.... lupa nih"
        mc "Takdir untuk lupa sesuatu yaa...."
        "Teman disamping" "{cps=25}Yaudah gapapa juga sih{/cps}"
        "Teman disamping" "{cps=25}Ohh iya nih{/cps}"
        "Teman disamping" "{cps=25}Aku lupa ada yang dikerjain dirumah, mungkin takdir juga gue lupa tuh{/cps}"
        mc "{cps=25}Ahahhahahha.. ok nih gapapa juga kok, lagi gabut juga gue{/cps}"
        "Teman disamping" "{cps=25}Yaudah gue cabut dulu yaa.... Dah{/cps}"
        mc "{cps=25}Ehh... Tunggu Bentar{/cps}"
        "Teman disamping" "{cps=25}Kenapa lagi ngab?{/cps}"

    menu: 
        "Mau ngerjain PR Matematika bareng nggak? ":
            jump kerumahMcBareng
        
        "Kita bicara sama Orang Tua kamu yuk, biar mereka ngertiin kamu ":
            jump kerumahTemenBareng
        
        "Aku mau pulang nih, ada yang gue kerjain dirumah ":
            jump pulangSendiri_sendiri
    
    
    return

#    STORY  L


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
        mc "{cps=25}Jadi inikah kota tujuanku{/cps}"
        
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
