#create mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#adding some more cities
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

#print out some cities
print "-" * 10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

#print out some states
print "-" * 10
print "Michigan's abbreviation is:", states['Michigan']
print "Florida's abbreviation is:", states['Florida']

#do it by using the state then the cities dict
print "-" * 10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:", cities[states['Florida']]

#print every state abbreviation
print "-" * 10
for state, abbr in states.items():
    print "%s is abbreviated %s" %(state, abbr)

#print every city
print "-" * 10
for abbr, city in cities.items():
    print "%s has the city %s" %(abbr, city)

#now do at the same time
print "-" * 10
for state, abbr in states.items():
    print "%s state is abbreviated %s and has city %s" %(state,
    abbr, cities[abbr])

print "-" * 10
#safely get an abbreviation by state that might not exist
print "search state:"
search = raw_input(">")
state = states.get(search)

if not state:
    print "Sorry, %s not found!" %search
else:
    print "%s is found with abbreviation %s and has city %s" %(search,
    states[search], cities[states[search]])

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The ctiy for the state 'TX' is: %s" % city
