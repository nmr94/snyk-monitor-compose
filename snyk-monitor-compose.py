import os
import yaml
import subprocess

SNYK_ORG_SLUG = "my-org-slug"

def find_docker_compose_files(path):
    docker_compose_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file == "docker-compose.yml":
                docker_compose_files.append(os.path.join(root, file))
    return docker_compose_files

def get_docker_images_from_compose_file(compose_file_path):
    docker_images = []
    with open(compose_file_path, 'r') as stream:
        try:
            compose_data = yaml.safe_load(stream)
            services = compose_data.get('services', {})
            for service in services.values():
                image = service.get('image')
                if image:
                    docker_images.append(image)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file: {compose_file_path}, {exc}")
    return docker_images

def main():
    docker_compose_files = find_docker_compose_files(".")

    all_docker_images = []
    for compose_file in docker_compose_files:
        print(f"Found docker-compose.yml: {compose_file}")
        images = get_docker_images_from_compose_file(compose_file)
        all_docker_images.extend(images)

    print("\nAll Docker images found:")
    for image in all_docker_images:
        print(f"Monitoring Docker image {image}")
        result = subprocess.run(
            f'snyk container monitor --org="{SNYK_ORG_SLUG}" {image}',
            shell=True,
            stdout=subprocess.PIPE
        )
        print(result.stdout.decode())

if __name__ == "__main__":
    main()
