# A python implementation of the Banker's Algorithm in Operating Systems using
# Processes and Resources
# {
# "Author: "Biney Kingsley (bluedistro@github.io)",
# "Date": 28-10-2018
# }
'''
The Banker's algorithm is a resource allocation and deadlock avoidance algorithm
developed by Edsger Dijkstra that tests for safety by simulating the allocation of
predetermined maximum possible amounts of all resources, and then makes a "s-state"
check to test for possible deadlock conditions for all other pending activities,
before deciding whether allocation should be allowed to continue.
[Source] Wikipedia
[Credit] Rosetta Code C implementation helped very much.
 (https://rosettacode.org/wiki/Banker%27s_algorithm)
'''

from __future__ import print_function
import numpy as np
import time


class Bankers_algorithm:

    def __init__(self, claim_vector, allocated_resources_table, maximum_claim_table):
        '''
        :param claim_vector: The maximum (in values) amount of each resources
         (eg. memory, interface, semaphores, etc.) available.
        :param allocated_resources_table: How much (in value) of each resource
        each process is currently holding
        :param maximum_claim_table: How much of each resource the system
        currently has available
        '''
        self.__claim_vector = claim_vector
        self.__allocated_resources_table = allocated_resources_table
        self.__maximum_claim_table = maximum_claim_table

    # check for allocated resources in line with each resource in the claim vector
    def __processes_resource_summation(self):
        allocated_resources = list()
        for i in range(len(self.__allocated_resources_table[0])):
            # dummy to perform addition of specific resources
            sum = 0
            for p_item in self.__allocated_resources_table:
                sum += p_item[i]
            allocated_resources.append(sum)
        return allocated_resources

    # check for available resources in line with each resource in the claim vector
    def __available_resources(self):
        return np.array(self.__claim_vector) - np.array(self.__processes_resource_summation())

    # implement safety checker by ensuring that max_claim[i][j] - alloc_table[i][j] <= avail[j]
    # in order words, calculating for the needs
    def __need(self):
        need = list()
        for i in range(len(self.__allocated_resources_table)):
            need.append(list(np.array(self.__maximum_claim_table[i])
                                     - np.array(self.__allocated_resources_table[i])))
        return need

    # build an index control dictionary to track original ids/indices
    #  of processes during removals in core operation
    def __need_index_manager(self):
        ni_manager = dict()
        for i in self.__need():
            ni_manager.update({self.__need().index(i): i})
        return ni_manager

    # core operation of the banker's algorithm
    def main(self, **kwargs):
        need_list = self.__need()
        alloc_resources_table = self.__allocated_resources_table
        available_resources = self.__available_resources()
        need_index_manager = self.__need_index_manager()
        # display information if needed
        # get the parameter that handles display
        for kw, val in kwargs.items():
            if kw and val is True:
                self.__pretty_data()
            elif kw and val is False:
                print ("[Warning] Muting data description.\n")
            else:
                print ("[Warning] Muting data description.\n")
        print("{:_^50}\n".format("_"))
        while len(need_list) != 0:
            safe = False
            for each_need in need_list:
                execution = True
                for i in range(len(each_need)):
                    if each_need[i] > available_resources[i]:
                        execution = False
                        break

                if execution:
                    safe = True
                    # get the original index of the process from ind_ctrl db
                    for original_need_index, need_clone in need_index_manager.items():
                        if each_need == need_clone:
                            process_number = original_need_index
                    # display the process id based on entry
                    print('Process {} is executing.'.format(process_number + 1))
                    # remove the process run from stack
                    need_list.remove(each_need)
                    # update available/freed resources stack
                    available_resources = np.array(available_resources) + \
                                                         np.array(alloc_resources_table[process_number])
                    # display available memory
                    print("Updated available resource stack for processes: {}"
                          .format(" ".join([str(x) for x in available_resources])))
                    break
                else:
                    pass

            if safe:
                print("The process is in a safe state.\n")

            if not safe:
                print("System in unsafe state. Aborting...\n")
                break

    # pretty display description of the allocated, maximum and claim
    # vector of the resources available
    def __pretty_data(self):

        # Information on Allocation Resource Table
        print("{:>8}".format("      Allocated Resource Table"))
        # print("{:^11} {:^8} {:^8} {:^8} {:^8}".format("  A", "B", "C", "D", "E"))
        # print("{:_^11} {:_^8} {:_^8} {:_^8} {:_^8}".format("  ", "_", "_", "_", "_"))
        for item in self.__allocated_resources_table:
            print("P{}".format(str(self.__allocated_resources_table.index(item) + 1)), end=" ")
            for it in item:
                print("{:^8}".format(it), end=" ")
            print("\n")

        # Information on Current System Resources
        print("{:>8}".format("      System Resource Table"))
        # print("{:^11} {:^8} {:^8} {:^8} {:^8}".format("  A", "B", "C", "D", "E"))
        # print("{:_^11} {:_^8} {:_^8} {:_^8} {:_^8}".format("  ", "_", "_", "_", "_"))
        for item in self.__maximum_claim_table:
            print("P{}".format(str(self.__maximum_claim_table.index(item) + 1)), end=" ")
            for it in item:
                print("{:^8}".format(it), end=" ")
            print("\n")

        # Information on Current Resource Usage by processes
        print("Current Usage by Active Processes: {:>11}"
              .format(str(" ".join([str(x) for x in self.__claim_vector]))))
        # Information on Current Resource Usage by processes
        print("Initial Available Resources: {:>15}"
              .format(str(" ".join([str(x) for x in
                                    self.__available_resources()]))))
        # make table visible during display
        time.sleep(1)


# test algorithm
def main():
    # test 1
    test_1_claim_vector = [8, 5, 9, 7]
    test_1_allocated_res_table = [[2, 0, 1, 1],
                                [0, 1, 2, 1],
                                [4, 0, 0, 3],
                                [0, 2, 1, 0],
                                [1, 0, 3, 0]]
    test_1_maximum_claim_table = [[3, 2, 1, 4],
                                [0, 2, 5, 2],
                                [5, 1, 0, 5],
                                [1, 5, 3, 0],
                                [3, 0, 3, 3]]
    # test 2
    test_2_claim_vector = [6, 5, 7, 6]
    test_2_allocated_res_table = [[1, 2, 2, 1],
                                [1, 0, 3, 3],
                                [1, 2, 1, 0]]
    test_2_maximum_claim_table = [[3, 3, 2, 2],
                                [1, 2, 3, 4],
                                [1, 3, 5, 0]]

    Bankers_algorithm(test_1_claim_vector, test_1_allocated_res_table,
                    test_1_maximum_claim_table).main(describe=True)

if __name__ == "__main__":
    main()