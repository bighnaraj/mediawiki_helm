# Introduction
deploy mediawiki on kubernetes cluster using helm chart

# Prerequisite
- Kubernetes Cluster (version - 1.14+)
- Helm (version - 3)

# Deployment Procedure
- pull the repo
- execute the deploy.sh file (bash deploy.sh)

# Fixes
- fixed the PersistentVolume Creation for application
- created a pv and pvc for mariadb manually
- fixed templates/deployment.yaml
- fixed chart/mariadb/templates/master-statefulset.yaml
