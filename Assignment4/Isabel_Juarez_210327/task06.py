from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from validation import Report

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
r = Report()

ontology = Namespace("http://example.org/ontology#")
person = Namespace("http://example.org/person#")
g.namespace_manager.bind('ontology', ontology, override=True)
g.namespace_manager.bind('person', person, override=True)

r.validate_task_06_00(g)

classes = {
    ontology.Person: "Person",
    ontology.Researcher: "Researcher",
    ontology.Student: "Student",
    ontology.Professor: "Professor",
    ontology.University: "University",
    ontology.Course: "Course"
}

for cls, label in classes.items():
    g.add((cls, RDF.type, RDFS.Class))
    g.add((cls, RDFS.label, Literal(label, datatype=XSD.string)))

g.add((ontology.Student, RDFS.subClassOf, ontology.Person))
g.add((ontology.Professor, RDFS.subClassOf, ontology.Person))
g.add((ontology.Researcher, RDFS.subClassOf, ontology.Person))

r.validate_task_06_01(g)

properties = {
    ontology.teaches: {
        "label": "teaches",
        "domain": ontology.Professor,
        "range": ontology.Course
    },
    ontology.studiesAt: {
        "label": "studiesAt",
        "domain": ontology.Student,
        "range": ontology.University
    },
    ontology.worksIn: {
        "label": "worksIn",
        "domain": ontology.Researcher,
        "range": ontology.University
    }
}

for prop, info in properties.items():
    g.add((prop, RDF.type, RDF.Property))
    g.add((prop, RDFS.label, Literal(info["label"], datatype=XSD.string)))
    g.add((prop, RDFS.domain, info["domain"]))
    g.add((prop, RDFS.range, info["range"]))

r.validate_task_06_02(g)

g.add((person.John, RDF.type, ontology.Student))
g.add((person.Sarah, RDF.type, ontology.Professor))
g.add((person.Oscar, RDF.type, ontology.Researcher))
g.add((person.UPM, RDF.type, ontology.University))
g.add((person.CourseAI, RDF.type, ontology.Course))

g.add((person.Sarah, ontology.teaches, person.CourseAI))
g.add((person.John, ontology.studiesAt, person.UPM))
g.add((person.Oscar, ontology.worksIn, person.UPM))

r.validate_task_06_03(g)

g.add((person.Oscar, FOAF.givenName, Literal("Oscar", datatype=XSD.string)))
g.add((person.Oscar, FOAF.familyName, Literal("Corcho", datatype=XSD.string)))
g.add((person.Oscar, FOAF.mbox, Literal("oscar.corcho@upm.es", datatype=XSD.string)))

r.validate_task_06_04(g)

r.save_report("_Task_06")

print("Task 06 completed and validated successfully.")

