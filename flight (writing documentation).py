class Flight:
    """A class that represents a flight.

    Attributes:
        number (int): the number of the flight.
        origin (str): place where the flight started from.
        destination (str): palce where the flight is going to.
        num_passengers (int): the number of passengers.
        total_weight (float): the sum of all weights transported.
        pilot (str): name of the pilot of the flight.
        crew (list): names of the crew people.

    Methods:
        display_flight_data(self):
            Prints out the data of the flight.
    """

    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """ Initializes an intance of Flight.
            Args:
                number (int): the number of the flight.
                origin (str): place where the flight started from.
                destination (str): palce where the flight is going to.
                num_passengers (int): the number of passengers.
                total_weight (float): the sum of all weights transported.
                pilot (str): name of the pilot of the flight.
                crew (list): names of the crew people.
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot
        self._crew = crew
        
    @property
    def total_weight(self):
        """Returns the total weight of the flight"""
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight

    @property
    def pilot(self):
        """Returns the name of the flight pilot"""
        return self._pilot

    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot

    @property
    def crew(self):
        """Returns the list of crew names"""
        return self._crew

    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew

    def display_flight_data(self):
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self.weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)
