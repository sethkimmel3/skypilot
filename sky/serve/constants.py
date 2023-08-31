"""Constants used for SkyServe."""

CONTROLLER_PREFIX = 'sky-serve-controller-'

CONTROLLER_TEMPLATE = 'sky-serve-controller.yaml.j2'

SERVE_PREFIX = '~/.sky/serve'

CONTROLLER_SYNC_INTERVAL = 20

JOB_PENDING_THRESHOLD = 5
JOB_WAITING_TIMEOUT = 30

# We need 200GB disk space to enable using Azure as controller, since its image
# size is 150GB.
CONTROLLER_RESOURCES = {'disk_size': 200, 'cpus': '4+'}

# A period of time to initialize your service. Any readiness probe failures
# during this period will be ignored.
DEFAULT_INITIAL_DELAY_SECONDS = 1200
DEFAULT_MIN_REPLICAS = 1

CONTROLLER_PORT_START = 20001
LOAD_BALANCER_PORT_START = 30001
LOAD_BALANCER_PORT_RANGE = '30000-40000'
