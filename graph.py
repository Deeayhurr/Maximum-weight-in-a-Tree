class Graph:
    """ This is a class graph that accepts a tuple and converts the tuple into a dictionary used to represent a graph
    data structure. It contains methods that help to solve the maximum weight in a tree algorithm problem """

    def __init__(self, graph_tuple):
        self.graph_tuple = graph_tuple
        self.graph_dict = {}
        self.unvisited_nodes = []
        self.visited_nodes = []
        self.cyclic_components = []
        self.not_cyclic_components = []
        self.cyclic = False

    def get_graph(self):
        """ Function to convert the input(tuple) to a graph using the dictionary Datatype """
        for shareholder, weight, spy in self.graph_tuple:
            self.graph_dict[shareholder] = [weight, spy]
        return self.graph_dict

    def get_parent_node(self, child_node):
        """This functions gets a key for any value. Therefore I am using it to get the parent node of any given node.
        That is the shareholder spying on another shareholder in this case
        https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/ """

        for key, value in self.graph_dict.items():
            if child_node == value[1]:
                return key
        return ""

    def get_child_node(self, parent_node):
        """ This functions get the child node; the shareholder that is spied on"""
        for key, value in self.graph_dict.items():
            if parent_node == key:
                return value[1]
        return ""

    def get_tree_root(self, components):
        for node_index in range(len(components)):
            parent_node = self.get_parent_node(components[node_index])
            if parent_node not in components:
                root_node = components[node_index]
                return root_node

    def is_cyclic(self):
        """ This function determines if the graph is cyclic and return a true or false value. It takes in graph as a
        parameter """
        for key in self.graph_dict.keys():
            self.unvisited_nodes.append(key)
            # edges.append((graph_dict[key][1]))
        # Check if component is cyclic
        for node_index in range(len(self.unvisited_nodes)):
            node = self.unvisited_nodes[node_index]
            self.visited_nodes.append(node)
            adjacent_node = self.graph_dict[node][1]
            # parent_node = unvisited_nodes[edges.index(node)] this returns a key value error if there is no parent node
            parent_node = self.get_parent_node(node)

            if (adjacent_node in self.visited_nodes) and (
                    (adjacent_node != parent_node) or (adjacent_node != "")):
                self.cyclic = True
                self.cyclic_components.append([parent_node, node, adjacent_node])
        if not self.cyclic_components:
            self.cyclic = False
        else:
            self.cyclic = True
            all_nodes = self.visited_nodes.copy()
            for component_index in range(len(self.cyclic_components)):
                component = self.cyclic_components[component_index]
                for node_index in range(len(component)):
                    node = component[node_index]
                    if node in all_nodes:
                        all_nodes.remove(node)
            self.not_cyclic_components = all_nodes.copy()

        return self.cyclic, self.cyclic_components, self.not_cyclic_components

    def solve_cyclic_graph(self):
        is_cyclic = self.cyclic
        if not is_cyclic:
            solution = self.solve_tree(self.visited_nodes)
            return solution
        else:
            components_max_weights = []
            for component_index in range(len(self.cyclic_components)):
                component = self.cyclic_components[component_index]
                vertex = component[0]
                component_a = component.copy()
                component_a.remove(vertex)
                solution_a = self.solve_tree(component_a)
                vertex_1 = self.get_child_node(vertex)
                component_b = component.copy()
                component_b.remove(vertex_1)
                solution_b = self.solve_tree(component_b)
                max_solution_weight = int(max(solution_a[0], solution_b[0]))
                if max_solution_weight == int(solution_a[0]):
                    solution = {"Maximum weight:": max_solution_weight, "Shareholders:": solution_a[1]}
                    components_max_weights.append(solution)
                else:
                    solution = {"Maximum weight:": max_solution_weight, "Shareholders:": solution_b[1]}
                    components_max_weights.append(solution)
            list_of_solution = []
            max_weight = 0
            for dict_index in components_max_weights:
                max_weight += dict_index["Maximum weight:"]
                list_of_solution.append(dict_index["Shareholders:"])

            solution_c = self.solve_tree(self.not_cyclic_components)
            final_max_solution_weight = int(max_weight) + int(solution_c[0])
            list_of_solution.append(solution_c[1])
            components_max_weights_solution = {"Maximum weight:":final_max_solution_weight,"Shareholders:":list_of_solution}
            return components_max_weights_solution

    def solve_tree(self, components):
        root_node = self.get_tree_root(components)
        return self.maximum_weight(root_node, components)

    def maximum_weight(self, root_node, components):
        grandchildren = []
        children = []
        grandchildren.append(root_node)

        components_size = len(components)
        child = self.get_child_node(root_node)
        if child == "":
            maximum_weight = int(self.graph_dict[root_node][0])
            return maximum_weight, root_node
        else:
            weight = int(self.graph_dict[root_node][0])  # the following steps takes into consideration the root node
            # and  get the maximum weight
            for count in range(components_size):
                for items in range(len(components)):
                    node = components[items]
                    if node == self.get_child_node(root_node):
                        grandchild_node = self.get_child_node(child)
                        if (grandchild_node not in grandchildren) and (grandchild_node in components):
                            weight = weight + int(self.graph_dict[grandchild_node][0])
                            grandchildren.append(grandchild_node)
                            root_node = grandchild_node
                        count += 1

            weight_2 = int(self.graph_dict[child][0])  # the next steps gets the maximum weight without taking into
            # consideration  the root node
            children.append(child)
            root_node = child

            for count in range(components_size):
                for items in range(len(components)):
                    node = components[items]
                    if node == self.get_child_node(root_node):
                        grandchild2_node = self.get_child_node(child)
                        if grandchild2_node not in children and (grandchild2_node in components):
                            weight_2 = weight_2 + int(self.graph_dict[grandchild2_node][0])
                            children.append(grandchild2_node)
                            root_node = grandchild2_node
                        count += 1

            maximum_weight = max(weight, weight_2)
            if maximum_weight == weight_2:
                return maximum_weight, children
            else:
                return maximum_weight, grandchildren



