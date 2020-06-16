
"""
@params
no_of_disk: input total number of disks
source_tower: the tower where initially all the disks are placed
destination_tower: the tower where all the disks will be shifted
auxilliary_tower:A extra tower for transfering the disks from source to destination
"""

def TowerOfHanoi(no_of_disk, source_tower, destination_tower, auxilliary_tower):

    """
    TowerOfHanoi(4,'A','B','C')
    Move disk 1 from A tower to  C tower
    Move disk 2 from  A tower to B tower
    Move disk 1 from C tower to  B tower
    Move disk 3 from  A tower to C tower
    Move disk 1 from B tower to  A tower
    Move disk 2 from  B tower to C tower
    Move disk 1 from A tower to  C tower
    Move disk 4 from  A tower to B tower
    Move disk 1 from C tower to  B tower
    Move disk 2 from  C tower to A tower
    Move disk 1 from B tower to  A tower
    Move disk 3 from  C tower to B tower
    Move disk 1 from A tower to  C tower
    Move disk 2 from  A tower to B tower
    Move disk 1 from C tower to  B tower
    """
    if no_of_disk == 1:
       print(f'Move disk 1 from {source_tower} tower to  {destination_tower} tower')
       return
    TowerOfHanoi(no_of_disk-1, source_tower, auxilliary_tower, destination_tower)
    print(f'Move disk {no_of_disk} from  {source_tower} tower to {destination_tower} tower')
    TowerOfHanoi(no_of_disk-1, auxilliary_tower, destination_tower, source_tower)


if __name__ == "__main__":
    TowerOfHanoi(4,'A','B','C')