# Characters
define f = Character("Fran")
define p = Character("Paola")
define fe = Character("Federico")
define g = Character("Gianni")
define e = Character("Erica")


# ==========================
# SALA0
# ==========================

# Ticket
define ticket = False

# Collections
default voices_of_music = {
    "harp": False,
    "rectangular_pianoforte": False,
    "tromba_marina": False,
    "archlute": False,
    "disc": False,
    "violin": False,
    "piano": False,
    "woodwinds": False,
    "french_horn": False
}


# ==========================
# SALA1
# ==========================

# Harp
define harp_sound_index = 0
define harp_unlock = False

# Music volume
$ renpy.music.set_volume(0.5, channel='music')

# ==========================
# SALA3
# ==========================
default sala3_found_keyhole = False
default sala3_have_key = False
default sala3_bach_solved = False
default sala3_mozart_solved = False 
default sala3_unlocked_sala4 = False
default statue_information = False

# piano1
default sala3_piano_sound_index = 0
default sala3_piano_unlocked = False

# ==========================
# SALA4
# ==========================

# tromba marina
default sala4_tromba_play_count = 0
default sala4_tromba_unlocked = False

# if talked with gianni
default sala4_met_gianni = False

# ==========================
# SALA5
# ==========================

# archlute
default sala5_archlute_play_count = 0
define sala5_archlute_unlocked   = False

# ==========================
# SALA6
# ==========================

# disc
default sala6_disc_play_count = 0
define sala6_disc_unlocked = False
define sala6_farinelli_puzzle_solved = False

# ==========================
# SALA7
# ==========================

# piano2
default sala7_piano_play_count = 0
default sala7_piano_unlocked   = False
default sala7_piano_quiz_solved = False
default sala7_finished          = False

# ==========================
# SALA8
# ==========================
default sala8_seen_backcase = False
default sala8_seen_frontcase = False
default sala8_puzzle_solved = False
default sala8_violin_play_count = 0
default sala8_violin_unlocked = False
default sala8_woodwinds_play_count = 0
default sala8_woodwinds_unlocked = False
default sala8_horns_play_count = 0
default sala8_horns_unlocked = False

# ==========================
# SALA9
# ==========================

default sala9_step_1 = False
default sala9_step_2 = False
default sala9_puzzle_done = False


#===================GAME START======================

# =========================================
# SALA0 dream
# =========================================

label start:
    scene black

    narrator "Across {color=#c28b61}Bologna{/color}, fragments of forgotten {color=#f788c0}Voices of Music{/color} lie scattered."
    narrator "Only when you truly hear them does the city reveal its most beautiful side."

    play music "Whispering Realms.mp3" fadein 3.0
    play sound "rain.mp3" loop fadein 3.0

    show fran_half at center
    with dissolve

    f "…Where am I?"
    f "I can’t see anything. Just rain… and a melody."

    hide fran_half
    with dissolve

    narrator "{color=#c28b61}Bologna{/color} has been a city you can “hear” for centuries."
    narrator "Sounds from churches, theatres, and students playing in the streets slowly gathered into a single {color=#c28b61}house of music{/color}."
    narrator "In that place, portraits whisper stories of the past, and instruments remember whose hands once played them."

    show fran_half at center
    with dissolve

    f "You mean… the {color=#c28b61}Music Museum{/color}?"
    f "And those {color=#f788c0}Voices of Music{/color} you mentioned—what exactly are they?"

    hide fran_half
    with dissolve

    narrator "{color=#c28b61}Nine rooms{/color}."
    narrator "In each one, a small fragment of a broken {color=#f788c0}Voice of Music{/color} may be hidden…"
    narrator "among instruments, manuscripts, portraits, and memories."

    narrator "When you piece them back together,"
    narrator "the music will tell you—"

    show fran_half at center
    with dissolve

    f "…"
    f "Tell me how to reach that place?"

    hide fran_half
    with dissolve

    narrator "When you open your eyes…"
    narrator "follow the streets."
    narrator "The city will guide you there."

    show fran_half at center
    with dissolve

    f "Wait—who are you?"
    f "Someone from this city, or…?"

    hide fran_half
    with dissolve

    narrator "The name doesn’t matter."
    narrator "What matters is whether you choose to {color=#f788c0}listen{/color}."

    $ renpy.pause(2.0, hard=False)

    narrator "Now… wake up."

    play music "Dream_Quiet_Rain_iRelax_Ent.mp3" fadein 3.0
    scene bedroom with fade
    show fran_half at center
    with dissolve

    f "…Ugh… my head."
    f "That dream again. The same rain, the same melody."

    f "A voice I can’t identify,"
    f "and those scattered {color=#f788c0}Voices of Music{/color}…"

    hide fran_half
    with dissolve

    f "Whatever. I should get up."
    f "Hm? What’s this?"

    play sound "drawer_open.mp3"
    $ renpy.pause(2.0, hard=False)

    f "Something’s inside the drawer…"

    play sound "paper.mp3"
    $ renpy.pause(0.5, hard=False)

    show ticket on table_small1 at Position(xalign=0.5, yalign=0.5)
    with dissolve

    f "…A ticket? When did this—"

    menu:
        "Check the back of the ticket":
            pass

    hide ticket on table_small1
    with dissolve

    show ticket on table_small2 at Position(xalign=0.5, yalign=0.5)
    with dissolve

    f "A {color=#c28b61}ticket{/color}…"
    f "It says: {color=#c28b61}“Museo internazionale e biblioteca della musica di Bologna”{/color}."

    f "If the dream means anything, the key must be there."

    menu:
        "Put the ticket away":
            $ ticket = True
            f "Might be useful later."
        "Leave it where it was":
            f "Feels strange… maybe I shouldn’t take it yet."

    hide ticket on table_small2
    with dissolve

    show fran_half at center
    with dissolve

    f "A {color=#c28b61}music museum{/color}."
    f "Nine rooms."
    f "And those {color=#f788c0}Voices of Music{/color} the dream mentioned…"
    f "What exactly am I going to find?"

    hide fran_half
    with dissolve

    menu:
        "Get dressed and head out":
            pass

    stop music fadeout 3.0
    stop sound fadeout 3.0

    scene black with fade
    play sound "door.wav"
    $ renpy.pause(1.0, hard=False)

    jump bologna_city


# =========================================
# SALA0 Street
# =========================================

label bologna_city:
    scene black with fade
    $ renpy.pause(1.0, hard=False)

    play sound "outside.mp3" fadein 3.0
    play music "street.mp3" fadein 3.0

    scene bologna1 with fade
    $ renpy.pause(1.0, hard=False)

    narrator "Evening in Bologna. Under the arcades, the lights flow like a slow, golden river."

    show fran_half at center
    with dissolve

    f "So this is Bologna…"
    f "The city feels alive. Not just people—something older, like echoes inside the bricks."

    f "The ticket says {color=#c28b61}“Strada Maggiore, 34”{/color}."
    f "If the dream was real, the {color=#f788c0}Voices of Music{/color} must be inside."

    hide fran_half
    with dissolve

    scene black with fade
    $ renpy.pause(2.0, hard=False)

    scene bologna2 with fade
    show fran_half at center
    with dissolve

    f "{color=#c28b61}Piazza Maggiore{/color}."
    f "People have listened to music here for centuries—"
    f "public concerts, church choirs, students playing on corners."
    f "If the whole city were an instrument, the museum would be its memory."

    hide fran_half
    with dissolve

    scene black
    with dissolve
    $ renpy.pause(2.0, hard=False)

    scene bologna3 with dissolve
    show fran_half at center
    with dissolve

    f "{color=#c28b61}Strada Maggiore{/color}… It should be this street."
    f "Number 34…"

    narrator "Through the tall windows, faint music seems to drift from within."

    f "This is it. The {color=#c28b61}Music Museum of Bologna{/color}."

    stop music fadeout 3.0
    stop sound fadeout 3.0

    hide fran_half
    with dissolve

    scene black with fade
    jump ticketOffice


# =========================================
# SALA0 entrance
# =========================================

label ticketOffice:
    scene black with fade
    scene ticketoffice with fade
    play music "TicketOffice - Frulingsstimmen Walzer.mp3" fadein 3.0 loop

    narrator "The entrance hall is warm and calm. Soft light, cheerful music—like being wrapped in sound."

    show fran_half at left
    with dissolve

    f "It’s beautiful…"
    f "Feels like music is still alive in the air."

    show paola_half at right
    with dissolve

    p "Good evening! Welcome to the {color=#c28b61}Music Museum of Bologna{/color}."
    p "I’m Paola. How can I help you?"

    f "Good evening. I’m Fran. I’d like to visit the museum."

    p "Of course. Do you have a {color=#c28b61}ticket{/color}?"

    if ticket:
        f "Yes, right here."
        show ticket on table_small2 at Position(xalign=0.5, yalign=0.5)
        with dissolve

        p "Let me check…"
        $ renpy.pause(2.0)
        p "Welcome!"
        hide ticket on table_small2
        with dissolve
    else:
        f "Ah—I forgot it in the drawer."
        p "No worries. You’re lucky—students enter for free today."
        show ticket on table_small2 at Position(xalign=0.5, yalign=0.5)
        with dissolve
        p "Here’s your {color=#c28b61}ticket{/color}."
        $ ticket = True
        hide ticket on table_small2
        with dissolve

    show booklet on table_small at Position(xalign=0.5, yalign=0.5)
    with dissolve

    p "And this is your {color=#c28b61}guidebook{/color}."
    p "It contains the map of all nine rooms and a short introduction to Bologna’s musical history."

    menu:
        "Pick up the guidebook":
            f "Thanks."
            menu:
                "Open it":
                    hide booklet on table_small
                    with dissolve
                    show leaflet at Position(xalign=0.5, yalign=0.5)
                    with dissolve
                "Put it away":
                    hide booklet on table_small
                    with dissolve
                    pass

    hide booklet on table_small
    with dissolve
  
    p "The exhibition rooms are upstairs. Just follow the staircase—you’ll see the first map right away."

    f "Thank you, Paola."

    p "You’re welcome. And if you ever feel lost, check your {color=#c28b61}guidebook{/color}."
    p "And… if you’re willing to listen carefully, the museum might just answer you."

    hide paola_half
    hide fran_half
    with dissolve

    stop music fadeout 3.0

    jump entrance


# =========================================
# SALA0 stairs
# =========================================

label entrance:
    scene entrance1 with fade
    play music "Entrance - Il zabaione musicale Act I Prologo l'Humor spensierato.mp3" fadein 3.0 loop

    narrator "The staircase leading upward glows softly."

    show fran_half
    with dissolve

    f "With music playing like this… it’s hard not to feel nervous."

    scene entrance2 with fade
    show fran_half
    with dissolve

    f "Almost there. Let’s keep going."
    f "If the dream was real, the {color=#f788c0}Voices of Music{/color} must be behind these doors."

    hide fran_half
    with dissolve

    scene map1 with fade
    show fran_half at left
    with dissolve

    f "This must be the museum map."

    hide fran_half
    with dissolve

    pause

    show map2 at Position(xalign=1.0, yalign=0.0)
    with dissolve

    narrator "The guidebook lists ten main sections:"
    narrator "1. Introduction to the museum itinerary"
    narrator "2. Friar Giambattista Martini"
    narrator "3. Father Martini’s friends"
    narrator "4. The idea of music"
    narrator "5. Books on music and instruments — 16th and 17th centuries"
    narrator "6. Farinelli and Italian opera in the 18th century"
    narrator "7. Gioachino Rossini and opera in the 19th century"
    narrator "8. Books on music and instruments — 18th and 19th centuries"
    narrator "9. Between the 19th and 20th centuries: Martucci and Respighi"
    narrator "10. Musicians and musical life in Bolognese institutions"

    show fran_half
    with dissolve

    f "Nine rooms… exactly like in the dream."
    f "Let’s start with the first one."

    f "The entrance should be on the left."

    hide fran_half
    with dissolve

    stop music fadeout 3.0

    jump sala1


# =========================================
# SALA1
# =========================================

