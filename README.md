# Demo: Red Panda

## Description

The core of this project is a docker compose configuration. A python producer service sends fake user data into RedPandas Stream (i.e Kafka). The consumer service read from the topic inserts the data into Postgres.


## Business Requirements

- Be able to process 500 messages per minute
## Technical Reqiurements

- Make sure we can spin up your solution with docker compose
- Use Postgres as the final datastore
- Use Red Pandas as the message broker
- Use Alembic for the postgres migration
## Setup

```bash
cd app
make startup
```


## References

- https://www.fadhil-blog.dev/blog/streaming-batch-worker/
- https://www.confluent.io/blog/kafka-listeners-explained/