class lightSwitch:
    is_on = False

    def Flip(self):
        self.is_on = not self.is_on
        print(self.is_on)

    def FlipMany(self, number : int):
            for i in range(number):
                self.flip()

def MultiplyByTwo(number:int): 
    return number*2

# class is light switch, is on is the attribute, flip is method. self is object instance.
# bedroom light is object

living_room_light = lightSwitch()
bedroom_light = lightSwitch()
living_room_light.Flip()
bedroom_light.Flip()

print(type(bedroom_light))
print(dir(bedroom_light))

# dir would state out the list of things that happaned
# string is an object with a class string
