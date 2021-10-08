rankings = {
"Bills": 3,
"Cardinals":1,
"Chiefs": 8,
"Raiders": 11,
"Buccaneers": 5,
"Packers" :4,
"Ravens" : 5,
"Cowboys" : 6,
"Chargers" : 7,
"Rams" : 9,
"Browns": 10,
"Seahawks" : 12,
"49ers" : 13,
"Panthers": 14,
"Bengals": 15,
"Broncos" : 16,
"Vikings": 17,
"Titans": 18,
"Saints": 19,
"Steelers": 20,
"Colts": 21,
"Patriots": 22,
"Washington": 23,
"Giants": 24,
"Eagles" : 25,
"Dolphins" : 26,
"Falcons" : 27,
"Jets": 28,
"Bears" : 29,
"Jaguars" : 30,
"Lions" : 31,
"Texans" : 32
}

matchup = []
doc = open("Week5Matchups.txt", mode="r", encoding='utf-8-sig')
for line in doc:
    for word in line.split():
        if word == "at":
            continue
        else:
            matchup.append(word)

#matchup = ["Bills", "Cardinals", "Raiders", "Chiefs","Bills", "Chiefs"]
i = 0
text = open("Week5Favorites.txt", "w")
while i < len(matchup):
    comp_dict = {}
    comp_dict[matchup[i]] = rankings[matchup[i]]
    i += 1
    comp_dict[matchup[i]] = rankings[matchup[i]]
    higherRank = min(comp_dict, key=comp_dict.get)
    text.write("The favorite based on power rankings in " + matchup[i-1] + " vs " + matchup[i] + " -> " + str(higherRank) + '\n')
    i+=1

text.close()
