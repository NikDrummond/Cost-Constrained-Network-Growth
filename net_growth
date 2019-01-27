function net = net_growth(method,N_max,NR,ER,t)
    
    % Initial network is a network of two nodes connected by a single edge
    N = 2;                      
    net = zeros(N,N);
    net(2,1) = 1;
    net(1,2) = 1;

    % Network generation

    % for each time point:
    for time = 1:t
        
        % If their are no nodes, stop growth
        if isempty(net)
            break
        end

    % -----
    % NODES
    % -----

        % First of all work out what the change in network size is
        A = N/N_max;                % node fraction max nodes
        A = NR*A*(1-A);             % work out change as fraction
        N_new = round(A*N_max);     % updated number of nodes 
        N_dif = N_new - N;          % difference in nodes

        % Add/remove nodes

        if N_dif > 0 % add new nodes
            row = zeros(length(net),N_dif);         
            col = zeros(N_dif,length(net)+N_dif);   
            net = [net row]; 
            net = [net; col];                        
            % index of new nodes
            new_nodes = N:N_new;        
        elseif N_dif< 0
            if abs(N_dif)>length(net)
                N_dif = length(net);
            end
            % randomly select number of nodes = to difference and remove row and column from matrix
            kill = randperm(length(net),abs(N_dif));
            % remove rows/cols
            net(kill,:) = []; 
            net(:,kill) = [];
        end 

    % -----
    % EDGES
    % -----

        if method == 0
            % if nodes added
            if N_dif > 0
            % for each new node (new_nodes)
                for new = 1:length(new_nodes)
                    E_new = zeros(length(net),1);
                    for E = 1:length(E_new)
                        E_new(E) = round(rand);
                    end
                    net(:,new_nodes(new)) = E_new;
                    net(new_nodes(new),:) = E_new;
                end
            end

        elseif method == 1

            % update network edges - in this version random chance of connection to
            % any existing node
            % determine the number of edges to add/remove using equation
            % based on current no. of nodes
            % get current fraction of capacity of EDGES
            cur_E = nnz(tril(net,-1)); % current number of edges, NB only take half, as symetric matrix
            max_E = round((((length(net)*length(net))-length(net))/2)); % maximum possible number of edges - (n squared - n) over 2
            fract_E = cur_E/max_E; % current fraction of edges
            new_E = ER*fract_E * (1-fract_E); % new fraction of edges
            E_new = round(new_E*max_E); % updated number of edges
            E_dif = E_new - cur_E; % difference in edges
            if E_dif > 0
                New_edges = nan(1,E_dif);
                edge_loop = 0;
                while edge_loop <= E_dif
                    edge_loop = edge_loop + 1;
                    % draw a number between 1 and length of nodes (a)
                    a = randi(length(net));
                    % draw a second one (b)
                    b = randi(length(net));
                    if a == b
                        continue
                    end
                    if net(a,b) == 1
                        continue
                    end
                    net(a,b) = 1;
                    net(b,a) = 1;
                    
                end
            elseif E_dif < 0
                New_edges = nan(1,abs(E_dif));
                edge_loop = 0;
                while edge_loop <= abs(E_dif)  
                    edge_loop = edge_loop + 1;
                    % draw a number between 1 and length of nodes (a)
                    a = randi(length(net));
                    % draw a second one (b)
                    b = randi(length(net));
                    if a == b
                        continue
                    end
                    if net(a,b) == 0
                        continue
                    end
                    net(a,b) = 0;
                    net(b,a) = 0;
                    
                end           
            end
        end
    % --------
    % CLEAN UP
    % --------

        % make sure/ check diagonal == 0
        for i = 1: length(net)
            net(i,i) = 0;
        end

        % remove any nodes with no edges
        remove = [];
        for i = 1:length(net)
            if sum(net(i,:)) == 0
                if sum(net(:,i)) == 0
                    % creat a vector of indicies where this is true
                    remove = [remove i];
                end
            end
        end
        if isempty(remove) == 0
            net(remove,:) = [];
            net(:,remove) = [];
        end
        empty(time) = length(remove);

        N = N_new;
    end
end
