# 在Linux Docker中使用国内镜像库（阿里云和腾讯云）

## 阿里云Docker镜像加速

1. **获取阿里云镜像加速地址**
   - 登录[阿里云容器镜像服务](https://cr.console.aliyun.com/)
   - 在左侧菜单选择"镜像加速器"
   - 复制专属加速器地址（每个用户有独立地址，格式如：`https://<your-id>.mirror.aliyuncs.com`）

2. **配置Docker使用阿里云镜像**
   - 编辑或创建Docker配置文件：
     ```bash
     sudo mkdir -p /etc/docker
     sudo tee /etc/docker/daemon.json <<-'EOF'
     {
       "registry-mirrors": ["https://<your-id>.mirror.aliyuncs.com"]
     }
     EOF
     ```
     将`<your-id>`替换为你的实际ID

   - 重启Docker服务：
     ```bash
     sudo systemctl daemon-reload
     sudo systemctl restart docker
     ```

## 腾讯云Docker镜像加速

1. **获取腾讯云镜像加速地址**
   - 腾讯云提供公共镜像地址：`https://mirror.ccs.tencentyun.com`

2. **配置Docker使用腾讯云镜像**
   - 编辑或创建Docker配置文件：
     ```bash
     sudo mkdir -p /etc/docker
     sudo tee /etc/docker/daemon.json <<-'EOF'
     {
       "registry-mirrors": ["https://mirror.ccs.tencentyun.com"]
     }
     EOF
     ```

   - 重启Docker服务：
     ```bash
     sudo systemctl daemon-reload
     sudo systemctl restart docker
     ```

## 验证配置是否生效

执行以下命令验证配置：
```bash
docker info
```
在输出中查找`Registry Mirrors`部分，确认列出的镜像地址是否正确。

## 注意事项

1. 如果`/etc/docker/daemon.json`已存在，需要手动编辑添加`registry-mirrors`字段
2. 可以同时配置多个镜像源，格式如下：
   ```json
   {
     "registry-mirros": [
       "https://<aliyun-id>.mirror.aliyuncs.com",
       "https://mirror.ccs.tencentyun.com"
     ]
   }
   ```
3. 对于非root用户，可能需要将用户加入docker组才能正常使用docker命令：
   ```bash
   sudo usermod -aG docker $USER
   ```
   然后退出重新登录生效
