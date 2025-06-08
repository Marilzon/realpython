class Processor:
    def __init__(self, local: str) -> None:
        self.local = local

    def start_sessionn(self):
        return f"Starting: {self.local=} process."

    def stop_session(self):
        return f"Stopping {self.local=} process."


class Job:
    def execute_transformations(self, processor: Processor):
        processor_result = processor.start_sessionn()
        transformations = f"Transformations: A -> B -> C."
        return f"{processor_result}\n -> {transformations}"

    def finalize_transformations(self, processor: Processor):
        return processor.stop_session()


environment = Processor("prd")
job = Job()

print(job.execute_transformations(environment))
print(job.finalize_transformations(environment))
