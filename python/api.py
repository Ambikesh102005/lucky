import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return

    contant = response.json()
    for artwork in contant["data"]:
        print(f"* {artwork['title']}")


main()
