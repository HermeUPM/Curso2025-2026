from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, FOAF, XSD
from validation import Report

g = Graph()
r = Report()

ontology = Namespace("http://example.org/ontology#")
person = Namespace("http://example.org/person#")
g.namespace_manager.bind('ontology', ontology)
g.namespace_manager.bind('person', person)

query1 = """
PREFIX ontology: <http://example.org/ontology#>
SELECT ?s ?label WHERE {
  ?s a ontology:Person .
  OPTIONAL { ?s rdfs:label ?label }
}
"""
results1 = g.query(query1)
for row in results1:
    print(row)

r.validate_task_07_01(g)

query2 = """
PREFIX ontology: <http://example.org/ontology#>
CONSTRUCT {
  ?prof a ontology:Professor ;
        ontology:teaches ?course .
}
WHERE {
  ?prof a ontology:Professor ;
        ontology:teaches ?course .
}
"""
subgraph = g.query(query2).graph
print("Subgraph triples:", len(subgraph))

r.validate_task_07_02(g)

query3 = """
PREFIX ontology: <http://example.org/ontology#>
ASK {
  ?r a ontology:Researcher ;
     ontology:worksIn ?u .
  ?u a ontology:University .
}
"""
result3 = g.query(query3)
print("Researcher working in a University?", bool(result3))

r.validate_task_07_03(g)

r.save_report("_Task_07")

print("Task 07 completed and validated successfully.")
