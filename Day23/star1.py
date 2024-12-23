connections: dict[str, set[str]] = {}

triple_sets = []

with open("data.txt") as f:
    for line in f:
        p1, p2 = line.strip().split("-")
        connections.setdefault(p1,set()).add(p2)
        connections.setdefault(p2,set()).add(p1)
        
    # for connection, short_list in connections.items():
    #     for idx, short_connection in enumerate(short_list):
    #         for other_short in short_list:
    #             if other_short in connections[short_connection]:
    #                 add = True
    #                 for triple_set in triple_sets:
    #                      if connection in triple_set and short_connection in triple_set and other_short in triple_set:
    #                         add = False
    #                         break
    #                 if add:
    #                     triple_sets.add((connection, short_connection, other_short))
    
    for connection1, connection1_set in connections.items():
        for connection2 in connection1_set:
            connection2_set = connections[connection2]
            for connection3 in connection1_set:
                if connection2 == connection3:
                    continue
                intersect = connection1_set.intersection(connection2_set)
                if connection3 in intersect:
                    triple = set((connection1, connection2, connection3))
                    if triple not in triple_sets:
                        triple_sets.append(triple)
    
    print(len(triple_sets))
    t_sets = []
    
    for triple_set in triple_sets:
        for item in triple_set:
            if item.startswith("t"):
                t_sets.append(triple_set)
                break            
    
    print(len(t_sets))
    
        

    