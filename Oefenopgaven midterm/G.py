positie_naar_beneden = 1
positie_naar_links = 2
positie_naar_rechts = 5
positie_omlaag = 4
positie_omhoog = 3
positie_naar_boven = 6

worpen = int(input())

for i in list(range(0,worpen)):
    richting = input()
    if richting == 'omhoog':
        dummy = positie_omlaag
        positie_omlaag = positie_naar_beneden
        positie_naar_beneden = positie_omhoog
        positie_omhoog = positie_naar_boven
        positie_naar_boven = dummy
    elif richting == 'rechts':
        dummy = positie_naar_links
        positie_naar_links = positie_naar_beneden
        positie_naar_beneden = positie_naar_rechts
        positie_naar_rechts = positie_naar_boven
        positie_naar_boven = dummy
    elif richting == 'omlaag':
        dummy = positie_omhoog
        positie_omhoog = positie_naar_beneden
        positie_naar_beneden = positie_omlaag
        positie_omlaag = positie_naar_boven
        positie_naar_boven = dummy
    elif richting == 'links':
        dummy = positie_naar_rechts
        positie_naar_rechts = positie_naar_beneden
        positie_naar_beneden = positie_naar_links
        positie_naar_links = positie_naar_boven
        positie_naar_boven = dummy

print(positie_naar_boven)