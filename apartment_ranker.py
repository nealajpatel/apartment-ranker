#Apartment Ranker
#by: Neal Patel because Kevin's a bitch
from __future__ import print_function
from prettytable import PrettyTable

#Apartment criteria weight
APARTMENT_RANK_MAX = 10
PRICE_RANK_MAX = 7.5
LOCATION_RANK_MAX = 1.5
COMMUTE_RANK_MAX = 1

#Target values for apartment
TARGET_PRICE = 1000
TARGET_FACILITIES = 5
FACILITIES = ["grocerystore","gym","bar","food","gas","park","tacobell","pool","tennis","basketball"]
TARGET_COMMUTE = 15

#Prompts user for apartment info
apartmentComplex = raw_input('Enter name of apartment complex: ')
price = int(input('Enter price of apartment: '))
facilities = raw_input('Enter facilities within 5mins of apartment (grocerystore,gym,bar,...): ')
commute = int(input('Enter commute to work in minutes: '))

#calculates and returns price ranking
def get_price_ranking():

    if price <= TARGET_PRICE:
        return PRICE_RANK_MAX
    else:
        ranking = PRICE_RANK_MAX - ((price - TARGET_PRICE)//100 * 0.5)
        return handle_negative_rank(ranking)

#calulates and returns location ranking
def get_facility_ranking():

    facilityList = facilities.split(",")
    facilitySet = set(FACILITIES)

    matches = [facility for facility in facilityList if facility in facilitySet]

    numFacilities = len(facilityList)

    if numFacilities >= TARGET_FACILITIES:
        return LOCATION_RANK_MAX
    else:
        ranking = LOCATION_RANK_MAX - ((TARGET_FACILITIES - numFacilities) * 0.3)
        return handle_negative_rank(ranking)

#calulates and returns commute ranking
def get_commute_ranking():

    if commute <= TARGET_COMMUTE:
        return COMMUTE_RANK_MAX
    else:
        ranking = COMMUTE_RANK_MAX - ((commute - TARGET_COMMUTE)//5 * 0.1)
        return handle_negative_rank(ranking)

#sets negative rankings to 0
def handle_negative_rank(rank):
    if rank < 0:
        rank = 0
    return rank

priceRanking = get_price_ranking()
locationRanking = get_facility_ranking()
commuteRanking = get_commute_ranking()
totalRanking = priceRanking + locationRanking + commuteRanking

t = PrettyTable(['Aparment Complex', 'Price Rank', 'Location Rank', 'Commute Rank', 'Total'])
t.add_row([apartmentComplex, priceRanking, locationRanking, commuteRanking, totalRanking])

print(t)
