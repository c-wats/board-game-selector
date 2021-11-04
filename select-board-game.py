#!/usr/bin/env python3

import json

with open('board-games.json') as file:
    boardGames = json.load(file)

def listBoardGames(boardGames):
    print("All games: ")
    for game in boardGames['boardGames']:
        identifier, name, minPlayers, maxPlayers, tags = game['id'], game['name'], game['minPlayers'], game['maxPlayers'], [tag for tag in game['tags']]
        print(f'{identifier}. {name}. {minPlayers}-{maxPlayers} players. Genre: {tags}')


def returnPlayableGames(numberOfPlayers):
    print(f"Games for {numberOfPlayers}: ")
    for game in boardGames['boardGames']:
        if numberOfPlayers >= int(game['minPlayers']) and numberOfPlayers <= int(game['maxPlayers']):
            print(game['name'])

def main():
    listBoardGames(boardGames)
    numberOfPlayers = int(input ("\nNumber of players: "))
    returnPlayableGames(numberOfPlayers)

main()