label sala1:
    scene black with fade
    scene entrance3 with fade
    play music "SALA1 - L Orfeo_ Toccata.mp3" fadein 3.0 loop

    show federico_half at right
    with dissolve

    fe "Hello, and welcome to the Music Museum of Bologna."
    fe "I’m Federico. I’ll guide you from the {color=#c28b61}first room{/color} to the {color=#c28b61}fifth room{/color}."

    show fran_half at left
    with dissolve

    f "Hi, I’m Fran."
    f "The atmosphere here… really isn’t like outside. It feels like I stepped out of the street into a different world."

    fe "In a way, you did."
    fe "This palace is called {i}Palazzo Sanguinetti{/i}. It began life as a noble residence in the sixteenth century."

    fe "In 1986 it was left to the city by its last owner, {color=#c28b61}Eleonora Sanguinetti{/color}."
    fe "After years of restoration, the frescoes were uncovered again, and in 2004 the museum finally opened to the public."

    f "So we’re not in a neutral exhibition space at all, but in a house that already comes with its own history."

    fe "Exactly."
    fe "From the staircase you came up, those trompe-l’oeil effects you saw are by {color=#c28b61}Luigi Busatti{/color} and {color=#c28b61}Francesco Santini{/color}."
    fe "They turned the climb up to the {i}piano nobile{/i}—the main floor—into a kind of visual stage entrance."

    scene sala1 with fade

    show federico_half at right
    with dissolve

    fe "The room we’re standing in now is known as the {i}Boscareccia{/i}, the “garden room”."
    fe "The forest landscapes on the walls are by {color=#c28b61}Vincenzo Martinelli{/color},"
    fe "and the sculptures of Bacchus and Ceres were made in the early career of {color=#c28b61}Pelagio Palagi{/color}."

    show fran_half at left
    with dissolve

    f "No wonder it feels like being surrounded by stage scenery…"
    f "It’s like standing at the centre of a stage, with a painted forest all around."

    fe "That’s exactly the idea."
    fe "This room works like a prologue to the museum—"
    fe "an imaginary woodland that leads you out of everyday life into a space devoted to music."

    fe "Here, the museum wants to pose a first question:"
    fe "what is music, really?"

    fe "Music is a curious kind of invention."
    fe "It lets you step out of time ruled by clocks and schedules,"
    fe "and into a time governed by {color=#c28b61}emotion{/color}—"
    fe "a time that belongs to myth, but is still tied to history."

    f "So when we listen to music,"
    f "we’re not just hearing a line of notes—we’re briefly living in another kind of time."

    fe "You could put it that way."
    fe "But music has an awkward side: once the sound stops, nothing material is left."

    fe "So if we want to understand music of the past, we have to rely on {color=#c28b61}fragile material traces{/color}."

    fe "Scores, theoretical treatises, the instruments themselves, even the portraits and frescoes on the walls."
    fe "None of these are music in themselves, yet they’re the only clues music has left behind."

    f "It’s a bit like trying to get to know someone who’s gone, just from their letters, photos, and furniture."

    fe "That’s a very good comparison."
    fe "And for these clues to really “speak”, someone has to collect them, preserve them, catalogue them, interpret them, and give them value again."

    fe "That’s a theme you’ll keep running into in the next few rooms."

    fe "As for the pieces of music themselves, they’re not like a painting or a building."
    fe "The canvas and the wall are already the work of art."
    fe "A poem can at least be fixed on a page."

    fe "Music, if it’s to be recorded, has to lean on many different sources—"
    fe "scores, manuscripts, theoretical books, instruments, eyewitness accounts in words…"
    fe "Each is important, but none of them alone can stand in for “the music itself”."

    show fran_half at left
    with dissolve

    f "So this room is basically reminding us that everything we’re about to see"
    f "is circling around sounds that have already vanished."

    fe "Exactly."
    fe "And among them, a few things may line up quietly with those {color=#f788c0}fragments of sound{/color} from your dream."

    fe "For example, take a look at that harp over there."

    f "That harp…"
    f "It feels strangely familiar, like I’ve seen it in the dream."

    fe "Go closer."
    fe "If you like, you can also listen to the sound it once made."

    menu harp:
        "Walk up to the harp and take a closer look":
            scene harp with fade
            show fran_half with dissolve
            f "Up close, every string, every line of the wood is so clear."
            f "It feels as if it’s holding its breath, waiting for someone to play it again."
            hide fran_half with dissolve

            menu harp_closer:
                "Play a short phrase on the harp" if harp_sound_index < 6:
                    stop music fadeout 2.0
                    $ harp_sound_index += 1
                    play sound f"./harp/{harp_sound_index}.mp3"
                    show fran_half with dissolve
                    if harp_unlock == False:
                        f "This sound… warm and clear."
                        f "For a moment I’m sure I’ve heard it somewhere before."
                    else:
                        f "It’s so beautiful it feels like it goes straight into my chest."
                    hide fran_half with dissolve
                    stop sound fadeout 2.0
                    play music "SALA1 - L Orfeo_ Toccata.mp3" fadein 3.0 loop
                    jump harp_closer

                "{color=#c28b61}This must be one of the Voices of Music from the dream{/color}" if harp_sound_index >= 2 and harp_unlock == False:
                    show fran_half with dissolve
                    f "Wait… this timbre…"
                    f "I’m sure of it. This harp is one of those {color=#f788c0}Voices of Music{/color} from my dream."
                    $ voices_of_music["harp"] = True
                    $ harp_unlock = True
                    narrator "You unlocked a new {color=#f788c0}Voice of Music{/color}: the harp."
                    hide fran_half with dissolve
                    scene sala1 with fade
                "Step back and look from a distance":
                    scene sala1 with fade
                    jump harp
        "Talk with Federico":
            scene sala1 with fade
            pass

    $ harp_sound_index = 0

    show federico_half at right
    with dissolve

    fe "The harp is beautiful, isn’t it?"

    show fran_half at left
    with dissolve

    f "And this room is full of fragments like that…"
    f "Scores, portraits, instruments… It’s like a table covered in puzzle pieces."

    fe "That’s what this part of the museum is trying to do."
    fe "Unlike a painting or a building, music is spread across many different physical forms."
    fe "None of them can stand alone for all of music."

    fe "So we need someone like you to walk from the first room to the last,"
    fe "and quietly link everything together in your mind."

    f "So if I keep going from room to room…"
    f "it’s like slowly recovering those lost sounds from their fragments."

    fe "Exactly."
    fe "When you’re ready, we’ll move on to the {color=#c28b61}second room{/color}."

    menu:
        "Go to the second room":
            hide federico_half
            hide fran_half
            with dissolve
            jump sala2
        "Stay here a bit longer":
            f "I’d like to stay here a little longer and get a feel for the room."
            fe "Of course. I’ll be waiting for you up ahead when you’re ready."
            hide federico_half
            hide fran_half
            with dissolve
            jump harp


# =========================================
# SALA2
# =========================================

label sala2:

    play music "SALA2 - G.B. Martini La Gnudi La Misarelli.mp3" fadein 2.0 loop

    scene sala2 with fade

    narrator "You step into the second room. In front of you hangs a round portrait on a beige wall, flanked by long frescoes. In the display cases, heavy scores and books lie open under the light."

    show federico_half at right
    show fran_half at left
    with dissolve

    fe "This is the second room."
    fe "From here on, you’ll really get to know the key figure behind this museum: {color=#c28b61}Father Giovanni Battista Martini (1706–1784){/color}."

    fe "Look at how the room is arranged:"
    fe "his round portrait in the centre, the frescoes with figures and ornaments on the sides,"
    fe "and in the cases, his {i}theoretical writings{/i}, his letters, and documents connected to him."

    hide fran_half
    hide federico_half
    with dissolve

    $ sala2_seen_martini = False

    jump sala2_loop



label sala2_loop:

    scene sala2
    with fade

    narrator "You stand in the middle of the second room."
    narrator "The round portrait, the frescoes on both sides, and the cases filled with manuscripts and books are all waiting quietly for you to look at them."

    menu:
        "Look around at the frescoes and the displays":
            jump sala2_paintings

        "Move closer to Father Martini’s portrait":
            $ sala2_seen_martini = True
            jump sala2_martini

        "Go on to the third room" if sala2_seen_martini:
            show federico_half at right
            show fran_half at left
            with dissolve

            f "I think I understand what this room is trying to say."
            f "Let’s move on."

            fe "All right. In the third room you’ll meet the circle of people around Martini—"
            fe "the musicians and friends who passed through Bologna."

            hide fran_half
            hide federico_half
            with dissolve

            stop music fadeout 2.0
            jump sala3

        "Head to the next room" if not sala2_seen_martini:
            narrator "Something holds you back. Before leaving, you feel you should get to know the priest in the portrait a little better."
            jump sala2_loop



label sala2_paintings:

    scene sala2painting1 with fade
    narrator "You look up at one of the frescoes: a figure reclining on cushions, caught somewhere between sleeping and waking."
    narrator "Soft colours and neoclassical decorations surround them, like the traces of a dream that has just ended."

    narrator "The label explains that this decoration wasn’t created especially for music,"
    narrator "but it is often read as an image of “contemplation” and “inspiration arriving”."

    scene sala2painting2 with fade
    narrator "On the opposite wall, the same figure has turned slightly, their gaze clearer now, their hand lifted as if answering an unseen call."
    narrator "If the first fresco was “inside the dream”, this one feels like “coming back from a dream and starting to act”."

    narrator "You suddenly think of yourself: it was also a strange dream that led you here, following its thread into this museum."

    jump sala2_loop



label sala2_martini:

    scene padreMartini with fade
    narrator "A round portrait hangs in the centre of the beige wall."
    narrator "The man in the painting wears a friar’s habit and sits at a desk, open scores and books at his hands, with shelves packed full of volumes behind him."

    show federico_half at right
    with dissolve

    show fran_half at left
    with dissolve
    fe "This is the real “soul” of the museum—"
    fe "{color=#c28b61}Father Giovanni Battista Martini{/color}."

    fe "He was a Franciscan friar and spent almost his entire life in {color=#c28b61}Bologna{/color}."
    fe "Exactly because he stayed here, he had the chance to draw music materials from all over Europe into this city, bit by bit."

    fe "To write as complete a {i}History of Music{/i} as possible,"
    fe "Martini came up with an almost encyclopaedic plan:"

    fe "—to collect {color=#c28b61}music books and scores{/color} from every period;"
    fe "—to create a {color=#c28b61}gallery of portraits of great musicians{/color};"
    fe "—and to build an important music library in {color=#c28b61}Bologna{/color}."

    f "Almost like shrinking the whole European musical world into a single room."

    fe "That’s one way to put it."
    fe "He wrote to scholars, politicians, and musicians all over Europe,"
    fe "exchanging materials and asking them to send works and portraits."

    fe "He was also an outstanding master of counterpoint."
    fe "Many young composers hoped to study with him,"
    fe "or at least receive a letter of recommendation."

    f "Did he have any “famous students”?"

    fe "He did."
    fe "For example, {color=#c28b61}Johann Christian Bach{/color},"
    fe "the youngest son of J. S. Bach;"
    fe "and another name you certainly know—{color=#c28b61}Wolfgang Amadeus Mozart{/color}."

    f "Mozart actually came here?"

    fe "Yes."
    fe "In the 1770s the young Mozart came to {color=#c28b61}Bologna{/color}."
    fe "Martini helped him prepare for his examination,"
    fe "so that he could be admitted to the {color=#c28b61}Accademia Filarmonica di Bologna{/color}."

    hide fran_half
    with dissolve

    narrator "The label beside the portrait quotes the music historian {color=#c28b61}Charles Burney{/color}:"
    narrator "\"Father Martini combined innocence and simplicity with a naturally cheerful, gentle, and kind character."
    narrator "No one has ever won my affection so strongly in a few hours;"
    narrator "to talk with him was like being with an old friend or elder brother.\""

    show fran_half at left
    with dissolve

    f "So he wasn’t the sort of “great man” you have to keep at a distance."
    f "He sounds like someone who really listened and was willing to share what he knew."

    fe "That’s exactly why people trusted him with their scores, manuscripts, and portraits."
    fe "Later, these collections became the core of the {color=#c28b61}Bologna music library{/color},"
    fe "and the deepest roots of today’s {color=#c28b61}museum{/color}."

    fe "Many of the books and scores you see in the cases"
    fe "were once piled up in his own room, on the shelves behind him in this painting."

    f "…So this room is basically saying:"
    f "to understand this museum, you first have to meet the priest sitting at this desk."

    fe "You’ve got the main point."
    fe "When you reach the later rooms, you might want to remember"
    fe "that there was always someone here quietly {i}writing everything down{/i}."

    hide fran_half
    hide federico_half
    with dissolve

    jump sala2_loop



# =========================================
# SALA3
# =========================================

