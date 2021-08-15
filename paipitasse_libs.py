
# Random message when bot is called
def tag_paipitasse_random_response():
    from random import randint
    tableSize=["Wrrraaaaaoooooonnnnnn", 
    "Quoi ?", 
    "Oui ?", 
    "Qu'est-ce que t'as encore ?", 
    "Fous-moi la paix chui bourré"]

    return tableSize[randint(0,len(tableSize)-1)]
#print(random_msg())

    

# Random message when member leave guild
def member_leave_guild_random_response():
    from random import randint
    tableSize=["Héééé tu me dois 10 balles", 
    "Ohhh l'enfoiré... S'est barré avec ma 8.6, enfant d'tes mooooorts !",
    "Bon vent fumier !",  
    "Tu vas regretter mon gadjo !",
    "Ah... je crois qu'il l'a mal pris... \nMais j'avais un coup dans l'nez... \nmais sa soeur était consentante hein !"]
    return tableSize[randint(0,len(tableSize)-1)]
# print(member_leave_guild_random_response())


# Random message when member join guild
def member_join_guild_random_response():
    from random import randint
    tableSize=["Héééé biloute, bienvenu", 
    "Viens donc dans l'taverne, il me reste quelques 8.6",
    "Ohh sacrebleu, ça faisait longtemps !",  
    "Ah bah tu tombes à point nommé ! \nC'est l'heure de l'apéro",
    "Ho bah tu tombes bien, on se demandait qui allait payer la prochaine tournée !"]
    return tableSize[randint(0,len(tableSize)-1)]
# print(member_join_guild_random_response())

# Random message when member join guild
def member_join_guild_random_announce(member_name):
    from random import randint
    tableSize=[f"Hé les gars y'a un nouveau ! \nC'est {member_name}",
    f"Get l'nouveau {member_name} ! ",
    f"Mes mooooorts y'a un nouveau {member_name} ! ",
    f"Hé y'a un nouveau gadjo\n{member_name} qui s'appelle"
    ]
    return tableSize[randint(0,len(tableSize)-1)]
# print(member_join_guild_random_response())