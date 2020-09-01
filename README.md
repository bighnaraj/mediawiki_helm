# Introduction
deploy mediawiki on kubernetes cluster using helm chart

# Prerequisite
- Kubernetes Cluster (version - 1.14+)
- Helm (version - 3)

# Deployment Procedure
- pull the repo (git clone)
- create 2 directories (/mnt/data and /mnt/wiki)
- create pv and pvc for mariadb manually using deploypvc.yaml (automation in progress)
  -- kubectl apply -f deploypvc.yaml
- execute helm (helm install my-release mediawiki_helm)

# Fixes
- fixed the PersistentVolume Creation for application
- created a pv and pvc for mariadb manually
- fixed templates/deployment.yaml
- fixed chart/mariadb/templates/master-statefulset.yaml
- fixed values.yaml
- fixed chart/mariadb/values.yaml

# Workaround
- Because of file access restriction, the application pod may crash. Execute the following if application pod crashes
  1) sudo chown -R 1001:1001 /mnt/wiki
  2) systemctl restart docker
  3) delete the mariadb and application pod
- Because of low memory the liveness and readiness may fail
  1) rm -rf /mnt/wiki/
  2) rm -rf /mnt/data/
