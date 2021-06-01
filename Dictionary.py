Dictionary:
    Hashtable based Collection of heteroginious items in (pair of Key & value) enclosed in curly brackets {}
            Duplicates not allowed () --> in context of only Keys
    Dictionaries are used to store data values in key:value pairs.
    Dictionary items are ordered, changeable, and does not allow duplicates.
        Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

Accessing Items:
    x = thisdict["model"]
    x = thisdict.get("model")    
    x = thisdict.keys()
    x = thisdict.fromkeys()
    x = thisdict.values() 
    x = thisdict.items() 
    
Add / Update Items:
    thisdict["year"] = 2018
    thisdict.update({"year": 2020}) 
    
Remove Items:
    thisdict.pop("model")
    thisdict.popitem()      --> Removes the Last items
    del thisdict["model"]
    del thisdict            --> Complete Dictionary
    thisdict.clear()

Dictionary Methods:
	get()	        Returns the value of the specified key
	keys()	        Returns a list containing the dictionary's keys
	fromkeys()	    Returns a dictionary with the specified keys and value
    values()	    Returns a list of all the values in the dictionary
    items()	        Returns a list containing a tuple for each key value pair	
    update()	    Updates the dictionary with the specified key-value pairs
    setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
	pop()	        Removes the element with the specified key
	popitem()	    Removes the last inserted key-value pair
    clear()	        Removes all the elements from the dictionary
	copy()	        Returns a copy of the dictionary
	
Loops in Dictionary:
    To obtain the Keys from Dictionary
        Way-1:  for x in thisdict:
                    print(x)
        Way-2:  for x in thisdict.keys():
                    print(x)         
	To obtain the Values from Dictionary
        Way-1:  for x in thisdict:
                    print(thisdict[x])        
        Way-2:  for x in thisdict.values():
                    print(x)         
    To obtain the Items from Dictionary
        Way-1:  for x, y in thisdict.items():
                    print(x, y) 

Dictionary Comprehensions:

    names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
    heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
        print zip(names, heros)

    Problem Statement: I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
        Genral Way: my_dict = {}
                    for name, hero in zip(names, heros):
                        my_dict[name] = hero
                        print my_dict
        Dict Comprehension:
                    my_dict = {name for name, hero in zip(names, heros)} --> To merge both list
                    
                    my_dict = {name for name, hero in zip(names, heros) if name != 'peter'}
    