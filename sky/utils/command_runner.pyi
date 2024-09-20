"""Stub file for sky.utils.command_runner.

This file is dynamically generated by stubgen and added with the
overloaded type hints for SSHCommandRunner.run(), as we need to
determine the return type based on the value of require_outputs.
"""
import enum
import typing
from typing import Any, Iterable, List, Optional, Tuple, Union

from typing_extensions import Literal

from sky import sky_logging as sky_logging
from sky.skylet import log_lib as log_lib
from sky.utils import subprocess_utils as subprocess_utils

GIT_EXCLUDE: str
RSYNC_DISPLAY_OPTION: str
RSYNC_FILTER_OPTION: str
RSYNC_EXCLUDE_OPTION: str
ALIAS_SUDO_TO_EMPTY_FOR_ROOT_CMD: str


def ssh_options_list(
    ssh_private_key: Optional[str],
    ssh_control_name: Optional[str],
    *,
    ssh_proxy_command: Optional[str] = ...,
    docker_ssh_proxy_command: Optional[str] = ...,
    timeout: int = ...,
    port: int = ...,
    disable_control_master: Optional[bool] = ...,
) -> List[str]:
    ...


class SshMode(enum.Enum):
    NON_INTERACTIVE: int
    INTERACTIVE: int
    LOGIN: int


class CommandRunner:
    node_id: str

    def __init__(
        self,
        node: Tuple[Any, ...],
        **kwargs,
    ) -> None:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: Literal[False] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> int:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: Literal[True],
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> Tuple[int, str, str]:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: bool = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> Union[Tuple[int, str, str], int]:
        ...

    def rsync(self,
              source: str,
              target: str,
              *,
              up: bool,
              log_path: str = ...,
              stream_logs: bool = ...,
              max_retry: int = ...) -> None:
        ...

    @classmethod
    def make_runner_list(cls: typing.Type[CommandRunner],
                         node_list: Iterable[Tuple[Any, ...]],
                         **kwargs) -> List[CommandRunner]:
        ...

    def check_connection(self) -> bool:
        ...

    def close_cached_connection(self) -> None:
        ...


class SSHCommandRunner(CommandRunner):
    ip: str
    port: int
    ssh_user: str
    ssh_private_key: str
    ssh_control_name: Optional[str]
    docker_user: str
    disable_control_master: Optional[bool]

    def __init__(
        self,
        node: Tuple[str, int],
        ssh_user: str,
        ssh_private_key: str,
        ssh_control_name: Optional[str] = ...,
        docker_user: Optional[str] = ...,
        disable_control_master: Optional[bool] = ...,
    ) -> None:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: Literal[False] = ...,
            port_forward: Optional[List[int]] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> int:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: Literal[True],
            port_forward: Optional[List[int]] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> Tuple[int, str, str]:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            require_outputs: bool = ...,
            port_forward: Optional[List[int]] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> Union[Tuple[int, str, str], int]:
        ...

    def rsync(self,
              source: str,
              target: str,
              *,
              up: bool,
              log_path: str = ...,
              stream_logs: bool = ...,
              max_retry: int = ...) -> None:
        ...


class KubernetesCommandRunner(CommandRunner):

    def __init__(
        self,
        node: Tuple[Tuple[str, str], str],
    ) -> None:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            port_forward: Optional[List[int]] = ...,
            require_outputs: Literal[False] = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> int:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            port_forward: Optional[List[int]] = ...,
            require_outputs: Literal[True],
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> Tuple[int, str, str]:
        ...

    @typing.overload
    def run(self,
            cmd: Union[str, List[str]],
            *,
            port_forward: Optional[List[int]] = ...,
            require_outputs: bool = ...,
            log_path: str = ...,
            process_stream: bool = ...,
            stream_logs: bool = ...,
            ssh_mode: SshMode = ...,
            separate_stderr: bool = ...,
            connect_timeout: Optional[int] = ...,
            source_bashrc: bool = ...,
            skip_lines: int = ...,
            **kwargs) -> Union[Tuple[int, str, str], int]:
        ...

    def rsync(self,
              source: str,
              target: str,
              *,
              up: bool,
              log_path: str = ...,
              stream_logs: bool = ...,
              max_retry: int = ...) -> None:
        ...
