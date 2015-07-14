class Digraph(object):
    """ A directed graph is a set of vertices and a collection of directed edges.  Each directed edge connects an
        ordered pair of vertices

        Main Data Structure: a list of lists of the vertices that each vertex points to

        House Keeping:
            number of vertices
            number of edges
    """

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.adj = [] # a list of adjacency lists
        for v in range(num_vertices):
            self.adj[v] = []

    def add_edge(self, v, w):
        """ Add an edge to the Digraph: v->w
            v: the tail vertex
            w: the head vertex
        """
        self.adj[v].append(w)
        self.num_edges += self.num_edges

    def reverse(self):
        """ Provode a digraph of the edges that point to each vertex (as opposed to the edges that point from each vertex)
        """
        reverse_digraph = Digraph(self.num_vertices)
        for v in range(num_vertices):
            for w in self.adj[v]:
                reverse_digraph.add_edge(w, v)
        return reverse_digraph
