# Пример выполнения тестового задания
## Операции

### Сборка docker образов
```
docker-compose build
docker-compose push
```

### Установка
Выполнить:
```
kubectl apply -f deploy/app-deployment.yaml
kubectl apply -f deploy/app-service.yaml
kubectl apply -f deploy/nginx-deployment.yaml
kubectl apply -f deploy/nginx-service.yaml
```

### Обновление приложения
Указать новую версию docker образа в deploy/app-deployment.yaml
Выполнить:
```
kubectl apply -f deploy/app-deployment.yaml
```

#### Проверка
```
kubectl rollout status deployment.v1.apps/app-deployment && echo Ok
```
```
curl "$(minikube service nginx-service --url)/api/healthcheck"
```

#### Откат
```
kubectl rollout status deployment.v1.apps/app-deployment || kubectl rollout undo deployment.v1.apps/app-deployment
```

## Тест обновления без простоя работы
Запускаем ApacheBench:
```
ab -n 10000 -c 10 "$(minikube service nginx-service --url)/api/healthcheck"
```

Паралельно запускаем обновление:
```
$ kubectl apply -f deploy/app-deployment.yaml                        
deployment.apps/app-deployment configured
```
Смотрим за процессом:
```
$ kubectl rollout status deployment.v1.apps/app-deployment && echo Ok        
Waiting for deployment "app-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "app-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "app-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "app-deployment" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "app-deployment" rollout to finish: 1 old replicas are pending termination...
deployment "app-deployment" successfully rolled out
Ok
```

Вывод ApacheBench:
```
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 192.168.99.100 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        nginx/1.16.0
Server Hostname:        192.168.99.100
Server Port:            31868

Document Path:          /api/healthcheck
Document Length:        2 bytes

Concurrency Level:      10
Time taken for tests:   36.967 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1580000 bytes
HTML transferred:       20000 bytes
Requests per second:    270.51 [#/sec] (mean)
Time per request:       36.967 [ms] (mean)
Time per request:       3.697 [ms] (mean, across all concurrent requests)
Transfer rate:          41.74 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   1.4      1      20
Processing:     2   34 101.4     22    3073
Waiting:        2   33 101.3     21    3073
Total:          3   36 101.4     24    3074

Percentage of the requests served within a certain time (ms)
  50%     24
  66%     29
  75%     33
  80%     36
  90%     47
  95%     61
  98%     87
  99%    160
 100%   3074 (longest request)
```

Успешно:
```
Complete requests:      10000
Failed requests:        0
```
