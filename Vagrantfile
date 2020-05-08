Vagrant.configure("2") do |config|
  config.vm.box = "gce"
  config.vm.provider :google do |google, override|
    google.google_project_id = "django-app-test-264502"
    ###google.google_client_email = "757312456074-compute@developer.gserviceaccount.com"
    google.google_json_key_location = "/Users/dohyoungkim/Downloads/Reservation-search-app/django-app-test-264502-c3bf68ae8d6c.json"
    # Define the name of the instance.
    google.name = "rev-web-app-dev"
    # Set the zone where the instance will be located. To find out available zones:
    # `gcloud compute zones list`.
    google.zone = "us-central1-a"
    # Set the machine type to use. To find out available types:
    # `gcloud compute machine-types list --zone asia-east1-c`.
    google.machine_type = "n1-standard-1"
    google.disk_size = "30"
    # Set the machine image to use. To find out available images:
    # `$ gcloud compute images list`.
    google.image = "centos-7-v20200403"
    override.ssh.username = "dohyoungkim"
    override.ssh.private_key_path = "/Users/dohyoungkim/.ssh/id_rsa"
  end
end
