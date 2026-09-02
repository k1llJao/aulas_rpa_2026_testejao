transacoes = [150.00, 23000.50, 870.00, -200.00, 540.00, 11000.00, 300.00]

for transacao in transacoes:
    if transacao > 10000.00:
        print(f"[ALERTA] Transação suspeita de R$ {transacao:.2f}: Encaminhada para auditoria.")
        continue
    elif transacao <= 0:
        print(f"[ERRO CRÍTICO] Transação inválida encontrada (R$ {transacao:.2f}). Interrompendo bot...")
        break
    else:
        print(f"[SUCESSO] Transação de R$ {transacao:.2f} processada.")
