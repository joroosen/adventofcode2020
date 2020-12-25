card_pub = 18356117
door_pub = 5909654

def transform(card_pub, door_pub):
    value = 1
    subject = 7
    card_loops = 0
    door_loops = 0
    encryption_key = 0

    while value != card_pub:
        value = value * subject
        value = value % 20201227
        card_loops += 1
    print("card loops: " + str(card_loops))

    value = 1
    while value != door_pub:
        value = value * subject
        value = value % 20201227
        door_loops += 1
    print("Door loops: " + str(door_loops))

    subject = card_pub
    door_enc = 0
    value = 1
    for i in range(door_loops):
        value = value * subject
        value = value % 20201227

    encryption_key = value

    # subject = door_pub
    # card_enc = 0
    # value = 1
    # for i in range(card_loops):
    #     value = value * subject
    #     card_enc = value % 20201227
    #
    # if door_enc == card_enc:
    #     encryption_key = door_enc
    # else:
    #     print("ERROR DECRYPTING")


    return(encryption_key)



print(transform(card_pub, door_pub))

