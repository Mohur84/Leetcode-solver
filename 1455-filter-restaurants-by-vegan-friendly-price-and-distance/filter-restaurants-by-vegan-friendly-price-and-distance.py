class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        result = []
        for restaurant in restaurants:
            id, rating, vegan, price, distance = restaurant
            if veganFriendly == 1 and vegan != 1:
                continue
            if price > maxPrice:
                continue
            if distance > maxDistance:
                continue
            result.append(restaurant)
        result.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [restaurant[0] for restaurant in result]