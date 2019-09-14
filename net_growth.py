def logistic(growth_rate = 2,carry_capacity = 0.3):
    return growth_rate*carry_capacity*(1-carry_capacity)

def logistic_net_binary(Nr=2,Er=2,Max_n=100,Iterations=50):
    adj = np.array([[0,1],[1,0]])
    growth = []
    cost = []
    for i in tqdm(range(Iterations)):
        growth.append(len(adj))
        
        # Number of nodes to add
        
        # new_n is the change in the numeber of nodes (+ve = increase, -ve decrease), so we convert the number of nodex to fraciton of carry capacity, work out xt+1, round to whole nodes, and subtract the current no. of nodes
        new_n = round(Max_n * logistic(Nr,len(adj)/Max_n)) - len(adj)

        # add or remove nodes
        if new_n > 0:
            n = len(adj)+new_n
            b = np.zeros((n,n))
            b[:len(adj),:len(adj)] = adj
            adj = np.copy(b)
        elif new_n < 0:
            remove = random.sample(range(0,len(adj)),abs(new_n))
            adj = np.delete(adj,remove,0)
            adj = np.delete(adj,remove,1)
            
        # stop if no network
        if len(adj) == 0:
            break

        # work out how many edges to add/remove    

        # get the current number of edges
        curr_e = np.count_nonzero(np.tril(adj))
        # get the current maximum number of edges
        max_e = (len(adj))*(len(adj)-1)/2
        # based on this, get the number of edges to add/remove
        new_e = round(max_e * logistic(Er, curr_e/max_e)) - curr_e
        


        # add/ remove edges

        # Add
        if new_e > 0:
            for e in range(new_e):
                row = random.randint(0,len(adj)-1)
                # get a column index
                col = random.randint(0,len(adj)-1)
                # if row == col, repeat until it doesnt
                while row == col:
                    row = random.randint(0,len(adj)-1)
                    col = random.randint(0,len(adj)-1)

                while adj[row,col] > 0:
                    row = random.randint(0,len(adj)-1)
                    col = random.randint(0,len(adj)-1)
                    while row == col:
                        row = random.randint(0,len(adj)-1)
                        col = random.randint(0,len(adj)-1)
                adj[row,col] = 1
                adj[col,row] = 1    

        # Remove
        elif new_e < 0:
            for e in range(abs(new_e)):
                row = random.randint(0,len(adj)-1)
                col = random.randint(0,len(adj)-1)
                while row == col:
                    row = random.randint(0,len(adj)-1)
                    col = random.randint(0,len(adj)-1)
                while adj[row,col] == 0:
                    row = random.randint(0,len(adj)-1)
                    col = random.randint(0,len(adj)-1)
                    while row == col:
                        row = random.randint(0,len(adj)-1)
                        col = random.randint(0,len(adj)-1)
                adj[row,col] = 0
                adj[col,row] = 0 

            # clean up - remove any unconnected nodes (a node dies if it is not part of a network)
        to_kill = [x for x in range(len(np.sum(adj,0))) if np.sum(adj,0)[x] == 0]
        if len(to_kill)>0:
            adj = np.delete(adj,to_kill,0)
            adj = np.delete(adj,to_kill,1) 
            
        cost.append(curr_e/max_e)
    
    return adj,growth,cost
