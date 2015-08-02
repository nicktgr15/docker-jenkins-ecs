FROM jenkins:1.596

USER root
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN apt-get update
RUN apt-get install python-pip -y
RUN pip install awscli

USER jenkins

RUN git config --global credential.helper '!aws codecommit credential-helper $@'
RUN git config --global credential.useHttpPath true
RUN git config --global user.email "me@mycompany.com"
RUN git config --global user.name "MyJenkinsServer"

COPY credentials /var/jenkins_home/.aws/credentials
