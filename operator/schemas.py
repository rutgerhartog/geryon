from pydantic import BaseModel

class EnvironmentVariable(BaseModel):
    key: str 
    value: str

class GraphicalApp(BaseModel):
    name: str 
    image: str 
    sa: bool = False 
    labels: dict[str, str | bool]
    env: list[EnvironmentVariable] 
    data: list[str]

    def render_k8s(self) -> dict:
        """Create a kubernetes spec file 
        """
        base = [
            {
                "apiVersion": "v1",
                "kind": "Pod",
                "metadata": {"name": self.name, "namespace": self.namespace},
                "spec": {
                    "containers": [
                        {
                            "name": "main",
                            "image": self.image,
                            "env": [{"name": "DISPLAY", "value": "x11:1.0"}],
                            "volumeMounts": [],
                        }
                    ],
                    "volumes": [],
                },
            }
        ]
        return base 