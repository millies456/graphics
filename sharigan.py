
from graphics import * #import everything



def main():
    #window size
    win = GraphWin ('circle design', 200,200)
    #each c creates a circle the first two are the coordinates and since i want to put everything in the middle its half of my window
    eyes= Circle(Point(100,100),100)
    eyes.draw(win)
    eyes.setFill('black')
    eyes.setOutline('black')

    eyes= Circle(Point(100,100),98)
    eyes.draw(win)
    eyes.setFill('red')
    eyes.setOutline('black')

    eyes= Circle(Point(100,100),60)
    eyes.draw(win)
    eyes.setFill('black')
    eyes.setOutline('black')

    eyes= Circle(Point(100,100),58)
    eyes.draw(win)
    eyes.setFill('red')
    eyes.setOutline('black')

    eyes= Circle(Point(100,100),10)
    eyes.draw(win)
    eyes.setFill('black')
    eyes.setOutline('black')

    eyes= Circle(Point(100,42),10)
    eyes.draw(win)
    eyes.setFill('black')
    eyes.setOutline('black')

    eyes= Circle(Point(100,160),10)
    eyes.draw(win)
    eyes.setFill('black')
    eyes.setOutline('black')

    eyes= Polygon(Point(100,160),Point(100,130),Point(98,160))
    eyes.draw(win)
    eyes.setFill('green')
    eyes.setOutline('black')

    eyes= Polygon(Point(100,42),Point(100,60),Point(98,42))
    eyes.draw(win)
    eyes.setFill('green')
    eyes.setOutline('black')





   

    win.setBackground('white')

    
    win.getMouse() 
    win.close()

main()