import tkinter as tk
import uuid

def mostrar_ransom_gui(on_submit):
    root = tk.Tk()
    root.title("SYSTEM LOCKED")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    victim_id = str(uuid.uuid4())[:8]

    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True)

    titulo_app = tk.Label(
        frame,
        text="☢︎ SimuLock v1.0",
        fg="white",
        bg="black",
        font=("Courier", 23, "bold")
    )

    titulo_msg = tk.Label(
        frame,
        text="⚠︎ SEUS ARQUIVOS FORAM CRIPTOGRAFADOS ⚠︎",
        fg="red",
        bg="black",
        font=("Courier", 22, "bold")
    )

    titulo_app.pack(pady=(10, 0))
    titulo_msg.pack(pady=(0, 20))

    info = tk.Label(
        frame,
        text=f"ID DA VÍTIMA: {victim_id}\n\n"
             "Todos os seus arquivos foram bloqueados.\n"
             "Envie 10 BTC (SIMULADO)\n\n"
             "Tempo restante para perda permanente:",
        fg="white",
        bg="black",
        font=("Courier", 14)
    )
    info.pack(pady=10)

    # ⏱️ TIMER
    tempo_label = tk.Label(
        frame,
        text="01:00",
        fg="red",
        bg="black",
        font=("Courier", 32, "bold")
    )
    tempo_label.pack(pady=10)

    tempo_restante = 24 * 60 * 60  # 24 horas em segundos

    def atualizar_timer():
        nonlocal tempo_restante

        horas = tempo_restante // 3600
        minutos = (tempo_restante % 3600) // 60
        segundos = tempo_restante % 60

        tempo_label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")

        if tempo_restante > 0:
            tempo_restante -= 1
            root.after(1000, atualizar_timer)
        else:
            tempo_label.config(text="TEMPO ESGOTADO", fg="darkred")

    atualizar_timer()

    entry = tk.Entry(
        frame,
        font=("Courier", 16),
        width=30,
        justify="center"
    )
    entry.pack(pady=10)

    result_label = tk.Label(
        frame,
        text="",
        fg="green",
        bg="black",
        font=("Courier", 12)
    )
    result_label.pack(pady=10)

    def submit():
        key = entry.get()
        ok = on_submit(key)

        if ok:
            result_label.config(text="✔︎ Arquivos restaurados", fg="green")
            root.after(2000, root.destroy)
        else:
            result_label.config(text="✖︎ Chave inválida", fg="red")

    botao = tk.Button(
        frame,
        text="DESBLOQUEAR",
        command=submit,
        bg="red",
        fg="white",
        font=("Courier", 14, "bold"),
        width=20
    )
    botao.pack(pady=20)

    root.mainloop()