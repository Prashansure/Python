cart = [
    {"name": "shirt", "price": 2000},
    {"name": "shoes", "price": 3000},
    {"name": "shirt", "price": 2000}
]

unique_items = []
seen_items = set()

for item in cart:
    if item["name"] not in seen_items:
        unique_items.append(item)
        seen_items.add(item["name"])

total_cost = sum(item["price"] for item in unique_items)

if total_cost > 5000:
    total_cost *= 0.9

print("Total cost:", total_cost)