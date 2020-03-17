import pygame
import sys
import math
import pygame.gfxdraw


spelplan = [["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"],
          ["0","0","0","0","0","0","0"]]
 
spelade_drag = [] # Irrelevant?
 
def valid_move(rad, kolumn):
  if kolumn < 0 or rad < 0 or kolumn > 6 or rad > 5 or spelplan[0][kolumn] != "0":
      return False
  return True
 
def p1move(rad, kolumn):
  if valid_move(rad, kolumn):
      if spelplan[5][kolumn] == "0":
          spelplan[5][kolumn] = "1"
          spelade_drag.append((5, kolumn, "p1"))
      elif spelplan[rad][kolumn] == "1" or spelplan[rad][kolumn] == "2":
          spelplan[rad-1][kolumn] = "1"
          spelade_drag.append((rad-1, kolumn, "p1"))
      else:
          p1move(rad + 1, kolumn)
  else:
      print("Inga slots lediga, försök igen!")
      
   
     
 
def p2move(rad, kolumn):
  if valid_move(rad, kolumn):
      if spelplan[5][kolumn] == "0":
          spelplan[5][kolumn] = "2"
          spelade_drag.append((5, kolumn, "p2"))
      elif spelplan[rad][kolumn] == "1" or spelplan[rad][kolumn] == "2":
          spelplan[rad - 1][kolumn] = "2"
          spelade_drag.append((rad-1, kolumn, "p2"))
      else:
          p2move(rad + 1, kolumn)
  else:
      print("Inga slots lediga, försök igen!")
     
 
def checkp1_win():
 for i in range(5):                # kollar vågrät vinst
     for j in range(3):
         if spelplan[j][i] == "1" and spelplan[j+1][i] == "1" and spelplan[j+2][i] == "1" and spelplan[j+3][i] == "1":
             return True
 
 for j in range(6):                # kollar lodrät vinst
     for i in range(2):
         if spelplan[j][i] == "1" and spelplan[j][i+1] == "1" and spelplan[j][i+2] == "1" and spelplan[j][i+3] == "1":
             return True
 
 for j in range(3):                # kollar negativ diagonal
     for i in range(4):
         if spelplan[j][i] == "1" and spelplan[j+1][i+1] == "1" and spelplan[j + 2][i + 2] == "1" and spelplan[j + 3][i + 3] == "1":
             return True
 
 for j in range(5, 0, -1):         # kollar positiv diagonal
     for i in range(4):
         if spelplan[j][i] == "1" and spelplan[j-1][i+1] == "1" and spelplan[j-2][i+2] == "1" and spelplan[j-3][i+3] == "1":
             return True
 return False
def checkp2_win():
 for i in range(5):                #kollar vågrät vinst
     for j in range(3):
         if spelplan[j][i] == "2" and spelplan[j+1][i] == "2" and spelplan[j+2][i] == "2" and spelplan[j+3][i] == "2":
             return True
 
 for j in range(6):                # kollar lodrät vinst
     for i in range(2):
         if spelplan[j][i] == "2" and spelplan[j][i+1] == "2" and spelplan[j][i+2] == "2" and spelplan[j][i+3] == "2":
             return True
            
 for j in range(3):                # kollar negativ diagonal
     for i in range(4):
         if spelplan[j][i] == "2" and spelplan[j+1][i+1] == "2" and spelplan[j + 2][i + 2] == "2" and spelplan[j + 3][i + 3] == "2":
             return True
 
 for j in range(5, 0, -1):         # kollar positiv diagonal
     for i in range(4):
         if spelplan[j][i] == "2" and spelplan[j-1][i+1] == "2" and spelplan[j-2][i+2] == "2" and spelplan[j-3][i+3] == "2":
             return True
 return False
 

def rita_ut():
    for i in spelplan:
        print(i)
    return spelplan


pygame.init()           ## Tar med alla pygamemoduler

kolumner = 7
rader = 7
squaresize = 100   ## Antal pixlar för varje spelruta
width = kolumner * squaresize   ## Skärmens bredd
height = rader * squaresize     ## Skärmens höjd

size = (width, height)

radie = int(squaresize/2-5)        ## Måttet för cirklarna, -5 för att lämna fem pixlar av blått i varje square


blå = (0,0,255)
svart = (0,0,0)
röd = (255,0,0)
gul = (255,255,0)


def draw_board():      ## Funktion för att ge spelplanen grafik
    for c in range(kolumner):
        for r in range(rader):
            pygame.draw.rect(screen, blå, (c*squaresize, r*squaresize+squaresize, squaresize, squaresize))        ## Rita rektanglar som är spelplanen och en extra squaresize för det svarta utrymmet högst upp
            pygame.draw.circle(screen, svart, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize/2)), radie)          ## Rita cirklar i de blå rektanglarna
    pygame.display.update()


