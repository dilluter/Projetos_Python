usuarios = [
    {"usuario": "admin", "senha": "1234"},
    {"usuario": "editor", "senha": "5678"},
    {"usuario": "visitante", "senha": "0000"},
    {"usuario": "igor", "senha": "2502"},
    {"usuario": "gabi", "senha": "2512"}
]

usuario_digitado = input("Digite seu usuário: ")
senha_digitada = input("Digite sua senha: ")

usuario_encontrado = next((u for u in usuarios if u["usuario"] == usuario_digitado and u["senha"] == senha_digitada), None)

if usuario_encontrado:
    print(f"✅ Bem-vindo, {usuario_encontrado['usuario']}!")
else:
    print("❌ Acesso negado! Usuário ou senha incorretos.")
