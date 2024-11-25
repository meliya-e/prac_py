class Sender:
    priznak = True
    @classmethod
    def report(cls):
        if cls.priznak:
            print("Greetings!")
            cls.priznak = False
        print("Get away")

class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            i.report()

a, b, c = Sender(), Sender(), Sender()
Asker().askall([a, b, c, a, b, c])
