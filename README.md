# Introduction
deploy mediawiki on kubernetes cluster using helm chart

# Prerequisite
- Kubernetes Cluster (version - 1.14+)
- Helm (version - 3)
- python 2.7

# Deployment Procedure
- pull the repo (git clone)
- Enter into the directory (cd mediawiki_helm)
- create 2 directories (mkdir -p /mnt/data /mnt/wiki)
- create pv and pvc for mariadb manually using deploypvc.yaml (automation in progress)
  -- kubectl apply -f deploypvc.yaml
- set the configuration parameters into the config file (vi mediawiki.conf)
- execute the automate.py file (python automate.py)
- fetch the absolute_path for the current directory (pwd)
- execute helm (helm install my-release absolute_path)

# Fixes
- fixed the PersistentVolume Creation for application
- created a pv and pvc for mariadb manually
- fixed templates/deployment.yaml
- fixed chart/mariadb/templates/master-statefulset.yaml
- fixed values.yaml
- fixed chart/mariadb/values.yaml

# Workaround (Automation in progress)
- Because of file access restriction, the application pod may crash. Execute the following if application pod crashes
  1) sudo chown -R 1001:1001 /mnt/wiki
  2) systemctl restart docker
  3) delete the mariadb and application pod. They will be redeployed by deployment config
- Because of low memory the liveness and readiness may fail. Execute the following.
  1) rm -rf /mnt/wiki/
  2) rm -rf /mnt/data/
  3) delete the mariadb and application pod. They will be redeployed by deploymeny config
