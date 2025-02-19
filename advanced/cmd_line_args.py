
def hello(name, lang):
   greetings = {
        "English":"Hello",
        "Spanish":"Hola",
        "French":"Halo"
    }
   msg = f"{greetings[lang]} {name}"
   print(msg)

if __name__ == "__main__":
   

    import argparse 

    parser = argparse.ArgumentParser(
        description="Provide greetings to the user"
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True,help="You need to enter name"

    )
    parser.add_argument(
        "-ln","--lang", metavar="language",
        required=True,help="Choose which language you want to get greetings",
        choices=["English","Spanish","French"]

    )

    args = parser.parse_args()
    hello(args.name, args.lang)

# msg = f"Hello,{args.name, args.lang}!"
# msg = f"{args.lang, args.name}!"

# print(msg)