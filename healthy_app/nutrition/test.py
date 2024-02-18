data = {'status': 'OK', 'selection': [{'sections': {'Breakfast': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_def3e4cb145bd13da0c352e5ef29eb89'}, 'Dinner': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_dded788c2e197297475926068d070592'}, 'Lunch': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_9abd5a420284399b9928d7345bec9296'}}}, {'sections': {'Breakfast': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_8be78cff9d5ab253a5ed6e0a24369874'}, 'Dinner': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_16816c49848f02394ee122b4deb92585'}, 'Lunch': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_8292d632f874b12ac866286a4a07299c'}}}, {'sections': {'Breakfast': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_2e21e0eb336fdb34dbb9e812b767883f'}, 'Dinner': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_303307262ce3aef78d89453a9bf5df71'}, 'Lunch': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_b2ab3c48ab7316a85a59ebbf1766e2e0'}}}, {'sections': {'Breakfast': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_1d320f4cc4db1fc9ccdb83e52376b874'}, 'Dinner': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_1165c82fd9f34038f0a51ade355d2aa9'}, 'Lunch': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_fcfb527a74492e49657a07ed30474395'}}}, {'sections': {'Breakfast': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_c0bddf8bca47bae1e3b9c0b94f01782b'}, 'Dinner': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_e3870f249f8bb053afdf0198d716594b'}, 'Lunch': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_9dca277577af9651d36a98c184872df4'}}}, {'sections': {'Breakfast': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_308654c4defe3f2acf28024f8e9cf247'}, 'Dinner': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_0564dada745eaa594577a53efc572958'}, 'Lunch': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_aff010584fd8a2aa9b12f179930821e0'}}}, {'sections': {'Breakfast': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_2619ab19d3003a5fb45e3bc7a6c34bbe'}, 'Dinner': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_b352305233953fe49a71ed449614e4b4'}, 'Lunch': {'assigned': 'http://www.edamam.com/ontologies/edamam.owl#recipe_64f3770f94e173c6f40df20e4630c57a'}}}]}
list_of_links = []
for i in range(7):
    list_of_links.append(data['selection'][i]['sections']['Breakfast']['assigned'])
    list_of_links.append(data['selection'][i]['sections']['Dinner']['assigned'])
    list_of_links.append(data['selection'][i]['sections']['Lunch']['assigned'])

print(list_of_links)

# for piece in data['selection']:
#

# for i in range(7):
#     print(data['selection'][i]['sections']['Breakfast'])

    # print(piece['sections']['Breakfast']['assigned'])
    # print(piece['sections']['Dinner']['assigned'])
    # print(piece['sections']['Lunch']['assigned'])