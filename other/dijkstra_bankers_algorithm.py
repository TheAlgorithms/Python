# A Python implementation of the Banker's Algorithm in Operating Systems using
# Processes and Resources
# {
# "Author: "Biney Kingsley (bluedistro@github.io), bineykingsley36@gmail.com",
# "Date": 28-10-2018
# }
"""
The Banker's algorithm is a resource allocation and deadlock avoidance algorithm
developed by Edsger Dijkstra that tests for safety by simulating the allocation of
predetermined maximum possible amounts of all resources, and then makes a "s-state"
check to test for possible deadlock conditions for all other pending activities,
before deciding whether allocation should be allowed to continue.
[Source] Wikipedia
[Credit] Rosetta Code C implementation helped very much.
 (https://rosettacode.org/wiki/Banker%27s_algorithm)
"""

import numpy as np
import time


class BankersAlgorithm:
    def __init__(
        self,
        claim_vector: list,
        allocated_resources_table: list,
        maximum_claim_table: list,
    ) -> None:
        """
        :param claim_vector: A nxn/nxm list depicting the amount of each resources
         (eg. memory, interface, semaphores, etc.) available.
        :param allocated_resources_table: A nxn/nxm list depicting the amount of each resource
        each process is currently holding
        :param maximum_claim_table: A nxn/nxm list depicting how much of each resource the system
        currently has available
        """
        self.__claim_vector = claim_vector
        self.__allocated_resources_table = allocated_resources_table
        self.__maximum_claim_table = maximum_claim_table

    def __processes_resource_summation(self) -> list:
        """
        This method checks for allocated resources in line with each resource in the claim vector
        """
        allocated_resources = list()
        for i in range(len(self.__allocated_resources_table[0])):
            sum = 0
            for p_item in self.__allocated_resources_table:
                sum += p_item[i]
            allocated_resources.append(sum)
        return allocated_resources

    def __available_resources(self) -> list:
        """
        This method checks for available resources in line with each resource in the claim vector
        """
        return np.array(self.__claim_vector) - np.array(
            self.__processes_resource_summation()
        )

    def __need(self) -> list:
        """
        This method implements safety checker by ensuring that
        max_claim[i][j] - alloc_table[i][j] <= avail[j]
        In order words, calculating for the needs
        """
        need = list()
        for i in range(len(self.__allocated_resources_table)):
            need.append(
                list(
                    np.array(self.__maximum_claim_table[i])
                    - np.array(self.__allocated_resources_table[i])
                )
            )
        return need

    def __need_index_manager(self) -> dict:
        """
        This function builds an index control dictionary to track original ids/indices
        of processes when altered during execution of method "main"
            Return: {0: [a: int, b: int], 1: [c: int, d: int]}
        >>> test_1_claim_vector = [8, 5, 9, 7]
        >>> test_1_allocated_res_table = [[2, 0, 1, 1],[0, 1, 2, 1],[4, 0, 0, 3],[0, 2, 1, 0],[1, 0, 3, 0]]
        >>> test_1_maximum_claim_table = [[3, 2, 1, 4],[0, 2, 5, 2],[5, 1, 0, 5],[1, 5, 3, 0],[3, 0, 3, 3]]
        >>> BankersAlgorithm(test_1_claim_vector, test_1_allocated_res_table, test_1_maximum_claim_table)._BankersAlgorithm__need_index_manager()
        {0: [1, 2, 0, 3], 1: [0, 1, 3, 1], 2: [1, 1, 0, 2], 3: [1, 3, 2, 0], 4: [2, 0, 0, 3]}
        """
        ni_manager = dict()
        for i in self.__need():
            ni_manager.update({self.__need().index(i): i})
        return ni_manager

    def main(self, **kwargs) -> None:
        """ 
        This method utilized the various methods in this class to simulate the Banker's algorithm
        Return: None
        >>> test_1_claim_vector = [8, 5, 9, 7]
        >>> test_1_allocated_res_table = [[2, 0, 1, 1],[0, 1, 2, 1],[4, 0, 0, 3],[0, 2, 1, 0],[1, 0, 3, 0]]
        >>> test_1_maximum_claim_table = [[3, 2, 1, 4],[0, 2, 5, 2],[5, 1, 0, 5],[1, 5, 3, 0],[3, 0, 3, 3]]
        >>> BankersAlgorithm(test_1_claim_vector, test_1_allocated_res_table, test_1_maximum_claim_table).main(describe=True)
              Allocated Resource Table
        P1    2        0        1        1     
        <BLANKLINE>
        P2    0        1        2        1     
        <BLANKLINE>
        P3    4        0        0        3     
        <BLANKLINE>
        P4    0        2        1        0     
        <BLANKLINE>
        P5    1        0        3        0     
        <BLANKLINE>
              System Resource Table
        P1    3        2        1        4     
        <BLANKLINE>
        P2    0        2        5        2     
        <BLANKLINE>
        P3    5        1        0        5     
        <BLANKLINE>
        P4    1        5        3        0     
        <BLANKLINE>
        P5    3        0        3        3     
        <BLANKLINE>
        Current Usage by Active Processes:     8 5 9 7
        Initial Available Resources:         1 2 2 2
        __________________________________________________
        <BLANKLINE>
        Process 3 is executing.
        Updated available resource stack for processes: 5 2 2 5
        The process is in a safe state.
        <BLANKLINE>
        Process 1 is executing.
        Updated available resource stack for processes: 7 2 3 6
        The process is in a safe state.
        <BLANKLINE>
        Process 2 is executing.
        Updated available resource stack for processes: 7 3 5 7
        The process is in a safe state.
        <BLANKLINE>
        Process 4 is executing.
        Updated available resource stack for processes: 7 5 6 7
        The process is in a safe state.
        <BLANKLINE>
        Process 5 is executing.
        Updated available resource stack for processes: 8 5 9 7
        The process is in a safe state.
        <BLANKLINE>                            
        """
        need_list = self.__need()
        alloc_resources_table = self.__allocated_resources_table
        available_resources = self.__available_resources()
        need_index_manager = self.__need_index_manager()
        for kw, val in kwargs.items():
            if kw and val is True:
                self.__pretty_data()
        print("{:_^50}".format("_"))
        print()
        while len(need_list) != 0:
            safe = False
            for each_need in need_list:
                execution = True
                for index, need in enumerate(each_need):
                    if need > available_resources[index]:
                        execution = False
                        break

                if execution:
                    safe = True
                    # get the original index of the process from ind_ctrl db
                    for original_need_index, need_clone in need_index_manager.items():
                        if each_need == need_clone:
                            process_number = original_need_index
                    print("Process {} is executing.".format(process_number + 1))
                    # remove the process run from stack
                    need_list.remove(each_need)
                    # update available/freed resources stack
                    available_resources = np.array(available_resources) + np.array(
                        alloc_resources_table[process_number]
                    )
                    print(
                        "Updated available resource stack for processes: {}".format(
                            " ".join([str(x) for x in available_resources])
                        )
                    )
                    break
            if safe:
                print("The process is in a safe state.")
                print()
            else:
                print("System in unsafe state. Aborting...")
                print()
                break

    def __pretty_data(self):
        """
        Properly align display of the algorithm's solution
        """
        print("{:>8}".format("      Allocated Resource Table"))
        for item in self.__allocated_resources_table:
            print(
                "P{}".format(str(self.__allocated_resources_table.index(item) + 1)),
                end=" ",
            )
            for it in item:
                print("{:^8}".format(it), end=" ")
            print()
            print()

        print("{:>8}".format("      System Resource Table"))
        for item in self.__maximum_claim_table:
            print(
                "P{}".format(str(self.__maximum_claim_table.index(item) + 1)), end=" "
            )
            for it in item:
                print("{:^8}".format(it), end=" ")
            print()
            print()

        print(
            "Current Usage by Active Processes: {:>11}".format(
                str(" ".join([str(x) for x in self.__claim_vector]))
            )
        )

        print(
            "Initial Available Resources: {:>15}".format(
                str(" ".join([str(x) for x in self.__available_resources()]))
            )
        )
        time.sleep(1)


if __name__ == "__main__":
    import doctest

    test_1_claim_vector = [8, 5, 9, 7]
    test_1_allocated_res_table = [
        [2, 0, 1, 1],
        [0, 1, 2, 1],
        [4, 0, 0, 3],
        [0, 2, 1, 0],
        [1, 0, 3, 0],
    ]
    test_1_maximum_claim_table = [
        [3, 2, 1, 4],
        [0, 2, 5, 2],
        [5, 1, 0, 5],
        [1, 5, 3, 0],
        [3, 0, 3, 3],
    ]
    doctest.testmod(
        extraglobs={
            "m": BankersAlgorithm(
                test_1_claim_vector,
                test_1_allocated_res_table,
                test_1_maximum_claim_table,
            ).main(describe=True)
        }
    )
