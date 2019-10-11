class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

def test_virus_instantiation_2():
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("Ebola", 0.7, 0.2)
    assert virus.name == "Ebola"
    assert virus.repro_rate == 0.7
    assert virus.mortality_rate == 0.2

def test_virus_instantiation_3():
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("Black Plague", 0.9, 0.1)
    assert virus.name == "Black Plague"
    assert virus.repro_rate == 0.9
    assert virus.mortality_rate == 0.1



