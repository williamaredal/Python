from collections import Counter
# Figuring out the roads to victory requiring the minimum number of cards to achieve victory in catan
# TODO write part about development cards

class Ledger:
    victoryPointCondition = 10
    villageSettlement = 1
    citySettlement = 2
    
    startVillages = 2 
    startCities = 0
    startRoads = 2
    startDevCards = 0
    maxVillages = 5
    maxCities  = 4
    maxRoads = 15
    maxDevCards = 25

    villageSpacingRequirement = 2

    longestRoad = {'requirement': 5, 'points' : 2} # minimum requirement is 5 connected
    largestArmy = {'requirement': 5, 'points' : 2} # minimum requirement is 3 knights, statistically you will need to draw 5 to get 3 knights

    constructionCosts ={
        'village' : {'wood' : 1, 'sheep' : 1, 'wheat' : 1, 'brick' : 1},
        'city' : {'wheat' : 2, 'ore' : 3},
        'road' : {'wood' : 1, 'brick' : 1},
        'development' : {'sheep' : 1, 'wheat' : 1, 'ore' : 1}
    }



class Player:

    def __init__(self, resourceCards, villages, availableVillages, cities, availableCities, roads, availableRoads, devCards, availableDevCards, longestRoad, largestArmy):
        self.resourceCards = resourceCards
        self.villages = villages
        self.availableVillages = availableVillages
        self.cities = cities
        self.availableCities = availableCities
        self.roads = roads
        self.availableRoads = availableRoads
        self.devCards = devCards
        self.availableDevCards = availableDevCards
        self.longestRoad = longestRoad
        self.largestArmy = largestArmy
    
    def updateResources(self, resources):
        self.resourceCards = resources

    def updateVillages(self, villages, availableVillages):
        self.villages = villages
        self.availableVillages = availableVillages

    def updateCities(self, cities, availableCities):
        self.cities = cities
        self.availableCities = availableCities

    def updateRoads(self, roads, availableRoads):
        self.roads = roads
        self.availableRoads = availableRoads
    
    def updateDevCards(self, devCards, availableDevCards):
        self.devCards = devCards
        self.availableDevCards = availableDevCards
    
    def updateSpecialCard(self, longestRoad, largestArmy):
        self.longestRoad = longestRoad
        self.largestArmy = largestArmy




def VictoryCondition(player, ledger):
    requiredScore = ledger.victoryPointCondition
    playerScore = (
        (player.villages * ledger.villageSettlement) +
        (player.cities * ledger.citySettlement) +
        (player.longestRoad * ledger.longestRoad['points']) + 
        (player.largestArmy * ledger.largestArmy['points'])
    )

    if playerScore < requiredScore:
        return False
    elif playerScore >= requiredScore:
        return True
    else:
        print('Point VictoryCondition met an error')


def BuildRoad(player, ledger):
    player.updateResources(
        Counter(player.resourceCards) +
        Counter(ledger.constructionCosts['road'])
        )
    player.updateRoads(
        player.roads + 1,  
        player.availableRoads - 1
        )


def BuildVillage(player, ledger):
    player.updateResources(
        Counter(player.resourceCards) +
        Counter(ledger.constructionCosts['village'])
        )
    player.updateVillages(
        player.villages + 1,
        player.availableVillages - 1
        )


def BuildCity(player, ledger):
    player.updateResources(
        Counter(player.resourceCards) + 
        Counter(ledger.constructionCosts['city'])
    )
    player.updateCities(
        player.cities + 1,
        player.availableCities - 1
    )
    player.updateVillages(
        player.villages - 1,
        player.availableVillages + 1
    )


def BuyDevCard(player, ledger):
    player.updateResources(
        Counter(player.resourceCards) +
        Counter(ledger.constructionCosts['development'])
    )
    player.updateDevCards(
        player.devCards + 1,
        player.availableDevCards - 1 
    )


def SetSpecialCard(player, ledger):
    if player.roads >= (ledger.longestRoad['requirement'] - (ledger.startRoads / ledger.startVillages)) and player.longestRoad == False:
        player.updateSpecialCard(True, player.largestArmy)
    if player.devCards >= (ledger.largestArmy['requirement']) and player.largestArmy == False:
        player.updateSpecialCard(player.longestRoad, True)
    else:
        return None



