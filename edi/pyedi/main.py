from .services.pipeline_service import PipelineService


if __name__ == "__main__":

    pipeline = PipelineService()

    result = pipeline.run("samples/837_actual_data.txt")

    print(result)