# 我用 Python 打扑克牌
suits = ['♠', '♦', '♥', '♣']
def want_card(card):
    if card[0:2] == "黑桃":
        suit = suits[0]
        number = card[2]
    elif card[0:2] == "方片":
        suit = suits[1]
        number = card[2]
    elif card[0:2] == "红心":
        suit = suits[2]
        number = card[2]
    elif card[0:2] == "梅花":
        suit = suits[3]
        number = card[2]
    print('┌────┐')
    print('│ {}      │'.format(number))
    print('│        │')
    print('│        │')
    print('│   {}    │'.format(suit))
    print('│        │')
    print('│        │')
    print('│      {} │'.format(number))
    print('└────┘')
want_card("梅花3")
want_card("红心K")
