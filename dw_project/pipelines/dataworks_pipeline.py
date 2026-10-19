from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "dataworks_pipeline", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    dataworks_pipeline__single_value_query = Process(
        name = "dataworks_pipeline__single_value_query",
        properties = ModelTransform(modelName = "dataworks_pipeline__single_value_query"),
        input_ports = None
    )

