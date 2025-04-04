在 Linux 环境中安装 Docker 的步骤如下（以 **Ubuntu/Debian** 为例，其他发行版类似）：

---

### **1. 卸载旧版本（如有）**
```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

---

### **2. 安装依赖工具**
```bash
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

---

### **3. 添加 Docker 官方 GPG 密钥**
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

---

### **4. 添加 Docker 软件源**
```bash
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

> **其他发行版**：  
> - CentOS/RHEL 替换为 `https://download.docker.com/linux/centos`  
> - Fedora 替换为 `https://download.docker.com/linux/fedora`

---

### **5. 安装 Docker Engine**
```bash
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
```

---

### **6. 启动 Docker 并设置开机自启**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---

### **7. 验证安装**
```bash
sudo docker run hello-world
```
如果看到欢迎信息，说明安装成功。

---

### **8. （可选）配置非 root 用户运行 Docker**
```bash
sudo usermod -aG docker $USER  # 将当前用户加入 docker 组
newgrp docker                 # 刷新组权限（或重新登录）
```
之后无需 `sudo` 即可运行 `docker` 命令。

---

### **其他 Linux 发行版**
- **CentOS/RHEL**：  
  ```bash
  sudo yum install -y yum-utils
  sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
  sudo yum install docker-ce docker-ce-cli containerd.io
  ```

- **Fedora**：  
  类似 CentOS，替换仓库地址为 `https://download.docker.com/linux/fedora/docker-ce.repo`。

- **Arch Linux**：  
  ```bash
  sudo pacman -S docker
  ```

---

### **常见问题**
1. **镜像加速**：编辑 `/etc/docker/daemon.json`，添加国内镜像源（如阿里云、腾讯云）：
   ```json
   {
     "registry-mirrors": ["https://<your-mirror>.mirror.aliyuncs.com"]
   }
   ```
   重启服务：`sudo systemctl restart docker`。

2. **防火墙问题**：确保防火墙允许 Docker 相关端口（如 2375、2376）。

---

通过以上步骤，你已成功在 Linux 上安装并配置 Docker。如需更多功能（如 Docker Compose），可参考官方文档。