label sala3:

    play music "SALA3 - Quaerite primum regnum Dei, K. 86mp3.mp3" fadein 2.0 loop

    scene sala3_main with fade

    if not _in_replay:
        show federico_half at right
        with dissolve
        show fran_half at left
        with dissolve

        fe "This is the {color=#c28b61}third room{/color}."
        fe "If the previous room felt like Father Martini’s “study”, this one is more like his “sitting room” and his circle of friends."
        f "The walls are almost completely covered with portraits, and there are two keyboard instruments in glass cases."
        fe "Some of the people here were his students; others were visiting composers, singers, or music historians."
        fe "Thanks to exchanges like these, Martini could stay in his monastery and still remain connected with the broader European musical world."

        hide fran_half
        hide federico_half
        with dissolve

    jump sala3_loop


label sala3_loop:

    scene sala3_main with fade
    narrator "You and Federico stand in the middle of the room. Rows of portraits hang on both sides, and along the wall two keyboard instruments rest inside glass cases."

    menu:
        "Look at the wall of portraits on the left":
            hide fran_half
            hide federico_half
            with dissolve
            jump sala3_paintings1

        "Look at the wall of portraits on the right":
            hide fran_half
            hide federico_half
            with dissolve
            jump sala3_paintings2

        "Go closer to the long keyboard instrument and the statue beside it":
            hide fran_half
            hide federico_half
            with dissolve
            jump sala3_piano_and_statue

        "Try to go on to the fourth room":
            hide fran_half
            hide federico_half
            with dissolve

            scene sala4_door with fade
            if sala3_unlocked_sala4:
                narrator "You push open the door to the next room. After the mechanism in the statue’s base was released, the handle is no longer so stubborn."
                stop music fadeout 2.0
                jump sala4
            else:
                narrator "The handle does not move at all, as if some hidden mechanism had locked it from the inside."
                narrator "Maybe there is still a clue somewhere in this room that you have not yet noticed."
                jump sala3_loop


label sala3_paintings1:

    scene sala3_paintings1 with fade

    narrator "You walk up to the portraits on the left wall. Golden frames line up in a row."
    narrator "Everyone here crossed paths with Father Martini in some way—through letters, scores, or visits in person."

    if not sala3_found_keyhole:
        narrator "You let your eyes travel from frame to frame, but for the moment you don’t notice any special mechanism."
        jump sala3_loop

    menu:
        "Look closely at the gentleman with the wig in the lower left corner" if not sala3_bach_solved:
            jump sala3_bach_quiz

        "Look closely at the young musician in the lower right corner" if not sala3_mozart_solved:
            jump sala3_mozart_quiz

        "That’s enough for now, go back to the centre of the room":
            jump sala3_loop


label sala3_bach_quiz:

    narrator "The portrait in the lower left shows a gentleman in a wig, calm-faced, holding a sheet of music."

    narrator "You run your fingers along the edge of the frame and feel a small raised spot that seems to be pressable."
    menu:
        "Press the small raised spot":
            narrator "A faint click comes from inside the frame. Behind the painting a narrow compartment opens, with a folded slip of paper inside."
            narrator "On it you read: {i}“Please say the name of this guest.”{/i}"

    show federico_half at right
    with dissolve

    fe "He was a composer active in London, and also a keyboard player."
    fe "As a young man he came to Bologna specifically to study counterpoint with Martini, and left behind a whole stack of exercises and letters."

    hide federico_half
    with dissolve

label sala3_bach_quiz_answer:
    menu:
        "He is the opera composer Johann Christian Bach.":
            $ sala3_bach_solved = True

            narrator "You say his name. The mechanism inside the frame clicks again, and a tiny piece of metal slides out of the hidden compartment."

            if sala3_mozart_solved and not sala3_have_key:
                $ sala3_have_key = True
                narrator "It fits perfectly with the metal piece you found behind the other portrait, forming a small, finely worked key."
            else:
                narrator "This piece of metal looks like only half of a key, with a clear break along one edge."

            jump sala3_paintings1

        "He is the composer Johann Sebastian Bach.":
            narrator "You try this name, but nothing happens inside the frame."
            narrator "Maybe the answer is not the better-known Bach."
            jump sala3_bach_quiz_answer

        "He is the opera composer Gluck.":
            narrator "You speak this name, and again nothing happens."
            jump sala3_bach_quiz_answer


label sala3_mozart_quiz:

    narrator "The portrait in the lower right shows a young musician. He looks slightly tense, staring towards the viewer, a medal pinned to his chest."

    narrator "On the side of the frame you find a small catch that can be pushed. When you press it, a narrow compartment opens behind the painting, with another slip of paper inside."
    narrator "It reads: {i}“If you recognise him, say his name.”{/i}"

    show federico_half at right
    with dissolve

    fe "This moment was extremely important for him."
    fe "Before coming to Bologna he had already travelled across half of Europe; here, he had to pass an examination to be admitted to the famous Philharmonic Academy."

    hide federico_half
    with dissolve

label sala3_mozart_quiz_answer:
    menu:
        "He is the Italian composer Rossini.":
            narrator "You try this name, but the mechanism remains silent."
            jump sala3_mozart_quiz_answer

        "He is the Austrian composer Wolfgang Amadeus Mozart.":
            $ sala3_mozart_solved = True

            narrator "You say his name. From inside the frame you hear a light metallic sound, and a curved piece of metal slides out from the hidden compartment."

            if sala3_bach_solved and not sala3_have_key:
                $ sala3_have_key = True
                narrator "It fits exactly together with the other metal piece, forming a small key."
            else:
                narrator "This piece looks like the other half of a key; the shape is still incomplete."

            jump sala3_paintings1

        "He is the singer Farinelli.":
            narrator "You say this name, but the frame remains completely still."
            jump sala3_mozart_quiz_answer


label sala3_paintings2:

    scene sala3_paintings2 with fade

    narrator "You move over to the portraits on the right wall. The faces here are even more varied."
    narrator "In an age without trains or recordings, music was already travelling between these people through manuscripts, letters, and memory."

    jump sala3_loop

label sala3_piano_and_statue:

    scene sala3_pianoandstatue with fade

    narrator "An unusual rectangular keyboard instrument stands open inside a glass case."
    narrator "Its case is long and narrow, resting on four turned legs; beside it is a bust with a serious expression."

    menu:
        "Go closer to the keyboard instrument in the glass case":
            jump sala3_piano_close

        "Go closer to the bust":
            jump sala3_statue

        "Return to the centre of the room":
            jump sala3_loop


label sala3_piano_close:

    scene sala3_piano_close with fade

    narrator "You lean towards the glass, almost able to make out each string and every small hammer."

    show federico_half at right
    with dissolve

    fe "This is a rectangular {color=#c28b61}pianoforte{/color} by {color=#c28b61}Joseph Glonner{/color}, built in Munich in 1780."
    fe "On the soundboard to the right you can still read his label in print and ink: {i}Josephus Glonner, Churfstl. Hof Clavecin Macher, 1780{/i}."
    fe "It tells us that he worked as a harpsichord maker at the court of the Elector of Bavaria."

    fe "The body is made from many types of wood: softwood for the bottom and soundboard, beech for the outer case, pearwood panels around the keyboard,"
    fe "and a whole internal frame of spruce, poplar and other woods bracing against the pull of the strings."
    fe "On the soundboard you can see painted flowers, a small paper rosette with eight openings, and the maker’s label framed in walnut."

    fe "Each note has two strings, and the long bridge and nut both curve in an S–shape across the soundboard."
    fe "Next to the tuning pins someone later wrote the note names in ink — {color=#c28b61}Do, Re, Mi{/color}, and so on."
    fe "Because they use {i}B{/i} for {i}Si{/i}, not for B flat as in German practice, we know those names were probably added here in Italy."

    fe "The keyboard runs from C1 up to F5, for a total of fifty–four keys."
    fe "Inside, the action is a German–style {color=#c28b61}Prellmechanik{/color}: small hammers mounted directly on the key levers, without a separate escapement."
    fe "The instrument has three hand stops: a {color=#c28b61}forte{/color} stop that raises the dampers, a {color=#c28b61}liuto{/color} stop that presses felt against the strings,"
    fe "and a very soft {color=#c28b61}pianissimo{/color} stop that places felt between the hammer heads and the strings."

    fe "In Bologna people used to say that this pianoforte once belonged to Father Martini himself."
    fe "But that is probably just a legend: in his keyboard works he writes for a slightly different compass, from around G0 to C5,"
    fe "while this instrument only goes from C1 to F5. More likely, it came to the city a little later, together with other instruments and scores."

    hide federico_half
    with dissolve

    narrator "You look again at the long, narrow case and the dense forest of hammers inside,"
    narrator "and imagine someone sitting down at it in a lamplit room, testing what this new kind of keyboard could do that a harpsichord could not."

    jump sala3_piano_close_loop


label sala3_piano_close_loop:

    menu:
        "Listen to the sound of this keyboard instrument" if sala3_piano_sound_index < 5:
            $ sala3_piano_sound_index += 1

            stop music fadeout 1.5
            play sound f"./rectangular_pianoforte/{sala3_piano_sound_index}.mp3"

            if sala3_piano_sound_index == 1:
                narrator "The sound begins to flow from the speakers near the case. It is more percussive than a harpsichord, yet still lighter and more fragile than a modern concert grand."
            else:
                narrator "The balance between attack and resonance feels more and more familiar, as if this pattern of strikes and echoes were answering something from your dream."

            stop sound fadeout 1.0
            play music "SALA3 - Quaerite primum regnum Dei, K. 86mp3.mp3" fadein 2.0 loop

            jump sala3_piano_close_loop

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if sala3_piano_sound_index >= 2 and not sala3_piano_unlocked:
            $ sala3_piano_unlocked = True
            $ voices_of_music["rectangular_pianoforte"] = True

            show fran_half at left
            with dissolve

            f "Wait… this colour of sound — not quite harpsichord, not yet modern piano —"
            f "I’ve definitely heard it in my dream as well."
            f "It must be one of the {color=#f788c0}Voices of Music{/color}."

            hide fran_half
            with dissolve

            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}:"
            narrator "a rectangular {color=#c28b61}pianoforte by Joseph Glonner{/color}, built in Munich in 1780 and later brought to Bologna."

            jump sala3_piano_close_loop

        "Leave the keyboard instrument and look around this corner of the room again":
            jump sala3_piano_and_statue


label sala3_statue:

    scene sala3_statue with fade
    if not statue_information:
        narrator "You walk up to the bust. The plaster figure stands on a round base, his features full and expressive."
        narrator "The label reads: {i}Ignoto — Antonio Bernacchi, busto in gesso, sec. XIX{/i}."
        narrator "He is {color=#c28b61}Antonio Bernacchi{/color}, an eighteenth–century singer, a castrato contralto and voice teacher, and one of the outstanding figures of the early eighteenth–century music world."
        narrator "He studied with Francesco Antonio Pistocchi and achieved great success on Italian stages, at German courts, and also in England."
        narrator "As his career developed, he gathered a large number of students—many of whom later became celebrated singers—and he twice served as president of the Bologna Philharmonic Academy."
        $ statue_information = True
    else:
        narrator "You look again at the bust of Antonio Bernacchi."

    menu:
        "Examine the bust carefully":
            if not sala3_found_keyhole:
                narrator "Following the curve of the base with your eyes, you notice a slightly recessed line at the back, like a seam that hides a mechanism."
                $ sala3_found_keyhole = True
                narrator "Deep in the crack you glimpse a faint metallic shine—a tiny keyhole."
            else:
                narrator "You check again. The narrow seam is still there, hinting at something hidden inside the base."
            jump sala3_statue

        "Touch the bust":
            if not sala3_found_keyhole:
                narrator "The surface of the base is rough and cold. For now you don’t feel any special structure."
            else:
                narrator "You run your fingers slowly along the seam until you touch the smooth metal edge around the keyhole."
                narrator "It feels like the right place for a small key."
                $ sala3_keyhole_examined = True
            jump sala3_statue

        "{color=#faf5a0}Try inserting the key{/color}" if sala3_have_key and sala3_keyhole_examined and not sala3_unlocked_sala4:
            narrator "You insert the small key assembled from the pieces behind the portraits into the tiny hole and turn it gently."
            narrator "A heavy mechanism grinds somewhere inside the wall, as if a bolt were being drawn back."
            $ sala3_unlocked_sala4 = True
            narrator "In the distance, the handle of the door to the next room gives a slight tremor, as though it has finally been released."
            jump sala3_statue

        "Go back to the corner with the keyboard instrument and the bust":
            jump sala3_piano_and_statue

        "Go back to the centre of the room":
            jump sala3_loop


