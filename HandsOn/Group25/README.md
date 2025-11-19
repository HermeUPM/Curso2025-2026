# GROUP25
## Nombre de los integrantes del grupo y usuarios de GitHub

- Nombre: Daniel Fernández Feás Usuario: @DanielFernandezFeas
- Nombre: Daniel Javier Flores Flores Usuario: @danielorse
- Nombre: Araceli Rubio García Usuario: @arubiio
- Nombre: Jaime Martín-Borregón Musso Usuario: @mborre1

## Descripción del trabajo
Selección de datasets Smart City (accidentalidad Madrid 2024 en CSV), evaluación de requisitos (R1–R6) y definición de la aplicación a construir.

## Estructura
Group25/
│
├── csv/
│   ├── 2024_Accidentalidad.csv
│   ├── 2024-Accidentalidad-updated.csv
│   └── 2024-Accidentalidad-with-links.csv
│
├── mappings/
│   ├── 2024-Accidentalidad-with-links.rml
│   ├── accidentes.yml
│   ├── config.ini
│   └── mapping.rml.ttl
│
├── ontology/
│   ├── accidents.ttl
│   └── examples.ttl
│
├── openrefine/
│   ├── accidentalidad-operations.json
│   └── operations-with-links.json
│
├── rdf/
│   └── (archivos RDF generados)
│
├── requirements/
│   ├── applicationRequirements.html
│   ├── datasetRequirements.html
│   └── Estructura_ConjuntoDatos_Accidentesev2.pdf
│
├── .gitattributes
├── analysis.html
├── README.md
│
├── selfAssessmentHandsOn1.md
├── selfAssessmentHandsOn2.md
├── selfAssessmentHandsOn3.md
└── selfAssessmentHandsOn4.md
Descripción de carpetas
csv/

Contiene los datasets de accidentalidad:

Dataset original.

Dataset corregido.

Dataset enriquecido con URIs.

mappings/

Incluye los mapeos para generación de RDF:

RML principal.

Configuración.

Mapeos auxiliares y plantillas.

ontology/

Contiene la ontología desarrollada para modelar el dominio:

Ontología principal.

Ejemplos de uso.

openrefine/

Incluye todas las operaciones ejecutadas durante la limpieza de datos.

rdf/

Almacena los resultados RDF generados mediante RMLMapper.

requirements/

Incluye los documentos de requisitos de la aplicación y del conjunto de datos.

Otros archivos

Incluye análisis, autoevaluaciones y metadatos del repositorio.

Flujo del proyecto

Procesamiento de datos originales (csv/).

Limpieza y normalización mediante OpenRefine (openrefine/).

Modelado ontológico (ontology/).

Creación de mapeos RML (mappings/).

Generación de datos RDF (rdf/).

Redacción de requisitos y análisis (requirements/).

Autoevaluaciones del alumnado (selfAssessmentHandsOn*.md).
