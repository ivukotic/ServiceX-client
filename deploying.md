
* https://servicex.readthedocs.io/en/latest/

pip install servicex-cli==1.0.0

kubectl config use-context docker-desktop
servicex init --cert-dir C:\Users\ilija\.globus # --namespace=sx-ilija
helm repo add ssl-hep https://ssl-hep.github.io/ssl-helm-charts/
helm repo update
helm install -f values.yaml --version v1.0.0 servicex ssl-hep/servicex

to deploy non-released chart:
* clone servicex git repo
* move your values.yaml to it
* do "helm dependency update servicex"
* deploy: "helm install -f values_with_ingress_controller.yaml servicex servicex"

START /B kubectl port-forward service/servicex-servicex-app 8000:8000
START /B kubectl port-forward service/servicex-minio 9000:9000
START /B kubectl port-forward service/servicex-rabbitmq 15672:15672
START /B kubectl port-forward service/servicex-postgresql 5432:5432



Client
kubectl run tmp-shell --rm -i --tty --image python:3.7-slim -- /bin/bash
apt-get update
apt-get -y install vim
vi servicex.yaml

python -m pip install func-adl-servicex

### GCE
pip3 install servicex-cli==1.0.0rc3
export PATH=$PATH:/home/ilijav/.local/bin
servicex init --cert-dir /home/ilijav/.globus