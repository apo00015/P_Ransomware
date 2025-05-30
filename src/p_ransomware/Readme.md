docker build -t ransonware-builder .
docker run --rm -v $(pwd)/output:/output ransonware-builder
