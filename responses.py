import random


def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '$hello':
        return 'Hey there!'
    
    if p_message == '$beep boop?':
        return 'I am robot, beep boop!'\

    if p_message == '$roll':
        return str(random.randint(1, 100))
    
    if p_message == '$help':
        return '`This is the help command, empty because Chris is lazy rn`'
    
    if p_message == '$author':
        return '`This bot was created by Christopher Materick, LTHS \'24`'
    
    