from typing import Dict, List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = 'd88135c1-29e6-4d7a-a9a1-3b5a52bdeab1'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'adding_numbers_service'
    is_public: bool = False
    displayName: str = 'Adding numbers service'
    icon: str = '<svg><text x="8" y="50" font-size="50">🧮</text></svg>'
    description: str = 'Service for adding numbers as string and number'
    properties: List[Property] = [
        Property(
            displayName='Text field',
            name='text_field',
            type=Property.Type.STRING,
            required=True,
            default='',
        ),
        Property(
            displayName='Number field',
            name='number_field',
            type=Property.Type.NUMBER,
            required=True,
            default='',
        ),
        Property(
            displayName='String/Number',
            name='toggle',
            type=Property.Type.BOOLEAN,
            required=True,
            default=True
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        properties: Dict = json.node.data.properties
        try:
            text_value: str = properties['text_field']
            number_value: int = properties['number_field']
            toggle_value = properties['toggle']
            result = int(text_value) + number_value
            await json.save_result({
                "result": result if toggle_value is True else str(result)
            })
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
