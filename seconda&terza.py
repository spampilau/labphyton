# moltiplicare due numeri inseriti dall'utente
  # a = input('Scrivi un numero');
  # b = input('Scrivi il numero per cui vuoi moltiplicare')
  # c = int(a) * int(b)
  # print('il tuo numero moltiplicato per', b, 'è:', c)


#creao file turtle
import turtle 
  #lezione del 10 marzo
def d_square(t, size, direction) :
  for i in [0,1,2,3]: 
        t.forward(size)       
        t.left(direction)
def d_triangle(r, size, direction) :
  for i in [0,1,2]: 
        r.forward(size)       
        r.right(direction)
def sum(a, b) :
  s = a + b
  return s
def koch(t, order, size):
  if order == 0:
      t.forward(size)
  else:
      for angle in [60, -120, 60, 0]:
         koch(t, order-1, size/3)
         t.left(angle)
      
#lezione del 5 marzo
window = turtle.Screen()
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()

a.color('blue') #cambiamo colore
b.color('orange')
#lezione del 10 marzo 
# d_square(a, 50, 90)
# d_triangle(b, 80, 120)
# koch(a, 4,1000)
first = input('Scrivi il primo numero');
second = input('Scrivi il secondo numero');
print(sum(int(first), int(second)))

'''
#lezione 5 marzo
#facciamo fare ad a un quadrato
for i in [0,1,2,3]: #oppure for i in range (0. 4) 
        a.forward(50)       
        a.left(90)   
# a.forward(50)
# a.left(90)
# a.forward(50)
# a.left(90)
# a.forward(50)
# a.left(90)

#facciamo fare ad b un triangolo 

b.forward(80)       
b.right(120)         
b.forward(80)
b.right(120)
b.forward(80)

#facciamo un quadrato colorato
for i in ['red','pink','orange','green', 'blue', 'dark violet', 'black', 'dark blue']: 
        c.color(i)
        c.forward(80)       
        c.right(100)
        c.forward(20)

#loop della window 
'''
  
window.mainloop()