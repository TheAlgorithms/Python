# Biney Kingsley, bineykingsley36@gmail.com, 27-12-2019
def assembly_line_scheduling(
    line1_entry: int,
    line2_entry: int,
    line1_stations_times: list,
    line2_stations_times: list,
    line1_exit: int,
    line2_exit: int,
    line1_stations_transfer_time: list,
    line2_stations_transfer_time: list,
) -> None:
    """
    Parameters
    ----------
    *line1_entry: The time taken for an auto to mount assembly line 1
    *line2_entry: The time taken for an auto to mount assembly line 2
    *line1_stations_times: A list of times taken for each station on line 1 to finish its task
    *line2_stations_times: A list of times taken for each station on line 2 to finish its task
    *line1_exit: The time taken for an auto to exit assembly line 1
    *line2_exit: The time taken for an auto to exit assembly line 2
    *line1_stations_transfer_time: A list of times taken for an auto to be moved from line 1 to
    an equivalent/similar station on line 2
    *line2_stations_transfer_time: A list of times taken for an auto to be moved from line 1 to
    an equivalent/similar station on line 1
    Scenario
    --------
    The Colonel Motors Corporation produces automobiles in a factory that has two assem-
    bly lines. An automobile chassis enters each assembly line,
    has parts added to it at a number of stations, and a finished auto exits at the end of
    the line. Each assembly line has n stations, numbered j = 1, 2, . . . , n. We denote
    the j th station on line i (where i is 1 or 2) by S i, j . The j th station on line 1 (S 1, j )
    performs the same function as the j th station on line 2 (S 2, j ). The stations were
    built at different times and with different technologies, however, so that the time
    required at each station varies, even between stations at the same position on the
    two different lines. We denote the assembly time required at station S i, j by a i, j .
    A chassis enters station 1 of one of the assembly lines, and
    it progresses from each station to the next. There is also an entry time e i for the
    chassis to enter assembly line i and an exit time x i for the completed auto to exit
    assembly line i.
    Normally, once a chassis enters an assembly line, it passes through that line
    only. The time to go from one station to the next within the same assembly line
    is negligible. Occasionally a special rush order comes in, and the customer wants
    the automobile to be manufactured as quickly as possible. For rush orders, the
    chassis still passes through the n stations in order, but the factory manager may
    switch the partially-completed auto from one assembly line to the other after any
    station. The time to transfer a chassis away from assembly line i after having gone
    through station S i, j is t i, j , where i = 1, 2 and j = 1, 2, . . . , n − 1 (since after
    the nth station, assembly is complete). 
    The problem is to determine which stations to choose from line 1 and which to choose from 
    line 2 in order to minimize the total time through the factory for one auto.

    * This problem is discussed and was taken from the book "Introduction to Algorithms" by
    Cormen, H. T. et al.

    Example
    -------
    >>> line1_entry = 2
    >>> line2_entry = 4
    >>> line1_exit = 3
    >>> line2_exit = 2
    >>> line1_stations_times = [7,9,3,4,8,4]
    >>> line2_stations_times = [8,5,6,4,5,7]
    >>> line1_stations_transfer_time = [2,3,1,3,4]
    >>> line2_stations_transfer_time = [2,1,2,2,1]
    >>> assembly_line_scheduling(line1_entry, line2_entry, line1_stations_times, line2_stations_times, line1_exit, line2_exit, line1_stations_transfer_time, line2_stations_transfer_time)
    line 1, station 1
    line 2, station 2
    line 1, station 3
    line 1, station 4
    line 2, station 5
    line 1, station 6
    """
    line1_rule = []
    line2_rule = []
    # f[_1], f_2: Fastest possible time to get a chassis from the starting point through station S_i,j
    f_1 = []
    f_2 = []
    f_star = []  # fastest time to get a chassis all the way through the factory
    l_star = (
        []
    )  # selected stations from each assembly line in the course of optimization
    f_1.append(line1_entry + line1_stations_times[0])
    f_2.append(line2_entry + line2_stations_times[0])
    for j in range(1, len(line1_stations_times)):
        # on line 1, check the next station choice with fastest time considering options on line 2 station equivalent as well
        line1_main = (
            f_1[j - 1] + line1_stations_times[j],
            f_2[j - 1] + line2_stations_transfer_time[j - 1] + line1_stations_times[j],
        )
        l1_station_minimum_time = min(line1_main)
        f_1.append(l1_station_minimum_time)
        line1_rule.append(line1_main.index(l1_station_minimum_time) + 1)
        # on line 2, check the next station choice with fastest time considering options on line 1 station equivalent as well
        line2_main = (
            f_2[j - 1] + line2_stations_times[j],
            f_1[j - 1] + line1_stations_transfer_time[j - 1] + line2_stations_times[j],
        )
        l2_station_minimum_time = min(line2_main)
        f_2.append(l2_station_minimum_time)
        line2_rule.append(line2_main.index(l2_station_minimum_time) + 1)
    for index in range(len(f_1)):
        if f_1[index] + line1_exit <= f_2[index] + line2_exit:
            f_star.append(f_1[index])
            l_star.append(1)
        else:
            f_star.append(f_2[index])
            l_star.append(2)
    for index, val in enumerate(l_star):
        print(f"line {val}, station {index+1}")


if __name__ == "__main__":
    import doctest

    line1_entry = 2
    line2_entry = 4
    line1_exit = 3
    line2_exit = 2
    line1_stations_times = [7, 9, 3, 4, 8, 4]
    line2_stations_times = [8, 5, 6, 4, 5, 7]
    line1_stations_transfer_time = [2, 3, 1, 3, 4]
    line2_stations_transfer_time = [2, 1, 2, 2, 1]
    doctest.testmod(
        extraglobs={
            "a": assembly_line_scheduling(
                line1_entry,
                line2_entry,
                line1_stations_times,
                line2_stations_times,
                line1_exit,
                line2_exit,
                line1_stations_transfer_time,
                line2_stations_transfer_time,
            )
        }
    )
