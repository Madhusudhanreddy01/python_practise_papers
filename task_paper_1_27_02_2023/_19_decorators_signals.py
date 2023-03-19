# 19. Write a program using decorators to print the traffic signal messages 
# Expected output - 
# RED : STOP 
# YELLOW : SLOW DOWN 
# GREEN : GO 
# The decorator should be working in this order


def traffic_signal(func):
    def wrapper(signal):
        if signal == 'RED':
            print('RED : STOP')
        elif signal == 'YELLOW':
            print('YELLOW : SLOW DOWN')
        elif signal == 'GREEN':
            print('GREEN : GO')
        else:
            print('Invalid signal')
        func(signal)
    return wrapper


@traffic_signal
def message(signal):
    pass


message('RED')
message('YELLOW')
message('GREEN')
message('Black')

# -------------------------------------------------------------
# def greet():
# 	print('Hello! ', end='')
	
# def mydecorator(fn):
# 	fn()
# 	print('How are you?')
# mydecorator(greet)
# Hello! How are you?

# --------------------------------------------------------------

# def traffic_signals(fn):
#     def inner_function():        
#         fn()
#     return inner_function

# @traffic_signals
# def red():
# 	print("RED : STOP")
# red()

# @traffic_signals
# def yellow():
# 	print("YELLOW : SLOW DOWN")

# yellow()

# @traffic_signals
# def green():
# 	print("GREEN : GO")

# green()