import random


class SpaceShip:
    def __init__(self, name, fuel, hull_condition=100, speed=0):
        self.name = name
        self.fuel = fuel
        self.hull_condition = hull_condition
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def travel(self, distance):
        fuel_needed = distance
        if fuel_needed > self.fuel:
            print("Недостаточно топлива!")
            return
        self.fuel -= fuel_needed

    def take_damage(self, amount):
        self.hull_condition -= amount
        if self.hull_condition < 0:
            self.hull_condition = 0

    def refuel(self, amount):
        self.fuel += amount


class CrewMember:
    def __init__(self, name, role, skills=None, health=100):
        self.name = name
        self.role = role
        self.skills = skills or {}
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100


class Mission:
    EVENT_EFFECTS = {
        "авария": "Во время полёта произошла авария.",
        "астероид": "Корабль попал в пояс астероидов.",
        "встреча": "Экипаж встретил дружественный корабль и получил топливо.",
    }

    def __init__(self, name, goals, resources=None, possible_events=None, crew=None):
        self.name = name
        self.goals = goals
        self.resources = resources or {}
        self.possible_events = possible_events or list(self.EVENT_EFFECTS)
        self.crew = crew or []
        self.completed_goals = []

    def complete_goal(self, goal):
        if goal in self.goals and goal not in self.completed_goals:
            self.completed_goals.append(goal)

    def is_complete(self):
        return len(self.completed_goals) == len(self.goals)

    def trigger_event(self, ship, event=None):
        if event is None:
            event = random.choice(self.possible_events)

        if event == "авария":
            ship.take_damage(20)
            for member in self.crew:
                member.take_damage(10)
        elif event == "астероид":
            ship.take_damage(35)
        elif event == "встреча":
            ship.refuel(self.resources.get("fuel_from_encounter", 10))

        return self.EVENT_EFFECTS[event]


if __name__ == "__main__":
    pilot = CrewMember("Алексей", "пилот", {"пилотирование": 90})
    engineer = CrewMember("Елена", "инженер", {"ремонт": 85})
    ship = SpaceShip("Восток", fuel=100)
    mission = Mission(
        "Экспедиция к Марсу",
        goals=["Достичь орбиты Марса", "Собрать образцы"],
        resources={"fuel_from_encounter": 15},
        crew=[pilot, engineer],
    )

    ship.set_speed(25)
    ship.travel(10)
    print(f"{ship.name}: топлива осталось {ship.fuel}, скорость {ship.speed}")
    print(mission.trigger_event(ship, "астероид"))
    print(f"Состояние корпуса: {ship.hull_condition}%")
