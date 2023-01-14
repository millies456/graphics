
from graphics import * #import functions



def design():
    #window size
    win = GraphWin ('circle design', 700,700)
    #each c creates a circle the first two are the coordinates and since i want to put everything in the middle its half of my window
    c= Circle(Point(350,350),350)
    c.draw(win)
    c.setFill('black')
    c.setOutline('black')

    c2 = Circle(Point(350,350),325)
    c2.draw(win)
    c2.setFill('red')
    c2.setOutline('black')

    c3 = Circle(Point(350,350),300)
    c3.draw(win)
    c3.setFill('yellow')
    c3.setOutline('black')

    c4 = Circle(Point(350,350),275)
    c4.draw(win)
    c4.setFill('orange')
    c4.setOutline('black')

    c5 = Circle(Point(350,350),250)
    c5.draw(win)
    c5.setFill('purple')
    c5.setOutline('black')

    c6= Circle(Point(350,350),225)
    c6.draw(win)
    c6.setFill('green')
    c6.setOutline('black')

    c7= Circle(Point(350,350),200)
    c7.draw(win)
    c7.setFill('blue')
    c7.setOutline('black')

    c8= Circle(Point(350,350),175)
    c8.draw(win)
    c8.setFill('purple')
    c8.setOutline('black')

    c9= Circle(Point(350,350),150)
    c9.draw(win)
    c9.setFill('yellow')
    c9.setOutline('black')

    c10 = Circle(Point(350,350),125)
    c10.draw(win)
    c10.setFill('green')
    c10.setOutline('black')

    c11 = Circle(Point(350,350),100)
    c11.draw(win)
    c11.setFill('red')
    c11.setOutline('white')

    c12 = Circle(Point(350,350),75)
    c12.draw(win)
    c12.setFill('blue')
    c12.setOutline('white')

    c13 = Circle(Point(350,350),50)
    c13.draw(win)
    c13.setFill('white')
    c13.setOutline('white')

    c14 = Circle(Point(350,350),50)
    c14.draw(win)
    c14.setFill('red')
    c14.setOutline('white')

    c15 = Circle(Point(350,350),50)
    c15.draw(win)
    c15.setFill('white')
    c15.setOutline('white')

    
    c16 = Circle(Point(350,350),25)
    c16.draw(win)
    c16.setFill('blue')
    c16.setOutline('white')


    c19 = Circle(Point(350,350),15)
    c19.draw(win)
    c19.setFill('yellow')
    c19.setOutline('white')



    c17 = Circle(Point(350,350),5)
    c17.draw(win)
    c17.setFill('pink')
    c17.setOutline('white')


    
    c18 = Circle(Point(350,350),2)
    c18.draw(win)
    c18.setFill('red')
    c18.setOutline('white')


    win.setBackground('white')

    
    win.getMouse() 
    win.close()

design()