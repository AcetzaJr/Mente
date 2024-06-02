def check_in_options(tag: str, options: list[str], value: str):
    for option in options:
        if option == value:
            return value
    print(f"> {tag} '{value}' not recognized")
    print("> valid options are:")
    for option in options:
        print(f"    * {option}")
    return None
