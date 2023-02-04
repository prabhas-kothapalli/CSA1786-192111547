colour(cherry, red).
colour(banana, yellow).
colour(apple, red).
colour(apple, green).
colour(orange, orange).
colour(X, unknown).

predict_fruit(X, C) :- colour(X, C), !.
predict_fruit(X, unknown).
