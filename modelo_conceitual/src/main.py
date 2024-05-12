import pandas as pd
from graphviz import Graph

dot = Graph()
dot.node("prof1", "prof. 1")
dot.node("prof2", "prof. 2")
dot.node("prof3", "prof. 3")
dot.node("profN", "prof. ...N")

dot.node("siglaU", "SIGLA[CURSO][PER.]")
dot.node("siglaV", "SIGLA[CURSO][PER.]")
dot.node("siglaW", "SIGLA[CURSO][PER.]")
dot.node("siglaX", "SIGLA[CURSO][PER.]")
dot.node("siglaY", "SIGLA[CURSO][PER.]")
dot.node("siglaZ", "SIGLA[CURSO][PER.]")

dot.edges(
    [
        ("prof1", "siglaV"),
        ("prof1", "siglaV"),
        ("prof1", "siglaV"),
        ("prof1", "siglaV"),
        ("prof1", "siglaW"),
        ("prof1", "siglaW"),
        ("prof1", "siglaW"),
        ("prof1", "siglaW"),
        ("prof2", "siglaU"),
        ("prof2", "siglaU"),
        ("prof2", "siglaU"),
        ("prof2", "siglaU"),
        ("prof3", "siglaX"),
        ("prof3", "siglaX"),
        ("prof3", "siglaX"),
        ("prof3", "siglaY"),
        ("prof3", "siglaY"),
        ("profN", "siglaZ"),
        ("profN", "siglaZ"),
        ("profN", "siglaZ"),
        ("profN", "siglaZ"),
        ("profN", "siglaY"),
        ("profN", "siglaY"),
    ]
)

dot.render("../output/output", view=False)
