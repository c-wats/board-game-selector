#!/usr/bin/env python3

import json

f = open('board-games.json',)
boardGames = json.load(f)
f.close()

def listBoardGames(boardGames):
    print("All games: ")
    for game in boardGames['boardGames']:
        identifier, name, minPlayers, maxPlayers, tags = game['id'], game['name'], game['minPlayers'], game['maxPlayers'], [tag for tag in game['tags']]
        print(f'{identifier}. {name}. {minPlayers}-{maxPlayers} players. Genre: {tags}')

def main():
    listBoardGames(boardGames)

main()
