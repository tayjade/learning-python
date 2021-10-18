#!/usr/bin/env python3

'''
Pep talk generator
'''

import random

def choose(some_list):
    choice = random.sample(some_list, 1)
    return choice 

if __name__ == "__main__":
    list_one = [
        'Champ, ',
        'Fact: ',
        'Everybody says ',
        'Dang... ',
        'Check it: ',
        'Just saying... ',
        'Superstar, ',
        'Tiger, ',
        'Self, ', 
        'Know this: ',
        'News alert: ', 
        'Girl, ',
        'Ace, ',
        'Excuse me but ',
        'Experts agree: ',
        'In my opinion, ',
        'Hear ye, hear ye: ',
        'Okay, listen up: ' 
    ]

    list_two = [
        'the mere idea of you ', 
        'your soul ', 
        'your hair today ',
        'everything you do ',
        'your personal style ',
        'every thought you have ',
        'that sparkle in your eye ',
        'your presence here ',
        'what you got going on ',
        'the essential you ',
        'your life\'s journey ',
        'that saucy personality ',
        'your DNA ',
        'that brain of yours ',
        'your choice of attire ',
        'the way you roll ',
        'whatever your secret is ',
        'all of y\'all '
    ]

    list_three = [
        'has serious game, ',
        'rains magic, ',
        'deserves the Nobel Prize, ',
        'raises the roof,',
        'breeds miracles, ',
        'is paying off big time, ',
        'shows mad skills, ',
        'just shimmers, ',
        'is a national treasure, ',
        'gets the party hopping, ',
        'is the next big thing, ',
        'roars like a lion, ',
        'is a rainbow factory, ',
        'is made of diamonds, ',
        'makes birds sing, ',
        'should be taught in school, ',
        'makes my world go \'round, ',
        'is 100 percent legit, '
    ]

    list_four = [
        '24/7.', 
        'can I get an amen?',
        'and that\'s a fact.',
        'so treat yourself.',
        'you feel me?',
        'that\'s just science.',
        'would I lie?',
        'for reals.',
        "mic drop.",
        'you hidden gem.',
        'snuggle bear.',
        'period.',
        'can I get an amen?',
        'now let\'s dance.',
        'high five!',
        'say it again!',
        'according to CNN.',
        'so get used to it.'
    ]

    while True:
        try:
            generate_message = input('Generate pep talk?    [y/n]\n').lower().strip()
            if generate_message == 'y':
                message = ''.join(choose(list_one) + choose(list_two) + choose(list_three) + choose(list_four))
                print(message)
            elif generate_message == 'n':
                exit()
            else:
                print('Unrecognized.')
        except Exception as e:
            print(e)
