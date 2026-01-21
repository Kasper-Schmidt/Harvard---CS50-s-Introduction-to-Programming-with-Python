import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")


    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist} # q er en parametre som kunstmuseet har opgivet i deres API forklaring, som kan bruges til at søge efter en munstner, så der kan søges efter Monet, Picasso osv 
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return
    
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")




main()