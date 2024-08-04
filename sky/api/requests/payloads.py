"""Payloads for the Sky API requests."""
import functools
import os
from typing import Dict, List, Optional, Tuple, Union

import pydantic

from sky import serve
from sky.skylet import constants
from sky.utils import common
from sky.utils import common_utils


@functools.lru_cache()
def request_body_env_vars() -> dict:
    env_vars = {}
    for env_var in os.environ:
        if env_var.startswith('SKYPILOT_'):
            env_vars[env_var] = os.environ[env_var]
    env_vars[constants.USER_ID_ENV_VAR] = common_utils.get_user_hash()
    return env_vars


class RequestBody(pydantic.BaseModel):
    env_vars: Dict[str, str] = request_body_env_vars()


class CheckBody(RequestBody):
    clouds: Optional[Tuple[str]]
    verbose: bool


class OptimizeBody(pydantic.BaseModel):
    dag: str
    minimize: common.OptimizeTarget = common.OptimizeTarget.COST


class LaunchBody(RequestBody):
    """The request body for the launch endpoint."""
    task: str
    cluster_name: str
    retry_until_up: bool = False
    idle_minutes_to_autostop: Optional[int] = None
    dryrun: bool = False
    down: bool = False
    backend: Optional[str] = None
    optimize_target: common.OptimizeTarget = common.OptimizeTarget.COST
    detach_setup: bool = False
    detach_run: bool = False
    no_setup: bool = False
    clone_disk_from: Optional[str] = None
    # Internal only:
    # pylint: disable=invalid-name
    quiet_optimizer: bool = False
    is_launched_by_jobs_controller: bool = False
    is_launched_by_sky_serve_controller: bool = False
    disable_controller_check: bool = False


class ExecBody(RequestBody):
    task: str
    cluster_name: str
    dryrun: bool = False
    down: bool = False
    backend: Optional[str] = None
    detach_run: bool = False


class StopOrDownBody(pydantic.BaseModel):
    cluster_name: str
    purge: bool = False


class StatusBody(pydantic.BaseModel):
    cluster_names: Optional[List[str]] = None
    refresh: common.StatusRefreshMode = common.StatusRefreshMode.NONE


class StartBody(RequestBody):
    cluster_name: str
    idle_minutes_to_autostop: Optional[int] = None
    retry_until_up: bool = False
    down: bool = False
    force: bool = False


class AutostopBody(pydantic.BaseModel):
    cluster_name: str
    idle_minutes: int
    down: bool = False


class QueueBody(pydantic.BaseModel):
    cluster_name: str
    skip_finished: bool = False
    all_users: bool = False


class CancelBody(pydantic.BaseModel):
    cluster_name: str
    job_ids: Optional[List[int]]
    all: bool = False
    # Internal only:
    try_cancel_if_cluster_is_init: bool = False


class ClusterJobBody(pydantic.BaseModel):
    cluster_name: str
    job_id: Optional[int]
    follow: bool = True


class ClusterJobsBody(pydantic.BaseModel):
    cluster_name: str
    job_ids: Optional[List[int]]


class StorageBody(pydantic.BaseModel):
    name: str


class RequestIdBody(pydantic.BaseModel):
    request_id: str


class EndpointBody(pydantic.BaseModel):
    cluster_name: str
    port: Optional[Union[int, str]] = None


class JobStatusBody(pydantic.BaseModel):
    cluster_name: str
    job_ids: Optional[List[int]]


class JobsLaunchBody(RequestBody):
    task: str
    name: str
    detach_run: bool
    retry_until_up: bool


class JobsQueueBody(pydantic.BaseModel):
    refresh: bool = False
    skip_finished: bool = False


class JobsCancelBody(pydantic.BaseModel):
    name: Optional[str]
    job_ids: Optional[List[int]]
    all: bool = False


class JobsLogsBody(pydantic.BaseModel):
    name: Optional[str]
    job_id: Optional[int]
    follow: bool = True
    controller: bool = False


class ServeUpBody(RequestBody):
    task: str
    service_name: str


class ServeUpdateBody(RequestBody):
    task: str
    service_name: str
    mode: serve.UpdateMode


class ServeDownBody(pydantic.BaseModel):
    service_names: Optional[Union[str, List[str]]]
    all: bool = False
    purge: bool = False


class ServeLogsBody(pydantic.BaseModel):
    service_name: str
    target: Union[str, serve.ServiceComponent]
    replica_id: Optional[int] = None
    follow: bool = True


class ServeStatusBody(pydantic.BaseModel):
    service_names: Optional[Union[str, List[str]]]
