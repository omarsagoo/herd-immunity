class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''

        with open(self.file_name, 'w') as file:
            file.write("_____________Metadata_File_______________\n")
            file.write(f"{pop_size}\t {vacc_percentage}\t {virus_name}\t {mortality_rate}\t \n")
            file.write("______________given_stats________________\n")
            file.write(f"""\n
                   Population Size: {pop_size},
            vaccination Percentage: {vacc_percentage*100}%,
                 Name of the virus: {virus_name},
           Mortality rate of virus: {mortality_rate*100}%,
  basic reproduction rate of virus: {basic_repro_num*100}%
                        \n""")
            file.write("_____________________________________________")
            file.close()


        

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        with open(self.file_name, 'a') as file:
            file.write("______________\n")
            if did_infect == False and random_person_vacc == True and random_person_sick == False:
                file.write(f"Neither {person._id} or {random_person._id} is sick because neither was infected.\n")
            elif random_person_sick == True and did_infect == None:
                file.write(f"{person._id} does not infect {random_person._id} because they were already sick. \n")
            elif did_infect == True and random_person_vacc == True:
                file.write(f"{random_person._id} does not gets infected by {person._id} because they were vaccinated.\n")
            elif did_infect == True:
                file.write(f"{person._id} infects {random_person._id} because they werent vaccinated")
            file.write("________________\n")
            file.close()
        

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        
        with open(self.file_name, 'a') as file:
            if did_die_from_infection == True:
                file.write(f"{person._id} died from the infection. ")
            else:
                file.write(f"{person._id} survived the infection")

    def log_time_step(self, time_step_number, sim_data):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''

        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        init_dead = sim_data.total_dead 
        newly_dead = sim_data.total_dead - init_dead
        init_infected = sim_data.total_infected
        newly_infected = sim_data.total_infected - init_infected 

        with open(self.file_name, 'a') as file: 
            file.write(f"Time step {time_step_number} has ended, beginning time step {time_step_number + 1}\n")
            file.write(f"number of people Infected: {newly_infected}")
            file.write(f"Newly Dead: {newly_dead}")
            file.write(f"Total Dead: {sim_data.total_dead}")
            file.write(f"Total Infected: {sim_data.total_infected}")




file1 = Logger('file.txt')
file1.write_metadata(10,.3,'ebola',.4,.2)