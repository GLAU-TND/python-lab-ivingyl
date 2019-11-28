try:
    n=int(input('Enter a no.') + input())
    n.count()


except(AttributeError):
    print('OOPS! Attribute Error Occurred')

except(TypeError):
    print('OOPS! Type Error Occurred')

except(ValueError):
    print('OOPS! Value Error Occurred')
