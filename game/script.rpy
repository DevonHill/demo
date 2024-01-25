# Bagian catatan
# Bab, Chapter, Part = Pergantian bab dan chapter ditampilkan, dan hanya part yang tidak diketahui player, kecuali membaca komentar pemisahan part di kodingan, atau menalar sendiri tiap perbedaan garis besar alur cerita 
# Selama belum ada gambar oficial, project ini bisa memakai gambar bajakan dulu
# Sprites karakter = nanti, gambar karakter dipisah tiap emosi yg digunakan, kemudian akan ada emosi dalam pikiran yang ditampilkan ke player sebagai sprites tambahan pada scene tertentu 
# Kalau sudah tahap launch game, ada baiknya dibuat video intro game diawal alur cerita. Serta endingnya juga 


# Bagian Define / Deklarasi gambar dan character
image bg cty = "images/cty.png"
image logo text = Text("This is a text displayable.", size=30)
image bg blck = "images/bg blck.png"
image prologue = "images/prologue.jpg"
image bg jett = "images/jett.jpg"
image bg mcHouse = "images/mcHouse.jpg"
image bg temenHouse = "images/temenHouse.jpg"

define slowdissolve = Dissolve(1.0)
define sh = Character("", window_background=None)
define mc = Character("[name]")
define mcd = Character("[name]", what_color="#65899e", who_color="#65899e")
define sr = Character("Sarah", color="#008cff")
define pt = Character("Putri", color="#4400ff")
define pttm = Character("Teman disamping")
define anon = Character("???", color="#ff0303")
define ibumc = Character("Ibu")
define ibuputri = Character("Ibu Putri")
define ayahputri = Character("Ayah Putri")

screen gender():
    vbox:
        xalign 0.5 ypos 0.2
        text "Gendermu?"


#  SCREEN P

# Next job = 
# 1. Fix bagian takdir, sekira terlihat berlebih dan tak Sberdaya *
# 2. Kerjain bagian tipe cowok *
# 3. Kerjain bagian choice buat next story yg 15 label (chapter 2)
# 4. Fix cps sesuai suasana
# 5. Pemisahan Part  *
# 6. Fixproblem kedap kedip tiap part *
# 7. Edit percakapan seolah olah mc belum terlalu akrab dengan putri *

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
        text "Apakah namamu [name]?"
 
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

# SCREEN BAB DAN JUDUL L

screen bab1_l():
    vbox:
        xalign 0.5 ypos 0.3
        text "{size=+50}BAB 1"

screen prologue_text():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}P r o l o g u e"

screen chapter_1():
    vbox:
        xalign 0.5 ypos 0.3
        text "{size=+50}CHAPTER 1"

screen chapter_2():
    vbox:
        xalign 0.5 ypos 0.3
        text "{size=+50}CHAPTER 2"

screen jdl_chpt1_l():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}Masa Perkenalan"

screen jdl_chpt1_p():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}Masa Perkenalan"

screen jdl_chpt2_p1():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}Kerumah Sendiri bawa Teman"

screen jdl_chpt2_p2():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}Ikut kerumah Teman"

screen jdl_chpt2_p3():
    vbox:
        xalign 0.5 ypos 0.42
        text "{size=+20}Pulang Sendiri kerumah"



# Deklarasikan karakter yang digunakan di game.
define mc = Character("[name]")


# START GAME


# Game dimulai disini.
label start:
    show prologue
    show screen gender
    menu:
        
        "Laki-Laki":
            jump name_l
        
        "Perempuan":
            jump name_p
    

    label name_l:
    hide screen gender
    python:
        name = renpy.input("Nama Panggilanmu?")

        name = name.strip() or "L"
    show screen Nama
    menu:
        "ya":
            jump enter_l
        
        "tidak":
            jump name_l   

    label name_p:
    hide screen gender
    python:
        name = renpy.input("Nama Panggilanmu?")
        
        name = name.strip() or "P"
    show screen Nama
    menu:
        "ya":
            jump enter_p
        
        "tidak":
            jump name_p



#    STORY  P



    label enter_p:
        hide screen Nama

        show bg blck
        show screen bab1_l
        with dissolve

        pause 1.0

        show screen prologue_text
        with dissolve

        window hide
        sh ""
         
        hide bg blck
        hide screen bab1_l
        hide screen prologue_text

        # show bg blck
        play music "audio/angin-sepoi.ogg" volume 5 fadein 1.0
        with slowdissolve
        mc "{cps=35}Ahh......{/cps}{cps=25} kota ini memang membosankan ya... {/cps}"
        mc "{cps=25}Mungkin Aku doang yang kerjaannya itu itu aja pas SMP dulu {/cps}"
        mc "{cps=20}Sepertinya ini sebuah tanda{/cps}"
        mc "{cps=13}Jadi inikah kehampaan tanpa sepi? {/cps}"
        stop music fadeout 2.3

        window hide
        # ^^^^^^ #
# Cara hide textbox renpy 
        # ^^^^^^ #

        
        show bg blck
        show screen chapter_1
        with dissolve

        pause 1.0

        show screen jdl_chpt1_p
        with dissolve

        window hide
        sh ""

        hide bg blck
        hide screen chapter_1
        hide screen jdl_chpt1_p
        
        # -----------------------------------------------------------

        #show bg blck
        with slowdissolve

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

        with dissolve

# ---------------------------------------------------------------------------------------------------------------------
# JANGAN LUPA MATIKAN / KOMENTAR BACKGROUND SEMENTARA SEBELUM COMMIT DAN PUSH KE GITHUB (jika gambar dari ilustrator belum rilis ngab :)
        show bg jett
        with slowdissolve
# ---------------------------------------------------------------------------------------------------------------------
# Musik sementara (bajakan)
        play music "audio/16A6.ogg" volume 1 loop

        anon"{cps=25}Apa kabar nih.. [name]? {/cps}"
        play sound "audio/bell-ding.ogg"
        mc "{cps=25}!?{/cps}"
        mc "{cps=25}Lumayan sih...{/cps}"
        "Teman disamping" "{cps=25}Udah lama nggak ketemu kamu nih...{/cps}"
        mc "{cps=25}Perasaan aku masih gitu gitu aja dah kerjaannya, mungkin kamu yang jarang liat{/cps}"
        "Teman disamping" "{cps=25}Mungkin........{/cps}"
        "Teman disamping" "{cps=25}Btw kamu ngapain duduk sendiri disini kaya kurang kerjaan?{/cps}"
        mc "{cps=25}Gabut doang sih...{/cps}"
        "Teman disamping" "{cps=25}Oalah...{/cps}"
        "Teman disamping" "{cps=25}Oh iya, nama kamu bukannya [name] ya..?{/cps}"
        mc "{cps=25}Ga salah kok...{/cps}"
        "Teman disamping" "{cps=25}Ga salah lagi yaa...?{/cps}"
        mc "{cps=25}Ahahahaha{/cps}"
        "Teman disamping" "{cps=25}Ada apa sih sebenarnya? Muka mu kok kelihatan pucat gitu?{/cps}"
        mc "{cps=25}Habis Frustasi aja sih, gaada hal lain kayak galau atau apa gitu sih{/cps}"
        mcd "{cps=25}Padahal gue habis Galau berat lah ASTAGAAA........{/cps}"
        mc "{cps=25}Rada bingung sama diri sendiri aja gue..{/cps}"
        "Teman disamping" "{cps=25}Oalah, ceritain dong{/cps}"
        "Teman disamping" "{cps=25}Spill dikit nggak ngaruh, hehe{/cps}"
        mcd "{cps=25}CkckckCk waduhh... dia emang temen dekat gue dulu sih.., tapi kalo udah kek gini beda cerita lah anjir. mending gw nyerah aja lah{/cps}"
        mc "{cps=40}Ehmm{/cps}"
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
        "Teman disamping" "{cps=15}Wahhh...{/cps}"
        "Teman disamping" "{cps=25}Kata-kata hari ini Keren juga ya... [name] {/cps}{cps=25}"
        mc "{cps=45}Yoi{/cps}"
        "Teman disamping" "{cps=25}Tapi ada benernya juga lu, gua jadi merasa lebih semangat dari kota yang bosan ini. {/cps}"
        "Teman disamping" "{cps=25}Tapi juga gue penasaran satu hal deh...{/cps}"
        "Teman disamping" "{cps=25}Ehh dua deh...{/cps}"
        "Teman disamping" "{cps=25}Sebenarnya...{/cps}"
        "Teman disamping" "{cps=25}Aku masih bingung gimana cara dapetin beasiswa, terus..... aku juga gatau mau milih jurusan kuliah apa nanti pas sudah lulus SMA nih [name]{/cps}"
        mc "{cps=20}Gini-gini{/cps}"
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
            jump kerumahMcBareng1
        
        "Kita bicara sama Orang Tua kamu yuk, biar mereka ngertiin kamu ":
            jump kerumahTemenBareng1
        
        "Ga jadi deh, aku lupa ada juga yang gue kerjain dirumah":
            jump pulangSendiri_sendiri1

    label kursi_umum2:
        # show bg cty bench
        mc "{cps=25}Memang cowo kadang gajelas...... tapi kadang lucu juga ngeliatnya. Lagian kuliah gampang, bahkan ada aja yang tinggal ngasih duit lulus juga tuh{/cps}"
        "Teman disamping" "{cps=25}Ohh gitu ya... Btw mau nanya [name]{/cps}"
        mc "Apaan tuch?"
        "Teman disamping" "{cps=25}Tipe cowomu gimana?{/cps}"
        mc "Wahhh, kalo itu sih...."

