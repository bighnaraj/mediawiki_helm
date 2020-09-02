import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open(r'mediawiki.conf'))

user_name = config.get('mediawiki', 'mediawikiUser')
password = config.get('mediawiki', 'mediawikiPassword')
email = config.get('mediawiki', 'mediawikiEmail')
wiki_name = config.get('mediawiki', 'mediawikiName')

db_name = config.get('db', 'name')
db_user = config.get('db', 'user')
db_password = config.get('db', 'password')
db_root_user = config.get('db', 'rootUser')
db_root_password = config.get('db', 'rootPassword')

db_volume_claim = config.get('db_volume', 'existingClaim')
db_volume_accessmode = config.get('db_volume', 'accessMode')
db_volume_size = config.get('db_volume', 'size')

master_service_type = config.get('master_service', 'type')
master_service_lb = config.get('master_service', 'loadBalancerIP')

master_volume_name = config.get('master_volume', 'name')
master_volume_reclaimPolicy = config.get('master_volume', 'reclaimPolicy')
master_volume_size = config.get('master_volume', 'size')

master_volume_claim_name = config.get('master_volume_claim', 'existingClaim')
master_volume_claim_size = config.get('master_volume_claim', 'size')

pod_security_enabled = config.get('podSecurityContext', 'enabled')
pod_security_fsgroup = config.get('podSecurityContext', 'fsGroup')

container_security_enabled = config.get('containerSecurityContext', 'enabled')
container_security_user = config.get('containerSecurityContext', 'runAsUser')



import yaml

fname = "values.yaml"

stream = open(fname, 'r')
data = yaml.load(stream)

data['mediawikiUser'] = user_name
data['mediawikiPassword'] = password
data['mediawikiEmail'] = email
data['mediawikiName'] = wiki_name

data['mariadb']['db']['name'] = db_name
data['mariadb']['db']['user'] = db_user
data['mariadb']['db']['password'] = db_password

data['mariadb']['master']['persistence']['existingClaim'] = db_volume_claim
data['mariadb']['master']['persistence']['size'] = db_volume_size

data['service']['type'] = master_service_type
data['service']['loadBalancerIP'] = master_service_lb

data['persistentVolumes']['name'] = master_volume_name
data['persistentVolumes']['reclaimPolicy'] = master_volume_reclaimPolicy
data['persistentVolumes']['size'] = master_volume_size

data['persistence']['existingClaim'] = master_volume_claim_name
data['persistence']['size'] = master_volume_claim_size

data['podSecurityContext']['enabled'] = bool(pod_security_enabled)
data['podSecurityContext']['fsGroup'] = int(pod_security_fsgroup)

data['containerSecurityContext']['enabled'] = bool(container_security_enabled)
data['containerSecurityContext']['runAsUser'] = int(container_security_user)


with open(fname, 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))
