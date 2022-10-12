# Starter values for computing
# Network address; Mask; Num of subnets; Max value of devices that need ip
def start_v():
    network_addr = input("Network address: ")
    prefix = int(input("Prefix of network: "))
    num_of_sub = int(input("Num of subnets: "))
    max_value_dev = int(input("Max value of hosts for one sub: "))
    return [network_addr, prefix, num_of_sub, max_value_dev]


start_list = start_v()
network_addr = start_list[0]
prefix = start_list[1]
num_of_sub = start_list[2]
max_value_dev = start_list[3]


# Function for checking is there enough ip
def enough_ip():
    needed_ip = num_of_sub * max_value_dev
    haved_ip = 2 ** (32 - int(prefix))
    # print(needed_ip)
    # print(haved_ip)
    if haved_ip >= needed_ip:
        return haved_ip
    else:
        start_v()


enough_ip()

# Function for rules of changing ip by mask
def rules_ip():
    ip_by_octat = []

    mask_bin = int(prefix) * "1" + (32 - int(prefix)) * "0"

    mask_bin_list = []
    for i in range(0, len(mask_bin), 8):
        mask_bin_list.append(mask_bin[i : i + 8])

    # mask_dec_list = [int(('0b' + i), 2) for i in mask_bin_list]

    return mask_bin_list


ip_by_octat = rules_ip()

table_of_prefix_value = {}
for i in range(0, 32):
    table_of_prefix_value.update({str(32 - i): 2**i})


# Prefix we will use
for i in table_of_prefix_value.keys():

    if int(int(table_of_prefix_value[i])) >= max_value_dev:
        prefix_need = [i, int(table_of_prefix_value[i])]
        break


# Network address in bin
def ip_in_bin(octet):
    m = str(bin(octet))
    m1 = [i for i in m]
    m1 = m1[2::]
    if len(m1) != 8:
        for i in range(0, 8 - len(m1)):
            m1.insert(0, "0")
    m2 = ["".join(m1)]
    return m2


ip_list_octet = network_addr.split(".")
ip_list_octet = [int(i) for i in ip_list_octet]
bin_ip_list = []
for i in range(len(ip_list_octet)):
    bin_ip_list.insert(i, ip_in_bin(int(ip_list_octet[i])))
    bin_ip_list[i] = bin_ip_list[i][0]


ip_list_sub = []


if int(prefix_need[0]) in range(25, 33):

    prom_ip_1 = ip_list_octet[3]
    prom_ip_2 = ip_list_octet[3] + prefix_need[1] - 1
    prom_ip_3 = ip_list_octet[2]
    prom_ip_4 = ip_list_octet[1]
    prom_ip_5 = ip_list_octet[0]

    ip_list_sub.append(
        [
            [prom_ip_5, prom_ip_4, prom_ip_3, prom_ip_1],
            [prom_ip_5, prom_ip_4, prom_ip_3, prom_ip_2],
        ]
    )
    for i in range(num_of_sub - 1):
        prom_ip_1 = prom_ip_2 + 1
        prom_ip_2 = ip_list_sub[i][1][3] + prefix_need[1]
        if prom_ip_1 > 255 or prom_ip_2 > 255:
            prom_ip_1 = 0
            prom_ip_2 = prom_ip_1 + prefix_need[1] - 1
            prom_ip_3 = prom_ip_3 + 1
            if prom_ip_3 > 255:
                prom_ip_3 = 0
                prom_ip_4 = prom_ip_4 + 1
            if prom_ip_4 > 255:
                prom_ip_4 = 0
                prom_ip_5 = prom_ip_5 + 1

            ip_list_sub.append(
                [
                    [prom_ip_5, prom_ip_4, prom_ip_3, prom_ip_1],
                    [prom_ip_5, prom_ip_4, prom_ip_3, prom_ip_2],
                ]
            )
            continue

        ip_list_sub.append(
            [
                [prom_ip_5, prom_ip_4, prom_ip_3, prom_ip_1],
                [prom_ip_5, prom_ip_4, prom_ip_3, prom_ip_2],
            ]
        )


# Results
print(25 * " " + "Subnetting - FLSM")
print(
    "Network address/prefix"
    + 5 * " "
    + "Number of subnets"
    + 5 * " "
    + "Max num of hosts for one sub\n"
    + 4 * " "
    + network_addr
    + "/"
    + str(prefix)
    + 17 * " "
    + str(num_of_sub)
    + 25 * " "
    + str(max_value_dev)
)

print()

print(
    "№Net"
    + 5 * " "
    + "Value of hosts"
    + 6 * " "
    + "Network address"
    + 5 * " "
    + "Broadcast address"
    + 8 * " "
    + "Usable hosts"
)

for i in range(num_of_sub):
    print(
        str(i + 1)
        + "\t"
        + 10 * " "
        + str(max_value_dev)
        + "\t"
        + 10 * " "
        + "{}.{}.{}.{}".format(
            ip_list_sub[i][0][0],
            ip_list_sub[i][0][1],
            ip_list_sub[i][0][2],
            ip_list_sub[i][0][3],
        )
        + "\t"
        + 7 * " "
        + "{}.{}.{}.{}".format(
            ip_list_sub[i][1][0],
            ip_list_sub[i][1][1],
            ip_list_sub[i][1][2],
            ip_list_sub[i][1][3],
        )
        + "\t"
        + 7 * " "
        + "{}.{}.{}.{} - {}.{}.{}.{}".format(
            ip_list_sub[i][0][0],
            ip_list_sub[i][0][1],
            ip_list_sub[i][0][2],
            ip_list_sub[i][0][3] + 1,
            ip_list_sub[i][1][0],
            ip_list_sub[i][1][1],
            ip_list_sub[i][1][2],
            ip_list_sub[i][1][3] - 1,
        )
    )
