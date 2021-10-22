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
  end


  config.vm.define "server-2" do |server2|
    server2.vm.network "private_network", ip:'192.168.33.61'
    server2.vm.hostname = "server-2"
    # server2.vm.provision :docker_compose, yml: "/vagrant/MachineLearning/docker-compose.yml", rebuild: true, run: "always"
  end
end