import time
import os


input_file = os.getcwd() + "/" + input("What file do you want to read? (NB! with .txt at the end)")
#input_word = input("What word would you like to find the frequency of? (NB! Only letters or numbers)")

print(input_file)


# Oppgave 1
# finne og hente tekst fra fil, telle alle ord og finne ordfrekvens

# åpner filen 'r' fra 'input' og lagrer dette som 'file'
file = open(input_file, "r")

file_txt = str(file.read())



# funksjon som fjerner symboler som ikke er relevante før ordtelling
def clean_count(text, chosen_word):

    chars = "\\`*_{}[]()>#+.,?!$"

# for løkke som går gjennom teksten etter uønskede karakterer fra 'chars' og erstatter dette med mellomrom 
    for c in chars:

# sjekker om teksten er fri for uønskede karakterer
        if c in text:
            text = text.replace(c, " ")

# etter tekst er sjekket for karakterer går funksjonen videre
        if c not in text:




# gjør om rettet 'text' til ord med 'split' og teller antall ord i 'text_len'
            text_words = text.split()
            text_len = len(text_words)

# 'total_list' til fremtidig fylling og skriving av 'new_file'
            total_list = []

            for word in text_words:
                current_word = word

# går gjennom tekst etter 'current_word'og teller antall ganger i 'count_word'
                count_word = []
                for w in text_words:
                    if w == current_word:
                        count_word.append(w)

                total_list.append([current_word, len(count_word)])

# skriver hele 'total_list' når den er ferdig


# går gjennom 'total_list' etter 'chosen_word'og finner antall ganger ordet dukker opp 'total_list[i][1]'
    a = []
    for i in range(0, len(total_list), 1):

        if total_list[i][0] == chosen_word:
            a = total_list[i][1]


# regner 'word_frequency' til 'chosen_word' med 'count_word' og 'text_len'
    word_frequency = (a/text_len)




# Oppgave 3
# lagre resultater som fil med antall ord som filnavn, hvor hver linje er ett ord fra teksten og hvor mange ganger det dukker opp


    new_file = open(str(text_len), "w+")
    
# for-løkke som er ment for å skrive hver linje i 'total_list' inn i 'new_file'
    with open(str(text_len), 'w') as f:
        for element in total_list:
            f.write("%s\n" % element)
        

# får ikke denne til å skrive 'total_list' siden det ikke er string, men en liste

# printer sentrale objekter når retting er ferdig
    print(text)
    print(text_words)
    print(total_list)
    
    print(text_len)
    print(a)
    print(word_frequency)
    while not input("Enter any button to exit"): time.sleep(0.1)

clean_count(file_txt, "the")


