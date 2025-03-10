# FastAPI Containerized Application

This repository contains a containerized FastAPI application with a Kubernetes deployment setup. The project is designed to be deployed locally.

## Table of Contents

- [Overview](#overview)
- [Infrastructure Setup](#infrastructure-setup)
- [API Server](#api-server)
  - [Application Code](#application-code)
  - [Containerization](#containerization)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Accessing the API](#accessing-the-api)
- [CI/CD with GitHub Actions](#cicd-with-github-actions)
- [License](#license)

## Overview

This project demonstrates a FastAPI application, containerized using Docker, and deployed on Kubernetes. It includes:
- A FastAPI API with a health check endpoint.
- A multi-stage Dockerfile for building the image.
- A Kubernetes manifest to deploy and expose the application.
- A GitHub Actions workflow to build, test, and push the Docker image.

## Infrastructure Setup

### Prerequisites

- **Docker:** Install from [docker.com](https://www.docker.com/get-started).
- **Kubernetes Cluster:**  [Minikube](https://minikube.sigs.k8s.io/docs/start/).
- **kubectl:** Install using the following:
  1. Install dependencies:
     ```bash
     sudo apt-get update && sudo apt-get install -y apt-transport-https ca-certificates curl
     ```
  2. Download the Google Cloud public signing key:
     ```bash
     sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
     ```
  3. Add the Kubernetes APT repository:
     ```bash
     echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
     ```
  4. Install kubectl:
     ```bash
     sudo apt-get update && sudo apt-get install -y kubectl
     ```
  5. Verify:
     ```bash
     kubectl version --client
     ```

## API Server

### Application Code

The FastAPI application is defined in `main.py`. It sets up a root endpoint which displays "Hello World", and a health endpoint that provides an "ok" message. There is also logging setup to ensure visability during the applications lifetime.

## Containerization

There is a small Dockerfile which utilizes a lightweight python 3.9 image to build. It only installs dependencies from `requirements.txt`, copies the project into a container, and starts the FastAPI server, exposing port 80 and using multiple workers for concurrency.

## Kubernetes Deployment

The Kubernetes manifest `k8s-deployment.yml` manages a pod running the FastAPI container. It uses a single replica, and pulls the container image from the Github Container Repository. The service exposes the application on port 80 using NodePort for local access.

## Deploying the manifest

**Apply the manifest**
```bash
kubectl apply -f k8s-deployment.yml
```

**Verify it is running**
```bash
kubectl get pods
kubectl get svc
```

**Expose the API**
- Using NodePort, or port-forwarding
```bash
kubectl port-forward svc/fastapi-service 8000:80
```
- Access via http://localhost:8000

## Accessing the API

**Root endpoint**
```bash
curl http://localhost:8000/
```
Expected Response
```bash
{"message": "Hello World!"}
```

**Health endpoint**
```bash
curl http://localhost:8000/health
```
Expected Response
```bash
{"status": "ok"}
```