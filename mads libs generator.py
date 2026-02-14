'''story = "O {adjective} {noun} went to the {place} to {verb} with a {celebrity}."
adjective = input('Enter an adjective: ')
noun = input('Enter noun: ')
place = input('Enter a place: ')
verb = input('Enter a verb: ')
celebrity = input('Enter a celebrity: ')
completed_story = story.format(adjective=adjective, noun=noun, place=place, verb=verb, celebrity=celebrity)
print("\nHere's your Mad Libs story: ")
print(completed_story)'''

def generate_mad_libs():
    story_template = """Era uma vez, um {adjective} {animal} que decidiu {verb} através do {place}. Eles
    encontre um {noun} que lhes ofereceu {adjective2} {food}."""
    print("Vamos criar uma história do Mad Libs!")

    adjective = input('Informe um adjetivo: ')
    animal = input('Informe um animal: ')
    verb = input('Informe um verbo: ')
    place = input('Informe um lugar: ')
    noun = input('Informe um substantivo: ')
    adjective2 = input('Informe outro adjetivo: ')
    food = input('Informe um tipo de comida: ')

    completed_story = story_template.format(adjective=adjective,
                                            animal=animal,
                                            verb=verb,
                                            place=place,
                                            noun=noun,
                                            adjective2=adjective2,
                                            food=food
    )

    print('\nYour Mad Libs Story: ')
    print(completed_story)

if __name__ == '__main__':
    generate_mad_libs()
