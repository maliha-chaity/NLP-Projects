from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"   # change this

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def create_graph_entry(tx, drug, side_effect, otc):
    tx.run("""
        MERGE (d:Drug {name: $drug})
        MERGE (s:SideEffect {name: $side_effect})
        MERGE (o:OTC {status: $otc})
        MERGE (d)-[:CAUSES]->(s)
        MERGE (d)-[:AVAILABLE_AS]->(o)
    """, drug=drug, side_effect=side_effect, otc=otc)

def push_to_graph(dataframe):
    with driver.session() as session:
        for _, row in dataframe.iterrows():
            session.write_transaction(
                create_graph_entry,
                row["Drug"],
                row["Side Effect"],
                row["OTC"]
            )