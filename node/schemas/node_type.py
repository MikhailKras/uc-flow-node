from typing import List
from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Property,
    NodeType as  DisplayOptions, OptionValue,
)

from node.schemas.enums import FirstField, SecondField


class NodeType(flow.NodeType):
    id: str = 'd88135c1-29e6-4d7a-a9a1-3b5a52bdeab1'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'holihop_beyond'
    is_public: bool = False
    displayName: str = 'Holihop Beyond'
    icon: str = '<svg><text x="8" y="50" font-size="50">🔄</text></svg>'
    description: str = 'Service with structure like a holihop'
    inputs: List[str] = ['main']
    outputs: List[str] = ['main']
    properties: List[Property] = [
        Property(
            displayName='Toggle',
            name='toggle',
            type=Property.Type.BOOLEAN,
            required=True,
            default=True,
        ),
        Property(
            displayName='First field',
            name='first_field',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Значение 1',
                    value=FirstField.FIRST_VALUE,
                    description='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value=FirstField.SECOND_VALUE,
                    description='Значение 2',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ]
                }
            )
        ),
        Property(
            displayName='Second field',
            name='second_field',
            type=Property.Type.OPTIONS,
            noDataExpression=True,
            options=[
                OptionValue(
                    name='Значение 1',
                    value=SecondField.FIRST_VALUE,
                    description='Значение 1',
                ),
                OptionValue(
                    name='Значение 2',
                    value=SecondField.SECOND_VALUE,
                    description='Значение 2',
                ),
            ],
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ]
                }
            )

        ),
        Property(
            displayName='Input email field',
            name='email_field',
            type=Property.Type.STRING,
            placeholder='example@mail.ru',
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ],
                    'first_field': [
                        FirstField.FIRST_VALUE,
                    ],
                    'second_field': [
                        SecondField.FIRST_VALUE,
                    ]
                }
            )
        ),

        Property(
            displayName='Input datetime field',
            name='datetime_field',
            type=Property.Type.DATETIME,
            displayOptions=DisplayOptions(
                show={
                    'toggle': [
                        True,
                    ],
                    'first_field': [
                        FirstField.SECOND_VALUE,
                    ],
                    'second_field': [
                        SecondField.SECOND_VALUE,
                    ]
                }
            )
        )
    ]
