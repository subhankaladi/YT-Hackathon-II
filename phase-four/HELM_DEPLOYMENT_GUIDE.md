# 🚀 Helm Chart Deployment Guide for Todo Chat Bot

## Overview
The `todo-chat-bot` Helm chart has been updated for local Minikube deployment with both frontend and backend services.

## Chart Structure
```
todo-chat-bot/
├── Chart.yaml                          # Chart metadata
├── values.yaml                         # Configuration values
├── charts/                            # Subcharts (if any)
├── templates/
│   ├── deployment.yaml               # Frontend & Backend deployments
│   ├── service.yaml                  # Frontend & Backend services
│   ├── serviceaccount.yaml          # Service account
│   ├── _helpers.tpl                 # Template helpers
│   ├── NOTES.txt                    # Post-installation notes
│   ├── hpa.yaml                     # Horizontal Pod Autoscaler
│   ├── ingress.yaml                 # Ingress (disabled)
│   ├── httproute.yaml               # HTTPRoute (disabled)
│   └── tests/
│       └── test-connection.yaml     # Connection test
└── .helmignore                      # Files to ignore
```

## Configuration (values.yaml)

### Frontend Configuration
- **Image**: `task-frontend:latest`
- **Port**: 3000 (container) → 30000 (Minikube NodePort)
- **Replicas**: 1
- **Resources**: 250m CPU request, 512Mi memory limit
- **Environment Variables**:
  - `NEXT_PUBLIC_API_URL`: http://localhost:8000
  - `NEXT_PUBLIC_DEBUG`: false
  - `BETTER_AUTH_SECRET`: Configured

### Backend Configuration
- **Image**: `task-backend:latest`
- **Port**: 8000 (container) → 30001 (Minikube NodePort)
- **Replicas**: 1
- **Resources**: 500m CPU request, 1Gi memory limit
- **Environment Variables**:
  - `DATABASE_URL`: Neon PostgreSQL connection string
  - `JWT_SECRET`: Configured
  - `OPENAI_API_KEY`: Configured
  - All other config variables

## Prerequisites

1. **Minikube**: Ensure Minikube is installed and running
   ```bash
   minikube start
   ```

2. **Helm**: Version 3.x or higher
   ```bash
   helm version
   ```

3. **kubectl**: Kubernetes command-line tool
   ```bash
   kubectl version --client
   ```

4. **Docker Images**: Built and loaded into Minikube
   - `task-frontend:latest`
   - `task-backend:latest`

## Deployment Steps

### Step 1: Load Docker Images into Minikube
```bash
# Method 1: Using minikube image load
minikube image load task-frontend:latest
minikube image load task-backend:latest

# Method 2: Use Minikube's Docker daemon
eval $(minikube docker-env)
docker build -t task-frontend:latest ./frontend
docker build -t task-backend:latest ./backend
```

### Step 2: Navigate to Chart Directory
```bash
cd /mnt/c/Users/a/Documents/GitHub/YT-Hackathon-II/phase-four
```

### Step 3: Lint the Chart (Optional but Recommended)
```bash
helm lint todo-chat-bot/
```

### Step 4: Install the Chart
```bash
# Basic installation
helm install todo-app ./todo-chat-bot

# With custom namespace
helm install todo-app ./todo-chat-bot -n default --create-namespace

# Dry run (preview)
helm install todo-app ./todo-chat-bot --dry-run --debug
```

### Step 5: Verify Deployment
```bash
# Check pods
kubectl get pods

# Check services
kubectl get services

# Check deployments
kubectl get deployments

# Describe a pod
kubectl describe pod <pod-name>
```

### Step 6: View Application
Once deployed, access:
- **Frontend**: http://localhost:30000
- **Backend API**: http://localhost:30001/docs

## Common Helm Commands

### List Releases
```bash
helm list
helm list --all-namespaces
```

### Get Values
```bash
helm get values todo-app
helm show values ./todo-chat-bot
```

