names = ["Фінляндія", "Швеція", "Норвегія", "Данія", "Ісландія", "Естонія", "Росія"]

def categorize_countries(fin, sw, nor, dan, ice, es, ru):
    nordic_countries = (fin, sw, nor, dan, ice)
    print("Nordic Countries:", nordic_countries)
    print("Estonia:", es)
    print("Russia:", ru)

categorize_countries(*names)
