"""Payloads for the Sky API requests."""
from typing import Dict, List, Optional, Tuple, Union

import pydantic

from sky import optimizer
from sky.api import common


class RequestBody(pydantic.BaseModel):
    env_vars: Dict[str, str] = {}


class CheckBody(RequestBody):
    clouds: Optional[Tuple[str]]
    verbose: bool


class OptimizeBody(pydantic.BaseModel):
    dag: str
    minimize: optimizer.OptimizeTarget = optimizer.OptimizeTarget.COST


class LaunchBody(RequestBody):
    """The request body for the launch endpoint."""
    task: str
    cluster_name: str
    retry_until_up: bool = False
    idle_minutes_to_autostop: Optional[int] = None
    dryrun: bool = False
    down: bool = False
    backend: Optional[str] = None
    optimize_target: optimizer.OptimizeTarget = optimizer.OptimizeTarget.COST
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
    idle_minutes_to_autostop: int
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


class CostReportBody(pydantic.BaseModel):
    all: bool


class JobStatusBody(pydantic.BaseModel):
    cluster_name: str
    job_ids: Optional[List[int]]
