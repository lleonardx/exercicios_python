linguagens = ["python", "js", "c", "java", "csharp"]
## FUNÇÃO DE ORDENAÇÃO
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

print(sorted(linguagens))