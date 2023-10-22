from cr8.bench_spec import Spec, Instructions
from pathlib import Path
from os import path
import inspect
import json


ITERATIONS = 1000


def args(only_shapes=False):
    file_directory = path.dirname(inspect.getfile(lambda: None))
    datasets = ['polygons.json', 'linestrings.json']
    id = 0
    for dataset in datasets:
        data_source = Path(file_directory) / 'data' / dataset
        with open(data_source.absolute()) as f:
            for line in f:
                record = json.loads(line)
                if only_shapes:
                    yield [record['shape']]
                else:
                    yield (id, record['shape'])
                id += 1


spec = Spec(
    setup=Instructions(statements=[
        "create table shaped(id integer primary key, shape geo_shape) with (number_of_replicas=0);",
        "create table bkd_shaped(id integer primary key, shape geo_shape index using bkdtree) with (number_of_replicas=0);"
    ]),
    teardown=Instructions(statements=[
        "drop table if exists shaped;",
        "drop table if exists bkd_shaped;"
    ]),
    queries=[
        {
            "statement": "insert into shaped (id, shape) values (?, ?)",
            "args": args(only_shapes=False),
            "iterations": ITERATIONS
        },
        {
            "statement": "select id from shaped where match(shape, ?)",
            "args": args(only_shapes=True),
            "iterations": ITERATIONS
        },
        {
            "statement": "insert into bkd_shaped (id, shape) values (?, ?)",
            "args": args(only_shapes=False),
            "iterations": ITERATIONS,
        },
        {
            "statement": "select id from bkd_shaped where match(shape, ?)",
            "args": args(only_shapes=True),
            "iterations": ITERATIONS
        }
    ]
)
