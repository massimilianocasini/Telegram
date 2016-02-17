import math
print "-" * 60, "\n"
print "\t" * 2 ,"CALCOLATRICE", "\n"
print "Completamente sviluppato da Alessandro Alfieri.\n" 
print "Licenza: Open Source "
print "Data: 17 Novembre 2010"
print "-" * 60, "\n" * 2

print "Scegli l'operazione che vuoi fare..."
print "1:Addizione-Sottrazione-Moltiplicazione-Divisione"
print "2:Elevazione a potenza"
print "3:Radice"
print "4:Esci"
print "\n" * 3
def Scelta(x):
   

   if x == 1:
      print input("Scrivi il calcolo: ")
      Scelta(input ("Scegli l'operazione: "))

   elif x == 2:
      print input("Scrivi numero: ") ** input("Scrivi esponente: ")
      Scelta(input ("Scegli l'operazione: "))

   elif x == 3:
      print math.sqrt (input("Scrivi numero: "))
      Scelta(input ("Scegli l'operazione: "))

   elif x == 4:
      clear()
      print "-" * 60, "\n"
      print "\tGRAZIE PER AVER SCARICATO QUESTA CALCOLATRICE", "\n"
      print "\t" * 2, "Alessandro Alfieri"
      print "-" * 60, "\n"
      exit()
  
   else:
    clear()
    print "Scelta sbagliata, amico! Fatti meno seghe cosi' vedi meglio i numeri!!! ;)", "\n"
    print "Scegli l'operazione che vuoi fare..."
    print "1:Addizione-Sottrazione-Moltiplicazione-Divisione"
    print "2:Elevazione a potenza"
    print "3:Radice"
    print "4:Esci"
    Scelta(input ("Scegli l'operazione: "))

def clear():
    import os
    if os.name == "posix": os.system("clear")
    elif os.name == "nt": os.system("cls")
    else: print "\n" * 40 
    


Scelta(input ("Scegli l'operazione: "))

