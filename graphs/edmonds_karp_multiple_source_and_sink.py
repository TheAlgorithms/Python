class FlowNetwork:
    def __init__(self, graph, sources, sinks):
        self.source_index = None
        self.sink_index = None
        self.graph = graph

        self._normalize_graph(sources, sinks)
        self.vertices_count = len(graph)
        self.maximum_flow_algorithm = None

    # make only one source and one sink
    def _normalize_graph(self, sources, sinks):
        if sources is int:
            sources = [sources]
        if sinks is int:
            sinks = [sinks]

        if len(sources) == 0 or len(sinks) == 0:
            return

        self.source_index = sources[0]
        self.sink_index = sinks[0]

        # make fake vertex if there are more
        # than one source or sink
        if len(sources) > 1 or len(sinks) > 1:
            max_input_flow = 0
            for i in sources:
                max_input_flow += sum(self.graph[i])

            size = len(self.graph) + 1
            for room in self.graph:
                room.insert(0, 0)
            self.graph.insert(0, [0] * size)
            for i in sources:
                self.graph[0][i + 1] = max_input_flow
            self.source_index = 0

            size = len(self.graph) + 1
            for room in self.graph:
                room.append(0)
            self.graph.append([0] * size)
            for i in sinks:
                self.graph[i + 1][size - 1] = max_input_flow
            self.sink_index = size - 1

    def find_maximum_flow(self):
        if self.maximum_flow_algorithm is None:
            raise Exception("You need to set maximum flow algorithm before.")
        if self.source_index is None or self.sink_index is None:
            return 0

        self.maximum_flow_algorithm.execute()
        return self.maximum_flow_algorithm.getMaximumFlow()

    def set_maximum_flow_algorithm(self, algorithm):
        self.maximum_flow_algorithm = algorithm(self)


class FlowNetworkAlgorithmExecutor:
    def __init__(self, flow_network):
        self.flow_network = flow_network
        self.verticies_count = flow_network.verticesCount
        self.source_index = flow_network.sourceIndex
        self.sink_index = flow_network.sinkIndex
        # it's just a reference, so you shouldn't change
        # it in your algorithms, use deep copy before doing that
        self.graph = flow_network.graph
        self.executed = False

    def execute(self):
        if not self.executed:
            self._algorithm()
            self.executed = True

    # You should override it
    def _algorithm(self):
        pass


class MaximumFlowAlgorithmExecutor(FlowNetworkAlgorithmExecutor):
    def __init__(self, flow_network):
        super().__init__(flow_network)
        # use this to save your result
        self.maximum_flow = -1

    def get_maximum_flow(self):
        if not self.executed:
            raise Exception("You should execute algorithm before using its result!")

        return self.maximum_flow


class PushRelabelExecutor(MaximumFlowAlgorithmExecutor):
    def __init__(self, flow_network):
        super().__init__(flow_network)

        self.preflow = [[0] * self.verticies_count for i in range(self.verticies_count)]

        self.heights = [0] * self.verticies_count
        self.excesses = [0] * self.verticies_count

    def _algorithm(self):
        self.heights[self.source_index] = self.verticies_count

        # push some substance to graph
        for nextvertex_index, bandwidth in enumerate(self.graph[self.source_index]):
            self.preflow[self.source_index][nextvertex_index] += bandwidth
            self.preflow[nextvertex_index][self.source_index] -= bandwidth
            self.excesses[nextvertex_index] += bandwidth

        # Relabel-to-front selection rule
        vertices_list = [
            i
            for i in range(self.verticies_count)
            if i != self.source_index and i != self.sink_index
        ]

        # move through list
        i = 0
        while i < len(vertices_list):
            vertex_index = vertices_list[i]
            previous_height = self.heights[vertex_index]
            self.process_vertex(vertex_index)
            if self.heights[vertex_index] > previous_height:
                # if it was relabeled, swap elements
                # and start from 0 index
                vertices_list.insert(0, vertices_list.pop(i))
                i = 0
            else:
                i += 1

        self.maximum_flow = sum(self.preflow[self.source_index])

    def process_vertex(self, vertex_index):
        while self.excesses[vertex_index] > 0:
            for neighbour_index in range(self.verticies_count):
                # if it's neighbour and current vertex is higher
                if (
                    self.graph[vertex_index][neighbour_index]
                    - self.preflow[vertex_index][neighbour_index]
                    > 0
                    and self.heights[vertex_index] > self.heights[neighbour_index]
                ):
                    self.push(vertex_index, neighbour_index)

            self.relabel(vertex_index)

    def push(self, from_index, to_index):
        preflow_delta = min(
            self.excesses[from_index],
            self.graph[from_index][to_index] - self.preflow[from_index][to_index],
        )
        self.preflow[from_index][to_index] += preflow_delta
        self.preflow[to_index][from_index] -= preflow_delta
        self.excesses[from_index] -= preflow_delta
        self.excesses[to_index] += preflow_delta

    def relabel(self, vertex_index):
        min_height = None
        for to_index in range(self.verticies_count):
            if (
                self.graph[vertex_index][to_index]
                - self.preflow[vertex_index][to_index]
                > 0
            ) and (min_height is None or self.heights[to_index] < min_height):
                min_height = self.heights[to_index]

        if min_height is not None:
            self.heights[vertex_index] = min_height + 1


if __name__ == "__main__":
    entrances = [0]
    exits = [3]
    # graph = [
    #     [0, 0, 4, 6, 0, 0],
    #     [0, 0, 5, 2, 0, 0],
    #     [0, 0, 0, 0, 4, 4],
    #     [0, 0, 0, 0, 6, 6],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    # ]
    graph = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

    # prepare our network
    flow_network = FlowNetwork(graph, entrances, exits)
    # set algorithm
    flow_network.set_maximum_flow_algorithm(PushRelabelExecutor)
    # and calculate
    maximum_flow = flow_network.find_maximum_flow()

    print(f"maximum flow is {maximum_flow}")