# ==========================
# SALA4
# ==========================

label sala4:

    play music "SALA4 - Telonius_ Concerto for tromba marina. Ensemble Arcimboldo.mp3" fadein 2.0 loop

    scene sala4main with fade

    narrator "Through the hidden door behind the statue, you step into a smaller, quieter room."
    narrator "The walls shift from bluish green to a warm cream, and the wooden instruments in the display cases glow softly under the lights."

    show fran_half at left
    with dissolve
    show federico_half at right
    with dissolve

    fe "This is the {color=#c28b61}fourth room{/color}."
    fe "It’s not a big space, but many visitors only realise after they leave that this room actually holds quite a few clues."

    hide federico_half
    with dissolve
    show gianni_half at right
    with dissolve

    g "Excuse me—did you two just come from the previous rooms?"

    f "Ah, yes, we just came from the third room."

    hide fran_half
    with dissolve
    show federico_half at left
    with dissolve

    fe "Good evening. You are…?"

    hide federico_half
    hide fran_half
    with dissolve

    narrator "A middle-aged man walks over from beside one of the wall labels, dressed simply but neatly, holding a slightly worn notebook in his hand."
    narrator "Under the lights, his grey-brown hair catches a faint silver sheen. The thin metal frames of his glasses make him look more like a researcher from the museum than an ordinary visitor."

    g "My name is {color=#c28b61}Gianni{/color}. You could say I’m an old regular here."
    g "I sometimes help out with student visits. And you two look pretty interested in all this."

    show fran_half at left
    with dissolve
    
    f "Nice to meet you, I’m Fran."
    f "This is Federico—he’s been guiding me through the museum."

    hide fran_half
    with dissolve
    show federico_half at left
    with dissolve

    fe "Good to meet you, Gianni. We were just about to start talking about this room."

    hide federico_half
    with dissolve
    show gianni_half at right
    with dissolve

    g "Then I won’t get in the way."
    g "If you get curious about any of the instruments or portraits, feel free to ask."

    $ sala4_met_gianni = True

    hide fran_half
    hide federico_half
    hide gianni_half
    with dissolve

    jump sala4_loop


label sala4_loop:

    scene sala4main
    with fade

    narrator "On one side of the room you see a neat row of portraits. On the other, inside a glass case, stand several string instruments of very different shapes."

    menu:
        "Look at the portraits on the wall":
            jump sala4_look_paintings

        "Go up to the glass case and look at the instruments" if not sala4_tromba_unlocked:
            jump sala4_look_instruments
        "Go up to the glass case and look at the instruments again" if sala4_tromba_unlocked:
            jump sala4_instrument_menu

        "Talk to Gianni about this room":
            jump sala4_talk_gianni

        "Leave the fourth room and go on to the next one":
            scene sala4main with fade
            show fran_half at left
            show federico_half at right
            with dissolve

            f "Let’s go on to the fifth room."

            fe "All right, we’ll continue to the next part of the tour."

            if sala4_tromba_unlocked:
                hide federico_half
                with dissolve
                show gianni_half at right
                with dissolve

                g "Don’t forget the sound you just heard."
                g "Some answers only show themselves when you’ve walked far enough."

            hide fran_half
            hide federico_half
            hide gianni_half
            with dissolve

            stop music fadeout 2.0
            jump sala5


label sala4_look_paintings:

    scene sala4paintings with fade

    narrator "Several portraits hang in a clean line on the wall: stern churchmen and scholars wearing academic caps."

    show fran_half at left
    with dissolve

    show gianni_half at right
    with dissolve

    g "Some of them follow the line of thought from the Renaissance writers like Zarlino and Galilei,"
    g "weaving together Pythagoras’s idea of {color=#c28b61}“cosmic harmony”{/color} with Christian visions of a heavenly choir."
    g "For them, polyphonic music wasn’t just something pleasant to listen to—it was a way of imitating the proportions and order of the universe."

    hide gianni_half
    with dissolve
    show federico_half at right
    with dissolve

    fe "Others focus more on the listener’s experience—like that line Leibniz later quotes:"
    fe "“Music is a hidden exercise in arithmetic of the soul.”"
    fe "When we hear consonance and dissonance, we’re actually feeling those tiny but precise differences in ratio."

    hide federico_half
    hide fran_half
    with dissolve

    jump sala4_loop


label sala4_look_instruments:

    scene sala4closer with fade

    narrator "Inside the glass case stand three slender string instruments."
    narrator "On the left is a tall, triangular instrument that almost reaches the top of the case; in the middle, a small pear-shaped long-necked lute; on the right, a fuller-bodied viol."

    show fran_half at left
    show federico_half at right
    with dissolve

    fe "From left to right—"
    fe "The first is called the {color=#c28b61}tromba marina{/color}, sometimes translated as “marine trumpet”."
    fe "Even though it has “trumpet” in the name, it’s actually a bowed string instrument, usually with a single main string."
    fe "Its specially designed bridge makes the string produce a metallic resonance, so the sound sits somewhere between strings and brass."

    fe "The instrument in the middle is a type of long-necked lute—slimmer than the more familiar lute, often used for accompaniment and improvisation."
    fe "The one on the right is a {i}viola da gamba{/i}, a member of the viol family, which in the Baroque period often provided a warm harmonic support to singers or keyboard instruments."

    hide federico_half
    with dissolve
    show gianni_half at right
    with dissolve

    g "Those sounds that feel halfway between a trumpet and a wooden resonance—that’s the {i}tromba marina{/i}."
    g "Theorists wrote about ratios of “consonance”, or about the harmony of the cosmos, all on paper,"
    g "while instrument makers took those ideas and turned them into objects: strange designs and structures that could actually vibrate, made of wood and strings."

    hide fran_half
    hide gianni_half
    with dissolve

    jump sala4_instrument_menu


