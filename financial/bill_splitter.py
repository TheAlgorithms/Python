"""
Program to split bills among a group
"""


# function to split bill among group
def split_bill(pool: "list[dict]") -> dict:
    """
    >>> split_bill([{'name': 'sam', 'contribution': 500}, {'name': 'rohan'\
, 'contribution': 200}, {'name': 'john', 'contribution': 50}])
    {'solution': [{'name': 'sam', 'payment': [{'name': 'rohan', 'contribution'\
: 50.0}, {'name': 'john', 'contribution': 200.0}]}], 'total': 750, 'each'\
: 250.0, 'pool': [{'name': 'sam', 'contribution': 500}, {'name': 'rohan'\
, 'contribution': 200}, {'name': 'john', 'contribution': 50}]}
    """
    contribution_List = [x["contribution"] for x in pool]
    total = sum(contribution_List)
    each = total / len(contribution_List)
    more = []
    less = []
    solution = []
    for i in pool:
        if i["contribution"] < each:
            less.append({"name": i["name"], "contribution": each - i["contribution"]})
        else:
            more.append({"name": i["name"], "contribution": i["contribution"] - each})
    for i in more:
        a = i["contribution"]
        m = [{"name": k["name"], "contribution": 0} for k in less]
        for j in range(len(less)):
            b = less[j]["contribution"]
            if a == 0:
                m[j]["contribution"] = 0
            elif a - b == 0:
                a = a - b
                m[j]["contribution"] = b
                less[j]["contribution"] = 0
            elif a - b > 0:
                a = a - b
                less[j]["contribution"] = 0
                m[j]["contribution"] = b
            elif a - b < 0:
                less[j]["contribution"] = b - a
                m[j]["contribution"] = a
                a = 0
        solution.append({"name": i["name"], "payment": m})
    return {"solution": solution, "total": total, "each": each, "pool": pool}


# function to print solutionution in a format
# result is the value returned by splitBill(pool) function
def print_solutionution(result: dict) -> None:
    """
    >>> print_solutionution({'solution': [{'name': 'sam', 'payment': [{'name': 'rohan'\
, 'contribution': 50.0}, {'name': 'john', 'contribution': 200.0}]}], 'total'\
: 750, 'each': 250.0, 'pool': [{'name': 'sam', 'contribution': 500}, {'name': 'rohan'\
, 'contribution': 200}, {'name': 'john', 'contribution': 50}]})
    sam paid    $500
    rohan paid    $200
    john paid    $50
    ------------------------------------------------------------------
    Total pool amount  : $750
    Per head           : $250.0
    ------------------------------------------------------------------
    rohan should pay $50.0 to sam
    john should pay $200.0 to sam
    ------------------------------------------------------------------
    """
    for i in result["pool"]:
        print(f"{i['name']} paid    ${i['contribution']}")
    print("------------------------------------------------------------------")
    print(f"Total pool amount  : ${result['total']}")
    print(f"Per head           : ${result['each']}")
    print("------------------------------------------------------------------")
    for i in result["solution"]:
        for j in i["payment"]:
            if j["contribution"] > 0:
                print(f"{j['name']} should pay ${j['contribution']} to {i['name']}")
        print("------------------------------------------------------------------")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
