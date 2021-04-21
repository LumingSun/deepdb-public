from ensemble_compilation.graph_representation import SchemaGraph, Table


def gen_cover_schema(csv_path="./ssb-benchmark/cover.csv"):

    schema = SchemaGraph()
    schema.add_table(Table('cover',
                           attributes=['c0','c1','c2','c3','c4','c5','c6','c7','c8','c9'],
                           irrelevant_attributes=None,
                           no_compression=['c0','c1','c2','c3','c4','c5','c6','c7','c8','c9'],
                           csv_file_location=csv_path,
                           table_size=581012, primary_key=['c0'],
                           ))

    return schema
