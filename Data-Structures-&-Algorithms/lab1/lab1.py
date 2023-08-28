class AssignmnetList:
    def __init__(self):
        self.list = []

    def additem(self,obj):
        self.list.append(obj)

        #score, totalpoint, totalweight

    def compute(self):
        sum = 0
        for i in self.list:
            sum += (i.gettotalweight() * (i.setscore / i.gettotalpoint()) / i.gettotalweight())
        return sum


    def tostring(self):
        for i in self.list:
            string = i.tostring()

class Assignment:
    def __init__(self, name, month, day, hour, minute, score, totalpoint, totalweight):
        self.name = name
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.score = score
        self.totalpoint = totalpoint
        self.totalweight = totalweight

    def getname(self):
        return self.name

    def getmonth(self):
        return self.month

    def getday(self):
        return self.day

    def gethour(self):
        return self.hour

    def getminute(self):
        return self.minute

    def getscore(self):
        return self.score

    def gettotalpoint(self):
        return self.totalpoint

    def gettotalweight(self):
        return self.totalweight

    def setscore(self, score):
        self.setscore = score

    def settotalpoint(self, totalpoint):
        self.totalpoint = totalpoint

    def settotalweight(self, totalweight):
        self.totalweight = totalweight


    def toString(self):
        name = str(self.name)
        month = str(self.month)
        score = str(self.score)
        day = str(self.day)
        totalpoint = str(self.totalpoint)
        return(self.name, self.month, self.score, self.day, self.totalpoint, self.hour)


class Lab(Assignment):
    def __init__(self, name, month, day, hour, minute, score, totalpoint, totalweight, specification):
        super().__init__(name, month, day, hour, minute, score, totalpoint, totalweight)
        self.specification = specification
    def toString(self):
        super().toString()

class Project(Assignment):
    def init(self, name, month, day, hour, minute,score, totalpoint, totalweight, datafile, specification):
        super().__init__(name, month, day, hour, minute, score, totalpoint, totalweight)
        self.specification = specification
        self.datafile = datafile

    def toString(self):
        super().toString()


def main():
    labobj = Lab('kiran', 6, 25, 3, 6, 88, 44, 7, 'specific')
    projectobj = Project('kiran', 6, 25, 6, 88, 44, 8, 50, 'lab3txt','Programming')
    asslistobj = AssignmnetList()
    asslistobj.additem(labobj)

    asslistobj = AssignmnetList()
    asslistobj.additem(projectobj)
    print(asslistobj.compute())
    asslistobj.tostring()


    print(labobj.toString())
    print(projectobj.tostring())

main()

