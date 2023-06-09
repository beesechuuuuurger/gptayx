# Copyright (C) 2022 Alteryx, Inc. All rights reserved.
#
# Licensed under the ALTERYX SDK AND API LICENSE AGREEMENT;
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.alteryx.com/alteryx-sdk-and-api-license-agreement
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Mock field class definition."""
from typing import Any, Callable, Iterable, Mapping, TYPE_CHECKING

from .constants import FieldType
from .record_ref import RecordRef

if TYPE_CHECKING:
    from .record_creator import RecordCreator


def _return_none_on_type_error(func: Callable) -> Callable:
    def inner(*args: Iterable, **kwargs: Mapping) -> Any:
        try:
            return func(*args, **kwargs)
        except TypeError:
            return None

    return inner


class Field:
    """Field mock."""

    def __init__(
        self,
        name: str,
        type: FieldType,
        size: int,
        scale: int,
        source: str,
        description: str,
    ) -> None:
        """Construct a field."""
        self.name = name
        self.type = type
        self.size = size
        self.scale = scale
        self.source = source
        self.description = description

    def equal_type(self, other_field: "Field") -> bool:
        """Check if another field has an equal type."""
        return (
            self.type == other_field.type
            and self.size == other_field.size
            and self.scale == other_field.scale
        )

    @_return_none_on_type_error
    def get_as_bool(self, record_ref: RecordRef) -> bool:
        """Get value of field as a boolean."""
        return bool(record_ref.get_field(self.name))

    @_return_none_on_type_error
    def get_as_double(self, record_ref: RecordRef) -> float:
        """Get value of a field as a double."""
        return float(record_ref.get_field(self.name))

    @_return_none_on_type_error
    def get_as_int32(self, record_ref: RecordRef) -> int:
        """Get value of a field as an int32."""
        return int(record_ref.get_field(self.name))

    @_return_none_on_type_error
    def get_as_int64(self, record_ref: RecordRef) -> int:
        """Get value of a field as an int64."""
        return int(record_ref.get_field(self.name))

    @_return_none_on_type_error
    def get_as_string(self, record_ref: RecordRef) -> str:
        """Get value of a field as a string."""
        return str(record_ref.get_field(self.name))

    @_return_none_on_type_error
    def get_as_blob(self, record_ref: RecordRef) -> bytes:
        """Get value of a field as a blob."""
        return bytes(record_ref.get_field(self.name))

    def get_null(self, record_ref: RecordRef) -> bool:
        """Check if the value of a field is null."""
        return record_ref.get_field(self.name) is None

    def set_from_bool(self, record_creator: "RecordCreator", value: bool) -> None:
        """Set value of a field as a boolean."""
        record_creator.set_field(self.name, bool(value))

    def set_from_double(self, record_creator: "RecordCreator", value: float) -> None:
        """Set value of a field as a double."""
        record_creator.set_field(self.name, float(value))

    def set_from_int32(self, record_creator: "RecordCreator", value: int) -> None:
        """Set value of a field as an int32."""
        record_creator.set_field(self.name, int(value))

    def set_from_int64(self, record_creator: "RecordCreator", value: int) -> None:
        """Set value of a field as an int64."""
        record_creator.set_field(self.name, int(value))

    def set_from_string(self, record_creator: "RecordCreator", value: str) -> None:
        """Set value of a field as a string."""
        record_creator.set_field(self.name, str(value))

    def set_from_blob(self, record_creator: "RecordCreator", value: bytes) -> None:
        """Set value of a field as a blob."""
        record_creator.set_field(self.name, bytes(value))

    def set_null(self, record_creator: "RecordCreator") -> None:
        """Set value of a field to null."""
        record_creator.set_field(self.name, None)
