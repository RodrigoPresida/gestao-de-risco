import pandas as pd
import numpy as np
import json
import os
import re
from datetime import datetime, timedelta

def generate_legal_data(input_path, output_path, nrows=5000):
    print(f"Lendo {nrows} registros de {input_path}...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    # Pegar apenas os primeiros nrows registros
    data_values = list(raw_data.values())[:nrows]
    
    print("Enriquecendo dados com métricas de Legal Ops...")
    
    # Lista de colunas enriquecidas
    enriched_data = []
    
    for idx, row in enumerate(data_values):
        texts = row['texts']
        # Ordenar chaves para pegar a primeira e última movimentação (assumindo ordem numérica negativa)
        keys = sorted([int(k) for k in texts.keys()])
        
        first_move = texts[str(min(keys))]
        last_move = texts[str(max(keys))]
        all_text = " ".join(texts.values()).lower()
        
        # Simular Data de Distribuição (entre 2015 e 2020)
        start_date = datetime(2015, 1, 1) + timedelta(days=np.random.randint(0, 1800))
        
        # Simular Data de Encerramento baseada no número de movimentações
        duration_days = len(keys) * np.random.randint(10, 40)
        end_date = start_date + timedelta(days=duration_days)
        
        # Extrair UF (simplificado)
        uf = "SP" if "sp" in all_text else "RJ" if "rj" in all_text else np.random.choice(["MG", "RS", "PR", "BA"])
        
        # Classificação de Risco (CPC 25) baseada em palavras-chave
        if "procedente" in all_text or "acordo" in all_text:
            risco = "Provável"
            probabilidade = np.random.uniform(0.7, 1.0)
        elif "improcedente" in all_text:
            risco = "Remoto"
            probabilidade = np.random.uniform(0.0, 0.3)
        else:
            risco = "Possível"
            probabilidade = np.random.uniform(0.3, 0.7)
            
        # Valores Financeiros
        valor_causa = np.random.uniform(5000, 500000)
        # Provisão baseada no risco
        if risco == "Provável":
            provisao = valor_causa * probabilidade
        elif risco == "Possível":
            provisao = valor_causa * 0.5 # Conservador
        else:
            provisao = 0
            
        # Custos (Honorários + Custas)
        custo_defesa = (duration_days / 30) * np.random.uniform(500, 2000)
        
        # Tipo de Ação (Simulado baseado em termos)
        if "danos morais" in all_text:
            tipo_acao = "Cível - Indenizatória"
        elif "trabalhista" in all_text:
            tipo_acao = "Trabalhista"
        elif "execução" in all_text:
            tipo_acao = "Cível - Execução"
        else:
            tipo_acao = "Cível - Outros"

        enriched_data.append({
            "processo_id": f"PROC-{2026}-{idx:05d}",
            "data_distribuicao": start_date.strftime("%Y-%m-%d"),
            "data_ultima_mov": end_date.strftime("%Y-%m-%d"),
            "lead_time_days": duration_days,
            "uf": uf,
            "tipo_acao": tipo_acao,
            "valor_causa": round(valor_causa, 2),
            "risco_cpc25": risco,
            "probabilidade_perda": round(probabilidade, 2),
            "valor_provisao": round(provisao, 2),
            "custo_defesa": round(custo_defesa, 2),
            "status": "Ativo" if "ativo" in row['label'].lower() else "Encerrado"
        })
        
    df_final = pd.DataFrame(enriched_data)
    df_final.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Sucesso! Base enriquecida salva em: {output_path}")

if __name__ == "__main__":
    input_file = "C:/Users/Administrator/Documents/Meus Projetos/legal-ops-strategic-analytics/data/labeled.json"
    output_file = "C:/Users/Administrator/Documents/Meus Projetos/legal-ops-strategic-analytics/data/legal_ops_dataset.csv"
    generate_legal_data(input_file, output_file)
