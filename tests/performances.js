import http from 'k6/http';
import { check, sleep } from 'k6';

export default function () {
  const res = http.get('http://98.66.183.97:8088');
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}