label sala4_instrument_menu:

    scene sala4closer
    with dissolve

    menu:
        "Listen closely to the sound of the tromba marina" if sala4_tromba_play_count < 5:

            $ sala4_tromba_play_count += 1

            stop music fadeout 1.0
            play sound f"./tromba_marina/{sala4_tromba_play_count}.mp3"

            narrator "You close your eyes. In your ears, a sound rises that lies somewhere between a trumpet and a string instrument."
            narrator "It doesn’t shine as brightly as modern orchestral brass, but it has a strange, slightly husky glow to it—like a signal carried from far away."

            $ renpy.pause(4.0, hard=False)

            stop sound fadeout 1.0
            play music "SALA4 - Telonius_ Concerto for tromba marina. Ensemble Arcimboldo.mp3" fadein 2.0 loop
            jump sala4_instrument_menu

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if not sala4_tromba_unlocked and sala4_tromba_play_count >= 2:
            show fran_half at left
            with dissolve
            narrator "You suddenly realise that this trembling tone, half like a trumpet and half like a human voice, is almost identical to that brief “signal” you heard in the dream."

            f "So that’s it…"
            f "This is also one of the seven {color=#f788c0}Voices of Music{/color}."

            $ sala4_tromba_unlocked = True
            $ voices_of_music["tromba_marina"] = True

            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}: {color=#c28b61}tromba marina{/color}."
            f "Now this instrument’s sound is firmly tied to the trail of clues from the dream."

            hide fran_half
            with dissolve

            narrator "You listen once more in your mind, making sure you won’t forget this strange timbre."
            jump sala4_loop

        "Step back and look at the room from a distance again":
            jump sala4_loop


label sala4_talk_gianni:

    scene sala4main with fade

    show fran_half at left
    show gianni_half at right
    with dissolve

    g "How does it feel? Doesn’t this room have a slightly different atmosphere from the previous ones?"

    f "Yeah… it feels more “abstract”, somehow."
    f "On one side there are long texts full of theory, and on the other there are instruments with very unusual shapes."
    f "It’s a bit like… traces left behind when theory lands in the real world."

    g "That’s a good way to put it."
    g "Before the eighteenth century, a lot of musical knowledge was packed into thick books—"
    g "history, theory, and composition methods all squeezed into the same volume."

    g "Some authors wrote about the “harmony of the cosmos”, others analysed the relationship between emotions and chords,"
    g "and instruments like the ones you just saw"
    g "were attempts to turn formulas, diagrams, and fantasies into tools that could really produce sound."

    g "The important thing is—"
    g "whether they were writers, patrons, or instrument makers, they were all trying to answer the same question:"
    g "“How do you make a fleeting art form something that can be understood and remembered?”"

    f "When you say it like that, it does sound a bit like Father Martini in the previous room."

    g "…Maybe so."
    g "Sometimes a person spends their whole life almost never leaving one city,"
    g "and yet what they record allows people centuries later to still “hear” music that vanished long ago."

    narrator "Gianni smiles slightly, and you can’t help feeling that you’ve seen that expression somewhere before."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala4_loop

# =========================================
# SALA5
# =========================================

label sala5:

    play music "SALA5 - Josquin Des Prez_ Adieu mes Amours.mp3" fadein 2.0 loop

    scene sala5main with fade

    show fran_half at left
    show federico_half at right
    with dissolve

    fe "This is the {color=#c28b61}fifth room{/color}."
    fe "From the entrance onward we’ve been talking about dreams, about people, about collections…"
    fe "Here we finally come back to the core of it all: {color=#c28b61}how a single piece of music is actually “built”{/color}."

    f "The instruments look quite similar at first glance, but there are lots of small differences. And there are scores spread out all over the tables."

    fe "Exactly. What you’re seeing here is a small cross-section of sixteenth- and seventeenth-century Italian musical culture."
    fe "On one side you have {color=#c28b61}early printed music{/color}—like that volume marked {i}“Harmonice Musices Odhecaton A”{/i},"
    fe "a collection printed with movable type in Venice in 1501, often regarded as one of the very first printed music books."

    fe "On the other side you have the instruments that sounded together with those scores: lutes, viols, woodwinds, serpentines…"
    fe "When nobles sang madrigals during festivities or at the dinner table, this was the kind of ensemble that supported the voices."
    fe "You can spend some time here listening to these instruments and ask yourself:"
    fe "Without these scores and these instruments, what would “the musical splendour of the seventeenth century” really have left behind?"

    hide fran_half
    hide federico_half
    with dissolve

    jump sala5_loop


label sala5_loop:

    scene sala5main
    with fade

    narrator "In the centre of the circular room, a ring of glass cases forms something like a small stage."
    narrator "Inside them, lutes, long-necked lutes, serpents, early flutes and viols stand side by side like a silent ensemble waiting to begin."
    narrator "Spread out around them are printed scores and theoretical treatises. The black notes on the page, the shining strings and polished wood together preserve the sound of sixteenth- and seventeenth-century Italian “halls of festivity”."

    menu:
        "Take a look at the instruments in the central display cases":
            jump sala5_look_instruments_overview

        "Talk with Federico about what this room is really about":
            jump sala5_talk_federico

        "Leave the fifth room and go on to the sixth":
            jump sala5_leave


label sala5_look_instruments_overview:

    scene sala5instruments1 with fade

    narrator "From a little distance, you circle the display cases: lutes, long-necked lutes, serpents, early flutes and viols stand side by side like a quiet band waiting offstage."

    show fran_half at left
    show federico_half at right
    with dissolve

    fe "From this angle you can roughly sense how the parts are distributed—"
    fe "which instruments carry the bass, which ones hold up the harmony, which sing the most exposed melodies, and which ones outline the space around everything."

    fe "The most striking are those {i}lutes with the very long necks and the many strings{/i}."
    fe "In sixteenth- and seventeenth-century court and church music they were real backbone instruments."

    hide fran_half
    hide federico_half
    with dissolve

    menu:
        "Step closer and look at each instrument in detail":
            jump sala5_look_instruments_closer
        "Step back again and look from a distance":
            jump sala5_loop


label sala5_look_instruments_closer:

    scene sala5instruments2 with fade

    narrator "You move closer to the glass. The outlines of the instruments become sharper: pear-shaped bodies, intricate rose-shaped soundholes, and the sinuous black curve of the serpent."
    narrator "On the lower shelves, madrigal collections, sacred works and theoretical manuscripts lie open. The printed notes look as if an entire era were being typeset on the page."

    show fran_half at left
    show federico_half at right
    with dissolve

    fe "Here you can almost see a “miniature model” of sixteenth- and seventeenth-century chamber and liturgical music."
    fe "Lutes and viols look after harmony and rhythm, recorders, transverse flutes and early oboes take the melodic lines,"
    fe "and the serpent and other low instruments hold up the deepest layer."

    fe "Those printed scores tell us that music was no longer just an art passed from mouth to ear."
    fe "It had become something that could be copied like a book and circulated across Europe, a kind of {color=#c28b61}cultural commodity{/color}."

    f "So when a piece sounds complete, it’s because all these lines are quietly working together in the background,"
    f "and the reason it can travel from city to city is that someone put those notes onto paper and printed them."

    fe "Exactly."
    fe "If you want to feel it more clearly, go and stand right in front of {color=#c28b61}that large lute in the middle{/color}."

    hide fran_half
    hide federico_half
    with dissolve

    jump sala5_archlute


label sala5_archlute:

    scene sala5instrumentclose with fade

    narrator "You stop in front of the central case. A large lute with an unusually long neck dominates your field of vision, its many strings woven together like a tight net."
    narrator "Three rose-shaped soundholes are carved into the soundboard, like three little constellations in a row. In the dim light of candles, they once glowed softly for banquets and services."

    if sala5_archlute_play_count == 0 and not sala5_archlute_unlocked:

        show fran_half at left
        show federico_half at right
        with dissolve

        fe "This is an {color=#c28b61}archlute{/color}."
        fe "Compared with a standard lute, it has extra bass courses, used to play continuo lines."
        fe "A lot of seventeenth-century cantatas, madrigals and sacred music moved forward step by step on a foundation like this."

        f "Just looking at all those strings, you can imagine how focused the player had to be."

        fe "If you like, you can try “hearing” its sound in your mind."

        hide fran_half
        hide federico_half
        with dissolve

    jump sala5_archlute_menu


label sala5_archlute_menu:

    scene sala5instrumentclose

    menu:
        "In your mind, imagine gently plucking a few strings" if sala5_archlute_play_count < 5:
            $ sala5_archlute_play_count += 1

            stop music fadeout 1.0
            play sound f"archlute/{sala5_archlute_play_count}.mp3"

            narrator "You close your eyes and almost feel a series of low, warm broken chords unfolding slowly upwards from the very bottom."

            $ renpy.pause(3.0, hard=False)

            stop sound fadeout 1.0
            play music "SALA5 - Josquin Des Prez_ Adieu mes Amours.mp3" fadein 2.0 loop
            jump sala5_archlute_menu

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if sala5_archlute_play_count >= 2 and not sala5_archlute_unlocked:

            show fran_half at left
            with dissolve

            f "…That feeling."
            f "I heard something like this in the dream as well."

            hide fran_half
            with dissolve

            narrator "You suddenly realise that the harmonies of the archlute line up with one of the faint threads of sound from your dream."

            show fran_half at left
            with dissolve

            f "So that’s it…"
            f "This is also one of the seven {color=#f788c0}Voices of Music{/color}."

            $ sala5_archlute_unlocked = True
            $ voices_of_music["archlute"] = True

            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}: {color=#c28b61}archlute{/color}."

            hide fran_half
            with dissolve

            jump sala5_archlute_menu

        "Step back and return to the centre of the room":
            jump sala5_loop


label sala5_talk_federico:

    scene sala5main with fade

    show fran_half at left
    show federico_half at right
    with dissolve

    fe "Do you remember that volume titled {i}“Harmonice Musices Odhecaton A”{/i} I mentioned earlier?"
    fe "Printed in Venice in 1501, it’s the first known collection of polyphonic music produced with movable type."

    fe "Before that, if you wanted to sing a polyphonic piece, you had to rely on handwritten parts or pure memorisation."
    fe "From that book onward, notes became something that could be reproduced on a large scale—"
    fe "as if someone had {color=#c28b61}pressed an entire evening’s sound at a banquet into sheets of paper{/color}."

    f "So the scores lying open in the cases aren’t really motionless paper,"
    f "they’re the singing, the conversations and the laughter of all those evenings."

    fe "Exactly."
    fe "In sixteenth- and seventeenth-century Italy, nobles and scholars often sang madrigals around the table, {i}a tavolino{/i}."
    fe "They mixed human voices with the instruments you see here—lutes, viols, recorders, flutes, {i}cornetti{/i}—"
    fe "and built a small world of voices right around the dishes."

    fe "The printed and manuscript sources that Father Martini collected later on"
    fe "almost preserve those “halls of festivity” in their entirety."
    fe "What you’re looking at now is not just a sample of scores, but a {color=#c28b61}miniature of seventeenth-century musical life{/color}."

    f "Thinking of it that way, the low notes of the archlute you just had me imagine aren’t just the harmonic skeleton,"
    f "they’re also helping the notes on those pages come back to life."

    fe "That’s right."
    fe "Whether it’s a madrigal at a banquet or a cantata in a church service,"
    fe "there is always a layer of bass and harmony supporting everything;"
    fe "and once the scores were printed, those structures could leave Bologna,"
    fe "travelling with booksellers and letters to Venice, Rome, Paris…"

    f "So this room is telling two stories at once:"
    f "how the sound of a piece is put together,"
    f "and how that sound was fixed on paper and carried elsewhere."

    fe "Exactly."
    fe "When you think back on this room later,"
    fe "try to remember two things at the same time—"
    fe "the structure of the harmony you heard in your mind, and the printed volumes moving across Europe."
    fe "Together they wove the musical world of that period."

    hide fran_half
    hide federico_half
    with dissolve

    jump sala5_loop



label sala5_leave:

    scene sala5main with fade

    show fran_half at left
    show federico_half at right
    with dissolve

    if not sala5_archlute_unlocked:
        f "I can’t shake the feeling that there’s a sound here I haven’t fully understood yet…"
        f "But maybe it’ll show up by itself the next time I come back to the museum."

    fe "From here on, {color=#c28b61}another guide{/color} will take over."

    f "The colleague you mentioned is…?"

    fe "Her name is {color=#c28b61}Erica{/color}."
    fe "She knows the eighteenth and nineteenth centuries much better than I do, and she follows present-day musical life in Bologna very closely as well."

    hide fran_half
    hide federico_half
    with dissolve

    stop music fadeout 2.0

    jump sala6

# ==========================
# SALA6
# ==========================

label sala6:

    play music "SALA6 - Broschi_ Artaserse_ Son qual nave.mp3" fadein 2.0 loop

    scene sala6main with fade

    narrator "You step into the sixth room. The walls suddenly turn a bright blue. Portraits, instruments, records and theatre sketches all rush into view at once, as if you had walked straight into the backstage of an opera house."

    show fran_half at left
    with dissolve

    show erica_half at right
    with dissolve

    e "Welcome to the {color=#c28b61}sixth room{/color}."
    e "From here on, I’ll be the one accompanying you through the rest of the museum."

    f "You must be Erica, right? Federico mentioned you."

    e "That’s me. I usually guide visitors through the more modern part of the collection."
    e "This room is a kind of turning point — from {color=#c28b61}star singers{/color} to the age of {color=#c28b61}recordings and discs{/color}."

    hide fran_half
    hide erica_half
    with dissolve

    jump sala6_loop


label sala6_loop:

    scene sala6main
    with fade

    narrator "On one wall, several rows of portraits are neatly arranged, one of them much larger than the others. On the opposite side, display cases show plucked-string instruments and an oversized black record."

    menu:
        "Look at the wall of portraits on the right":
            jump sala6_paintings1

        "Walk up to the very large portrait on the left":
            jump sala6_farinelli

        "Look at the display case with the plucked instruments":
            jump sala6_small_instruments

        "Walk over to the record":
            jump sala6_disc

        "Leave the sixth room and continue onward":
            scene sala6main with fade
            show fran_half at left
            show erica_half at right
            with dissolve

            f "It almost feels as if Farinelli’s voice were still circling around us."
            e "Next we’ll step into another era — Rossini and nineteenth-century opera."

            hide fran_half
            hide erica_half
            with dissolve

            stop music fadeout 2.0
            jump sala7


label sala6_paintings1:

    scene sala6paintings1 with fade

    narrator "The right-hand wall is lined with portraits. On the bottom row, one figure gently holds a violin, his expression calm and self-contained."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "These are people who played important roles in eighteenth-century musical life in Italy."
    f "The one at the bottom with the violin… he feels different from the others somehow."

    e "Good eye."

    show antoniovivaldi at Position(xalign=0.5, yalign=0.5)
    with dissolve

    e "That painting is labelled “Presunto ritratto di Antonio Vivaldi (sec. XVII)” —"
    e "which means {i}“Presumed portrait of Antonio Vivaldi”{/i}."

    f "“Presumed”? So you’re not completely sure?"

    e "Exactly."
    e "Seventeenth- and eighteenth-century portraits often have no clear author, and no reliable inscriptions."
    e "Later generations had to compare clothing, facial features, the violin in his hands, and documentary sources to make a guess."
    e "So some portraits can only be filed under “possibly this person”."

    f "Still… his eyes really do look like someone with a lot of stories."

    e "Vivaldi himself was known in Venice as the red-haired priest, {i}il prete rosso{/i} —"
    e "a composer, a violin virtuoso, and one of the key innovators of the concerto across Europe."
    e "His music, his pupils and pupils of his pupils, and his published scores"
    e "all flowed into the musical networks of northern Italy."

    hide antoniovivaldi
    with dissolve

    $ renpy.pause(2.0)
    e "But if we’re talking about a true “superstar”, the main character of this room is actually on the other wall."

    hide fran_half
    hide erica_half
    with dissolve

    jump sala6_loop


label sala6_farinelli:

    scene sala6paintings2 with fade

    narrator "You walk up to the huge painting. The sitter wears red and blue ceremonial robes, one hand resting on a keyboard instrument."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "This is a portrait of {color=#c28b61}Carlo Broschi{/color},"
    e "better known by his stage name: {i}Farinelli{/i}. The painter is Corrado Giaquinto, and the work dates from around 1753."

    f "The legendary castrato singer?"

    e "Exactly. In the world of eighteenth-century opera, there was a simple and brutal rule:"
    e "“Whether the opera succeeds or not depends first on the singer.”"

    e "A star like Farinelli concentrated everything audiences found irresistible at the time —"
    e "insane technical skill, brilliant high notes, sparkling coloratura, and an ability to push whole sections of the audience’s emotions up in waves."
    e "From Italy to London and on to the court in Madrid, wherever he appeared became the centre of the operatic world."

    e "The BGM you’re hearing now —"
    e "“{i}Son qual nave{/i}” — is an aria his brother {i}Riccardo Broschi{/i} wrote specifically for him."
    e "Those never-ending chains of ornaments are there so he could show off on stage as much as possible."

    $ renpy.pause(2.0)

    jump sala6_farinelli_puzzle


label sala6_farinelli_puzzle:

    e "Let me throw you a question."
    e "Do you think it’s possible to find an actual recording of {color=#c28b61}Farinelli himself{/color} in this museum?"

    menu:
        "Probably yes. He was so famous that someone must have recorded his voice":
            e "It sounds reasonable, but one detail doesn’t quite fit—"
            e "Farinelli was born in 1705 and died in 1782, while repeatable sound recording arrived only at the end of the nineteenth century."
            e "The timelines don’t match. Want to try again?"

            hide fran_half
            hide erica_half
            with dissolve

            jump sala6_farinelli_puzzle

        "Probably not.":
            e "Exactly."
            e "What we hear today on recordings of so-called “Farinelli arias”"
            e "are later singers and orchestras, using the surviving scores and written descriptions to {color=#c28b61}re-imagine{/color} his voice."

            f "So what we hear is other people’s understanding of his voice, not the voice he himself left behind."

            e "Right."
            e "But these kinds of “imagined voices” are also a form of memory."

            $ sala6_farinelli_puzzle_solved = True

            hide fran_half
            hide erica_half
            with dissolve

            jump sala6_loop


label sala6_small_instruments:

    scene sala6small_instruments with fade

    narrator "Inside a glass case hang three small plucked-string instruments, with rows of fine-printed music laid out beneath them."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "These belong to the mandolin family: on the left an early {i}mandolino{/i}, the one in the middle a little larger, and on the right something closer to the mandolin we know today."
    e "From aristocratic salons to late-night serenades in the street, they were popular all across Italy."

    f "From left to right, I can almost hear the sound getting closer to what I imagine as “a serenade played under someone’s window”."

    e "Exactly. You can think of them as eighteenth- and nineteenth-century versions of a “pop instrument”."

    hide fran_half
    hide erica_half
    with dissolve

    jump sala6_loop


label sala6_disc:

    scene sala6disc with fade

    narrator "On another display a comically large black disc leans against a stand, with words like “DISQUE” and “PATHÉ” printed on the label."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "This section is about the arrival of {color=#c28b61}recordings and discs{/color}."
    e "With these, voices could be copied and taken home, played again and again,"
    e "instead of existing only in the theatre on that one particular evening."

    f "This disc is huge — it doesn’t look much like the vinyl records I’m used to seeing."

    e "It’s a large-format {color=#c28b61}Pathé record{/color} from the early twentieth century."
    e "Back then every company had its own size and its own playback system, so each disc made quite a visual statement."

    hide fran_half
    hide erica_half
    with dissolve

    menu:
        "Step closer and look at the details on the disc":
            jump sala6_disc_closer

        "Go back to the centre of the room for now":
            jump sala6_loop


label sala6_disc_closer:

    scene sala6disc_closer with fade

    narrator "You lean in and the text on the central label comes into focus:"
    narrator "“DISQUE PATHÉ”, number 5851, the title “{i}Andalucia (Popy), Valse{/i}”."
    narrator "The black surface is covered in tightly packed grooves that spiral outward."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "This is a Pathé recording of the waltz “Andalucia” by Popy."
    e "To listen to it, you need a specific type of phonograph, so that the stylus can travel along those grooves"
    e "and let the music that was once captured there “grow” out of the horn again."

    hide fran_half
    hide erica_half
    with dissolve

    jump sala6_disc_menu


label sala6_disc_menu:

    scene sala6disc_closer

    menu:
        "Gently set the disc spinning and listen to the recorded sound" if sala6_disc_play_count < 5:
            $ sala6_disc_play_count += 1

            stop music fadeout 1.0
            play sound f"disc/{sala6_disc_play_count}.mp3"

            narrator "First there is a soft hiss from the horn, and then the music appears. The recording is far from perfect, yet it feels both close to your ear and strangely distant in time."

            $ renpy.pause(4.0, hard=False)

            stop sound fadeout 1.0
            play music "SALA6 - Broschi_ Artaserse_ Son qual nave.mp3" fadein 2.0 loop
            jump sala6_disc_menu

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if sala6_disc_play_count >= 2 and sala6_farinelli_puzzle_solved and not sala6_disc_unlocked:

            show fran_half at left
            with dissolve

            f "…Right now it feels less like I’m standing in front of a display case,"
            f "and more like I’m eavesdropping on some distant evening’s ball through an old machine."

            hide fran_half
            with dissolve

            narrator "You suddenly remember that, in your dream, there was a slight noise, which came from the record."

            show fran_half at left
            with dissolve

            f "So that’s it…"
            f "This is also one of the seven {color=#f788c0}Voices of Music{/color}."
            f "From here on, beautiful voices can truly be preserved."

            $ sala6_disc_unlocked = True
            $ voices_of_music["disc"] = True

            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}: {color=#c28b61}recorded sound{/color}, the preservation of voices and music."

            hide fran_half
            with dissolve

            jump sala6_disc_menu

        "Step away from the record and return to the centre of the room":
            jump sala6_loop

# ==========================
# Sala7
# ==========================

label sala7:

    play music "SALA7 - Il Barbiere di Siviglia_ Largo al factotum.mp3" fadein 2.0 loop

    scene sala7main with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    narrator "You step into the seventh room. The pink walls suddenly make everything feel brighter. Portraits, busts, manuscripts and playbills run all around the walls, and in the centre a polished grand piano stands on a glass platform."

    e "Welcome to the {color=#c28b61}seventh room{/color}."
    e "From here on, the faces you see will start looking more and more like the “modern people” we recognise."

    f "Even the colours feel much more intense…"

    e "That’s very nineteenth century."
    e "Opera became one of the central events of city life, and composers and singers turned into {color=#c28b61}public figures{/color}."
    e "Starting with Rossini, {color=#c28b61}popular opera (melodramma){/color} reached its peak in Italy and in the major European cities."

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "We meet again."
    f "Hi, Gianni."

    g "Have you found more of the {color=#f788c0}Voices of Music{/color}?"
    f "Yes."
    g "Good. Take your time and look around this room first."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala7_loop


label sala7_loop:

    scene sala7main
    with fade

    narrator "The pink walls make the whole room feel as if it were lit by stage lights. Portraits crowd the walls, and in the middle a grand piano stands quietly on its glass base."

    menu:
        "Look at the portraits on the left wall":
            jump sala7_paintings1

        "Look at the portraits on the right wall":
            jump sala7_paintings2

        "Walk over to the grand piano":
            jump sala7_piano

        "Talk with Erica about what this room is about":
            jump sala7_talk_erica

        "Share a few impressions with Gianni":
            jump sala7_talk_gianni

        "Leave the seventh room and move on":
            if sala7_finished:
                scene sala7main with fade

                show fran_half at left
                show erica_half at right
                with dissolve

                f "I think I’m starting to see it: the most successful scores don’t just live for a single performance, they stay on the theatre posters for years."
                e "Exactly."

                hide erica_half
                with dissolve

                show gianni_half at right
                with dissolve

                g "Along this path where words, music and stage action are woven more and more tightly together, the nineteenth-century ideal eventually converges on Richard Wagner."
                g "People in Bologna became passionate about Wagner quite early on."
                g "The 1871 performance of {color=#c28b61}Lohengrin{/color} in Bologna is often seen as the starting point of his fame in Italy."
                g "I’ll be waiting for you in the next room."

                hide gianni_half
                hide fran_half
                with dissolve

                stop music fadeout 2.0

                jump sala8
            else:
                narrator "You have a feeling there are still pieces of the puzzle in this room that you haven’t quite put together yet, and you’re not ready to leave."
                jump sala7_loop


label sala7_paintings1:

    scene sala7paintings1 with fade

    narrator "The portraits on the left wall feel surprisingly familiar. On the bottom row, a dark-haired woman looks straight ahead, her gaze bright and steady, with a quiet confidence."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "In the nineteenth century, music no longer belonged only to courts and churches; it became part of {color=#c28b61}urban middle-class life{/color}."
    f "The woman at the bottom… she really looks like someone who belongs at the centre of the stage."
    e "Your instinct is spot on."

    show isabella_colbran at Position(xalign=0.5,yalign=0.5)
    with dissolve

    e "That painting is titled {i}“Ritratto di Isabella Colbran”{/i} (around 1806–07)."
    e "She was one of the most famous Spanish sopranos of her time, and later became the wife of {color=#c28b61}Gioachino Rossini{/color}."

    f "Rossini as in the composer of {i}The Barber of Seville{/i}?"

    e "Yes — the composer of the BGM you’re hearing right now."
    e "Rossini wrote several leading roles specifically for Isabella Colbran."
    e "For many members of the audience, she wasn’t just “the person playing a role”, she was the symbol of the entire theatre."
    e "In nineteenth-century opera, singers and composers were both artists and carefully watched public figures."

    hide erica_half
    hide fran_half
    hide isabella_colbran
    with dissolve

    jump sala7_loop


label sala7_paintings2:

    scene sala7paintings2 with fade

    narrator "The right wall carries more portraits, with some handwritten scores displayed between them."

    show fran_half at left
    show gianni_half at right
    with dissolve

    g "Starting from Rossini, {color=#c28b61}popular opera (melodramma){/color} exploded across Italy and the big cities of Europe."

    f "So opera stopped being something only a small group could afford to see?"

    g "Exactly. A successful opera could stay on theatre posters for years."
    g "Audiences would come back again and again to see the same piece, to hear the same singer perform the same aria."

    g "Little by little, the composer stopped being “the person who just supplies the music for a play”,"
    g "and became the one who shapes the timing, emotion and structure of the whole work."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala7_loop


label sala7_piano:

    scene sala7piano with fade

    narrator "A polished grand piano fills one corner of the room, its lid wide open like a wooden wing. The carved legs are elegant, and the floor beneath the glass platform mirrors its outline."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "Compared with the early keyboard instruments you saw in the previous rooms, this one is already very close to the {color=#c28b61}modern piano{/color} we know."
    e "A stronger internal frame and tighter steel strings allow it to fill much larger spaces — even opera houses — with sound."

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "In nineteenth-century Bologna, a piano like this might be found in a theatre rehearsal room, in an aristocratic salon,"
    g "or in the drawing room of a well-off middle-class family."
    g "Arias from popular operas were constantly arranged for piano and played at home, over and over again."

    f "No wonder the BGM in this room feels like it’s drifting in from an opera house somewhere."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala7_piano_menu


label sala7_piano_menu:

    scene sala7_piano_closer with fade

    narrator "You stand in front of the piano. Under the glass cover the keys line up in a clean row. Even without anyone sitting at it, it gives the impression that music could start at any moment."

    menu:
        "Listen to the sound of the piano" if sala7_piano_play_count < 5:
            $ sala7_piano_play_count += 1

            stop music fadeout 1.0
            play sound f"piano/{sala7_piano_play_count}.mp3"

            narrator "Clear, full notes ring through the room. They are stronger than the keyboards you heard earlier, much closer to the sound of a modern concert grand."

            $ renpy.pause(3.0, hard=False)

            stop sound fadeout 1.0
            play music "SALA7 - Il Barbiere di Siviglia_Largo al factotum.mp3" fadein 2.0 loop
            jump sala7_piano_menu

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if sala7_piano_play_count >= 2 and not sala7_piano_unlocked:
            show fran_half at left
            with dissolve

            f "…I’ve heard this sound in my dream as well."
            f "It isn’t a church organ, and it isn’t one of those older keyboards."
            f "It’s this kind of tone — bright, with a slight metallic edge."

            hide fran_half
            with dissolve

            narrator "You realise that the timbre of this piano matches one of the brief flashes of sound from your dream almost exactly."

            show fran_half at left
            with dissolve

            f "So that’s it…"
            f "This is also one of the {color=#f788c0}“Voices of Music”{/color} from the dream."

            $ sala7_piano_unlocked = True
            $ voices_of_music["piano"] = True

            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}: the grand piano."

            hide fran_half
            with dissolve

            jump sala7_piano_menu

        "Look more closely at how the piano is built":
            jump sala7_piano_puzzle

        "Step away from the piano and return to the centre of the room":
            if sala7_piano_unlocked and sala7_piano_quiz_solved:
                $ sala7_finished = True
            jump sala7_loop


