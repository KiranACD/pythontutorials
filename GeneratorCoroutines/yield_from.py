from inspect import getgeneratorlocals, getgeneratorstate
from webbrowser import get

def song():
    yield 'I am a lumberjack and I am okay'
    yield 'I sleep all night and I work all day'

def play_song():
    s = song()
    yield from s
    yield 'song finished'
    print('player is exiting')

player = play_song()
print(getgeneratorstate(player), getgeneratorlocals(player))
print('--------------------------------------------------------')
print(next(player))
print(getgeneratorstate(player), getgeneratorlocals(player))
print('--------------------------------------------------------')
s = getgeneratorlocals(player)['s']

print(getgeneratorstate(player), getgeneratorstate(s))

print('--------------------------------------------------------')
print(next(player))
print(getgeneratorstate(player), getgeneratorstate(s))

print('--------------------------------------------------------')
print(next(player))
print(getgeneratorstate(player), getgeneratorstate(s))

print('--------------------------------------------------------')
print(next(player))
print(getgeneratorstate(player), getgeneratorstate(s))