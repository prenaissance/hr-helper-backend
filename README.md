# python backend

# create conda enviroment

conda create --name <envname> --file requirements.txt

# activate conda enviromen

conda activate <envname>

# deactivate conda enviroment

conda deactivate

# run project

python main.py or python3 main.py

## Requests schema

> Note: timestamp should be consistently formatted between all requests
> (e.g. all timestamps ISO formatted or all timestamps UNIX epoch)

### GET /api/statistics/preview

```ts
type StatisticsPreviewDF {
    clicksToConvert: number;
    clicksToShare: number;
    timeToConvert: number;
    timeToShare: number;
    timestamp: string;
}

type return = StatisticsPreviewDF[];
```

### GET /api/statistics/[:dimension]?column=[:column]

> Note: query/ path parameters SHOULD NOT be directly injected into the query, validate the input

```ts
type GroupedStatistics = {
    field: string;
    values: number;
}

type return = GroupedStatistics[];
```

#### Example: GET /api/statistics/clicksToConvert?column=device

```json
[
  {
    "field": "Mobile",
    "values": [
      1, 2, 3
    ]
  },
  {
    "field": "Desktop",
    "values": [
      4, 9, 10
    ]
  }
]
```

### GET /api/metrics/preview

```ts
type MetricsPreview = {
    totalClicks: number;
    uniqueClicks: number;
    averageTime: number;
    conversionRate: number;
    shareRate: string;
}

type return = MetricsPreview;
```

### GET /api/metrics/[:dimension]

> Note: query/ path parameters SHOULD NOT be directly injected into the query, validate the input

```ts
type GroupedMetric = {
    period: string;
    value: number;
}

type return = GroupedMetric[];
```

#### Example: GET /api/metrics/clicks

```json
[
  {
    "period": "1AM",
    "value": 12
  },
  {
    "period": "2AM",
    "value": 14
  }
]
```

TODO: Describe login schema after you implement it
