$script = <<-SCRIPT
echo "I like Vagrant"
echo "I love Linux"
ls -la
date > ~/vagrant_provisioned_at
SCRIPT

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

  config.vm.provision :shell, path: "./scripts/bootstrap.sh"
  config.vm.provision :file, source: "file.txt", destination: "file.txt"
  config.vm.provision :file, source: "./folder", destination: "folder"

  config.vm.define "server-1" do |server1|
    server1.vm.network "private_network", ip:'192.168.33.61'
    server1.vm.hostname = "server-1"
    server1.vm.provision "shell", inline: "echo Hi Class!"
    server1.vm.provision "shell", inline: $script
    server1.vm.provision "shell" do |s|
      s.inline = "echo $1 $2"
      s.args = ["AT", "Class!"]
    end
    server1.vm.provision "docker" do |d|
      d.run "hello-world"
    end
  end


  config.vm.define "server-2" do |server2|
    server2.vm.network "private_network", ip:'192.168.33.61'
    server2.vm.hostname = "server-2"
  end
end