def gameplay():        ## Funktion för att rita ut brickorna
    if len(spelade_drag) % 2 == 0:
        if 45 < posx < 55  or 145 < posx < 155 or 245 < posx < 255 or 345 < posx < 355 or 445 < posx < 455 or 545 < posx < 555 or 645 < posx < 655 or 745 < posx < 755:  ## Om musklicket sker inom 10 pixlar från cirkelns center
            if 145 < posy < 155 or 245 < posy < 255 or 345 < posy < 355 or 445 < posy < 455 or 545 < posy < 555 or 645 < posy < 655 or 745 < posy < 755:
                pygame.gfxdraw.filled_circle(screen, posx, posy, int(squaresize/2-5), röd)        ## Ritar ut en cirkel i samma storlek som de svarta, fast annan färg.
    elif len(spelade_drag) % 2 != 0:
        if 45 < posx < 55  or 145 < posx < 155 or 245 < posx < 255 or 345 < posx < 355 or 445 < posx < 455 or 545 < posx < 555 or 645 < posx < 655 or 745 < posx < 755:  ## Om musklicket sker inom 10 pixlar från cirkelns center
            if 145 < posy < 155 or 245 < posy < 255 or 345 < posy < 355 or 445 < posy < 455 or 545 < posy < 555 or 645 < posy < 655 or 745 < posy < 755:
                pygame.gfxdraw.filled_circle(screen, posx, posy, int(squaresize/2-5), gul)      ## Ritar ut en cirkel i samma storlek som de svarta, fast annan färg.
    pygame.display.update()

screen = pygame.display.set_mode(size)      ## Behövs för att få upp skärmen,
draw_board()        ## Rita ut brädet

runda = 0  ## P1 eller P2

while True:
    
    for event in pygame.event.get():        ##fönstret stängs inte
        if event.type == pygame.QUIT:  ## så man kan stänga programmet i krysset
              sys.exit()
        
        count = len(spelade_drag)  

        if event.type == pygame.MOUSEBUTTONDOWN: # action vid musklick 
            print(event.pos)
              
            if count % 2 == 0:                  ## Båda körde samtidigt, så behövde hålla koll på vems runda det är
                ## SPELARE 1s DRAG
                posx = event.pos[0]         ## Tar elementen i tupeln av position i (x,y) vid musklick. Dvs positionen på X-axeln resp. Y-axeln.
                posy = event.pos[1]        ## och man vet då vilken kolumn(X) eller rad(Y) eftersom varje kolumn/rad är inom spannet på 100 pixlar 
                if 45 < posx < 55  or 145 < posx < 155 or 245 < posx < 255 or 345 < posx < 355 or 445 < posx < 455 or 545 < posx < 555 or 645 < posx < 655 or 745 < posx < 755:  ## Om pilen är inom 10 pixlar från cirkelns center
                    if 145 < posy < 155 or 245 < posy < 255 or 345 < posy < 355 or 445 < posy < 455 or 545 < posy < 555 or 645 < posy < 655 or 745 < posy < 755:
                        val = int(math.floor(posx/squaresize))      ## Istället för att man skriver in 1-7 så ser den vart man trycker. Floor returnerar största möjliga int, men inte större än x. dvs att istället för att kolumn 2 har ett värde på 200-299, får den värdet 2. Jämfört med att skriva 2 i terminalen.
                        p1move(0, val)
                        rita_ut()
                        gameplay() ## Lägger ut en bricka
                        p1win = checkp1_win()   
                        if p1win == True:
                            print("P1 wins")
                            break
                        runda += 1
                        
            elif count % 2 == 1:
                ## SPELARE 2s DRAG
                posx = event.pos[0]
                posy = event.pos[1]
                if 45 < posx < 55  or 145 < posx < 155 or 245 < posx < 255 or 345 < posx < 355 or 445 < posx < 455 or 545 < posx < 555 or 645 < posx < 655 or 745 < posx < 755:  
                     if 145 < posy < 155 or 245 < posy < 255 or 345 < posy < 355 or 445 < posy < 455 or 545 < posy < 555 or 645 < posy < 655 or 745 < posy < 755:
                        val = int(math.floor(posx/squaresize)) 
                        p2move(0, val)
                        rita_ut()
                        gameplay()
                        p2win = checkp2_win()
                        if p2win == True:
                            print("P2 wins")
                            break
                        runda += 1
    
                        
            runda = runda % 2 
            



