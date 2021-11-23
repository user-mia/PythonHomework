class Animal:

    def eat(self):
        print('我是动物，我需要吃')

    def sleep(self):
        print('我是动物，我需要睡')


class Rabbit(Animal):
    def eat(self):
        print("我是兔子，我吃艹")

    def sleep(self):
        print('我是兔子，我要睡觉！')


class Tiger(Animal):
    def eat(self):
        print('我是老虎，我出肉')

    def sleep(self):
        print('我是兔子，我要睡觉！')


def eat(Animal1: 'Animal'):
    Animal1.eat()


def sleep(Animal1: 'Animal'):
    Animal1.sleep()


rabbit = Rabbit()
tiger = Tiger()
eat(rabbit)
sleep(rabbit)

eat(tiger)
sleep(tiger)
