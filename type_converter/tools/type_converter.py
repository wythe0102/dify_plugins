from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class TypeConverterTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        input_str = tool_parameters['input_str']

        yield self.create_variable_message("out_str",str(input_str))
        # convert int
        out_int = self.create_variable_message("out_int", 0)
        try:
            out_int = self.create_variable_message("out_int",int(input_str))
        except Exception:
            pass
        finally:
            yield out_int
        # convert float
        out_float = self.create_variable_message("out_float", 0.0)
        try:
            out_float = self.create_variable_message("out_float", float(input_str))
        except Exception:
            pass
        finally:
            yield out_float
        # convert eval
        out_eval = self.create_variable_message("out_eval", 0)
        try:
            out_eval = self.create_variable_message("out_eval", eval(input_str))
        except Exception:
            pass
        finally:
            yield out_eval

