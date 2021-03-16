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
    maxVillages = 5
    maxCities  = 4
    maxRoads = 15

    longestRoad = {'requirement': 5, 'points' : 2}
    largestArmy = {'requirement': 3, 'points' : 2}

    constructionCosts ={
        'village' : {'wood' : 1, 'sheep' : 1, 'wheat' : 1, 'brick' : 1},
        'city' : {'wheat' : 2, 'ore' : 3},
        'road' : {'wood' : 1, 'brick' : 1},
        'development' : {'sheep' : 1, 'wheat' : 1, 'ore' : 1}
    }



class Player:

    def __init__(self, resourceCards, villages, availableVillages, cities, availableCities, roads, availableRoads, longestRoad, largestArmy):
        self.resourceCards = resourceCards
        self.villages = villages
        self.availableVillages = availableVillages
        self.cities = cities
        self.availableCities = availableCities
        self.roads = roads
        self.availableRoads = availableRoads
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
    
    def updateSpecialCard(self, longestRoad, largestArmy):
        self.longestRoad = longestRoad
        self.largestArmy = largestArmy


spentResources = {'wood' : 0, 'sheep' : 0, 'wheat' : 0, 'brick' : 0, 'ore' : 0}

p1 = Player(
    spentResources,
    Ledger.startVillages,
    Ledger.maxVillages - Ledger.startVillages,
    Ledger.startCities,
    Ledger.maxCities - Ledger.startCities,
    Ledger.startRoads,
    Ledger.maxRoads - Ledger.startRoads,
    False, 
    False
    )


print(vars(p1))
count = 0

while (
    (p1.villages * Ledger.villageSettlement) +
    (p1.cities * Ledger.citySettlement) +
    (p1.longestRoad * Ledger.longestRoad['points']) + 
    (p1.largestArmy * Ledger.largestArmy['points'])
    ) < Ledger.victoryPointCondition:
    count += 1
    print('\n\n\ncount: ', count, '\nvictory points: ', int(p1.villages * Ledger.villageSettlement) + (p1.cities * Ledger.citySettlement))

    if p1.roads >= 6 and p1.longestRoad == False:
        p1.updateSpecialCard(True, p1.largestArmy)

    if p1.availableVillages > 0 and p1.availableRoads >= 2:

        # VILLAGE AFTER BUILDING 1 ROAD
        if p1.roads > 2 and p1.roads <= 4:
            p1.updateResources(
                Counter(p1.resourceCards) +
                Counter(Ledger.constructionCosts['road'])
                )
            p1.updateRoads(
                p1.roads + 1,  
                p1.availableRoads - 1
                )
    
            p1.updateResources(
                Counter(p1.resourceCards) +
                Counter(Ledger.constructionCosts['village'])
                )
            p1.updateVillages(
                p1.villages + 1,
                p1.availableVillages - 1
                )
                
        # VILLAGE AFTER BUILDING 2 ROADS
        else:
            for n in range(0,2):
                p1.updateResources(
                    Counter(p1.resourceCards) +
                    Counter(Ledger.constructionCosts['road'])
                    )
                p1.updateRoads(
                    p1.roads + 1,
                    p1.availableRoads - 1
                    )

            p1.updateResources(
                Counter(p1.resourceCards) +
                Counter(Ledger.constructionCosts['village'])
            )
            p1.updateVillages(
                p1.villages + 1,
                p1.availableVillages - 1
            )
        print('\nbuilt a village')
        print(' p1 cities: ', p1.cities, '\n available cities: ', p1.availableCities)
        print('\n p1 villages: ',p1.villages, '\n available villages: ', p1.availableVillages)
        print('', p1.resourceCards)


    # CITY
    elif p1.availableCities > 0:
        p1.updateResources(
            Counter(p1.resourceCards) + 
            Counter(Ledger.constructionCosts['city'])
        )
        p1.updateCities(
            p1.cities + 1,
            p1.availableCities - 1
        )
        p1.updateVillages(
            p1.villages - 1,
            p1.availableVillages + 1
        )
        print('\nbuilt a city')
        print(' p1 cities: ', p1.cities, '\n available cities: ', p1.availableCities)
        print('\n p1 villages: ',p1.villages, '\n available villages: ', p1.availableVillages)
        print('', p1.resourceCards)

    # COULD NOT BUILD MORE VICTORY POINTS
    else:
        print('something went wrong XD')
        print(p1.availableRoads)

        if p1.availableRoads < 2:
            print('Not enough roads available')
        elif p1.availableVillages < 1 and p1.availableCities < 1:
            print('No available villages or cities')
        elif p1.villages < 1:
            print('No available villages')
        elif p1.availableCities < 1:
            print('No available cities')

        else:
            print('Unexpected error...')
        break


#print(vars(p1))
print(sum(p1.resourceCards.values()), ' Resource cards is required using this strategy')
#print((p1.villages * Ledger.villageSettlement) + (p1.cities * Ledger.citySettlement))
