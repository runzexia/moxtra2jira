# moxtra2jira

接收Moxtra Outgoing Webhooks的消息，并转发到JIRA的Project automation



### Usage:

```
$ git clone https://github.com/runzexiaa/moxtra2jira.git
$ cd moxtra2jira
$ docker build -t moxtra2jira . 
$ docker run -dit -p 8080:8080 moxtra2jira $JIRA_ADDRESS
```



 