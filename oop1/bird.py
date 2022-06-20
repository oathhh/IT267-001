from turtle import color


bird_type = 'parrot'
class Bird:
    #class variable
    bird_name = 'peter'

    def __init__(self) -> None:
        #instance variable
        self.color = color

        #local variable
        contry = 'Thailand'
        print (contry)

    def show(self):
        return f'{Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    my_bird = Bird('Red,Yellow')
    print(bird_type)
    print(my_bird.color)
    print(my_bird.bird_name)