label sala7_piano_puzzle:

    scene sala7_piano_closer with fade

    narrator "You study the piano in detail: the heavy body, the dense grid of metal strings, the frame just visible inside — all completely different from the older keyboards you saw earlier."

    show fran_half at left
    show erica_half at right
    with dissolve

    e "Since you’ve noticed the differences, let’s try a little “piano mechanism quiz”."
    e "Compared to the early keyboard instruments you saw before, why can a grand piano like this fill a much larger space with a sound close to what we hear in an opera theatre?"

    hide erica_half
    with dissolve

    menu:
        "Because its wooden frame is very light, so it resonates more easily":
            show erica_half at right
            with dissolve

            e "Lightness does help resonance,"
            e "but if you only had a light wooden frame, the strings couldn’t be pulled very tight, and the sound would actually be limited."

            hide erica_half
            hide fran_half
            with dissolve

            narrator "You feel something is missing from this explanation and decide to take another look."
            jump sala7_piano_puzzle

        "Because it uses a metal frame and high-tension steel strings, which produce a much bigger sound":
            show erica_half at right
            with dissolve

            e "That answer is very close to the real story."
            e "Nineteenth-century pianos make extensive use of a {color=#c28b61}metal frame{/color}, which can withstand much greater string tension,"
            e "and with improved hammer action the sound carries clearly even in theatres and concert halls."

            hide erica_half
            with dissolve

            show gianni_half at right
            with dissolve

            g "You can think of it this way:"
            g "what used to be an instrument suited to small salons has been redesigned into something that can address an entire city."
            g "A single piano can make people think of a whole orchestra — that’s one reason piano arrangements of operatic arias became so popular in the nineteenth century."

            hide gianni_half
            hide fran_half
            with dissolve

            $ sala7_piano_quiz_solved = True

            narrator "You now have a much clearer picture of how this piano works. It no longer feels like a mere display object, but like a machine engineered to push sound outwards."

            jump sala7_piano_menu

        "Because it has fewer keys than earlier instruments, so each note is more focused":
            show erica_half at right
            with dissolve

            e "The number of keys does change from instrument to instrument,"
            e "but what really affects volume and projection is the string tension and inner structure, not “having fewer keys”."

            hide erica_half
            hide fran_half
            with dissolve

            narrator "Thinking back to the clarity of the sound you just heard, you realise the answer must lie elsewhere."
            jump sala7_piano_puzzle

        "Because the inside is packed with hollow resonance boxes that bounce the sound around endlessly":
            show erica_half at right
            with dissolve

            e "Resonance spaces are important, of course,"
            e "but if you only had “hollowness” and reflections, the sound would turn muddy instead of having the sharp outline you just heard."

            hide erica_half
            hide fran_half
            with dissolve

            narrator "You recall how clear the tone was and decide that the explanation must be different."
            jump sala7_piano_puzzle


