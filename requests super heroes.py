import requests


def get_list_of_heroes(some_list):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url).json()
    heroes_list = []
    for item in response:
        if item["name"] in some_list:
            heroes_list.append(item)
    heroes_list.sort(key=lambda x: x['powerstats']['intelligence'], reverse=True)
    return heroes_list


def make_heroes_rating(some_list):
    heroes_list = get_list_of_heroes(some_list)
    print(f"Давайте посмотрим, кто же среди таких героев как {', '.join(some_list)} самый умный: ")
    for id, hero in enumerate(heroes_list):
        print(f"На {id + 1} месте по интеллекту стоит {hero['name']} "
              f"с показателем {hero['powerstats']['intelligence']} единиц интеллекта")


if __name__ == '__main__':
    make_heroes_rating(['Hulk', 'Captain America', 'Thanos'])
