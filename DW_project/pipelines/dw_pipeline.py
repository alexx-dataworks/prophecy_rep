from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "dw_pipeline", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    dw_pipeline__single_value_query = Process(
        name = "dw_pipeline__single_value_query",
        properties = ModelTransform(modelName = "dw_pipeline__single_value_query"),
        input_ports = None
    )

