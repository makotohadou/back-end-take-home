import pandas as pd
from GraphUtils import Graph
from TakeHome import formatPathList

def testShortest():
    dfRoutes = pd.read_csv('../data/routes.csv')
    graph = Graph()
    for index, row in dfRoutes.iterrows():
        graph.add_edge(row[1],row[2])
        
    assert formatPathList(graph.dijsktra("JFK","YYZ")) == [["JFK","YYZ"]]
    assert formatPathList(graph.dijsktra("COO","WAW")) == [["COO","ABJ"],["ABJ","IST"],["IST","WAW"]]
    


if __name__ == "__main__":
    testShortest()
    print("Everything passed!!")