### Upgrade Deployment
```bash
# Update chart
helm upgrade todo-app ./todo-chat-bot

# Override specific values
helm upgrade todo-app ./todo-chat-bot \
  --set backend.env.OPENAI_API_KEY="sk-new-key"

# Update replicas
helm upgrade todo-app ./todo-chat-bot \
  --set frontend.replicaCount=2 \
  --set backend.replicaCount=2
```

### Uninstall Release
```bash
helm uninstall todo-app
helm uninstall todo-app -n default
```

### Debug Commands
```bash
# Template rendering
helm template todo-app ./todo-chat-bot

# Check dependencies
helm dependency list ./todo-chat-bot

# Verify integrity
helm lint ./todo-chat-bot
```

## Kubernetes Monitoring

### View Logs
```bash
# Frontend logs
kubectl logs -f -l app=frontend

# Backend logs
kubectl logs -f -l app=backend

# Specific pod
kubectl logs <pod-name>

# Multiple lines from start
kubectl logs -l app=frontend --tail=50
```

### Port Forwarding
```bash
# Frontend
kubectl port-forward svc/todo-chat-bot-frontend 3000:3000

# Backend
kubectl port-forward svc/todo-chat-bot-backend 8000:8000
```

### Resource Usage
```bash
# Pod resources
kubectl top pods

# Node resources
kubectl top nodes
```

### Troubleshooting
```bash
# Describe pod (events and status)
kubectl describe pod <pod-name>

# Check events
kubectl get events --sort-by='.lastTimestamp'

# Pod status
kubectl get pods -o wide

# Service endpoints
kubectl get endpoints
```

## Advanced Configuration

### Custom Values File
Create `custom-values.yaml`:
```yaml
frontend:
  replicaCount: 2
  resources:
    requests:
      cpu: 500m
      memory: 512Mi

backend:
  replicaCount: 2
  resources:
    requests:
      cpu: 1000m
      memory: 1Gi
```

Deploy with custom values:
```bash
helm install todo-app ./todo-chat-bot -f custom-values.yaml
```

### Environment-Specific Deployments
```bash
# Development
helm install todo-app-dev ./todo-chat-bot \
  -n development --create-namespace \
  --set backend.env.DEBUG="true"

# Production
helm install todo-app-prod ./todo-chat-bot \
  -n production --create-namespace \
  --set frontend.replicaCount=3 \
  --set backend.replicaCount=3
```

## Package and Distribution

### Create Helm Package
```bash
helm package ./todo-chat-bot
# Creates: todo-chat-bot-0.2.0.tgz
```

### Upload to Repository
```bash
# Create index
helm repo index .

# Or upload to Helm Hub, GitHub Pages, etc.
```

## Health Checks

The chart includes liveness and readiness probes:

- **Frontend**: HTTP GET to `/` on port 3000
- **Backend**: HTTP GET to `/docs` on port 8000

Initial delay: 30 seconds
Period: 10 seconds

## Security Considerations

1. **Secrets**: Store sensitive data in Kubernetes Secrets
```bash
kubectl create secret generic app-secrets \
  --from-literal=openai-key="sk-xxx" \
  --from-literal=db-password="xxx"
```

2. **RBAC**: Service accounts have appropriate permissions

3. **Resource Limits**: Configured per pod

4. **Network Policies**: Can be added as needed

## Troubleshooting

### Pods not starting
```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Services not accessible
```bash
kubectl get services
kubectl port-forward svc/<service-name> 3000:3000
```

### Image pull errors
```bash
# Verify images are loaded
minikube image ls

# Reload images if needed
minikube image load task-frontend:latest
```

### Performance issues
```bash
# Check resource usage
kubectl top pods
kubectl top nodes

# Adjust limits in values.yaml
```

## Cleanup

### Remove Installation
```bash
helm uninstall todo-app
kubectl delete namespace default  # If using custom namespace
```

### Clean Minikube
```bash
minikube stop
minikube delete
```

## Additional Resources

- [Helm Documentation](https://helm.sh/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/)

---

**Last Updated**: 2026-02-04
**Chart Version**: 0.2.0
**App Version**: 1.0.0
