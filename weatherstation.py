class WeatherStation:
    def __init__(self, name ):
        self.__name = name
        self.__all_observation = []
    def add_observation(self, observation: str):
        self.__all_observation.append(observation)
    def latest_observation(self):

        length = len(self.__all_observation)
        if(length> 1):
            return self.__all_observation[length-1]
        return self.__all_observation
    def number_of_observations(self):
        return len(self.__all_observation)
    def __str__(self):
        return f"{self.__name} {len(self.__all_observation)}"
        
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)
    