def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cycle():
    turn_right()
    move()

def wall_on_left():
    turn_left()
    ans = front_is_clear()
    turn_right()


while at_goal() == False:
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and wall_on_left():
        turn_right()
    else:
        cycle()