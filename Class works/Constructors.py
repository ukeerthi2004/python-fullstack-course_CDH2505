class Hotstar:
    def _init_(self,name):
        self.name = name
        print(f"Hey {self.name}!\nWelcome to the Hotstar")
    def playvideo(self):
        print("Ads will run")
        print("Limited access for videos")
        print("Limited Quality")
        print("Speed is limited upto 2x")
        print("Background run is not possible")
    def login(self):
        print("Limited logins")
    def search(self):
        print("You can search")
    def menu(self):
        print("You can see the menu ")
    def addtofav(self):
        print("You can add movies to the fav list")

class PremiumHotstar(Hotstar):
    def _init_(self,name):
        self.name = name
        print(f"Hey {self.name}")
        print("Welcome to the Hotstar")
    def playvideo(self):
        print("No ads will run")
        print("access for all videos")
        print("High Quality")
        print("Speed is upto 4x")
        print("Background run is Possible")
    def login(self):
        print("Muliple  logins")

sathwik = PremiumHotstar()
sathwik.playvideo()
sathwik.login()
sathwik.search()
sathwik.addtofav()
sathwik.menu()
vinay = Hotstar()
vinay.playvideo()
vinay.login()
vinay.search()
vinay.addtofav()
vinay.menu()


