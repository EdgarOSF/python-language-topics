class ListaTareas:
    def __init__(self, tareas):
        self._tareas = list(tareas)

    def __len__(self):
        return len(self._tareas)

    def __getitem__(self, index):
        return self._tareas[index]

    def __contains__(self, item):
        return item in self._tareas

    def __iter__(self):
        return iter(self._tareas)



tareas = ListaTareas(["estudiar", "caminar", "leer"])

print(len(tareas))          # 3
print(tareas[1])            # caminar
print(tareas[-1])           # leer
print(tareas[0:2])          # ["estudiar", "caminar"]
print("leer" in tareas)     # True

for tarea in tareas:
    print(tarea)