# Dari sini alur ceritanya bakalan dibagi 15, tapi alur utamanya nanti bakalan jadi 9 karena cuma ada percakapan flashback mengenai pilihan dibawah
    menu: 
        "Cowo yang good looking, terus punya penghasilan sendiri, perhatian, cool, setia, effort sudah pasti. terusss.... murah hati, sabar, taat ibadah, kagak pelit, cowo yang royal, dan yang pasti se-agama ":
            jump tipe_cowo1

        "Cukup satu kata, gabisa kalo nggak satu frekuensi, titik":
            jump tipe_cowo2

        "Tipe yang bisa buat gua bahagia udah cukup kok":
            jump tipe_cowo3

    label tipe_cowo1:
        # show bg cty bench
        "Teman disamping" "{cps=25}Gilaaa.... se Elit itu kah spek Cowo mu?{/cps}"
        mc "{cps=25}Ahhahaahaa iya juga sih, cukup jadi tipe idaman aja sih kalo itu{/cps}"
        mc "{cps=25}Tapi kalonya bisa dapet yang kaya gitu, auto ngamuk sendiri deh gua di kamar{/cps}"
        "Teman disamping" "{cps=25}Kalonya gue bisa jadi gitu juga sih, tapi versi senyum-senyum sendiri{/cps}"
        mc "{cps=25}Oalah, gitu....{/cps}"
        "Teman disamping" "{cps=25}Sadar diri juga sih kalo mau nyari kelas berat kek gitu hehe{/cps}"
        "Teman disamping" "{cps=25}Ohh iya nih{/cps}"
        "Teman disamping" "{cps=25}Aku lupa ada yang dikerjain dirumah nih..{/cps}"
        mc "{cps=25}Ahahhahahha.. ok nih gapapa juga kok, lagi gabut juga gue{/cps}"
        "Teman disamping" "{cps=25}Yaudah gue cabut dulu yaa.... Dah{/cps}"
        mc "{cps=25}Ehh... Tunggu Bentar{/cps}"
        "Teman disamping" "{cps=25}Kenapa lagi nih?{/cps}"
        
    menu: 
        "Mau ngerjain PR Matematika bareng nggak? ":
            jump kerumahMcBareng21
        
        "Aku main kerumahmu bisa nggak? ":
            jump kerumahTemenBareng21
        
        "Ga jadi deh, aku lupa ada juga yang gue kerjain dirumah":
            jump pulangSendiri_sendiri21
    
    label tipe_cowo2:
        # show bg cty bench
        "Teman disamping" "{cps=25}Waduh... cukup membagongkan juga ini orang satu{/cps}"
        mc "{cps=25}Frekuensi musiknya, healingnya, gamenya, hobinya, makanannya.{/cps}"
        mc "{cps=25}Tapi sebenarnya kagak masalah juga kalo cuman satu atau dua hal yang se-frekuensi{/cps}"
        mc "{cps=25}Karena maksudku satu frekuensi itu biar ga banyak debat doang sih.{/cps}"
        "Teman disamping" "{cps=25}Ohh, iya iya.{/cps}"
        "Teman disamping" "{cps=25}Ada benernya juga yaa, soalnya kalo satu frekuensi bakalan lebih langgeng atau bisa jadi satu passion deh.{/cps}"
        mc "{cps=25}Nahhh.... itu tuh maksud gue.{/cps}"
        "Teman disamping" "{cps=25}Ohh iya nih{/cps}"
        "Teman disamping" "{cps=25}Aku lupa ada yang dikerjain dirumah, nih..{/cps}"
        mc "{cps=25}Ahahhahahha.. ok nih gapapa juga kok, lagi gabut juga gue{/cps}"
        "Teman disamping" "{cps=25}Yaudah gue cabut dulu yaa.... Dah{/cps}"
        mc "{cps=25}Ehh... Tunggu Bentar{/cps}"
        "Teman disamping" "{cps=25}Kenapa lagi nih?{/cps}"

    menu: 
        "Mau ngerjain PR Matematika bareng nggak? ":
            jump kerumahMcBareng22
        
        "Aku main kerumahmu bisa nggak? ":
            jump kerumahTemenBareng22
        
        "Ga jadi deh, aku lupa ada juga yang gue kerjain dirumah":
            jump pulangSendiri_sendiri22
    
    label tipe_cowo3:
        # show bg cty bench
        "Teman disamping" "{cps=25}Cukup simpel juga yaa...{/cps}"
        mc "{cps=25}Iya dong, masa enggak?{/cps}"
        "Teman disamping" "{cps=50}Ye{/cps}"
        mc "{cps=25}Yaa..... begitulah, yang penting hidup itu dibawa hepi aja sih{/cps}"
        "Teman disamping" "{cps=50}Ye{/cps}"
        mc "{cps=25}Apaan dah, ngeselin tauu{/cps}"
        mc "{cps=25}Iya deng, maap{/cps}"
        "Teman disamping" "{cps=25}Ohh iya nih{/cps}"
        "Teman disamping" "{cps=25}Aku lupa ada yang dikerjain dirumah, nih..{/cps}"
        mc "{cps=25}Ahahhahahha.. ok nih gapapa juga kok, lagi gabut juga gue{/cps}"
        "Teman disamping" "{cps=25}Yaudah gue cabut dulu yaa.... Dah{/cps}"
        mc "{cps=25}Ehh... Tunggu Bentar{/cps}"
        "Teman disamping" "{cps=25}Kenapa lagi nih?{/cps}"

    menu: 
        "Mau ngerjain PR Matematika bareng nggak? ":
            jump kerumahMcBareng23
        
        "Aku main kerumahmu bisa nggak? ":
            jump kerumahTemenBareng23
        
        "Ga jadi deh, aku lupa ada juga yang gue kerjain dirumah":
            jump pulangSendiri_sendiri23
    
    label kursi_umum3:
        # show bg cty bench
        mc "{cps=25}Mau kemanapun juga kita tetap berjalan sesuai kehendak tuhan kok. Jadi ya... hidup slowing down aja sih, udah The Best LAH.... walau dikerjain orang juga, jadi pengalaman lumayan juga {/cps}"
        "Teman disamping" "{cps=25}Iya sih.... masalahnya, gimana pun juga gue mau berusaha tetap gagal terus, serasa udah ditakdirkan buat gue gagal gituh{/cps}"
        mc "{cps=25}Yaa... kalo menurut lo gitu gue juga setuju sih {/cps}"
        mc "{cps=25}Kok kita rasanya dari dulu susah banget yaa buat ngejar nilai dia. Padahal dia sendiri malas belajar, kerjaannya cuman main hp doang terus tidur tapi nilainya tau tau diatas kita semua, serasa itu takdir dia yang buat dia jenius diantara satu sekolah kita.{/cps}"
        "Teman disamping" "{cps=25}Siapa namanya tuh?{/cps}"
        mc "Aduh.... lupa nih"
        mc "Dia orangnya pendiam juga masalahnya"
        mc "Takdir untuk lupa sesuatu yaa...."
        "Teman disamping" "{cps=25}Yaudah gapapa juga sih{/cps}"
        "Teman disamping" "{cps=25}Ohh iya nih{/cps}"
        "Teman disamping" "{cps=25}Aku lupa ada yang dikerjain dirumah, mungkin takdir juga gue lupa tuh{/cps}"
        mc "{cps=25}Ahahhahahha.. ok nih gapapa juga kok, lagi gabut juga gue{/cps}"
        "Teman disamping" "{cps=25}Yaudah gue cabut dulu yaa.... Dah{/cps}"
        mc "{cps=25}Ehh... Tunggu Bentar{/cps}"
        "Teman disamping" "{cps=25}Kenapa lagi nih?{/cps}"

    menu: 
        "Mau ngerjain PR Matematika bareng nggak? ":
            jump kerumahMcBareng3
        
        "Aku main kerumahmu bisa nggak? ":
            jump kerumahTemenBareng3
        
        "Ga jadi deh, aku lupa ada juga yang gue kerjain dirumah ":
            jump pulangSendiri_sendiri3
    
# ------------------------------------------------------------------

