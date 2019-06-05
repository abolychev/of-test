# Пример выполнения тестового задания
## Операции
### Установка
Выполнить:
```
kubectl apply -f deploy/app-deployment.yaml
kubectl apply -f deploy/app-service.yaml
kubectl apply -f deploy/nginx-deployment.yaml
kubectl apply -f deploy/nginx-service.yaml
```

### Обновление
Указать новую версию образа в deploy/app-deployment.yaml
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
