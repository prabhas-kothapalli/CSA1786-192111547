location(desk, office).
location(apple, kitchen).
location(flashlight, desk).

find_location(Item, Location) :- location(Item, Location).