#Bagian Kerumah MC Bareng
# Bagian ini akan berisi alur utama yang dimana mc akan lupa nama temannya dan bertanya kemudian mereka bakalan kerumah si mc selagi mengerjakan PR Matimatikam bareng. Dan untuk next part atau babnya nanti mereka bakalan sering ketemu karena temennya si mc atau putri udah tau rumah mc

        # Dikarenakan si putri lama tidak ketemu dengan mc, jadinya mereka otomatis beda sekolah dan beda pr
    label kerumahMcBareng1:
        pttm "{cps=25}Wah boleh banget tuhh {/cps}"
        mc "{cps=25}Ayo kalo gitu, kita langsung aja yaa...{/cps}"
        pttm "{cps=25}Oke, tapi kamu jalan kaki?{/cps}"
        mc "{cps=25}Boleh sih, tapi kalo mau cepet aku bisa nebeng sepeda kamu kan?{/cps}"
        pttm "{cps=25}Yaudah nih.. sini naik{/cps}"
        mc "{cps=25}Woke, injak gas jangan lupa yaa....{/cps}"
        pttm "{cps=25}Kamu kira kita naik mobil napah{/cps}"
        pttm "{cps=25}Kita naik sepeda deng{/cps}"
        mc "{cps=25}Oke kak... kalo gitu langsung cus aja nih, lama bet{/cps}"
        pttm "{cps=25}Iya deh iya{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        play music "audio/musikpiano-santai" fadein 0.5
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena dia sedang memikirkan apa yang telah kami bicarakan tadi{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahku {/cps}"
        sh "{cps=35}kemudian kami langsung masuk ke ruang tamu, karena kelihatan tidak ada orang di rumah{/cps}"
        hide bg blck
        stop music

        show bg mcHouse
        with slowdissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        mc "{cps=35}Saya pulang!!{/cps}"
        pttm "{cps=35}Wahhhh! rumahmu bagus juga yaa..{/cps}"
        play sound "audio/bell-ding.ogg"
        anon "{cps=35}Ada siapa itu?? {/cps}"
        mc "{cps=35}Ohh, ini [name] bawa teman kerumah bu{/cps}"
        ibumc"{cps=35}Ohh gitu{/cps}"
        ibumc"{cps=35}Bawa temanmu duduk dulu tuh [name]{/cps}"
        mc "{cps=35}Iya bu{/cps}"
        ibumc"{cps=35}Kalo gitu Ibu buatkan teh dulu ya..{/cps}"
        pttm "{cps=35}Waduh jadi ngerepotin nih Tante{/cps}"
        mc "{cps=35}Gapapa, udah kebiasaan juga kalo ada tamu{/cps}"
        pttm "{cps=35}Ohh gitu yaa{/cps}"
        mcd "{cps=35}('Kami ngerjain PR nanti dimana yaa?')"
        mcd "{cps=35}('Sepertinya aku akan tanya dia')"
        mc "{cps=35}Ohh iya nih, kita ngerjainnya dimana nih?{/cps}"
        pttm "{cps=35}Hmmm, disini aja deh{/cps}"
        mc "{cps=35}Oke deh{/cps}"
        ibumc"{cps=35}Ini tehnya diminum dulu{/cps}"
        pttm "{cps=35}Ohh, iya Tante{/cps}"
        ibumc"{cps=35}Ohh iya, namamu siapa ya..?{/cps}"
        mcd "{cps=35}('!!')"
        mcd "{cps=35}('Aku lupa juga nanyain nama dia ternyata dari tadi')"
        pttm "{cps=35}Nama saya Putri Tante{/cps}"
        ibumc"{cps=35}Oalah...{/cps}"
        mc "{cps=35}Baru ingat aku{/cps}"
        pt "{cps=35}Kenapa tuh?{/cps}"
        mc "{cps=35}Dari tadi belum nanya nama kamu nih Put{/cps}"
        pt "{cps=35}Nahh, betul juga tuh{/cps}"
        mc "{cps=35}Ayo buka buku Put{/cps}"
        pt "{cps=35}Siap{/cps}"
        ibumc"{cps=35}Kalo gitu ibu ke kamar dulu yaa [name]{/cps}"
        ibumc"{cps=35}Yang semangat ngerjainnya{/cps}"
        mc "{cps=35}Oke Bu...{/cps}"
        " " "{cps=35}Ibuku pun langsung pergi ke kamar, dan kami tinggal berdua {/cps}"
        pt "{cps=35}Btw kita kan beda sekolah{/cps}"
        mc "{cps=35}Ehh, bener juga tuh{/cps}"
        pt "{cps=35}Yang pasti beda PR kan{/cps}"
        mc "{cps=35}Iya sih....{/cps}"
        mc "{cps=35}Tapi kayaknya kita satu materi{/cps}"
        pt "{cps=35}Hmmmm, Aku sih punya PR di Buku LKS yang ini{/cps}"
        mc "{cps=35}Wahhh.... kalo aku di buku catatan sih, dikasih gurunya langsung soal{/cps}"
        mc "{cps=35}Tapi karena Jam pelajarannya habis soal yang ini jadi PR{/cps}"
        pt "{cps=35}Ohh gitu yaa....{/cps}"
        mc "{cps=35}Ehh bentar{/cps}"
        pt "{cps=35}!!{/cps}"
        mc "{cps=35}Soal kita kurang lebih sama deh{/cps}"
        mc "{cps=35}Cuman beda angka doang, jumlah soalnya sama-sama 5 lagi{/cps}"
        pt "{cps=35}Berarti bisa aja lah saling bantu hehe...{/cps}"
        mc "{cps=35}Ahhahahhaha{/cps}"
        stop music fadeout 1.0
        
        play music "audio/musikpiano-santai.ogg" fadein 0.5 loop
        show bg blck
        with dissolve
        sh "{cps=35}Kami pun mulai mengerjakan PR Matematika bersama-sama{/cps}"
        sh "{cps=35}Dengan saling bertanya satu sama lain ketika kebingungan{/cps}"
        sh "{cps=35}Kami pun selesai mengerjakan dalam waktu yang cukup singkat{/cps}"
        sh "{cps=35}Dalam sisa waktu yang kami habiskan sebelum hari menjelang malam{/cps}"
        sh "{cps=35}Tanpa kami sadari waktu pun berlalu setelah kami berbicara tentang Jurusan kuliah{/cps}"
        hide bg blck

        show bg mcHouse
        with dissolve
        mc "{cps=35}Nah Put, kamu jam segini enggak dimarahin orang rumah kalo pulang{/cps}"
        pt "{cps=35}Udah jam 05:00 aja yaa...{/cps}"
        mc "{cps=35}Iya nih..{/cps}"
        pt "{cps=35}Boleh aja sih asalkan sebelum menjelang malam{/cps}"
        mc "{cps=35}Ohh gitu{/cps}"
        pt "{cps=35}Kalo gitu aku Pamit yaa{/cps}"
        mc "{cps=35}Oke Put{/cps}"
        ibumc"{cps=35}Jangan lupa mampir lagi yaa Putri{/cps}"
        mcd "{cps=35}Ehh! kaget..., tiba-tiba aja ada Ibu disini"
        pt "{cps=35}Iya Tante{/cps}"
        mc "{cps=35}Dadah Put....{/cps}"
        pt "{cps=35}Dadah [name]....{/cps}"
        mcd "{cps=35}Akhirnya PR Mtk selesai juga, tinggal kerjain yang lain aja deh terus tidur"
        hide bg mcHouse        
        stop music fadeout 0.5
        # buat screen untuk kelanjutan di esok harinya


    label kerumahMcBareng21:
        # show bg mcHouse
        pttm "{cps=25}Bisa aja sih, sekalian liat-liat kalo ada cowok ganteng dijalan {/cps}"
        mc "{cps=25}Kalo gitu, tanpa basa basi langsung aja yuk!{/cps}"
        pttm "{cps=25}Oke, kamu jalan kaki aja yaa...{/cps}"
        mc "{cps=25}Gampang.....{/cps}"
        mc "{cps=25}Aku sering jogging juga disekitar sini tiap minggu{/cps}"
        pttm "{cps=25}Ohh iya, jangan-jangan rumahmu dekat sini makanya kamu milih jalan aja{/cps}"
        mc "{cps=25}Nggak juga deng{/cps}"
        pttm "{cps=25}Yaudah nih malah entar lama disini, kita langsung jalan aja{/cps}"
        mc "{cps=25}Oke{/cps}"
        
        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena fokus kami terahlihkan melihat orang-orang di jalan pulang{/cps}"
        sh "{cps=35}Apalagi nafasku yang sedang terengah-engah saat lari{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahku {/cps}"
        sh "{cps=35}kemudian kami langsung masuk ke ruang tamu, karena kelihatan tidak ada orang di rumah{/cps}"
        hide bg blck
        stop music

        show bg mcHouse
        with slowdissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        mc "{cps=35}Sa.. sa..ya pulangggg!!{/cps}"
        pttm "{cps=35}Kamu kelelahan yaa habis jogging?{/cps}"
        mc "{cps=35}Hhhuuhh... lumayan sih...{/cps}"
        play sound "audio/bell-ding.ogg"
        anon "{cps=35}Ada siapa itu?? {/cps}"
        mc "{cps=35}Ohh, ini [name] bawa teman kerumah bu{/cps}"
        ibumc"{cps=35}Ohh gitu{/cps}"
        ibumc"{cps=35}[name] sama temenmu dibawa istirahat dulu tuh{/cps}"
        mc "{cps=35}Iya bu{/cps}"
        ibumc"{cps=35}Kalo gitu Ibu buatkan teh dulu ya..{/cps}"
        pttm "{cps=35}Waduh jadi ngerepotin nih Tante{/cps}"
        mc "{cps=35}Gapapa, udah kebiasaan juga kalo ada tamu{/cps}"
        pttm "{cps=35}Ohh gitu yaa{/cps}"
        mcd "{cps=35}('Kami ngerjain PR nanti dimana yaa?')"
        mcd "{cps=35}('Sepertinya aku akan istirahat dulu sebentar')"
        mc "{cps=35}Kayaknya kamu cepat sekali tadi, jadi kelelahan aku ngejarnya{/cps}"
        pttm "{cps=35}Ahhahahhaha, kasian deh lu...{/cps}"
        mcd "{cps=35}('Phewww, emang rada ngeselin sih.'){/cps}"
        mcd "{cps=35}('Tapi kalo dipikir lagi jikalau dia duluan didepan pasti kelewatan hahaha'){/cps}"
        " " "{cps=35}Aku pun akhirnya lebih tenang sekarang dengan sedikit tersenyum membayangkan dia terlalu jauh didepan{/cps}"
        " " "{cps=35}Dengan tenangnya Ibuku tiba-tiba datang mengagetkan kami{/cps}"
        ibumc"{cps=35}NAHHHH!!, ini tehnya diminum dulu{/cps}"
        pttm "{cps=35}Ehh iya Tante{/cps}"
        mcd "{cps=35}('Widihh, cepet banget dah bikin kaget aja...'){/cps}"
        ibumc"{cps=35}Ohh iya, namamu siapa ya..?{/cps}"
        mcd "{cps=35}('!!')"
        mcd "{cps=35}('Aku lupa juga nanyain nama dia ternyata dari tadi')"
        pttm "{cps=35}Nama saya Putri Tante{/cps}"
        ibumc"{cps=35}Oalah...{/cps}"
        ibumc"{cps=35}Kalo gitu ibu ke kamar dulu yaa [name]{/cps}"
        mc "{cps=35}Oke Bu...{/cps}"
        " " "{cps=35}Ibuku pun langsung pergi ke kamar, dan kami tinggal berdua{/cps}"
        mc "{cps=35}Baru ingat aku{/cps}"
        pt "{cps=35}Kenapa tuh?{/cps}"
        mc "{cps=35}Dari tadi belum nanya nama kamu nih Put{/cps}"
        pt "{cps=35}Nahh, betul juga tuh{/cps}"
        mc "{cps=35}Kok bisa ya...?{/cps}"
        pt "{cps=35}Gatau dah.. kamu kepikiran yang itu mulu sih, makanya sampai lupa nanyain nama{/cps}"
        mc "{cps=35}Lah... yang mana sih?{/cps}"
        pt "{cps=35}Kamu nanya..?{/cps}"
        mc "{cps=35}Ohh iya ada yang kutanya nich{/cps}"
        pt "{cps=35}Apaan tuch..?{/cps}"
        mc "{cps=35}Daritadi kita belum buka buku PR yaa..?{/cps}"
        pt "{cps=35}Ohh iya nih{/cps}"
        pt "{cps=35}Btw kita kan beda sekolah{/cps}"
        mc "{cps=35}Ehh, bener juga tuh{/cps}"
        pt "{cps=35}Yang pasti beda PR kan{/cps}"
        mc "{cps=35}Iya sih....{/cps}"
        mc "{cps=35}Tapi kayaknya kita satu materi{/cps}"
        pt "{cps=35}Hmmmm, Aku sih punya PR di Buku LKS yang ini{/cps}"
        mc "{cps=35}Wahhh.... kalo aku di buku catatan sih, gurunya tiba-tiba ngasih soal{/cps}"
        mc "{cps=35}Tapi karena Jam pelajarannya habis soal yang ini jadi PR waktu itu Put{/cps}"
        pt "{cps=35}Ohh gitu yaa....{/cps}"
        mc "{cps=35}Ehh bentar{/cps}"
        pt "{cps=35}......... . . .{/cps}"
        mc "{cps=35}Soal kita kurang lebih sama deh{/cps}"
        mc "{cps=35}Cuman beda angka doang, jumlah soalnya sama-sama 5 lagi{/cps}"
        pt "{cps=35}Berarti bisa aja sih kita Kerja sama hehe...{/cps}"
        mc "{cps=35}Ahhahahhaha{/cps}"
        stop music fadeout 1.0
        
        show bg blck
        with dissolve
        play music "audio/musikpiano-santai.ogg" fadein 0.5 loop
        sh "{cps=35}Kami pun mulai mengerjakan PR Matematika bersama-sama{/cps}"
        sh "{cps=35}Dengan saling bertanya satu sama lain ketika kebingungan{/cps}"
        sh "{cps=35}Kami pun mengerjakannya dengan penuh bahagia dan canda tawa{/cps}"
        sh "{cps=35}Sampai kami lupa akan apa yang membatasi kami{/cps}"
        sh "{cps=35}Yaitu waktu yang sudah menunjukan pukul 18.00{/cps}"
        hide bg blck

        show bg mcHouse
        with dissolve
        mc "{cps=35}Nah Put, kamu jam segini enggak dimarahin orang rumah kalo pulang{/cps}"
        pt "{cps=35}Udah jam 6 malam aja yaa...{/cps}"
        mc "{cps=35}Iya nih..{/cps}"
        pt "{cps=35}Waduhh... kita kebablasan yaa...{/cps}"
        pt "{cps=35}Mana belum selesai lagi Tugas kita{/cps}"
        mc "{cps=35}Kamu gimana sih...{/cps}"
        pt "{cps=35}Lah.... bukannya kamu yang bicara mulu daritadi{/cps}"
        mc "{cps=35}Yaudah lah...{/cps}"
        mc "{cps=35}Sisa 2 soal tinggal kerjain sendiri aja nanti gak masalah kok{/cps}"
        pt "{cps=35}Kalo gitu Aku mau pulang dulu yaa sebelum larut malam{/cps}"
        mc "{cps=35}Semoga aman di jalan nihh{/cps}"
        pt "{cps=35}Tenang.....{/cps}"
        ibumc"{cps=35}Jangan lupa mampir lagi yaa Putri{/cps}"
        mcd "{cps=35}Ehh! kaget..., tiba-tiba aja ada Ibu disini"
        pt "{cps=35}Iya Tante{/cps}"
        mc "{cps=35}Dadah Put....{/cps}"
        pt "{cps=35}Dadah [name]....{/cps}"
        mcd "{cps=35}Akhirnya PR Mtk sisa 2 aja lagi, habis ngerjain kayaknya tugas yang lain nanti aja lah terus langsung tidur deh.."
        hide bg mcHouse        
        # buat screen untuk kelanjutan di esok harinya
        stop music fadeout 0.5



    label kerumahMcBareng22:
        # show bg mcHouse
        pttm "{cps=25}Bebas aja sih, kalo mau ikut sepedaku sini{/cps}"
        mc "{cps=25}Oke, btw langsung aja nih? {/cps}"
        pttm "{cps=25}Ya iyalah, entar kelamaan Kita disini{/cps}"
        mc "{cps=25}Liat-liat ya kalo ada cowok yang vibenya mirip gue{/cps}"
        pttm "{cps=25}Oke deh{/cps}"
        mc "{cps=25}KITA TEROBOSSS!!!!!!!{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena fokus kami terahlihkan melihat orang-orang di jalan pulang{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahku {/cps}"
        sh "{cps=35}kemudian kami langsung masuk ke ruang tamu, karena kelihatan tidak ada orang di rumah{/cps}"
        hide bg blck
        stop music

        show bg mcHouse
        with slowdissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        mc "{cps=35}Saya pulang!!{/cps}"
        pttm "{cps=35}Wahhhh! rumahmu bagus juga yaa..{/cps}"
        play sound "audio/bell-ding.ogg"
        anon "{cps=35}Ada siapa itu?? {/cps}"
        mc "{cps=35}Ohh, ini [name] bawa teman kerumah bu{/cps}"
        ibumc"{cps=35}Ohh gitu{/cps}"
        ibumc"{cps=35}[name] sama temenmu dibawa istirahat dulu tuh{/cps}"
        mc "{cps=35}Iya bu{/cps}"
        ibumc"{cps=35}Kalo gitu Ibu buatkan teh dulu ya..{/cps}"
        pttm "{cps=35}Waduh jadi ngerepotin nih Tante{/cps}"
        mc "{cps=35}Gapapa, udah kebiasaan juga kalo ada tamu{/cps}"
        pttm "{cps=35}Ohh gitu yaa{/cps}"
        mcd "{cps=35}('Kami ngerjain PR nanti dimana yaa?')"
        mcd "{cps=35}('Sepertinya aku akan istirahat dulu sebentar')"
        mc "{cps=35}Kayaknya kamu cepat sekali tadi, jadi kelelahan aku ngejarnya{/cps}"
        pttm "{cps=35}Ahhahahhaha, kasian deh lu...{/cps}"
        mcd "{cps=35}('Phewww, emang rada ngeselin sih.'){/cps}"
        mcd "{cps=35}('Tapi kalo dipikir lagi jikalau dia duluan didepan pasti kelewatan hahaha'){/cps}"
        " " "{cps=35}Aku pun akhirnya lebih tenang sekarang dengan sedikit tersenyum membayangkan dia terlalu jauh didepan{/cps}"
        " " "{cps=35}Dengan tenangnya Ibuku tiba-tiba datang mengagetkan kami{/cps}"
        ibumc"{cps=35}NAHHHH!!, ini tehnya diminum dulu{/cps}"
        pttm "{cps=35}Ehh iya Tante{/cps}"
        mcd "{cps=35}('Widihh, cepet banget dah bikin kaget aja...'){/cps}"
        ibumc"{cps=35}Ohh iya, namamu siapa ya..?{/cps}"
        mcd "{cps=35}('!!')"
        mcd "{cps=35}('Aku lupa juga nanyain nama dia ternyata dari tadi')"
        pttm "{cps=35}Nama saya Putri Tante{/cps}"
        ibumc"{cps=35}Oalah...{/cps}"
        ibumc"{cps=35}Kalo gitu ibu ke kamar dulu yaa [name]{/cps}"
        mc "{cps=35}Oke Bu...{/cps}"
        " " "{cps=35}Ibuku pun langsung pergi ke kamar, dan kami tinggal berdua{/cps}"
        mc "{cps=35}Baru ingat aku{/cps}"
        pt "{cps=35}Kenapa tuh?{/cps}"
        mc "{cps=35}Dari tadi belum nanya nama kamu nih Put{/cps}"
        pt "{cps=35}Nahh, betul juga tuh{/cps}"
        mc "{cps=35}Kok bisa ya...?{/cps}"
        pt "{cps=35}Gatau dah.. kamu kepikiran yang itu mulu sih, makanya sampai lupa nanyain nama{/cps}"
        mc "{cps=35}Lah... yang mana sih?{/cps}"
        pt "{cps=35}Kamu nanya..?{/cps}"
        mc "{cps=35}Ohh iya ada yang kutanya nich{/cps}"
        pt "{cps=35}Apaan tuch..?{/cps}"
        mc "{cps=35}Daritadi kita belum buka buku PR yaa..?{/cps}"
        pt "{cps=35}Ohh iya nih{/cps}"
        pt "{cps=35}Btw kita kan beda sekolah{/cps}"
        mc "{cps=35}Ehh, bener juga tuh{/cps}"
        pt "{cps=35}Yang pasti beda PR kan{/cps}"
        mc "{cps=35}Iya sih....{/cps}"
        mc "{cps=35}Tapi kayaknya kita satu materi{/cps}"
        pt "{cps=35}Hmmmm, Aku sih punya PR di Buku LKS yang ini{/cps}"
        mc "{cps=35}Wahhh.... kalo aku di buku catatan sih, gurunya tiba-tiba ngasih soal{/cps}"
        mc "{cps=35}Tapi karena Jam pelajarannya habis soal yang ini jadi PR waktu itu Put{/cps}"
        pt "{cps=35}Ohh gitu yaa....{/cps}"
        mc "{cps=35}Ehh bentar{/cps}"
        pt "{cps=35}......... . . .{/cps}"
        mc "{cps=35}Soal kita kurang lebih sama deh{/cps}"
        mc "{cps=35}Cuman beda angka doang, jumlah soalnya sama-sama 5 lagi{/cps}"
        pt "{cps=35}Berarti bisa aja sih kita Kerja sama hehe...{/cps}"
        mc "{cps=35}Ahhahahhaha{/cps}"
        stop music fadeout 1.0
        
        show bg blck
        with dissolve
        play music "audio/musikpiano-santai.ogg" fadein 0.5 loop
        sh "{cps=35}Kami pun mulai mengerjakan PR Matematika bersama-sama{/cps}"
        sh "{cps=35}Dengan saling bertanya satu sama lain ketika kebingungan{/cps}"
        sh "{cps=35}Kami pun mengerjakannya dengan penuh bahagia dan canda tawa{/cps}"
        sh "{cps=35}Sampai kami lupa akan apa yang membatasi kami{/cps}"
        sh "{cps=35}Yaitu waktu yang sudah menunjukan pukul 18.00{/cps}"
        hide bg blck

        show bg mcHouse
        with dissolve
        mc "{cps=35}Nah Put, kamu jam segini enggak dimarahin orang rumah kalo pulang{/cps}"
        pt "{cps=35}Udah jam 6 malam aja yaa...{/cps}"
        mc "{cps=35}Iya nih..{/cps}"
        pt "{cps=35}Waduhh... kita kebablasan yaa...{/cps}"
        pt "{cps=35}Mana belum selesai lagi Tugas kita{/cps}"
        mc "{cps=35}Kamu gimana sih...{/cps}"
        pt "{cps=35}Lah.... bukannya kamu yang bicara mulu daritadi{/cps}"
        mc "{cps=35}Yaudah lah...{/cps}"
        mc "{cps=35}Sisa 2 soal tinggal kerjain sendiri aja nanti gak masalah kok{/cps}"
        pt "{cps=35}Kalo gitu Aku mau pulang dulu yaa sebelum larut malam{/cps}"
        mc "{cps=35}Semoga aman di jalan nihh{/cps}"
        pt "{cps=35}Tenang.....{/cps}"
        ibumc"{cps=35}Jangan lupa mampir lagi yaa Putri{/cps}"
        mcd "{cps=35}Ehh! kaget..., tiba-tiba aja ada Ibu disini"
        pt "{cps=35}Iya Tante{/cps}"
        mc "{cps=35}Dadah Put....{/cps}"
        pt "{cps=35}Dadah [name]....{/cps}"
        mcd "{cps=35}Akhirnya PR Mtk sisa 2 aja lagi, habis ngerjain kayaknya tugas yang lain nanti aja lah terus langsung tidur deh.."
        hide bg mcHouse        
        # buat screen untuk kelanjutan di esok harinya
        stop music fadeout 0.5


    label kerumahMcBareng23:
        # show bg mcHouse
        pttm "{cps=25}Santai aja loh, lagian kita paling-paling ngerjain PR doang kan{/cps}"
        mc "{cps=25}Iya, paling gitu doang sih {/cps}"
        mc "{cps=25}Btw, kamu kenal nggak cowok yang kayak tipeku tadi?{/cps}"
        pttm "{cps=25}Banyak cowo yang pernah kamu liat pake mata itu emangnya mereka kalo pengen pacaran gamau ceweknya hepi gituh?{/cps}"
        mc "{cps=25}Hmmmm, iya juga sih{/cps}"
        pttm "{cps=25}Berarti banyak banget yang bisa kamu pilih atuh{/cps}"
        pttm "{cps=25}Yaudah nih, langsung aja naik sepedaku biar ga banyak bacot{/cps}"
        mc "{cps=25}Dih, iyain deh{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena fokus kami terahlihkan melihat orang-orang di jalan pulang{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahku {/cps}"
        sh "{cps=35}kemudian kami langsung masuk ke ruang tamu, karena kelihatan tidak ada orang di rumah{/cps}"
        hide bg blck

        show bg mcHouse
        with slowdissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        mc "{cps=35}Saya pulang!!{/cps}"
        pttm "{cps=35}Wahhhh! rumahmu bagus juga yaa..{/cps}"
        play sound "audio/bell-ding.ogg"
        anon "{cps=35}Ada siapa itu?? {/cps}"
        mc "{cps=35}Ohh, ini [name] bawa teman kerumah bu{/cps}"
        ibumc"{cps=35}Ohh gitu{/cps}"
        ibumc"{cps=35}[name] sama temenmu dibawa istirahat dulu tuh{/cps}"
        mc "{cps=35}Iya bu{/cps}"
        ibumc"{cps=35}Kalo gitu Ibu buatkan teh dulu ya..{/cps}"
        pttm "{cps=35}Waduh jadi ngerepotin nih Tante{/cps}"
        mc "{cps=35}Gapapa, udah kebiasaan juga kalo ada tamu{/cps}"
        pttm "{cps=35}Ohh gitu yaa{/cps}"
        mcd "{cps=35}('Kami ngerjain PR nanti dimana yaa?')"
        mcd "{cps=35}('Sepertinya aku akan istirahat dulu sebentar')"
        mc "{cps=35}Kayaknya kamu cepat sekali tadi, jadi kelelahan aku ngejarnya{/cps}"
        pttm "{cps=35}Ahhahahhaha, kasian deh lu...{/cps}"
        mcd "{cps=35}('Phewww, emang rada ngeselin sih.'){/cps}"
        mcd "{cps=35}('Tapi kalo dipikir lagi jikalau dia duluan didepan pasti kelewatan hahaha'){/cps}"
        " " "{cps=35}Aku pun akhirnya lebih tenang sekarang dengan sedikit tersenyum membayangkan dia terlalu jauh didepan{/cps}"
        " " "{cps=35}Dengan tenangnya Ibuku tiba-tiba datang mengagetkan kami{/cps}"
        ibumc"{cps=35}NAHHHH!!, ini tehnya diminum dulu{/cps}"
        pttm "{cps=35}Ehh iya Tante{/cps}"
        mcd "{cps=35}('Widihh, cepet banget dah bikin kaget aja...'){/cps}"
        ibumc"{cps=35}Ohh iya, namamu siapa ya..?{/cps}"
        mcd "{cps=35}('!!')"
        mcd "{cps=35}('Aku lupa juga nanyain nama dia ternyata dari tadi')"
        pttm "{cps=35}Nama saya Putri Tante{/cps}"
        ibumc"{cps=35}Oalah...{/cps}"
        ibumc"{cps=35}Kalo gitu ibu ke kamar dulu yaa [name]{/cps}"
        mc "{cps=35}Oke Bu...{/cps}"
        " " "{cps=35}Ibuku pun langsung pergi ke kamar, dan kami tinggal berdua{/cps}"
        mc "{cps=35}Baru ingat aku{/cps}"
        pt "{cps=35}Kenapa tuh?{/cps}"
        mc "{cps=35}Dari tadi belum nanya nama kamu nih Put{/cps}"
        pt "{cps=35}Nahh, betul juga tuh{/cps}"
        mc "{cps=35}Kok bisa ya...?{/cps}"
        pt "{cps=35}Gatau dah.. kamu kepikiran yang itu mulu sih, makanya sampai lupa nanyain nama{/cps}"
        mc "{cps=35}Lah... yang mana sih?{/cps}"
        pt "{cps=35}Kamu nanya..?{/cps}"
        mc "{cps=35}Ohh iya ada yang kutanya nich{/cps}"
        pt "{cps=35}Apaan tuch..?{/cps}"
        mc "{cps=35}Daritadi kita belum buka buku PR yaa..?{/cps}"
        pt "{cps=35}Ohh iya nih{/cps}"
        pt "{cps=35}Btw kita kan beda sekolah{/cps}"
        mc "{cps=35}Ehh, bener juga tuh{/cps}"
        pt "{cps=35}Yang pasti beda PR kan{/cps}"
        mc "{cps=35}Iya sih....{/cps}"
        mc "{cps=35}Tapi kayaknya kita satu materi{/cps}"
        pt "{cps=35}Hmmmm, Aku sih punya PR di Buku LKS yang ini{/cps}"
        mc "{cps=35}Wahhh.... kalo aku di buku catatan sih, gurunya tiba-tiba ngasih soal{/cps}"
        mc "{cps=35}Tapi karena Jam pelajarannya habis soal yang ini jadi PR waktu itu Put{/cps}"
        pt "{cps=35}Ohh gitu yaa....{/cps}"
        mc "{cps=35}Ehh bentar{/cps}"
        pt "{cps=35}......... . . .{/cps}"
        mc "{cps=35}Soal kita kurang lebih sama deh{/cps}"
        mc "{cps=35}Cuman beda angka doang, jumlah soalnya sama-sama 5 lagi{/cps}"
        pt "{cps=35}Berarti bisa aja sih kita Kerja sama hehe...{/cps}"
        mc "{cps=35}Ahhahahhaha{/cps}"
        stop music fadeout 1.0
        
        show bg blck
        with dissolve
        play music "audio/musikpiano-santai.ogg" fadein 0.5 loop
        sh "{cps=35}Kami pun mulai mengerjakan PR Matematika bersama-sama{/cps}"
        sh "{cps=35}Dengan saling bertanya satu sama lain ketika kebingungan{/cps}"
        sh "{cps=35}Kami pun mengerjakannya dengan sederhana dan sedikit bercanda{/cps}"
        sh "{cps=35}Akhirnya pun tugas kami selesai{/cps}"
        sh "{cps=35}Akan tetapi, ternyata tiba-tiba Ibuku datang dan bertanya {/cps}"
        hide bg blck

        show bg mcHouse
        with dissolve
        ibumc"{cps=35}Udah jam 17:20 nih {/cps}"
        mc "{cps=35}Nah Put, kamu jam segini enggak dimarahin orang rumah kalo pulang{/cps}"
        pt "{cps=35}Udah jam 5 lewat malam aja yaa...{/cps}"
        mc "{cps=35}Iya nih..{/cps}"
        pt "{cps=35}Waduhh... kita kebablasan yaa...{/cps}"
        pt "{cps=35}Untung udah selesai Tugas kita{/cps}"
        mc "{cps=35}Yaudah lah... kamu bisa aja kan sendiri malam gini Put?{/cps}"
        mc "{cps=35}Semoga aman di jalan nihh{/cps}"
        pt "{cps=35}Tenang.....{/cps}"
        ibumc"{cps=35}Jangan lupa mampir lagi yaa Putri{/cps}"
        mcd "{cps=35}Ehh! kaget..., tiba-tiba aja ada Ibu disini"
        pt "{cps=35}Iya Tante{/cps}"
        mc "{cps=35}Dadah Put....{/cps}"
        pt "{cps=35}Dadah [name]....{/cps}"
        mcd "{cps=35}Akhirnya PR selesai juga, habis selesai ngerjain tugas yang lain langsung tidur deh.."
        hide bg mcHouse        
        # buat screen untuk kelanjutan di esok harinya
        stop music fadeout 0.5



        

    label kerumahMcBareng3:
        # show bg mcHouse
        pttm "{cps=25}Boleh kok.... {/cps}"
        pttm "{cps=25}Semoga kita dapat takdir nilai paling tinggi hehehe {/cps}"
        mc "{cps=25}Yang dapat nilai tinggi mah aku sih kayaknya ahhahahahha {/cps}"
        pttm "{cps=25}Daripada debat Siapa yang bakalan dapat nilai tertinggi di Sekolah nanti......{/cps}"
        pttm "{cps=25}Mendingan Siapa yang paling baik dan rutin belajar yang bakalan paling tinggi nilainya nanti gimana? {/cps}"
        mc "{cps=25}Hehe, boleh juga tuh{/cps}"
        mc "{cps=25}Btw langsung aja yok, keburu dapat takdir hujan dijalan ahahahhahah{/cps}"
        pttm "{cps=25}Kalo gitu sini naik Dibelakang{/cps}"
        mc "{cps=25}Oke kakak yang baik hati{/cps}"
        mc "{cps=25}Kayaknya takdir sedang berpihak baik denganku sekarang{/cps}"
        pttm "{cps=25}Yaelah, masih bahas itu juga njir{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahku {/cps}"
        sh "{cps=35}kemudian kami langsung masuk ke ruang tamu, karena kelihatan tidak ada orang di rumah{/cps}"
        hide bg blck
        stop music

        show bg mcHouse
        with slowdissolve
        play music "audio/musik-normal.ogg" fadein 1.5 loop
        mc "{cps=35}Saya pulang!!{/cps}"
        pttm "{cps=35}Wahhhh! rumahmu bagus juga yaa..{/cps}"
        anon "{cps=35}Ada siapa itu?? {/cps}"
        mc "{cps=35}Ohh, ini [name] bawa teman kerumah bu{/cps}"
        ibumc"{cps=35}Ohh gitu{/cps}"
        ibumc"{cps=35}Bawa temanmu duduk dulu tuh [name]{/cps}"
        mc "{cps=35}Iya bu{/cps}"
        ibumc"{cps=35}Kalo gitu Ibu buatkan teh dulu ya..{/cps}"
        pttm "{cps=35}Waduh jadi ngerepotin nih Tante{/cps}"
        mc "{cps=35}Gapapa, udah kebiasaan juga kalo ada tamu{/cps}"
        pttm "{cps=35}Ohh gitu yaa{/cps}"
        mcd "{cps=35}('Kami ngerjain PR nanti dimana yaa?')"
        mcd "{cps=35}('Sepertinya aku akan tanya dia')"
        mc "{cps=35}Ohh iya nih, kita ngerjainnya dimana nih?{/cps}"
        pttm "{cps=35}Hmmm, disini aja deh{/cps}"
        mc "{cps=35}Oke deh{/cps}"
        ibumc"{cps=35}Ini tehnya diminum dulu{/cps}"
        pttm "{cps=35}Ohh, iya Tante{/cps}"
        ibumc"{cps=35}Ohh iya, namamu siapa ya..?{/cps}"
        mcd "{cps=35}('!!')"
        mcd "{cps=35}('Aku lupa juga nanyain nama dia ternyata dari tadi')"
        pttm "{cps=35}Nama saya Putri Tante{/cps}"
        ibumc"{cps=35}Oalah...{/cps}"
        mc "{cps=35}Baru ingat aku{/cps}"
        pt "{cps=35}Kenapa tuh?{/cps}"
        mc "{cps=35}Dari tadi belum nanya nama kamu nih Put{/cps}"
        pt "{cps=35}Nahh, betul juga tuh{/cps}"
        mc "{cps=35}Ayo buka buku Put{/cps}"
        pt "{cps=35}Siap{/cps}"
        ibumc"{cps=35}Kalo gitu ibu ke kamar dulu yaa [name]{/cps}"
        ibumc"{cps=35}Yang semangat ngerjainnya{/cps}"
        mc "{cps=35}Oke Bu...{/cps}"
        " " "{cps=35}Ibuku pun langsung pergi ke kamar, dan kami tinggal berdua {/cps}"
        pt "{cps=35}Btw kita kan beda sekolah{/cps}"
        mc "{cps=35}Ehh, bener juga tuh{/cps}"
        pt "{cps=35}Yang pasti beda PR kan{/cps}"
        mc "{cps=35}Iya sih....{/cps}"
        mc "{cps=35}Tapi kayaknya kita satu materi{/cps}"
        pt "{cps=35}Hmmmm, Aku sih punya PR di Buku LKS yang ini{/cps}"
        mc "{cps=35}Wahhh.... kalo aku di buku catatan sih, dikasih gurunya langsung soal{/cps}"
        mc "{cps=35}Tapi karena Jam pelajarannya habis soal yang ini jadi PR{/cps}"
        pt "{cps=35}Ohh gitu yaa....{/cps}"
        mc "{cps=35}Ehh bentar{/cps}"
        pt "{cps=35}!!{/cps}"
        mc "{cps=35}Soal kita kurang lebih sama deh{/cps}"
        mc "{cps=35}Cuman beda angka doang, jumlah soalnya sama-sama 5 lagi{/cps}"
        pt "{cps=35}Berarti bisa aja sih kita Kerja sama hehe...{/cps}"
        mc "{cps=35}Ahhahahhaha{/cps}"
        stop music fadeout 1.0
        
        play music "audio/musikpiano-santai.ogg" fadein 0.5 loop
        show bg blck
        with dissolve
        sh "{cps=35}Kami pun mulai mengerjakan PR Matematika bersama-sama{/cps}"
        sh "{cps=35}Dengan saling bertanya satu sama lain ketika kebingungan{/cps}"
        sh "{cps=35}Kami pun selesai mengerjakannya dengan puas{/cps}"
        sh "{cps=35}Dalam sisa waktu yang kami habiskan sebelum hari menjelang malam{/cps}"
        sh "{cps=35}Tanpa kami sadari waktu pun berlalu setelah kami baru saja selesai mengerjakan PR kami{/cps}"
        hide bg blck

        show bg mcHouse
        with dissolve
        mc "{cps=35}Nah Put, kamu jam segini enggak dimarahin orang rumah kalo pulang{/cps}"
        pt "{cps=35}Udah jam 05:12 aja yaa...{/cps}"
        mc "{cps=35}Iya nih..{/cps}"
        pt "{cps=35}Boleh aja sih asalkan sebelum menjelang malam{/cps}"
        mc "{cps=35}Ohh gitu{/cps}"
        pt "{cps=35}Kalo gitu aku Pamit yaa{/cps}"
        mc "{cps=35}Oke Put{/cps}"
        ibumc"{cps=35}Jangan lupa mampir lagi yaa Putri{/cps}"
        mcd "{cps=35}Ehh! kaget..., tiba-tiba aja ada Ibu disini"
        pt "{cps=35}Iya Tante{/cps}"
        mc "{cps=35}Dadah Put....{/cps}"
        pt "{cps=35}Dadah [name]....{/cps}"
        mcd "{cps=35}Akhirnya PR Mtk selesai juga, tinggal kerjain yang lain aja deh terus tidur"
        hide bg mcHouse
        stop music fadeout 0.5
        # buat screen untuk kelanjutan di esok harinya




#Bagian Kerumah Temen Bareng
# Bagian ini berisi alur utama yg dimana mc bakalan main dengan teman disampingnya yaitu si putri. Dan untuk next  part atau bab nanti mereka bakalan sering ketemu karena mc sering main kerumahnya
    label kerumahTemenBareng1:

#  KHUSUS label ini terdapat pembicaraan mc dengan ortu teman yg duduk disampingnya, yaitu si putri. jadi, Khusus dibagian ini mereka gaakan main bareng. Serta, Putri bakalan didukung untuk memilih jalan hidupnya nanti saat lulus

        pttm "{cps=25}Tapi...... kamu yakin? {/cps}"
        mc "{cps=25}Yakin sih, udah pernah juga masalahnya ngehadapin kek gituan{/cps}"
        pttm "{cps=25}Ohh, gitu.....{/cps}"
        mc "{cps=25}Btw rumah kamu jauh nggak?{/cps}"
        pttm "{cps=25}Lumayan juga sih, sekitar 2 km dari sini{/cps}"
        mc "{cps=25}Kalo gitu aku boleh ikut dibelakangmu nggak?{/cps}"
        pttm "{cps=25}Boleh banget kok, lagian aku kagak tega juga ngeliat temen yang pengen bantu aku tapi aku nggak support dia.{/cps}"
        mc "{cps=25}Nah.. mending kita langsung aja kalo gitu kerumahmu nih, keburu lama{/cps}"
        mc "{cps=25}Hati-hati yaa.....{/cps}"
        pttm "{cps=25}Oke........{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        play music "audio/musikpiano-santai.ogg" fadein 0.3 loop
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin dia sedang memikirkan bagaimana pembicaraan kami nanti dengan orang tuanya{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahnya {/cps}"
        sh "{cps=35}kemudian dia mengetok pintu dan langsung masuk ke ruang tamu{/cps}"
        sh "{cps=35}Aku pun juga ikut masuk kedalam{/cps}"
        hide bg blck
        stop music fadeout 0.5

# Akan terjadi penjelasan kepada Ibunya dahulu kemudian ayahnya karena belum pulang kerja. Kemudian untuk cara menjelaskannya berbeda karena Ibu butuh perasaan kemudan Ayah butuh logika.
        show bg temenHouse
        with slowdissolve
        play music "audio/musik-cafe.ogg" fadein 0.5 loop
        pttm "{cps=25}Kita sampai nih [name].....{/cps}"
        mc "{cps=25}Lumayan sihh rumahmu{/cps}"
        pttm "{cps=25}Biasa aja sih....{/cps}"
        mc "{cps=25}Setidaknya layak untuk dihuni di zaman sekarang{/cps}"
        stop music
        play sound "audio/bell-ding.ogg"
        anon "{cps=25}ADA SIAPA ITU!!?{/cps}"
        # tambahkan lagu yang bikin thriller kaya backsound ace attorney 
        mcd "{cps=25}Siapa yang berteriak ya?{/cps}"
        pttm "{cps=25}Ini Putri Pah...{/cps}"
        mcd "{cps=25}ehh!? Putri......?{/cps}"
        ibuputri "{cps=25}Kamu dengan Siapa itu?{/cps}"
        pt "{cps=25}Sama [name] Mah teman lama Putri yang itu...{/cps}"        
        ibuputri "{cps=25}Oh.., Ibu tidak kenal{/cps}"
        mcd "{cps=25}Sepertinya Ibunya Putri ini dingin sekali{/cps}"
        ibuputri "{cps=25}Mau apa kamu sama dia disini?{/cps}"
        mcd "{cps=25}Hmmmmm, apakah aku yang harus menjelaskannya?{/cps}"

    menu : 
        "Jelaskan dengan lantang dan jujur" :
            jump debatIbuPutri1
        
        "Jelaskan dengan santun dan sopan, tapi menggunakan kata sindiran untuk hal sensitif" :
            jump debatIbuPutri2
        
        "Biarkan Putri yang menjelaskan sambil temani" :
            jump debatIbuPutri3

    label debatIbuPutri1:

    label debatIbuPutri2:

    label debatIbuPutri3:
    

    label kerumahTemenBareng21:
        # show bg temenHouse
        pttm "{cps=25}Bisa aja sih, sekalian liat-liat kalo ada cowok ganteng dijalan {/cps}"
        mc "{cps=25}Kalo gitu, tanpa basa basi langsung aja ngab{/cps}"
        pttm "{cps=25}Oke, kamu jalan kaki aja yaa...{/cps}"
        mc "{cps=25}Gampang.....{/cps}"
        mc "{cps=25}Aku sering jogging juga disekitar sini tiap minggu{/cps}"
        pttm "{cps=25}Ohh iya, jangan-jangan rumahmu dekat sini makanya kamu milih jalan aja{/cps}"
        mc "{cps=25}Nggak juga deng{/cps}"
        pttm "{cps=25}Yaudah nih malah entar lama disini, kita langsung cus aja{/cps}"
        mc "{cps=25}Oke{/cps}"
        
        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena fokus kami terahlihkan melihat orang-orang di jalan pulang{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahnya {/cps}"
        sh "{cps=35}kemudian dia mengetok pintu dan langsung masuk ke ruang tamu{/cps}"
        sh "{cps=35}Aku pun juga ikut masuk kedalam{/cps}"
        hide bg blck

        show bg temenHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}"
        

    label kerumahTemenBareng22:
        # show bg temenHouse
        pttm "{cps=25}Bebas aja sih, kalo mau ikut sepedaku sini{/cps}"
        mc "{cps=25}Oke, btw langsung aja nih? {/cps}"
        pttm "{cps=25}Ya iyalah, entar kelamaan Kita disini{/cps}"
        mc "{cps=25}Liat-liat ya kalo ada cowok yang vibenya mirip gue{/cps}"
        pttm "{cps=25}Oke deh{/cps}"
        mc "{cps=25}KITA TEROBOSSS!!!!!!!{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena fokus kami terahlihkan melihat orang-orang di jalan pulang{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahnya {/cps}"
        sh "{cps=35}kemudian dia mengetok pintu dan langsung masuk ke ruang tamu{/cps}"
        sh "{cps=35}Aku pun juga ikut masuk kedalam{/cps}"
        hide bg blck

        show bg temenHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}"

    label kerumahTemenBareng23:
        # show bg temenHouse
        pttm "{cps=25}Santai aja loh, lagian kita paling-paling ngerjain PR doang kan{/cps}"
        mc "{cps=25}Iya, paling gitu doang sih {/cps}"
        mc "{cps=25}Btw, kamu kenal nggak cowok yang kayak tipeku tadi?{/cps}"
        pttm "{cps=25}Banyak cowo yang pernah kamu liat pake mata itu emangnya mereka kalo pengen pacaran gamau ceweknya hepi gituh?{/cps}"
        mc "{cps=25}Hmmmm, iya juga sih{/cps}"
        pttm "{cps=25}Berarti banyak banget yang bisa kamu pilih atuh{/cps}"
        pttm "{cps=25}Yaudah nih, langsung aja naik sepedaku biar ga banyak bacot{/cps}"
        mc "{cps=25}Dih, iyain deh{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena fokus kami terahlihkan melihat orang-orang di jalan pulang{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahnya {/cps}"
        sh "{cps=35}kemudian dia mengetok pintu dan langsung masuk ke ruang tamu{/cps}"
        sh "{cps=35}Aku pun juga ikut masuk kedalam{/cps}"
        hide bg blck

        show bg temenHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}"


    label kerumahTemenBareng3:
        # show bg temenHouse
        pttm "{cps=25}Boleh kok, jarang-jarang juga temenku yang mau main kerumahku {/cps}"
        mc "{cps=25}Emangnya kenapa? {/cps}"
        pttm "{cps=25}Gua termasuk Introvert mah orangnya, jadi ga punya banyak temen kek lu sih{/cps}"
        mc "{cps=25}Ohh iya ya... lupa gue{/cps}"
        pttm "{cps=25}Jadi gimana nih? jadi kan?{/cps}"
        mc "{cps=25}Jelas dong...{/cps}"
        pttm "{cps=25}Oke nih, kebetulan Rumahku agak jauh, jadi naik dibelakang Sepedaku aja [name]{/cps}"
        mc "{cps=25}Ohh, ok kalo begitu{/cps}"
        pttm "{cps=25}Aku pengen membalas terimakasih juga{/cps}"
        pttm "{cps=25}Sini cepetan naik, entar malah lama{/cps}"
        pttm "{cps=25}Kan banyak juga tuh orang bilang 'Time is Money' {/cps}"
        mc "{cps=25}Waktu itu emas sih menurutku{/cps}"
        pttm "{cps=25}Yahh.... kurang lebih kalo gitu{/cps}"
        pttm "{cps=25}Btw udah siap?{/cps}"
        mc "{cps=25}Siap salah!{/cps}"
        pttm "{cps=25}Ahahhahahha....{/cps}"
        
        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=35}Di perjalanan kami berdua terdiam entah kenapa{/cps}"
        sh "{cps=35}Menurutku mungkin karena fokus kami terahlihkan melihat orang-orang di jalan pulang{/cps}"
        sh "{cps=35}Setelah beberapa waktu sampai sekarang, perjalanan kami dari tempat duduk umum pun berakhir {/cps}"
        sh "{cps=25}Kami berdua pun sampai di rumahnya {/cps}"
        sh "{cps=35}kemudian dia mengetok pintu dan langsung masuk ke ruang tamu{/cps}"
        sh "{cps=35}Aku pun juga ikut masuk kedalam{/cps}"
        hide bg blck

        show bg temenHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}"


