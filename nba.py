
"Modules for work with the function"
import requests
import sys
from collections import defaultdict

def get_pairs_players(n):
    """
        Give a player heights print a list of all pairs of players whose 
        height in inches adds up to the integer input to the application
        :param n: int
        :return: list

        >>> getpairsPlayers(139)
        - Nate Robinson  Brevin Knight
        - Nate Robinson  Mike Wilks
    """
    "request of type get to endpoint with the data of the nba players, after convert json to dict"
    response = requests.get("https://mach-eight.uc.r.appspot.com").json()

    "we proceed to create a new dict of type list with class defaultdict (good resource)"
    v = defaultdict(list)

    """we iterate over the array of players and group the names of the players based on the height
        Ejem 70: ["Nombre Jugador1", "Nombre Jugador2"]
    """
    for item in response['values']:
        v[int(item['h_in'])].append(item['first_name'] +" "+ item['last_name'])

    "str to append final output with height pairs"
    pairs = ""

    "we proceed to loop through the h_in key to get the height"
    for height in v:
        "check if pair height exits in the new dict"
        nw_h = n - height
        if nw_h in v:
            "we proceed to obtain the first players based on their height pair"
            for player1 in v[nw_h]:
                "we proceed to obtain the second players based on their height pair"
                for player2 in v[height]:
                    "conditions for not show duplicated players with same height"
                    if player2 < player1:
                        pairs += f"- {player2}  {player1}\n"

    "return condition if exists results pairs or not on str pairs"                         
    return pairs if len(pairs) > 0 else "No matches found"

"""function main"""
def run():
    try:
        "get numeric argument from the command line (height)"
        arg_h = int(sys.argv[1])
        "call a function for find pairs players"
        result = get_pairs_players(arg_h)
        "show result in command line"
        print(result)
    except:
        print("Argument passed is not int")

if __name__ == '__main__':
    run()
    

        






