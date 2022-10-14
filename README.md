# RedPandas Example

## Description

A python producer service sends data into RedPandas Stream (i.e Kafka). The consumer service insert the data into
Postgres.

The Postgres database is created with alembic.

## Setup

```
cd app
make startup
```


## References

- https://www.fadhil-blog.dev/blog/streaming-batch-worker/
- https://www.confluent.io/blog/kafka-listeners-explained/