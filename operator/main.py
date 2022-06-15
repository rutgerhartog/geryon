import kopf
import kubernetes
from schemas import GraphicalApp


@kopf.on.create("apprequest")
def spawn_app(spec: dict, name: str, namespace: str, logger, **kwargs):

    kubernetes.config.load_incluster_config()
    api = kubernetes.client.ApiClient()

    api_instance = kubernetes.client.CustomObjectsApi(api)

    template = api_instance.get_cluster_custom_object(
        "apps.local", "v1beta1", "apptemplates", spec["AppTemplate"]
    )
    app = GraphicalApp.parse_obj(template)
    yaml_objects = app.render_k8s(spec, name, namespace)

    # TODO: check if client is allowed to spawn this container

    logger.info(yaml_objects)
    kubernetes.utils.create_from_yaml(api, yaml_objects=yaml_objects)
    return "OK"