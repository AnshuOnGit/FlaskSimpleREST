def loadDB():
    cities = []
    with open('db.csv', 'r') as file:
        for line in file.readlines():
            city = {}
            words = line.split(',')
            city['name'] = words[0].strip('\n')
            city['lat'] = words[1].strip('\n')
            city['lon'] = words[2].strip('\n')
            cities.append(city)
    return cities

def writeToDB(lines):
    with open('db.csv', 'w') as file:
        for line in lines:
            file.write(line.get('name') + ','
                       + line.get('lat') + ','
                       + line.get('lon')+ '\n')


if __name__ == '__main__':
    cities = loadDB()
    cities.append({'name':'Bodh Gaya', 'lat' : '0', 'lon' : '0'})
    writeToDB(cities)




