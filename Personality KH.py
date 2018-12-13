import pyautogui as pg
import webbrowser as wb
import time as t

points = 0

show = pg.prompt("What is your favorite show? ")

if show =="New Girl":
    wb.open("https://www.youtube.com/watch?v=aW3LEVGQ-lE")
    pg.alert("That is a really good show!")
    points -= 5
    t.sleep(3)
elif show == "Peppa Pig":
    wb.open("https://www.youtube.com/watch?v=DP1pQkm9Op0")
    pg.alert("So good!")
    points += 20
    t.sleep(3)
elif show =="Barbie Life in the Dream House":
    wb.open("https://www.youtube.com/watch?v=Ky_k3Tfvkoo")
    pg.alert("yas kween")
    points -= 3
    t.sleep(3)
elif show =="South Park":
    pg.alert("kewl")
    t.sleep(3)
elif show =="Caillou":
    wb.open("https://www.youtube.com/watch?v=H8u6gON8X6E")
    pg.alert("love that show")
    points += 10
    t.sleep(3)
elif show =="Impractical Jokers":
    wb.open("https://www.youtube.com/watch?v=0SKut-tRK4U ")
    pg.alert("nice!")
    points -= 2
    t.sleep(3)
else:
      pg.alert("Your favorite show is " + show)

sport = pg.prompt("What is your favorite sport? ")

if sport =="Lacrosse":
    pg.alert("same!!")
    points += 14
    wb.open("https://www.youtube.com/watch?v=dFEGWC9NM9A")
    t.sleep(3)
elif sport =="Soccer":
     wb.open("https://www.youtube.com/watch?v=TY4TM7dV1YU")
     pg.alert("cool!")
     points += 6
     t.sleep(3)
elif sport =="Hockey":
     pg.alert("ew gross todd plays")
     points -= 10
     t.sleep(3)
elif sport =="gymnastics":
     wb.open("https://www.youtube.com/watch?v=HFbKJiUG_7I")
     pg.alert("k")
     points -= 2
     t.sleep(3)
elif sport =="Curling":
     wb.open("https://www.youtube.com/watch?v=WXHh_wadqPw")
     pg.alert("good sport good sport")
     points += 7
     t.sleep(3)
elif sport =="football":
     pg.alert("ok")
     points += 12
     t.sleep(3)
else:
    pg.alert("Your favorite sport is " + sport)

subject = pg.prompt("What is your favorite subject? ")          

if subject =="Science":
    pg.alert("um ok, doesn't compare to el")
    wb.open("https://www.youtube.com/watch?v=sinQ06YzbJI")
    points -= 3
    t.sleep(3)
elif subject =="Math":
     wb.open("https://www.youtube.com/watch?v=EgjCLhoI9Mk")
     pg.alert("wrong.")
     points -= 12
     t.sleep(3)
elif subject =="Spanish":
     wb.open("https://www.youtube.com/watch?v=dBTGxLc-lv0")
     pg.alert("hola")
     points += 6
     t.sleep(3)
elif subject =="Computer Science":
     pg.alert("ok")
     points += 1
     t.sleep(3)
elif subject =="history":
     wb.open("https://www.youtube.com/watch?v=xn5wcMX9Jb0")
     pg.alert("k")
     points += 16
     t.sleep(3)
elif subject =="Mr.Bowes office":
     wb.open("https://www.youtube.com/watch?v=z6I-AEm7lTI")
     pg.alert("peyton...")
     points -= 9
     t.sleep(3)
else:
    pg.alert("Your favorite subject is " + subject)

person = pg.prompt("Who is your favorite person? ")

if person =="Todd":
     wb.open("https://www.youtube.com/watch?v=rtwCkm-rVx0 ")
     pg.alert("lillian confused face")
     points += 15
     t.sleep(3)
elif person =="Sofia":
     wb.open("whttps://www.youtube.com/watch?v=RPoBE-E8VOc")
     pg.alert("it should be eleanor")
     points += 16
     t.sleep(3)
elif person =="Kate":
     pg.alert("correct")
     points += 100
     t.sleep(3)
elif person =="Nicky":
     wb.open("https://www.youtube.com/watch?v=XTgFtxHhCQ0")
     pg.alert("oh")
     points += 17
     t.sleep(3)
elif person =="Peyton":
     pg.alert("why")
     points -= 4
     t.sleep(3)
elif person =="Alex":
     wb.open("https://www.youtube.com/watch?v=UIAcxSSwN1o")
     pg.alert("spizziri pledge")
     points += 60
     t.sleep(3)
    
else:
    pg.alert("Your favorite person is " + person)

food == pg.prompt("What is your favorite person? ")

if food =="pasta":
     wb.open("https://www.youtube.com/watch?v=JGBE3eLpvm0")
     pg.alert("yum")
     points += 8
     t.sleep(3)
elif food =="pancakes":
    wb.open("https://www.youtube.com/watch?v=XDSDaFhOuo4")
    pg.alert("same")
    points += 22
    t.sleep(3)
elif food =="cheese":
     wb.open("https://www.youtube.com/watch?v=5p5JvZxr4iM")
     pg.alert("cool")
     points -= 10
     t.sleep(3)
elif food =="chocolate cake":
     pg.alert("want that right now")
     points += 1
     t.sleep(3)

else:
    pg.alert("Your favorite person is " + food)
pg.alert(points)

