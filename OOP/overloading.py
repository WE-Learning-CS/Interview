''' 공식적으로 지원하지 않기 때문에 다른 방법을 활용해야 한다.'''
class OverLoading():
    def exam(self, name):
        print(name)
        
    def exam(self, name, number = 0):
        print(name, number)
        
    def exam(number, name):
        print(name, number)
        
o = OverLoading()
o.exam('Kim')
o.exam('Kim', 1)