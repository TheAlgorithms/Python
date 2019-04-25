class FlowNetwork:
    def __init__(self, graph, sources, sinks):
        self.sourceIndex = None
        self.sinkIndex = None
        self.graph = graph

        self._normalizeGraph(sources, sinks)
        self.verticesCount = len(graph)
        self.maximumFlowAlgorithm = None

    # make only one source and one sink
    def _normalizeGraph(self, sources, sinks):
        if sources is int:
            sources = [sources]
        if sinks is int:
            sinks = [sinks]

        if len(sources) == 0 or len(sinks) == 0:
            return

        self.sourceIndex = sources[0]
        self.sinkIndex = sinks[0]

        # make fake vertex if there are more
        # than one source or sink
        if len(sources) > 1 or len(sinks) > 1:
            maxInputFlow = 0
            for i in sources:
                maxInputFlow += sum(self.graph[i])


            size = len(self.graph) + 1
            for room in self.graph:
                room.insert(0, 0)
            self.graph.insert(0, [0] * size)
            for i in sources:
                self.graph[0][i + 1] = maxInputFlow
            self.sourceIndex  = 0

            size = len(self.graph) + 1
            for room in self.graph:
                room.append(0)
            self.graph.append([0] * size)
            for i in sinks:
                self.graph[i + 1][size - 1] = maxInputFlow
            self.sinkIndex = size - 1


    def findMaximumFlow(self):
        if self.maximumFlowAlgorithm is None:
            raise Exception("You need to set maximum flow algorithm before.")
        if self.sourceIndex is None or self.sinkIndex is None:
            return 0

        self.maximumFlowAlgorithm.execute()
        return self.maximumFlowAlgorithm.getMaximumFlow()

    def setMaximumFlowAlgorithm(self, Algorithm):
        self.maximumFlowAlgorithm = Algorithm(self)


class FlowNetworkAlgorithmExecutor(object):
    def __init__(self, flowNetwork):
        self.flowNetwork = flowNetwork
        self.verticesCount = flowNetwork.verticesCount
        self.sourceIndex = flowNetwork.sourceIndex
        self.sinkIndex = flowNetwork.sinkIndex
        # it's just a reference, so you shouldn't change
        # it in your algorithms, use deep copy before doing that
        self.graph = flowNetwork.graph
        self.executed = False

    def execute(self):
        if not self.executed:
            self._algorithm()
            self.executed = True

    # You should override it
    def _algorithm(self):
        pass



class MaximumFlowAlgorithmExecutor(FlowNetworkAlgorithmExecutor):
    def __init__(self, flowNetwork):
        super(MaximumFlowAlgorithmExecutor, self).__init__(flowNetwork)
        # use this to save your result
        self.maximumFlow = -1

    def getMaximumFlow(self):
        if not self.executed:
            raise Exception("You should execute algorithm before using its result!")

        return self.maximumFlow

class PushRelabelExecutor(MaximumFlowAlgorithmExecutor):
    def __init__(self, flowNetwork):
        super(PushRelabelExecutor, self).__init__(flowNetwork)

        self.preflow = [[0] * self.verticesCount for i in range(self.verticesCount)]

        self.heights = [0] * self.verticesCount
        self.excesses = [0] * self.verticesCount

    def _algorithm(self):
        self.heights[self.sourceIndex] = self.verticesCount

        # push some substance to graph
        for nextVertexIndex, bandwidth in enumerate(self.graph[self.sourceIndex]):
            self.preflow[self.sourceIndex][nextVertexIndex] += bandwidth
            self.preflow[nextVertexIndex][self.sourceIndex] -= bandwidth
            self.excesses[nextVertexIndex] += bandwidth

        # Relabel-to-front selection rule
        verticesList = [i for i in range(self.verticesCount)
                        if i != self.sourceIndex and i != self.sinkIndex]

        # move through list
        i = 0
        while i < len(verticesList):
            vertexIndex = verticesList[i]
            previousHeight = self.heights[vertexIndex]
            self.processVertex(vertexIndex)
            if self.heights[vertexIndex] > previousHeight:
                # if it was relabeled, swap elements
                # and start from 0 index
                verticesList.insert(0, verticesList.pop(i))
                i = 0
            else:
                i += 1

        self.maximumFlow = sum(self.preflow[self.sourceIndex])

    def processVertex(self, vertexIndex):
        while self.excesses[vertexIndex] > 0:
            for neighbourIndex in range(self.verticesCount):
                # if it's neighbour and current vertex is higher
                if self.graph[vertexIndex][neighbourIndex] - self.preflow[vertexIndex][neighbourIndex] > 0\
                        and self.heights[vertexIndex] > self.heights[neighbourIndex]:
                    self.push(vertexIndex, neighbourIndex)

            self.relabel(vertexIndex)

    def push(self, fromIndex, toIndex):
        preflowDelta = min(self.excesses[fromIndex],
                           self.graph[fromIndex][toIndex] - self.preflow[fromIndex][toIndex])
        self.preflow[fromIndex][toIndex] += preflowDelta
        self.preflow[toIndex][fromIndex] -= preflowDelta
        self.excesses[fromIndex] -= preflowDelta
        self.excesses[toIndex] += preflowDelta

    def relabel(self, vertexIndex):
        minHeight = None
        for toIndex in range(self.verticesCount):
            if self.graph[vertexIndex][toIndex] - self.preflow[vertexIndex][toIndex] > 0:
                if minHeight is None or self.heights[toIndex] < minHeight:
                    minHeight = self.heights[toIndex]

        if minHeight is not None:
            self.heights[vertexIndex] = minHeight + 1

if __name__ == '__main__':
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
    flowNetwork = FlowNetwork(graph, entrances, exits)
    # set algorithm
    flowNetwork.setMaximumFlowAlgorithm(PushRelabelExecutor)
    # and calculate
    maximumFlow = flowNetwork.findMaximumFlow()

    print("maximum flow is {}".format(maximumFlow))
