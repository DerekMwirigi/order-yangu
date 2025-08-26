FROM google/cloud-sdk:latest

# Install JDK 21 (Temurin) from Adoptium
RUN apt-get update && apt-get install -y wget gnupg \
    && wget -O- https://packages.adoptium.net/artifactory/api/gpg/key/public | tee /etc/apt/trusted.gpg.d/adoptium.asc \
    && echo "deb https://packages.adoptium.net/artifactory/deb bookworm main" > /etc/apt/sources.list.d/adoptium.list \
    && apt-get update \
    && apt-get install -y temurin-21-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

    EXPOSE 8085