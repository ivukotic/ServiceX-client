curl -L -O https://raw.githubusercontent.com/elastic/beats/7.12/deploy/kubernetes/filebeat-kubernetes.yaml

user/pass river-dev-logs
indices river-dev* filebeat-*

add to filebeat.yml
    setup:
      kibana:
        host: "https://atlas-kibana.mwt2.org:5601"
      dashboards:
        enabled: true
        kibana-index: .kibana-dev

change environment vars:
            - name: ELASTICSEARCH_HOST
              value: atlas-kibana.mwt2.org
            - name: ELASTICSEARCH_PORT
              value: "9200"
            - name: ELASTICSEARCH_USERNAME
              value: river-dev-logs
            - name: ELASTICSEARCH_PASSWORD
              value: river-dev-logs

test: 
kubectl create -f logger.yaml


Removed from ServiceX git:

from values.yaml
# Settings for sending logging messages to an elasticsearch service
elasticsearchLogging:
  enabled: False
  host: 'host'
  port: 9200
  user: 'user account'
  password: 'password'

from configmap:

    {{ if .Values.elasticsearchLogging.enabled }}
    ELASTIC_SEARCH_LOGGING_ENABLED = True
    ES_HOST = '{{ .Values.elasticsearchLogging.host }}'
    ES_PORT = '{{ .Values.elasticsearchLogging.port }}'
    ES_USER = '{{ .Values.elasticsearchLogging.user }}'
    ES_PASS = '{{ .Values.elasticsearchLogging.password }}'
    {{ else }}
    ELASTIC_SEARCH_LOGGING_ENABLED = False
    {{ end }}

from reference.md:
| `elasticsearchLogging.enabled`       | Set to True to enable writing of reports to an external ElasticSearch system | False |
| `elasticsearchLogging.host`          | Hostname for external ElasticSearch server | |
| `elasticsearchLogging.port`          | Port for external ElasticSearch Server           | 9200 |
| `elasticsearchLogging.user`          | Username to connect to external ElasticSearch Server | |
| `elasticsearchLogging.password`      | Password to connect to external ElasticSearch Server | |
