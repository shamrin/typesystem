import typing
import decimal

T = typing.TypeVar("T")


@typing.overload
def Decimal(
    *, default: typing.Optional[decimal.Decimal] = ..., allow_null: bool = ...
) -> typing.Optional[decimal.Decimal]:
    ...


@typing.overload
def Decimal(*, default: decimal.Decimal = ...) -> decimal.Decimal:
    ...


@typing.overload
def Choice(*, choices: typing.List[T] = ..., default: T = ..., allow_null: bool = ...) -> T:
    ...


@typing.overload
def String(*, default: str = ...) -> str:
    ...


@typing.overload
def String(*, default: typing.Optional[str] = ..., allow_null: bool = ...) -> typing.Optional[str]:
    ...


@typing.overload
def Integer(*, default: int = ...) -> int:
    ...


@typing.overload
def Integer(*, default: typing.Optional[int] = ..., allow_null: bool = ...) -> typing.Optional[int]:
    ...


@typing.overload
def Reference(to: typing.Type[T]) -> T:
    ...


@typing.overload
def Array(items: typing.Any = None) -> typing.Any:
    ...


from typesystem.base import Message, ParseError, Position, ValidationError
from typesystem.fields import (
    Any,
    Array,
    Boolean,
    Choice,
    Date,
    DateTime,
    Decimal,
    Field,
    Float,
    Integer,
    Number,
    Object,
    String,
    Text,
    Time,
    Union,
)
from typesystem.forms import Jinja2Forms
from typesystem.json_schema import from_json_schema, to_json_schema
from typesystem.schemas import Reference, Schema, SchemaDefinitions
from typesystem.tokenize.positional_validation import validate_with_positions
from typesystem.tokenize.tokenize_json import tokenize_json, validate_json
from typesystem.tokenize.tokenize_yaml import tokenize_yaml, validate_yaml

__version__ = "0.2.4"
__all__ = [
    "Array",
    "Any",
    "Boolean",
    "Choice",
    "Date",
    "DateTime",
    "Decimal",
    "Integer",
    "Jinja2Forms",
    "Field",
    "Float",
    "Number",
    "Object",
    "Reference",
    "String",
    "Text",
    "Time",
    "Union",
    # Schemas
    "Schema",
    "SchemaDefinitions",
    # Exceptions
    "ParseError",
    "ValidationError",
    "Message",
    "Position",
    # JSON Schema
    "from_json_schema",
    "to_json_schema",
    # Positional error marking
    "tokenize_json",
    "tokenize_yaml",
    "validate_json",
    "validate_yaml",
    "validate_with_positions",
]
