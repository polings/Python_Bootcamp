import random


def randomly_split(sum_number, split_count, round_digits):
    """
    Randomly splits a total sum into a specified number of rounded parts.
    """
    rand_number_list = [random.random() for _ in range(split_count)]
    norm = sum_number / sum(rand_number_list)
    split_number_list = [round(x * norm, round_digits) for x in rand_number_list]
    return split_number_list


def turrets_generator():
    """
    Generator that creates turret objects with randomized personality traits and basic actions.
    """
    personality_traits = ["neuroticism", "openness", "conscientiousness", "extraversion", "agreeableness"]
    trait_dist = randomly_split(sum_number=100, split_count=len(personality_traits), round_digits=2)
    obj_traits = dict(zip(personality_traits, trait_dist))
    obj = {
        "personality": obj_traits,
        "shoot": lambda self: "Shooting",
        "search": lambda self: "Searching",
        "talk": lambda self: "Talking"
    }
    yield type("Turret", (object,), obj)()


def main():
    instance_generator = turrets_generator()
    instance = next(instance_generator)
    print("Class: Turret")
    print("Personality traits:")
    for key, value in instance.personality.items():
        print(f"   - {key} - {value}")
    print(f"Actions: {instance.shoot()}, {instance.search()}, {instance.talk()}")


if __name__ == "__main__":
    main()
