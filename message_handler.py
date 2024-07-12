# message_handler for Study Group 5
    # provides language options for two programs

#FizzBizz Program

FIZZBIZZ_MESSAGES_FR = {
    "INTRO_ORIGZ": "\n\nBienvenue dans la version originale du jeu fizzbizz !!\n",
    "INTRO_VARIZZ": "\nIl s'agit d'une variante du jeu fizzbizz. Pour jouer, suivez les instructions.\n",
    "GO_ON_MSG": "\nVous verrez une liste de chiffres accompagnée de quelques mots. Voyez si vous pouvez déterminer un modèle. Appuyez sur Entrée pour continuer.",
    "SIGN_OFF": "\nMerci de jouer ! Prenez le temps d'examiner la liste imprimée. Êtes-vous capable de prédire quand chaque mot apparaîtra ?\n",
    "VALUE_PROMPT": "Veuillez indiquer deux chiffres entre 2 et 9 (par exemple : 2, 9): ",
    "WORD_PROMPT": "Veuillez indiquer trois mots (par exemple : séparer, par, des virgules) : ",
    "CHOICE_PROMPT": "\nBienvenue dans le jeu FizzBizz ! Vous avez le choix entre deux versions.\n  1. FizzBizz original\n  2. Variante de FizzBizz\n\nLequel voulez-vous jouer (1 ou 2) ? ",
    "INVALID_CHOICE": 'Choix non valide. Veuillez saisir "1" ou "2".',
    "ERROR_WORDS": "Entrée non valide. Veuillez saisir trois mots.",
    "ERROR_VALUE_RANGE": "Entrée non valide. L'entrée ne peut être que des chiffres entre 2 et 9.",
    "ERROR_VALUES": "Entrée non valide. Veuillez saisir deux chiffres."
}

FIZZBIZZ_MESSAGES_EN = {
    "INTRO_ORIGZ": "\n\nWelcome to the original version of the fizzbizz game!\n",
    "INTRO_VARIZZ": "\nThis is a variant of the fizzbizz game. To play, please follow the instructions.\n",
    "GO_ON_MSG": "\nYou will see a list of numbers along with some words. See if you can determine the pattern.\nPress ENTER to continue.",
    "SIGN_OFF": "\nThanks for playing! Take some time and look over the printed list. Are you able to predict when each word would appear?\n",
    "VALUE_PROMPT": "Please provide two numbers between 2 and 9 (e.g., 2, 9):  ",
    "WORD_PROMPT": "Please provide three words (e.g., separate,with,commas):  ",
    "CHOICE_PROMPT": "\nWelcome to the FizzBizz game! There are two versions you can choose from.\n  1. Fizz Bizz Origz\n  2. Fizz Bizz Varizz\n\nWhich would you like to play (1 or 2)?:  ",
    "INVALID_CHOICE": "Invalid choice. Please enter 1 or 2.",
    "ERROR_WORDS": "Invalid input. Please enter three words.",
    "ERROR_VALUE_RANGE": "Invalid input. Input can only be digits between 2 and 9.",
    "ERROR_VALUES": "Invalid input. Please enter two numbers."
}

def get_messages_fizzbizz():
    while True:
        language = input("Language (FR / EN) : ").upper()
        if language == "EN":
            fizzbizz_messages = FIZZBIZZ_MESSAGES_EN
            return fizzbizz_messages
        elif language == "FR":
            fizzbizz_messages = FIZZBIZZ_MESSAGES_FR
            return fizzbizz_messages
        else:
            pass





# Age Facts program

AGEFACTS_MESSAGES_EN= {
    "language" : "EN",
    "HEADER" : "\n-------------- Age Facts ----------------",
    "msg_10000_future": "You will be 10,000 days old in {days_till_10000} days.",
    "msg_10000_past": "You were 10,000 days old {days_till_10000} days ago.",
    "msg_10000_present": "You're 10,000 days old today!",
    "msg_skeleton_percentage": "{regen_amt} of your skeleton has been replaced!",
    "msg_skeleton_replacements": "Your skeleton has been replaced {regen_amt} times!",
    "msg_insect": "The amount of insects you have eaten is probably equal to {insect_amt} loaves of bread.",
    "RANDOM_STAT": "Here's a random statistic: {random_stat}",
    "STATUS_ERROR": "Sorry! This time didn't work. Please try again. See status code: {response_status_code}",
    "BIRTHDATE": "\nWhen were you born (YYYY-MM-DD)? ",
    "ERROR_MSG": "This program is not yet set up for time travellers. Please enter a date before tomorrow to continue.",
    "AGE_MSG": "\nYou are {years} years, {months} months, and {days} days old.",
    "MONTHS_MSG": "Your age in months: {age_in_months}",
    "WEEKS_MSG": "Your age in weeks: {age_in_weeks}",
    "DAYS_MSG": "Your age in days: {age_in_days}\n",
    "HISTORICAL_MSG": "\nHere is a historical event that happened on your birthdate:\n    {event_on_birthdate}.\n",
    "TRY_AGAIN_MSG": "Would you like to try another birthdate?  ",
    "SALUTATION": "\nTill next time!\n"
}


AGEFACTS_MESSAGES_FR = {
    "language" : "FR",
    "HEADER" : "\n-------------- faits sur l'âge ----------------",
    "msg_10000_future": "Tu auras 10 000 jours dans {days_till_10000} jours.",
    "msg_10000_past": "Vous aviez 10 000 jours il y a {days_till_10000} jours.",
    "msg_10000_present": "Vous avez 10 000 jours aujourd'hui !",
    "msg_skeleton_percentage": "{regen_amt}% de votre squelette a été remplacé !",
    "msg_skeleton_replacements": "Votre squelette a été remplacé {regen_amt} fois !",
    "msg_insect": "La quantité d'insectes que vous avez mangés équivaut à environ {insect_amt} pains.",
    "RANDOM_STAT": "Voici une statistique aléatoire : {random_stat}.",
    "STATUS_ERROR": "Cette fois-ci n'a pas fonctionné. Veuillez réessayer. Voir le code d'état : {response_status_code}",
    "BIRTHDATE": "\nDate de naissance (YYYY-MM-DD)? ",
    "ERROR_MSG": "Ce programme n'est pas encore configuré pour les voyageurs temporels. Veuillez saisir une date antérieure à demain pour continuer.",
    "AGE_MSG": "\nVous avez {years} ans, {months} mois et {days} jours.",
    "MONTHS_MSG": "Votre âge en mois : {age_in_months}",
    "WEEKS_MSG": "Votre âge en semaines : {age_in_weeks}",
    "DAYS_MSG": "Votre âge en jours : {age_in_days}\n",
    "HISTORICAL_MSG": "\nVoici un événement historique qui s'est produit à votre date de naissance :\n    {event_on_birthdate}.\n",
    "TRY_AGAIN_MSG": "Voulez-vous essayer une autre date de naissance ? ",
    "SALUTATION": "\nÀ la prochaine fois !\n"
}

def get_messages_agefacts():
    while True:
        language = input("Language (FR / EN) : ").upper()
        if language == "EN":
            agefacts_messages = AGEFACTS_MESSAGES_EN
            return agefacts_messages
        elif language == "FR":
            agefacts_messages = AGEFACTS_MESSAGES_FR
            return agefacts_messages
        else:
            pass

