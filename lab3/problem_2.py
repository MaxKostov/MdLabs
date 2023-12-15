def find_cheapest_price(n, flights, start, dst, K):
    adj_list = [[] for _ in range(n)]
    for f in flights:
        adj_list[f[0]].append((f[1], f[2]))

    queue = [(start, 0, -1)]

    min_cost = float("inf")

    while queue:
        city, cost, stops = queue.pop(0)
        if city == dst:
            min_cost = min(min_cost, cost)
            continue

        if stops < K:
            for next_city, price in adj_list[city]:
                if cost + price < min_cost:
                    queue.append((next_city, cost + price, stops + 1))

    if min_cost == float("inf"):
        return "no route"

    return min_cost


num_cities = int(input("n = "))
flights = eval(input("flights= "))
start = int(input("start = "))
destination = int(input("destination = "))
stops = int(input("k = "))

print(
    f"The optimal path with at most {stops} stop from city {start} to {destination} has cost {find_cheapest_price(num_cities, flights, start, destination, stops)}"
)