label sala7_talk_erica:

    scene sala7main with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "How does it feel? Compared with the earlier rooms, doesn’t it seem more like “real people” are looking back at you from these frames?"

    f "It does. The people before felt far away — here it’s as if they could just step out of the frames and sit down at the piano to practise."

    e "A big part of nineteenth-century music history is actually the history of {color=#c28b61}city life{/color}."
    e "Rehearsals, premieres, house concerts, recordings… music moved away from purely liturgical rites and court celebrations and became part of many people’s everyday routines."

    f "So that’s why the piano becomes so important."

    e "Exactly."
    e "A single piano can accompany, can stand in for an entire ensemble, and can be used to rehearse with singers."
    e "In a way, it’s like a small {color=#c28b61}theatre{/color} you can move into your living room."

    hide erica_half
    hide fran_half
    with dissolve

    jump sala7_loop


label sala7_talk_gianni:

    scene sala7main with fade

    show fran_half at left
    show gianni_half at right
    with dissolve

    g "Have you noticed that, from Father Martini’s room all the way here,"
    g "the instruments have changed, the sounds have changed — and people’s ideas about their own image have changed too?"

    f "At the beginning everyone seemed more worried about how to write music down."
    f "Later on, they start caring about how they themselves are seen."

    g "Maybe."
    g "But one thing doesn’t change: there is always someone listening."
    g "Without a listener, all these scores, portraits, phonographs and pianos would lose their meaning."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala7_loop

# ==========================
# Sala8
# ==========================
label sala8:

    play music "SALA8 - Schubert_ Octet in F major, D.803.mp3" fadein 2.0 loop

    scene sala8main with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "Welcome to the {color=#c28b61}eighth room{/color}."
    e "From here on, you’re no longer looking at the room of a single composer,"
    e "but at an entire {i}ensemble{/i} — and how it was slowly pieced together."

    f "There are so many instruments here… and they all feel a bit more “modern” than in the earlier rooms."

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "If the earlier rooms were about individual stories, this one is about how “many voices start speaking together”."
    g "Especially these woodwinds and brass — they started as signals, and only later became part of the musical language."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala8_loop


label sala8_loop:

    scene sala8main
    with fade

    narrator "You stand in the middle of the room. In the front glass case, a whole row of flutes, oboes, clarinets and bassoons lines up from low to high."
    narrator "If you walk around to the back, you see open full scores and parts, and near the glass a long, low-pitched instrument."
    narrator "On the side, behind another glass panel, several natural horns form golden circles around a dark wooden violin at the centre."

    menu:

        "Look at the front of the case (woodwind instruments)":
            jump sala8_look_instruments_front

        "Look at the back of the case (scores and bass parts)":
            jump sala8_look_instruments_back

        "Go to the side and look at the horns and the violin":
            if sala8_puzzle_solved:
                jump sala8_look_violin
            else:
                jump sala8_violin_locked_hint

        "Talk with Erica and Gianni about what this room means":
            jump sala8_talk_guides

        "Leave the eighth room and move on":
            scene sala8main with fade
            show fran_half at left
            show erica_half at right
            with dissolve

            f "I feel like I can hear an entire ensemble rehearsing inside my head now."

            e "Then let’s carry those sounds with us, and head to the last room."

            hide erica_half
            with dissolve

            show gianni_half at right
            with dissolve

            g "Remember the sound of the violin, the horns, and these woodwinds."
            g "Once you put all the fragments together, they’ll help you tie all your earlier memories into one line."

            hide gianni_half
            hide fran_half
            with dissolve

            stop music fadeout 2.0
            jump sala9


label sala8_look_instruments_front:

    scene sala8_instruments1 with fade

    narrator "You walk up to the front of the case. A whole row of woodwind instruments stretches from left to right:"
    narrator "flutes, oboes, clarinets, bassoons… like slender tree trunks rising gradually from low notes to higher ones."

    show erica_half at right
    with dissolve

    e "You can roughly think of them as one big group —"
    e "all of them are {color=#f788c0}woodwinds{/color}, painting colours onto the melody."

    e "In the eighteenth century, the “Mechanical and Craft Arts” volume of the {color=#c28b61}Encyclopédie{/color} had a line that said:"
    e "“There is no natural phenomenon, and no human emotion, that cannot be imitated by musical instruments.”"
    e "The shrill piccolo in a storm, or a dark horn call suggesting ghosts — both grow out of that way of imagining things."

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "But if all you have are signals and no melody, people get tired very quickly."
    g "So composers brought the woodwinds into the orchestra, let them weave between strings and brass,"
    g "sometimes like the wind, sometimes like a storyteller walking among the other voices."

    hide gianni_half
    with dissolve

    $ sala8_seen_frontcase = True

    jump sala8_woodwinds_menu


label sala8_woodwinds_menu:

    scene sala8_instruments1

    menu:
        "Listen to a short passage for the woodwinds" if sala8_woodwinds_play_count < 5:
            $ sala8_woodwinds_play_count += 1

            stop music fadeout 1.0
            play sound f"woodwinds/{sala8_woodwinds_play_count}.mp3"

            narrator "A brief woodwind ensemble rises out of the orchestra you’re imagining:"
            narrator "the flute draws bright lines up high, the oboe and clarinet seem to be talking to each other, and the bassoon quietly supports everything at the bottom."

            $ renpy.pause(3.0, hard=False)

            stop sound fadeout 1.0
            play music "SALA8 - Schubert_ Octet in F major, D.803.mp3" fadein 2.0 loop
            jump sala8_woodwinds_menu

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if sala8_woodwinds_play_count >= 2 and not sala8_woodwinds_unlocked:
            $ sala8_woodwinds_unlocked = True

            show fran_half at left
            with dissolve

            f "…The “colour” here is completely different from the solo instruments in the earlier rooms."
            f "It’s not one person standing under a spotlight — it’s several lines wandering through the air together."

            hide fran_half
            with dissolve

            narrator "You feel that you’ve fixed in your memory the light, detailed presence of the woodwinds inside the orchestra."
            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}: the woodwinds."
            $ voices_of_music["woodwinds"] = True

            jump sala8_woodwinds_menu

        "Step away from the woodwinds and return to the centre of the room":
            jump sala8_loop


label sala8_look_instruments_back:

    scene sala8_instruments2 with fade

    narrator "You walk around to the back of the case. Under the glass lies a row of full scores and parts, the paper slightly yellowed with age."
    narrator "On the lowest tier, close to the glass, a long-bodied bass instrument rests with its metal keys catching the light."

    show erica_half at right
    with dissolve

    e "These scores are from the eighteenth and nineteenth centuries."
    e "Early music printing used movable type and woodcuts, later followed by {color=#c28b61}copper engraving{/color} and {color=#c28b61}lithography{/color}."

    e "Italian composers would send their manuscripts to big cities north of the Alps to be printed,"
    e "and the finished full scores and parts would then travel back to theatres and orchestras all over Europe."

    e "You can see that flutes, oboes, clarinets and bassoons each have their own staff,"
    e "and together with the strings and horns they form a tightly woven {i}carpet of harmony{/i}."

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "If you look closely at a full score, you’ll see the name of each instrument at the start of every line."
    g "It’s like someone is arranging the seating plan: who sits at the front, who keeps the pulse, who leads everyone forward."

    hide gianni_half
    with dissolve

    $ sala8_seen_backcase = True

    if sala8_seen_backcase and sala8_seen_frontcase and not sala8_puzzle_solved:
        jump sala8_puzzle_intro
    else:
        jump sala8_loop


label sala8_violin_locked_hint:

    scene sala8main with fade

    show gianni_half at right
    with dissolve

    g "Of course the violin is important, but—"
    g "if you haven’t really worked out what all these woodwinds and horns are doing yet,"
    g "you might not quite understand what it’s trying to tell you when you walk up to it."

    hide gianni_half
    with dissolve

    narrator "Maybe you should spend a bit more time with the front and back of the case, then come back here."

    jump sala8_loop


label sala8_puzzle_intro:

    scene sala8_instruments1 with fade

    narrator "After looking carefully at both sides of the case, you have a rough sense of how these instruments relate to each other."

    show erica_half at right
    with dissolve

    e "Since you’ve been paying such close attention, how about answering a couple of questions?"

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "Don’t worry, it’s not an exam."
    g "We just want to check that when you hear those sounds again, your mind knows who is speaking."

    hide gianni_half
    with dissolve

    jump sala8_puzzle_questions


label sala8_puzzle_questions:

    scene sala8_instruments2

    $ correct = 0

    menu:
        "{color=#c28b61}Among these sounds, which one most feels like it was made to send a clear, far-reaching “signal”?{/color}"
        
        "The slim wooden tube whose sound feels like someone speaking close to your ear — the flute":
            pass
        "The bright, coiled metal instrument that can be heard clearly outdoors — the horn":
            $ correct += 1
        "The small, carefully held instrument under the chin, with a delicate tone — the violin":
            pass

    menu:
        "{color=#c28b61}In a full orchestra, which group of instruments most often lays down a broad, continuous background of harmony?{/color}"

        "The percussion section, with bass drum, cymbals and other rhythmic effects":
            pass
        "A row of horns taking turns passing phrases along":
            pass
        "All those flutes, oboes, clarinets and bassoons together — the woodwind section":
            $ correct += 1

    menu:
        "{color=#c28b61}If you wanted to draw a clear “main melodic line” over that background, who gets called on most often to play it?{/color}"

        "The whole row of violins at the front, surrounded by horns and woodwinds":
            $ correct += 1
        "The bassoons at the edge, with their lower, more supporting sound":
            pass
        "The horns at the back, which come in from time to time to strengthen the atmosphere":
            pass

    if correct == 3:
        $ sala8_puzzle_solved = True

        scene sala8main with fade

        show gianni_half at right
        with dissolve

        g "Good. You’ve sorted out the roles of some key players in this ensemble."
        g "Now go back and listen to that violin again —"
        g "you may find that it’s not just playing a solo, it’s speaking to everyone at once."

        hide gianni_half
        with dissolve

        jump sala8_loop
    else:
        scene sala8main with fade

        show erica_half at right
        with dissolve

        e "Not quite, you’re still missing a piece or two."
        e "That’s all right — take another turn around the case. You’ll spot more clues."

        hide erica_half
        with dissolve

        jump sala8_loop


label sala8_look_violin:

    scene sala8_violinclose with fade

    narrator "You walk over to the side of the case."
    narrator "A violin hangs in the middle of the glass, its four strings running from the fingerboard all the way up to the scroll,"
    narrator "the f-holes clear and dark under the lights."
    narrator "Several natural horns form golden loops around it, as if lightly enclosing it at the centre."

    show erica_half at right
    with dissolve

    e "From the shape you can tell this is a standard {color=#f788c0}violino (violin){/color}."
    e "It isn’t a {i}viola d’amore{/i} with extra sympathetic strings,"
    e "but one of the most common and most important string instruments in eighteenth- and nineteenth-century orchestras."

    e "In ever-growing ensembles, the violins often stand in the very front,"
    e "drawing the melodic line that people remember most easily,"
    e "giving direction to the colours of the woodwinds, the signals of the horns, and the deep voices underneath."

    hide erica_half
    with dissolve

    jump sala8_violin_menu


