from google.cloud import run_v2

parent = "projects/speedy-victory-336109/locations/us-central1"
service_id = "pwmtest2"
service_name = parent + '/services/' + service_id
client = run_v2.ServicesClient()

def sample_create_service():
    port = run_v2.ContainerPort(container_port=80)
    container = run_v2.Container(
        image = 'gcr.io/speedy-victory-336109/nginx:v1',
        ports = [port]
    )
    ingress = run_v2.IngressTraffic(2)
    template=run_v2.RevisionTemplate(
        containers = [container]
    )
    service = run_v2.Service(
        template = template,
        ingress = ingress
    )
    request = run_v2.CreateServiceRequest(
        parent = parent,
        service_id = service_id,
        service = service
    )

    operation = client.create_service(request=request)
    response = operation.result()
    print(response)


def sample_update_service():
    port = run_v2.ContainerPort(container_port=80)
    resources = run_v2.ResourceRequirements(
        limits = {"cpu":"1", "memory": "2Gi"},
        cpu_idle = False
    )
    container = run_v2.Container(
        image = 'gcr.io/speedy-victory-336109/nginx:v2',
        ports = [port],
        resources = resources
    )
    ingress = run_v2.IngressTraffic(2)
    template=run_v2.RevisionTemplate(
        containers = [container],
        max_instance_request_concurrency = 1
    )   
    service = run_v2.Service(
        name = service_name,
        template = template,
        ingress = ingress
    )
    request = run_v2.UpdateServiceRequest(
        service = service
    )
    operation = client.update_service(request=request)
    print("Waiting for operation to complete...")
    response = operation.result()
    print(response)

def sample_get_service():
    request = run_v2.GetServiceRequest(
        name=service_name,
    )
    response = client.get_service(request=request)
    print(response)

sample_update_service()