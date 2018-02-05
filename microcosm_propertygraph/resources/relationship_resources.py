"""
Relationship resources.

"""
from marshmallow import Schema, fields
from microcosm_flask.fields import EnumField
from microcosm_flask.paging import PageSchema


def make_relationship_schema(type_enum_cls):
    class RelationshipSchema(Schema):
        startId = fields.String(
            attribute="start_id",
            required=True,
        )
        endId = fields.String(
            attribute="end_id",
            required=True,
        )
        type = EnumField(
            type_enum_cls,
            required=True,
        )
        properties = fields.Dict(
            required=True,
        )

    return RelationshipSchema


class SearchRelationshipSchema(PageSchema):
    """
    Base search schema for relationships. Can be overridden by services
    to support customized querying criteria.

    """
    pass
