from typing import Dict
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            properties: Dict = json.node.data.properties
            result = dict()
            result['first_field'] = properties["first_field"]
            result['second_field'] = properties["second_field"]
            result['email'] = properties.get('email_field')
            result['datetime'] = properties.get('datetime_field')
            await json.save_result(result)
            json.state = RunState.complete

        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error

        return json
    