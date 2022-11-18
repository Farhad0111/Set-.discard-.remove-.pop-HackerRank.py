class Farhad:
    def Faru(self):
        self.a=int(input())
        self.b=set(list(map(int,input().split())))
        self.c=int(input())
        for i in range(0,self.c):
            p=input().split()
            if p[0]=='remove':
                self.b.remove(int(p[1]))
            elif p[0]=='discard':
                self.b.discard(int(p[1]))
            else:
                self.b.pop()
        print(sum(self.b))
farhad=Farhad()
farhad.Faru()