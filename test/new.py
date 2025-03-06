#Антон Создать задачу, Проставить отметку о выполнении и проверить что completed ==True
import requests
def test_task_done():
    name="generated_new"
    body = {"title": f"{name}", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body={"completed": 'true'}
    requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    response = requests.get(f"https://todo-app-sky.herokuapp.com/{id}")
    assert response.status_code == 200
    assert response.json()['title'] == name
    assert response.json()['completed'] == True