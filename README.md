# LLM Zoomcamp Project

## Launching Qdrant with Docker

To launch Qdrant using Docker, run the following command:

```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

This will:
- Start Qdrant on port 6333 (REST API) and 6334 (gRPC)
- Mount the `qdrant_storage` directory for persistent storage
- Use the official Qdrant Docker image

### Verify Qdrant is Running

Once started, you can verify Qdrant is running by visiting:
- Web UI: http://localhost:6333/dashboard
- API endpoint: http://localhost:6333

### Stop Qdrant

To stop the Qdrant container:
```bash
docker ps  # Find the container ID
docker stop <container_id>
```