#Bagian Pulang Sendiri-sendiri 
# Bagian ini akan berisi alur utama yang dimana si mc dan temannya pulang kerumah masing masing dikarenakan ada urusan atau kesibukan mereka sendiri sendiri yang dimana nanti si mc bakal tetap ngerjain pr mtk nya. Dan untuk next bab atau part nanti, mereka bakalan ketemu lagi nggak sengaja karena lupa minta kontak, jadi akan ada perbedaan alur cerita di waktu yang sama tapi mereka akan berpisah sementara dengan saling mengucapkan nama diakhir
    label pulangSendiri_sendiri1:
        # show bg mcHouse
        pttm "{cps=25}Oalah, gituu........{/cps}"
        pttm "{cps=25}Iya-iya, aku juga sih{/cps}"
        mc "{cps=25}Dadah...!!{/cps}"
        pttm "{cps=25}Dahhhh.....!!{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=25}Pada akhirnya kami pulang kerumah masing-masing{/cps}"
        sh "{cps=25}Dan aku pun juga lupa bertanya namanya {/cps}"
        sh "{cps=25}Setelah menempuh beberapa waktu{/cps}"
        sh "{cps=25}Aku pun sampai dirumahku sendiri{/cps}"
        hide bg blck

        show bg mcHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}" 

    label pulangSendiri_sendiri21:
        # show bg mcHouse
        pttm "{cps=25}Oalah, gituu........{/cps}"
        pttm "{cps=25}Iya-iya, aku juga sih{/cps}"
        mc "{cps=25}Dadah...!!{/cps}"
        pttm "{cps=25}Dahhhh.....!!{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=25}Pada akhirnya kami pulang kerumah masing-masing{/cps}"
        sh "{cps=25}Aku berjalan sambil melihat orang-orang sekitar{/cps}"
        sh "{cps=25}Dan aku pun juga lupa bertanya namanya ternyata{/cps}"
        sh "{cps=25}Setelah menempuh beberapa waktu{/cps}"
        sh "{cps=25}Aku pun sampai dirumahku sendiri{/cps}"
        hide bg blck

        show bg mcHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}" 
        
    label pulangSendiri_sendiri22:
        # show bg mcHouse
        pttm "{cps=25}Oalah, gituu........{/cps}"
        pttm "{cps=25}Iya-iya, aku juga sih{/cps}"
        mc "{cps=25}Dadah...!!{/cps}"
        pttm "{cps=25}Dahhhh.....!!{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=25}Pada akhirnya kami pulang kerumah masing-masing{/cps}"
        sh "{cps=25}Aku berjalan sambil melihat orang-orang sekitar{/cps}"
        sh "{cps=25}Dan aku pun juga lupa bertanya namanya ternyata{/cps}"
        sh "{cps=25}Setelah menempuh beberapa waktu{/cps}"
        sh "{cps=25}Aku pun sampai dirumahku sendiri{/cps}"
        hide bg blck

        show bg mcHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}" 
        
    label pulangSendiri_sendiri23:
        # show bg mcHouse
        pttm "{cps=25}Oalah, gituu........{/cps}"
        pttm "{cps=25}Iya-iya, aku juga sih{/cps}"
        mc "{cps=25}Dadah...!!{/cps}"
        pttm "{cps=25}Dahhhh.....!!{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=25}Pada akhirnya kami pulang kerumah masing-masing{/cps}"
        sh "{cps=25}Aku berjalan sambil melihat orang-orang sekitar{/cps}"
        sh "{cps=25}Dan aku pun juga lupa bertanya namanya ternyata{/cps}"
        sh "{cps=25}Setelah menempuh beberapa waktu{/cps}"
        sh "{cps=25}Aku pun sampai dirumahku sendiri{/cps}"
        hide bg blck

        show bg mcHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}" 

    label pulangSendiri_sendiri3:
        # show bg mcHouse
        pttm "{cps=25}Oalah, gituu........{/cps}"
        pttm "{cps=25}Iya-iya, aku juga sih{/cps}"
        mc "{cps=25}Dadah...!!{/cps}"
        pttm "{cps=25}Dahhhh.....!!{/cps}"

        hide bg jett
        stop music fadeout 2.3

        show bg blck
        with dissolve
        sh "{cps=25}Pada akhirnya kami pulang kerumah masing-masing{/cps}"
        sh "{cps=25}Dan Aku pun juga lupa bertanya namanya {/cps}"
        sh "{cps=25}Aku pun berpikir bahwa takdir membuatku lupa bertanya namanya{/cps}"
        sh "{cps=25}Setelah menempuh beberapa waktu{/cps}"
        sh "{cps=25}Aku pun sampai dirumahku sendiri{/cps}"
        hide bg blck

        show bg mcHouse
        with slowdissolve
        mc "{cps=25}asasas {/cps}" 


    return



#    STORY  L



    label enter_l:
        hide screen Nama
        
        show bg blck
        show screen bab1_l
        with dissolve

        pause 1.0

        show screen prologue_text
        with dissolve

        window hide
        sh ""
         
        hide bg blck
        hide screen bab1_l
        hide screen prologue_text

        
        #show bg cty
        with slowdissolve
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

    window hide

    show bg blck
    show screen chapter_1
    with dissolve

    pause 1.0

    show screen jdl_chpt1_l
    with dissolve

    window hide
    sh ""

    hide bg blck
    hide screen chapter_1
    hide screen jdl_chpt1_l
    
    #show bg schl
    with slowdissolve
    mc "Jadi ini sekolahnya?"
    mc "Berapa lama aku pergi sehingga sekolah ini terlihat berbeda"
    mc "Terakhir kali aku di kota ini waktu aku masih kecil"
    mc "Banyak sekali yang berbeda termasuk sekolah ini"
    mc "Aku belum pernah masuk ke dalamnya sih waktu aku masih kecil"
    mc "Siapa peduli"
    mc "Aku akan menepati janjiku"
    #show bg side_schl


    return
