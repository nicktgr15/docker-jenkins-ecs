FROM jenkins:1.596

USER root
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN apt-get update
RUN apt-get install python-pip -y
RUN pip install awscli

USER jenkins

git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.useHttpPath true
git config --global user.email "me@mycompany.com"
git config --global user.name "MyJenkinsServer"

mdkir /var/jenkins_home/.aws
echo "[default]" >> /var/jenkins_home/.aws/credentials
echo "output = json" >> /var/jenkins_home/.aws/credentials
echo "region = us-east-1" >> /var/jenkins_home/.aws/credentials
