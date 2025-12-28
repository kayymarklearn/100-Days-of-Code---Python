2025-12-24 13:18

Status: Incomplete

Tags: [[Day 17 - OOP (Creating Classes)]]

# Code snippets and Examples

```
class Car:

def __init__(self,seats):

self.seats = seats

print(f"My car has {self.seats} seats")

  

car_1 = Car(4)

car_2 = Car(3)
```

```
class User:

def __init__(self, user_id, username):

	self.id = user_id

	self.username = username
	self.followers = 0

user_1 = User(1, "Mark")

  

user_2 = User(2, "Baba")
```

```
class User:

def __init__(self, user_id, username):

self.id = user_id

self.username = username

self.followers = 0

self.following = 0

  

def follow(self, user):

user.followers += 1

self.following += 1

user_1 = User(1, "Mark")

  

user_2 = User(2, "Baba")

  

user_1.follow(user_2)

  

print(user_2.followers)

print(user_2.following)

  

print(user_1.followers)

print(user_1.following)
```