label sala8_violin_menu:

    scene sala8_violinclose

    menu:
        "Listen to the sound of this violin" if sala8_violin_play_count < 5:
            $ sala8_violin_play_count += 1

            stop music fadeout 1.0
            play sound f"violin/{sala8_violin_play_count}.mp3"

            narrator "The bow hair presses onto the string; at first the sound is a little rough, then it stretches out into a long, continuous line."

            $ renpy.pause(3.0, hard=False)

            stop sound fadeout 1.0
            play music "SALA8 - Schubert_ Octet in F major, D.803.mp3" fadein 2.0 loop
            jump sala8_violin_menu

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if sala8_violin_play_count >= 2 and not sala8_violin_unlocked:
            show fran_half at left
            with dissolve

            f "…This sound was in my dream as well."
            hide fran_half
            with dissolve

            narrator "You realise that the timbre of this violin matches one of the sounds you heard in the dream."

            show fran_half at left
            with dissolve

            f "So that’s what it was—"

            $ sala8_violin_unlocked = True
            $ voices_of_music["violin"] = True

            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}: the violin."

            hide fran_half
            with dissolve

            jump sala8_violin_menu

        "Listen to the sound of the natural horns" if sala8_horns_play_count < 4:
            $ sala8_horns_play_count += 1

            stop music fadeout 1.0
            play sound f"french_horn/{sala8_horns_play_count}.mp3"

            narrator "The natural horn, without valves, produces a series of slightly grainy long notes,"
            narrator "its pitch jumping between harmonics as the tension of the lips changes."

            $ renpy.pause(3.0, hard=False)

            stop sound fadeout 1.0
            play music "SALA8 - Schubert_ Octet in F major, D.803.mp3" fadein 2.0 loop

            jump sala8_violin_menu

        "{color=#faf5a0}This is one of the “Voices of Music” from the dream{/color}" if sala8_horns_play_count >= 2 and not sala8_horns_unlocked:
            $ sala8_horns_unlocked = True
            $ voices_of_music["french_horn"] = True

            show fran_half at left
            with dissolve

            f "…This sound isn’t the same as the {i}tromba marina{/i},"
            f "but it has the same feeling of a “signal” — like something being lit in the distance."

            hide fran_half
            with dissolve

            narrator "You hold on to the call of the natural horn."
            narrator "You have unlocked a new {color=#f788c0}“Voice of Music”{/color}: the horn."

            jump sala8_violin_menu

        "Step back and return to the centre of the room":
            jump sala8_loop


label sala8_talk_guides:

    scene sala8main with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "If the earlier rooms were about “collecting” and “recording”,"
    e "this one is really about {color=#f788c0}collaboration{/color}."

    e "To have so many sounds appear at the same time in one ensemble,"
    e "you need instrument makers, composers, performers — and also patrons and listeners — all working together."

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "Sometimes the violin part in a piece isn’t actually very complicated."
    g "But because it stands at the front of everyone else, it becomes the “spokesperson of memory”."

    g "Years later, people may no longer remember the full orchestration,"
    g "but they can still hum the leading melody."

    f "Just like the sounds in my dream—"
    f "I may not remember every single note, but the overall beauty is still crystal clear."

    g "Then keep carrying them with you."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala8_loop


# ==========================
# Sala9
# ==========================
default allow_leave_sala9 = False

label sala9:

    play music "SALA9 - Preludio, corale e fuga, P. 30_ I. Preludio. Lento - Presto.mp3" fadein 2.0 loop

    scene sala9main with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "Welcome to {color=#c28b61}Room 9{/color}. This is the last room on today’s route."
    e "From Room 1 onward, you’ve been walking through several centuries of musical memory."
    e "Here, we want to ask a different question: when the old ways of writing are questioned, {color=#c28b61}where does music go next{/color}?"

    hide erica_half
    hide fran_half
    with dissolve

    jump sala9_loop


label sala9_loop:

    scene sala9main with fade

    menu:
        "Look at the paintings on the wall":
            jump sala9_paintings

        "Walk over to the gramophone in the corner":
            jump sala9_gramophone

        "Talk with Erica and Gianni about what all this means":
            jump sala9_talk_guides

        "Go back to any earlier room for another look":
            jump sala9_back_to_other_rooms

        "Leave this room (go back towards the entrance)":
            jump sala9_leave

    jump sala9_loop


label sala9_paintings:

    scene sala9paintings with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "The large painting in the centre shows {color=#c28b61}Giuseppe Martucci (1856–1909){/color}."
    e "He was an Italian composer, pianist and conductor. He taught at the Bologna Conservatory and later became its director."
    e "Unlike the operatic mainstream in Italy at the time, he strongly championed the symphonic traditions of Brahms and other German–Austrian composers,"
    e "bringing a more “European” way of listening to instrumental music into Italy."

    e "Thanks to Martucci’s efforts, Bologna became one of the few places in Italy to truly absorb the symphonic tradition."
    e "He believed that {i}“real modernity must carry a respect for the classical.”{/i}"

    f "So he was someone who looked forward, but refused to let go of tradition."

    e "Exactly. For him, the future of music wasn’t about throwing the past away, but about understanding it again, in a new light."

    show Ottorino_Respighi at Position(xalign=0.5, yalign=0.5)
    with dissolve

    e "Down on the left, in the slightly smaller portrait, is his student —"
    e "{color=#c28b61}Ottorino Respighi (1879–1936){/color}."

    e "Respighi studied composition here in Bologna and later taught here as well. He also went to Russia to study orchestration with Lyadov and Rimsky-Korsakov,"
    e "so he developed an exceptional sense for musical colour."

    e "Pieces like {i}Pines of Rome{/i} and {i}Fountains of Rome{/i} are famous for their refined timbres, modes and “play of light and shade”."
    e "He drew inspiration from early music and modal writing, yet kept working with tonality — just stretching it into something more dramatic and expansive."

    f "It sounds like he was a bit bolder than his teacher."

    e "You could put it that way. He wasn’t a strict guardian of the classical language like Martucci,"
    e "but he also didn’t abandon tonality the way more radical modernists did."
    e "Instead, he carved out a kind of “new classical language of light and shadow” between the two."

    hide fran_half
    hide erica_half
    hide Ottorino_Respighi
    with dissolve

    jump sala9_loop


label sala9_gramophone:

    scene sala9box with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "This early gramophone in the corner marks a huge turning point at the end of the nineteenth century."
    e "For the first time, sound could be stored and carried to faraway places."

    e "For the generation of Martucci and Respighi,"
    e "this meant that music no longer travelled only through scores, but could now move as sound itself."

    hide fran_half
    hide erica_half
    with dissolve

    jump sala9_loop


label sala9_talk_guides:

    scene sala9main with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "The whole museum has really been circling around one question:"
    e "“How do we remember sounds that are no longer here?”"

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "And all those fragments of the {color=#f788c0}Voices of Music{/color} you’ve been chasing…"
    g "Yes, they were scattered through these rooms — but their meaning doesn’t belong only to the past."

    g "Sometimes those sounds recombine inside your own memory."
    g "Perhaps they’re already leading you somewhere else."

    hide gianni_half
    hide fran_half
    with dissolve

    jump sala9_loop


label sala9_back_to_other_rooms:

    scene sala9main with fade

    narrator "You decide to go back to one of the earlier rooms, just to check whether you’ve missed any sound."

    menu:
        "Go back to Room 1":
            jump sala1_loop
        "Go back to Room 2":
            jump sala2_loop
        "Go back to Room 3":
            jump sala3_loop
        "Go back to Room 4":
            jump sala4_loop
        "Go back to Room 5":
            jump sala5_loop
        "Go back to Room 6":
            jump sala6_loop
        "Go back to Room 7":
            jump sala7_loop
        "Go back to Room 8":
            jump sala8_loop
        "On second thought, I’ll stay here for now":
            jump sala9_loop


label sala9_leave:

    python:
        total_fragments = sum(1 for v in voices_of_music.values() if v)

    if total_fragments < 9 and not allow_leave_sala9:

        scene sala9main with fade

        show fran_half at left
        show erica_half at right
        with dissolve

        e "The {color=#f788c0}Voices of Music{/color} are made up of nine fragments in total."
        e "Right now, you’ve only found [total_fragments]."

        e "Maybe in one of the earlier rooms, there’s still an instrument or a sound waiting for you."

        hide erica_half
        with dissolve

        show gianni_half at right
        with dissolve

        g "Don’t rush to leave."
        g "The most important sounds often appear when you turn back one more time."

        hide gianni_half
        hide fran_half
        with dissolve

        menu:
            "Go back and keep searching":
                jump sala9_loop
            "Unlock all the Voices of Music":
                $ allow_leave_sala9 = True
                jump sala9_leave

    scene sala9main with fade

    show fran_half at left
    show erica_half at right
    with dissolve

    e "You’ve now gathered all the fragments of sound."

    hide erica_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "From harp and old strings, to experiment al keyboards, trumpeting signals, and voices captured on disc…"
    g "On paper, they’re unrelated — but inside you, they’ve linked up into a single line."

    g "What really matters now is this:"
    g "{i}Which of these sounds are you going to carry with you when you leave?{/i}"

    hide gianni_half
    hide fran_half
    with dissolve

    stop music fadeout 2.0

    jump museum_entrance


# =========================================
# Ending
# =========================================

label museum_entrance:

    scene ending_ticket_office with fade

    play music "TicketOffice - Frulingsstimmen Walzer.mp3" fadein 3.0 loop

    show fran_half at left
    show paola_half at right
    with dissolve

    p "Welcome back, Fran."
    p "You’ve been in the museum for quite a while."

    f "…Yes."
    f "It feels like I’ve walked a very long path."

    hide paola_half
    hide fran_half
    with dissolve

    narrator "All across {color=#c28b61}Bologna{/color}, there are forgotten fragments of the {color=#f788c0}Voices of Music{/color}."
    narrator "Once you truly hear them, the most beautiful side of this city finally opens up to you."

    show gianni_half at right
    with dissolve
    g "Congratulations, Fran."
    g "You’ve found all nine fragments."

    show fran_half at left
    with dissolve
    f "So… that sentence from the dream was real?"
    f "It was you all along — you were the voice speaking to me."

    g "Do you believe it now?"

    narrator "Gianni looks at you. There’s a hint of mischief in his eyes, and also a long-missing kind of gentleness."

    g "Since you’ve made it all the way to the end—"
    g "it’s only fair that I keep my promise from the beginning."

    hide fran_half
    hide gianni_half
    with dissolve

    jump ending_sky


label ending_sky:

    scene black with fade
    $ renpy.pause(1.0, hard=False)

    $ renpy.pause(1.0, hard=False)

    scene ending_bologna_sky with fade
    stop music fadeout 2.0
    play music "Whispering Realms.mp3" fadein 3.0 loop

    "Suddenly, the ground beneath your feet feels light, almost weightless."

    "When your vision comes back into focus, the whole city has unfolded beneath you."

    "A sea of red rooftops rolls away in waves, streets crossing between them like drawn lines."
    "In the distance you can make out towers, churches, the main square, all set into the evening light."

    show fran_half at left
    with dissolve

    f "…Is this… Bologna?"
    f "From up here, it really does look like one giant score."

    hide fran_half
    with dissolve

    show gianni_half at right
    with dissolve

    g "It was a song to begin with."
    g "Most of the time people are too busy getting from one place to another to remember to listen."

    g "You’ve heard the choirs in the churches, and the students playing on the street corners."
    g "You listened to voices from the past inside the museum,"
    g "and now you’re hearing the sound this city is making right now."

    hide gianni_half
    show fran_half at left
    with dissolve

    f "…The wind, the bells, people talking in the square…"
    f "and all those instruments I heard in the museum are still echoing in my ears."

    f "So the “most beautiful place” wasn’t one particular room, or one special object."
    f "It was—"

    f "—this moment, when I treat all of this as one piece of music being played around me."

    show gianni_half at right
    with dissolve

    g "Exactly."
    g "Music doesn’t live locked away in a museum."
    g "The museum just helps you line up the clues, so that once you walk back out, you can hear everything a little more clearly."

    g "From now on you’ll study here, live here, get lost, make mistakes, start again."
    g "All of that will become your own melody."
    g "As for me…"

    "Gianni’s voice grows softer. You feel the air gently shift around you."

    hide gianni_half
    with dissolve

    "He slowly fades from view, leaving only the breathing city at your feet."
    hide fran_half
    with dissolve

    $ renpy.pause(3.0, hard=False)

    "{color=#32a852}{size=42}When you leave the rooms behind, you don’t carry images of the objects with you — you carry their echoes.{/size}\n{size=32}In Bologna, sound never really disappears. It simply changes form, and keeps walking at your side.{/size}{/color}"

    $ renpy.pause(3.0, hard=False)

    menu:
        "Return to the main menu":
            return
        "Go back to the museum entrance":
            stop music fadeout 2.0
            jump ticketOffice
