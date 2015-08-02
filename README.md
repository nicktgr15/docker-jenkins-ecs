# docker-jenkins-ecs

A jenkins docker container that can be used with the AWS EC2 Container Service (ECS).

## Example Task Definition

```
{
  "containerDefinitions": [
    {
      "volumesFrom": [],
      "portMappings": [
        {
          "hostPort": 8080,
          "containerPort": 8080,
          "protocol": "tcp"
        }
      ],
      "command": [],
      "environment": [],
      "essential": true,
      "entryPoint": [],
      "links": [],
      "mountPoints": [
        {
          "containerPath": "/var/run/docker.sock",
          "sourceVolume": "docker-sock",
          "readOnly": false
        },
        {
          "containerPath": "/usr/bin/docker",
          "sourceVolume": "docker-bin",
          "readOnly": false
        },
        {
          "containerPath": "/usr/lib/libdevmapper.so.1.02",
          "sourceVolume": "libdevmapper",
          "readOnly": false
        },
        {
          "containerPath": "/usr/lib/libudev.so.0",
          "sourceVolume": "libudev",
          "readOnly": false
        }
      ],
      "memory": 1024,
      "name": "jenkins",
      "cpu": 200,
      "image": "nicktgr15/docker-jenkins-ecs"
    }
  ],
  "volumes": [
    {
      "host": {
        "sourcePath": "/usr/bin/docker"
      },
      "name": "docker-bin"
    },
    {
      "host": {
        "sourcePath": "/var/run/docker.sock"
      },
      "name": "docker-sock"
    },
    {
      "host": {
        "sourcePath": "/lib64/libdevmapper.so.1.02"
      },
      "name": "libdevmapper"
    },
    {
      "host": {
        "sourcePath": "/lib64/libudev.so.0"
      },
      "name": "libudev"
    }
  ],
  "family": "jenkins"
}
```
