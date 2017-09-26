#!/usr/bin/env python
import requests
import json
import logging
import tornado.web
from datetime import datetime
from dateutil import tz
from logging.config import fileConfig

fileConfig('logging_config.ini')
BaseJiraAddress = 'http://jira.daocom.io'
LOG = logging.getLogger()


class MyDumpHandler(tornado.web.RequestHandler):
    def post(self):
        post_body = self.request.body.decode("utf-8")
        LOG.info("get request %s", post_body)
        post_dict = json.loads(post_body)
        post_dict['event']['timestamp'] = self._convert_timezone(post_dict['event']['timestamp'])
        jira_dict = {'data': post_dict}
        request = BaseJiraAddress + self.request.uri
        self._execute_px_post_request(jira_dict, request)

    def _convert_timezone(self, time):
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('Asia/Shanghai')
        utc = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
        utc = utc.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)
        return central.strftime('%Y-%m-%d %H:%M:%S')

    def _execute_px_post_request(self, params, request):
        headers = {'Content-Type': 'application/json'}
        r = requests.post(
            request,
            data=json.dumps(params), headers=headers)
        LOG.info("get response %s", r)
        if r.status_code != requests.codes.ok:
            LOG.error("request jira error %s", r)
            self.write_error(r.status_code, r)
        else:
            self.write(dict())
        r.close()


if __name__ == "__main__":
    tornado.web.Application([(r"/.*", MyDumpHandler), ]).listen(8080)
    tornado.ioloop.IOLoop.instance().start()
