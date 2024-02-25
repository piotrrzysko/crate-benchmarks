# Storage

* table `shaped`: 1000 rows, 11.0 MiB
* table `bkd_shaped`: 1000 rows, 7.5 MiB

# Benchmark

```
# Running setUp
# Running benchmark

## Running Query:
   Statement:
     insert into shaped (id, shape) values (?, ?)
   Concurrency: 1
   Iterations: 1000
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:17<00:00, 58.28 requests/s]
Runtime (in ms):
    mean:    16.249 ± 0.962
    min/max: 5.431 → 111.228
Percentile:
    50:   9.470 ± 15.524 (stdev)
    95:   49.680
    99.9: 105.415

## Running Query:
   Statement:
     select id from shaped where match(shape, ?)
   Concurrency: 1
   Iterations: 1000
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:09<00:00, 108.57 requests/s]
Runtime (in ms):
    mean:    8.404 ± 1.010
    min/max: 0.844 → 275.738
Percentile:
    50:   3.225 ± 16.289 (stdev)
    95:   31.275
    99.9: 171.330

## Running Query:
   Statement:
     insert into bkd_shaped (id, shape) values (?, ?)
   Concurrency: 1
   Iterations: 1000
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:09<00:00, 105.22 requests/s]
Runtime (in ms):
    mean:    8.704 ± 0.417
    min/max: 5.409 → 108.524
Percentile:
    50:   6.325 ± 6.727 (stdev)
    95:   16.795
    99.9: 85.953

## Running Query:
   Statement:
     select id from bkd_shaped where match(shape, ?)
   Concurrency: 1
   Iterations: 1000
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:04<00:00, 249.64 requests/s]
Runtime (in ms):
    mean:    3.307 ± 0.775
    min/max: 0.729 → 250.693
Percentile:
    50:   1.353 ± 12.512 (stdev)
    95:   7.662
    99.9: 188.443
# Running tearDown
```