spentResources = {'wood' : 0, 'sheep' : 0, 'wheat' : 0, 'brick' : 0, 'ore' : 0}

p1 = Player(
    spentResources,
    Ledger.startVillages,
    Ledger.maxVillages - Ledger.startVillages,
    Ledger.startCities,
    Ledger.maxCities - Ledger.startCities,
    Ledger.startRoads,
    Ledger.maxRoads - Ledger.startRoads,
    Ledger.startDevCards,
    Ledger.maxDevCards - Ledger.startDevCards,
    False, 
    False
    )


print(vars(p1))
count = 0
# TODO remove this test
print(str(Ledger.longestRoad['requirement'] - (Ledger.startRoads / 2)))


while VictoryCondition(p1, Ledger) == False:
    print('\n\n\ncount: ', count, '\nvictory points: ', int(p1.villages * Ledger.villageSettlement) + (p1.cities * Ledger.citySettlement))
    SetSpecialCard(p1, Ledger)

    if p1.availableVillages > 0 and p1.availableRoads >= Ledger.villageSpacingRequirement:
        # VILLAGE AFTER BUILDING 1 ROAD
        if p1.roads > Ledger.villageSpacingRequirement and p1.roads <= (Ledger.villageSpacingRequirement * 2):
            BuildRoad(p1, Ledger)
            BuildVillage(p1, Ledger)
    
        # VILLAGE AFTER BUILDING 2 ROADS
        else:
            for r in range(0, Ledger.villageSpacingRequirement):
                BuildRoad(p1, Ledger)

            BuildVillage(p1, Ledger)

        print('\nbuilt a village')
        print(' p1 cities: ', p1.cities, '\n available cities: ', p1.availableCities)
        print('\n p1 villages: ',p1.villages, '\n available villages: ', p1.availableVillages)
        print(' p1 devCards: ', p1.devCards, '\n available devCards: ', p1.availableDevCards)
        print('', p1.resourceCards)


    # CITY
    elif p1.availableCities > 0:
        BuildCity(p1, Ledger)

        print('\nbuilt a city')
        print(' p1 cities: ', p1.cities, '\n available cities: ', p1.availableCities)
        print('\n p1 villages: ',p1.villages, '\n available villages: ', p1.availableVillages)
        print(' p1 devCards: ', p1.devCards, '\n available devCards: ', p1.availableDevCards)
        print('', p1.resourceCards)
    
    # DEVCARD
    elif p1.availableDevCards > 0:
        BuyDevCard(p1, Ledger)

        print('\nbought a devCard')
        print(' p1 cities: ', p1.cities, '\n available cities: ', p1.availableCities)
        print('\n p1 villages: ',p1.villages, '\n available villages: ', p1.availableVillages)
        print(' p1 devCards: ', p1.devCards, '\n available devCards: ', p1.availableDevCards)
        print('', p1.resourceCards)

    # COULD NOT BUILD MORE VICTORY POINTS
    else:
        print('something went wrong XD')

        if p1.availableRoads < Ledger.villageSpacingRequirement:
            print('Not enough roads available')
        elif p1.availableVillages < 1 and p1.availableCities < 1:
            print('No available villages or cities')
        elif p1.villages < 1:
            print('No available villages')
        elif p1.availableCities < 1:
            print('No available cities')
        elif p1.availableDevCards < 1:
            print('No available devCards')

        else:
            print('Unexpected error...')
        break

print('\n\nwon the game')
print(' p1 cities: ', p1.cities, '\n available cities: ', p1.availableCities)
print('\n p1 villages: ',p1.villages, '\n available villages: ', p1.availableVillages)
print(' p1 devCards: ', p1.devCards, '\n available devCards: ', p1.availableDevCards)
print('', p1.resourceCards)

#print(vars(p1))
print('\n\n', sum(p1.resourceCards.values()), ' Resource cards is required using this strategy')
#print((p1.villages * Ledger.villageSettlement) + (p1.cities * Ledger.citySettlement))
