coffeetypes = open("/Users/a1209899754/Desktop/coffeetypes.txt" , "r")
import turtle
def coffeedefinition(x):
    if x == "yes":
        y = eval(input("Would you like to add some water in it？  "))
        if y == "yes":
            print("ok,wait a minute,let me add some watter.")
            y = 1
            z = eval(input("Would you like to add some milk？  "))
            if z == "yes":
                l = eval(input("How much milk do you wanna add?  "))
                a = eval(input("Add some milk foam sir/lady?   "))
                if a == "yes":
                    d = eval(input("how much MF do you want?   "))
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                         
                if a == "no":
                    d = 2
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
            if z == "no":
                l = 2
                a = eval(input("Add some milk foam sir/lady?   "))
                if a == "yes":
                    d = eval(input("how much MF do you want?   "))
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2 
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                if a == "no":
                    d = 2
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                
        if y == "no":
            y = 2
            z = eval(input("Would you like to add some milk？  "))
            if z == "yes":
                l = eval(input("How much milk do you wanna add?  "))
                a = eval(input("Add some milk foam sir/lady?   "))
                if a == "yes":
                    d = eval(input("how much MF do you want?   "))
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                                
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                                
                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                                
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

                if a == "no":
                    d = 2
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                                
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                                
                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and (int(list[1])-10) < l < (int(list[1])+10) and (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                         
            if z == "no":
                l = 2
                a = eval(input("Add some milk foam sir/lady?   "))
                if a == "yes":
                    d = eval(input("how much MF do you want?   "))
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")
                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  (int(list[2])-10) < d < (int(list[2])+10) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

                         
                if a == "no":
                    d = 2
                    f = eval(input("Some caramel?  "))
                    if f == "yes":
                        f = 1
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

                    if f == "no":
                        f = 2
                        t = eval(input("And what about the chocolate?  "))
                        if t == "yes":
                            t = 1
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

                        if t == "no":
                            t = 2
                            print("ok, let's make a drink!")
                            for line in coffeetypes:
                                list = line.split()
                                if y == int(list[0]) and l == int(list[1]) and  d == int(list[2]) and f == int(list[3]) and t == int(list[4]):
                                    print("you make a new coffee -----",list[5])
                            print("That was a really nice drink!")
                            h = (eval(input("Do you want to add some pigment to your coffee in order to make it more beatiful?   ")))
                            if h == "yes":
                                paintCoffee(eval(input("What kind of color that you want?   ")))
                            if h =="no":
                                paintCoffee("black")

    if x == "no":
        print("Welcome back next time!")

    
def paintCoffee(i):
    import random
    turtle.pensize(3)
    x = eval(input("What kind of size of coffee that you want?  "))
    if x == "large":
        turtle.pencolor("cyan")
        turtle.penup()
        turtle.circle(120,90)
        turtle.pendown()
        turtle.circle(120,180)
        turtle.left(90)
        turtle.forward(240)
        turtle.fillcolor(i)
        turtle.begin_fill()
        turtle.right(180)
        turtle.fd(40)
        turtle.pencolor("brown")
        turtle.left(90)
        turtle.fd(280)
        turtle.right(90)
        turtle.fd(160)
        turtle.right(90)
        turtle.fd(280)
        turtle.end_fill()
        turtle.right(90)
        turtle.fd(160)
        turtle.left(90)
        turtle.penup()
        turtle.forward(70)
        turtle.pendown()
        turtle.pencolor("green")
        turtle.right(30)
        turtle.fd(80)
        turtle.fillcolor("pink")
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()
        turtle.right(30)
        turtle.fd(35)
        print("here you go, large size of a cup of coffee, enjoy!")
    if x == "middle":
        turtle.pencolor("cyan")
        turtle.penup()
        turtle.circle(90,90)
        turtle.pendown()
        turtle.circle(90,180)
        turtle.left(90)
        turtle.forward(180)
        turtle.fillcolor(i)
        turtle.begin_fill()
        turtle.right(180)
        turtle.fd(30)
        turtle.pencolor("brown")
        turtle.left(90)
        turtle.fd(230)
        turtle.right(90)
        turtle.fd(120)
        turtle.right(90)
        turtle.fd(230)
        turtle.end_fill()
        turtle.right(90)
        turtle.fd(120)
        turtle.left(90)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.pencolor("green")
        turtle.right(30)
        turtle.fd(60)
        turtle.fillcolor("pink")
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()
        turtle.right(30)
        turtle.fd(25)
        print("here you go, middle size of a cup of coffee, enjoy!")
    if x == "small":
        turtle.pencolor("cyan")
        turtle.penup()
        turtle.circle(60,90)
        turtle.pendown()
        turtle.circle(60,180)
        turtle.left(90)
        turtle.forward(120)
        turtle.fillcolor(i)
        turtle.begin_fill()
        turtle.right(180)
        turtle.fd(20)
        turtle.pencolor("brown")
        turtle.left(90)
        turtle.fd(160)
        turtle.right(90)
        turtle.fd(80)
        turtle.right(90)
        turtle.fd(160)
        turtle.end_fill()
        turtle.right(90)
        turtle.fd(80)
        turtle.left(90)
        turtle.penup()
        turtle.forward(34)
        turtle.pendown()
        turtle.pencolor("green")
        turtle.right(30)
        turtle.fd(30)
        turtle.fillcolor("pink")
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()
        turtle.right(30)
        turtle.fd(15)
        print("here you go, small size of a cup of coffee, enjoy!")

        
        
coffeedefinition(eval(input("Do you want to drink some coffee?  ")))
