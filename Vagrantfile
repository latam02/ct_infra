Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end

  config.vm.boot_timeout = 600

  #configure provisioners on tha machine
  config.vm.provision :docker
  config.vm.provision :docker_compose

  config.vm.define "ci-server" do |ciserver|
    ciserver.vm.network "private_network", ip:'192.168.33.60'
    ciserver.vm.hostname = "ci-server"
    ciserver.vm.provision :file, source:"./docker/docker-compose.ci.yml", destination:"docker-compose.yml"
    ciserver.vm.provision :docker_compose, yml:"/home/vagrant/docker-compose.yml", run:"always"
  end
end