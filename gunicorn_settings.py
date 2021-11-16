import os

accesslog = '-'
bind = ['0.0.0.0:8080']

keyfile = os.getenv('LIMS_SSL_KEYFILE')
certfile = os.getenv('LIMS_SSL_CERTFILE')
ca_certs = os.getenv('LIMS_SSL_CA_CERTS')
