import requests


EMBLEM_URLS = {
    "UNRANKED": "https://static.wikia.nocookie.net/leagueoflegends/images/1/13/Season_2023_-_Unranked.png",
    "IRON": "https://static.wikia.nocookie.net/leagueoflegends/images/f/f8/Season_2023_-_Iron.png",
    "BRONZE": "https://static.wikia.nocookie.net/leagueoflegends/images/c/cb/Season_2023_-_Bronze.png",
    "SILVER": "https://static.wikia.nocookie.net/leagueoflegends/images/c/c4/Season_2023_-_Silver.png/revision/latest?cb=20231007195834",
    "GOLD": "https://static.wikia.nocookie.net/leagueoflegends/images/7/78/Season_2023_-_Gold.png/revision/latest?cb=20231007195829",
    "PLATINUM": "https://static.wikia.nocookie.net/leagueoflegends/images/b/bd/Season_2023_-_Platinum.png/revision/latest?cb=20231007195833",
    "EMERALD": "https://static.wikia.nocookie.net/leagueoflegends/images/4/4b/Season_2023_-_Emerald.png/revision/latest?cb=20231007195827",
    "DIAMOND": "https://static.wikia.nocookie.net/leagueoflegends/images/3/37/Season_2023_-_Diamond.png/revision/latest?cb=20231007195826",
    "MASTER": "https://static.wikia.nocookie.net/leagueoflegends/images/d/d5/Season_2023_-_Master.png/revision/latest?cb=20231007195832",
    "GRANDMASTER": "https://static.wikia.nocookie.net/leagueoflegends/images/6/64/Season_2023_-_Grandmaster.png/revision/latest?cb=20231007195830",
    "CHALLENGER": "https://static.wikia.nocookie.net/leagueoflegends/images/1/14/Season_2023_-_Challenger.png/revision/latest?cb=20231007195825",
}

SERVER_OPTIONS = {
    "euw1": "EUW",
    "eun1": "EUNE",
    "na1": "NA",
    "br1": "BR",
    "jp1": "JP",
    "kr": "KR",
    "la1": "LAN",
    "la2": "LAS",
    "tr1": "TR",
    "oc1": "OCE",
    "ru": "RU",
    "sg2": "SG",
    "th2": "TH",
    "vn2": "VN",
    "tw2": "TW",
}


def request(game_name: str, tagline: str, server: str = "EUW") -> dict:
    print("Requesting...")

    response = requests.get(
        url=f"http://127.0.0.1:8000/api/{server}/{game_name}-{tagline}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Response: {response.status_code}. Something went wrong.")
