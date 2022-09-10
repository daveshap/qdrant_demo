# qdrant_demo
Public demo testing qdrant

## Requirements

- https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package
- https://www.docker.com/products/docker-desktop/
- https://hub.docker.com/r/qdrant/qdrant

This will map the port as well as the volume. Check for the volume in Docker Desktop -> Volumes
`docker run -p 6333:6333 -v ./qdrant_storage:/qdrant/storage qdrant/qdrant`


## Qdrant stuff

- https://qdrant.tech/
- https://github.com/qdrant/qdrant/blob/master/QUICK_START.md
- https://qdrant.tech/articles/neural-search-tutorial/