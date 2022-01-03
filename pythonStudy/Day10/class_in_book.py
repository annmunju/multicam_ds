class Bicycle():

    def move(self, speed):
        print(f'자전거: 시속 {speed}킬로미터로 전진')

    def turn(self, direction):
        print(f'자전거 {direction}회전')

    def stop(self):
        print(f'자전거({self.weel_size}, {self.color}): 정지')

my_bicycle = Bicycle()
my_bicycle.weel_size = 26
my_bicycle.color = 'black'

my_bicycle.move(100)
my_bicycle.turn('좌')
my_bicycle.stop()