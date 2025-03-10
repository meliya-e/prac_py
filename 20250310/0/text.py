import cmd
import calendar

class textcal(cmd.Cmd):
    prompt = "calendar> "
    tc = calendar.TextCalendar()
    Month = {m.name: m.value for m in calendar.Month}
    
    def help_prmonth(self):
        print("Print a month’s calendar")

    def help_pryear(self):
        print("Print the calendar for an entire year")

    def do_prmonth(self, arg):
        year, month = arg.split()
        self.tc.prmonth(int(year), self.Month[month])

    def do_pryear(self, arg):
        self.tc.pryear(int(arg))

    def do_EOF(self, arg):
        return True

    def complete_prmonth(self, text, line, begidx, endidx):
        return [m for m in self.Month if m.startwith(text)] 

    #def complete_pryear(self, text, line, begidx, endidx):
        
if __name__ == '__main__':
    textcal().cmdloop()
