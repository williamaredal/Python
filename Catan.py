from collections import Counter
from tqdm import tqdm
from random import choice
from matplotlib import pyplot as plt

# Figuring out the roads to victory requiring the minimum number of cards to achieve victory in catan
# TODO sort the dictionaries directly by value key pair 'cardsToVictory'
# figure out how many possible combinations the three choices can produce so that i can get an accurate sample
 
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

    initialResourceUsage = {'wood' : 0, 'sheep' : 0, 'wheat' : 0, 'brick' : 0, 'ore' : 0}



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


def PlayerScore(player, ledger):
    playerScore = int(
        (player.villages * ledger.villageSettlement) +
        (player.cities * ledger.citySettlement) +
        (player.longestRoad * ledger.longestRoad['points']) + 
        (player.largestArmy * ledger.largestArmy['points'])
    )
    return playerScore


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





numberOfSimulations = 10000
simulatedGames = {}

with tqdm(total=numberOfSimulations, desc='Simulating random Catan strategies') as pbar:

    for s in range(numberOfSimulations):
        
        p1DecisionTree = []
        p1 = Player(
            Ledger.initialResourceUsage,
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

        
        while VictoryCondition(p1, Ledger) == False:

            possibleChoices = [c for c in range(1,4) if
                c == 1 and p1.availableVillages > 0 and p1.availableRoads >= Ledger.villageSpacingRequirement
                or c == 2 and p1.availableCities > 0 and p1.villages > 0
                or c == 3 and p1.availableDevCards > 0
                ]
            randomDecision = choice(possibleChoices)
            SetSpecialCard(p1, Ledger)
            p1DecisionTree.append(randomDecision)

            # VILLAGE
            if randomDecision == 1:
                # VILLAGE AFTER BUILDING 1 ROAD
                if p1.roads > Ledger.villageSpacingRequirement and p1.roads <= (Ledger.villageSpacingRequirement * 2):
                    BuildRoad(p1, Ledger)
                    BuildVillage(p1, Ledger)
            
                # VILLAGE AFTER BUILDING 2 ROADS
                else:
                    for r in range(0, Ledger.villageSpacingRequirement):
                        BuildRoad(p1, Ledger)

                    BuildVillage(p1, Ledger)

            # CITY
            elif randomDecision == 2:
                BuildCity(p1, Ledger)

            # DEVCARD
            elif randomDecision == 3:
                BuyDevCard(p1, Ledger)

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
            
        simulatedGames[s] = {
            'decisionTree' : p1DecisionTree,
            'victoryPoints' : PlayerScore(p1, Ledger),
            'cardsToVictory' : sum(p1.resourceCards.values()),
            'spentResources' : p1.resourceCards,
            'villages' : p1.villages,
            'availableVillages' : p1.availableVillages,
            'cities' : p1.cities,
            'availableCities' : p1.availableCities,
            'roads' : p1.roads,
            'availableRoads' : p1.availableRoads,
            'devCards' : p1.devCards,
            'availableDevCards' : p1.availableDevCards,
            'longestRoad' : p1.longestRoad,
            'largestArmy' : p1.largestArmy
            }

        pbar.update(1)
        
# TESTS
for s in simulatedGames:
    print(simulatedGames[s])
    break
    

plt.scatter([s for s in simulatedGames], [simulatedGames[s]['cardsToVictory'] for s in simulatedGames], color="blue", alpha=0.5)

plt.show()
'''
# Temp
lowestCardDistance = []
for s in simulatedGames:
    lowestCardDistance.append(simulatedGames[s]['cardsToVictory'])

lowestCardDistance.sort()
print(lowestCardDistance)
'''