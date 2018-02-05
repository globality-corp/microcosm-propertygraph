"""
Node resources.

"""
from marshmallow import Schema, fields
from microcosm_flask.paging import PageSchema


class NodeSchema(Schema):
    id = fields.String(
        required=True,
    )
    labels = fields.List(
        fields.String,
        required=True,
    )
    properties = fields.Dict(
        required=True,
    )


class SearchNodeSchema(PageSchema):
    """
    Base search schema for nodes. Can be overridden by services
    to support customized querying criteria.

    """
    pass
