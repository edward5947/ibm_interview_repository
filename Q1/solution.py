def check_request():

    N = int(input("input the number of tshirt the store has"))
    N_str = str(input("input the tshirt size the store has))"))
    M = int(input("input the request size"))
    M_str = str(input("input the requested t shirt size))"))


    size_dict = {"M":0,
                 "S":-1,
                 "L":1}

    N_list = sorted([size_dict[n[-1]]*len(n) for n in N_str.split()], reverse=True)
    M_list = sorted([size_dict[n[-1]]*len(n) for n in M_str.split()], reverse=True)

    if all([N_list[n] >= M_list[n] for n in range(M)]):
        return "Yes"
    else:
        return "No"

print(check_request())