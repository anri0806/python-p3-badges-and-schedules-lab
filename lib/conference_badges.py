def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    
    new_list = []
    
    for room in range(1,9):
        new_list.append(f"Hello, {names[room - 1]}! You'll be assigned to room {room}!")
            
    return new_list

    
def printer(names):
    
    for batch in batch_badge_creator(names):
        print(batch)
    
    for room in assign_rooms(names):
        print(room)
    