from neo4j import GraphDatabase


class GraphService:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_friendship(self, note_a_id, note_b_id, similarity_score):
        with self._driver.session() as session:
            session.run(
                "MERGE (a:Note {id: $a_id}) "
                "MERGE (b:Note {id: $a_id}) "
                "MERGE (a)-[:RELATED {score: $score}]->(b)",
                a_id=note_a_id,
                b_id=note_b_id,
                score=similarity_score,
            )
