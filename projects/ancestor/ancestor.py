# python3 projects/ancestor/test_ancestor.py -v

def earliest_ancestor(ancestors, starting_node, children=None, visited=None):
    # Save all of the 'children' to a separate list
    if children is None:
        children = [i[1] for i in ancestors]
    # Instantiate 'visited' set
    if visited is None:
        visited = set()
    # if the node doesn't have parents and wasn't visited return -1
    if starting_node not in children and starting_node not in visited:
        return -1

    # find a a parent of a starting node
    for i in ancestors:
        if i[1] is starting_node:
            node = i[0]
            visited.add(node)
            # run the function on the parent
            return earliest_ancestor(ancestors, node, children, visited)

    return starting_node
