# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class SwitchEnums:

    @schemas.classproperty
    def ON(cls) -> typing.Literal["on"]:
        return Switch.validate("on")

    @schemas.classproperty
    def OFF(cls) -> typing.Literal["off"]:
        return Switch.validate("off")


@dataclasses.dataclass(frozen=True)
class Switch(
    schemas.Schema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "on": "ON",
            "off": "OFF",
        }
    )
    enums = SwitchEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["on"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["on"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["off"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["off"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["on","off",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "on",
        "off",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "on",
                "off",
            ],
            validated_arg
        )