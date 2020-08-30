list = []

txt = "dette er en tekst som skal deles opp.hva skjer, dersom dette er vanskelig, med punktum?"


chars = "\\`*_{}[]()>#+-.,?!$"
for c in chars:
    if c in txt:
        txt = txt.replace(c, " ")

# Problemer dersom tekst ikke skrevet rett, feks manglende mellomrom mellom punktum eller andre tegn


list = txt.split()

print(txt)


print(list)