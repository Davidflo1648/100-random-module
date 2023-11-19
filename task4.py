import random

ability_scores = ["strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma"]

classes = {
    "fighter": ["strength", "constitution"],
    "wizard": ["intelligence", "wisdom"],
    "rogue": ["dexterity", "charisma"],
    "cleric": ["wisdom", "charisma"],
    "ranger": ["dexterity", "wisdom"],
    "bard": ["charisma", "dexterity"]
}
races = {
    "human": {"strength": 1, "intelligence": 1, "wisdom": 1, "dexterity": 1, "constitution": 1, "charisma": 1},
    "elf": {"intelligence": 2, "dexterity": 2},
    "dwarf": {"constitution": 2, "wisdom": 2},
    "halfling": {"dexterity": 2, "charisma": 2},
    "gnome": {"intelligence": 2, "constitution": 2},
    "half-elf": {"charisma": 2, "random": 2},
    "half-orc": {"strength": 2, "constitution": 1},
    "dragonborn": {"strength": 2, "charisma": 1},
    "tiefling": {"intelligence": 1, "charisma": 2}
}
genders = {
    "male": {"he": "he", "him": "him", "his": "his"},
    "female": {"he": "she", "him": "her", "his": "her"},
    "non-binary": {"he": "they", "him": "them", "his": "their"}
}
names = {
    "human": {
        "male": ["Adam", "Ben", "Carl", "David", "Evan", "Frank", "George", "Henry", "Ian", "Jack"],
        "female": ["Alice", "Beth", "Clara", "Diana", "Eve", "Fiona", "Grace", "Hannah", "Iris", "Jane"],
        "non-binary": ["Alex", "Blair", "Casey", "Drew", "Eli", "Finley", "Gray", "Harper", "Ivy", "Jesse"]
    },
    "elf": {
        "male": ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan"],
        "female": ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna"],
        "non-binary": ["Aeren", "Aila", "Aranis", "Ari", "Aster", "Bryn", "Cael", "Dara", "Eir", "Fen"]
    },
    "dwarf": {
        "male": ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk"],
        "female": ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda"],
        "non-binary": ["Arin", "Bryn", "Dori", "Edi", "Fari", "Geri", "Hari", "Iri", "Kari", "Lori"]
    },
    "halfling": {
        "male": ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle"],
        "female": ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla"],
        "non-binary": ["Ash", "Bliss", "Cass", "Dell", "Fay", "Gill", "Joss", "Kit", "Lee", "Nell"]
    },
    "gnome": {
        "male": ["Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug"],
        "female": ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli"],
        "non-binary": ["Bix", "Clix", "Dax", "Flix", "Gix", "Jix", "Kix", "Lex", "Mix", "Rix"]
    },
    "half-elf": {
        "male": ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan"],
        "female": ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna"],
        "non-binary": ["Aeren", "Aila", "Aranis", "Ari", "Aster", "Bryn", "Cael", "Dara", "Eir", "Fen"]
    },
    "half-orc": {
        "male": ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront"],
        "female": ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Vola"],
        "non-binary": ["Bash", "Dorn", "Gesh", "Hark", "Lash", "Mash", "Nash", "Rash", "Thok", "Zash"]
    },
    "dragonborn": {
        "male": ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr"],
        "female": ["Akra", "Biri", "Daar", "Farideh", "Harann", "Flavilar", "Jheri", "Kava", "Korinn", "Mishann"],
        "non-binary": ["Ash", "Bryn", "Cora", "Dara", "Esha", "Fira", "Gora", "Hara", "Isha", "Jora"]
    },
    "tiefling": {
        "male": ["Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai"],
        "female": ["Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia"],
        "non-binary": ["Asra", "Bela", "Cira", "Dela", "Era", "Fela", "Gora", "Hela", "Kira", "Lela"]
    }
}

suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

def roll_dice(number, sides):
    dice_results = []
    for i in range(number):
        dice_result = random.randint(1, sides)
        dice_results.append(dice_result)
    return dice_results

def generate_ability_scores(rolling_system):
    ability_scores = []

    for i in range(rolling_system):
        dice_results = roll_dice(3, 6)

        if rolling_system == 4:
            dice_results.append(roll_dice(1, 6)[0])
            dice_results.remove(min(dice_results))

        if rolling_system == 5:
            dice_results = [roll_dice(1, 6)[0] if x == 1 else x for x in dice_results]

        ability_score = sum(dice_results)
        ability_scores.append(ability_score)

    return ability_scores

def generate_character():
    character = {}
    character_class = random.choice(list(classes.keys()))
    character["class"] = character_class
    character_race = random.choice(list(races.keys()))
    character["race"] = character_race
    character_gender = random.choice(list(genders.keys()))
    character["gender"] = character_gender
    character_name = random.choice(names[character_race][character_gender])
    character["name"] = character_name
    ability_scores = generate_ability_scores(4)
    character_abilities = {}
    for i in range(len(ability_scores)):
        ability_score = ability_scores[i]
        ability_name = ability_scores[i]
        if ability_name in classes[character_class]:
            ability_score = max(ability_scores)
            ability_scores.remove(ability_score)

        if ability_name in races[character_race]:
            ability_score += races[character_race][ability_name]

        character_abilities[ability_name] = ability_score
    character["abilities"] = character_abilities
    return character

def print_character(character):
    print(f"{character['name']} is a {character['gender']} {character['race']} {character['class']}.")
    print("Their abilities are:")
    for ability, score in character["abilities"].items():
        print(f"{ability}: {score}")

def create_deck():
    deck = []

    for suit in suits:
        for rank in ranks:
            card = f"{rank} of {suit}"
            deck.append(card)
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal_hand(deck, hand_size):
    hand = []
    for i in range(hand_size):
        card = deck.pop()
        hand.append(card)
    return hand

def print_hand(hand):
    print("You got:")
    for card in hand:
        print(card)

character = generate_character()
print_character(character)
deck = create_deck()
deck = shuffle_deck(deck)
hand = deal_hand(deck, 5)
print_hand(hand)

    